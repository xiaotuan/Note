[toc]

### 7.2 设计 API

可以使用 Service 或者 ContentProvider 为第三方应用开发 API。当实现 API 时，开发者需要考虑一些事情。是否需要处理并发请求？每次只处理一个客户端请求是否足够？API 是否只包含一个或是很少的操作？或者是一组更加复杂的方法？这些问题的答案将决定实现远程 API 最合适的方法。

另一个要考虑的细节是是否与其他开发者分享该 API，或者是只用于自己的应用（也就是说只有开发者自己发布该插件）。如果是第一种情况，可以考虑构建一个库工程，使用易于使用的 Java API 包装客户端的实现。如果只是自己使用 API，可以使用 AIDL 或者 Messager。

如果只是单向地使用 API ，第 6 章所述的 IntentService 即可满足需求。在这种情况下，只需在清单文件中添加必要的权限，并确保 Service 的 `android:exported` 属性设为 true。

#### 7.2.1 AIDL

编写 Java 接口和编写 AIDL 文件还是有些不同的。

首先，对所有的非原始类型参数，需要指定如下三种类型方向指示符之一：`in`、`out`、`inout`。`in` 类型方向指示符只用于输入，客户端不会看到 Service 对对象的修改。`out` 类型表明输入对象不包含相关的数据，但会由 Service 生成相关的数据。`inout` 类型是上面两种类型的结合。切记只使用需要的类型，因为每种类型都有相应的消耗。

另一个需要记住的是，所有用于通信的自定义类都需要创建一个 AIDL 文件，用来声明该类实现了 Parcelable 接口。

下面的代码片段是一个名为 CustomData.aidl 的 AIDL 文件示例。它应该和 Java 源代码文件放在同一个包里。

```java
package com.apt1.sampleapi;

parcelable CustomData;
```

最后，需要在 AIDL 文件中引入所有需要的自定类，如下所示：

```java
package com.apt1.sampleapi;

import com.apt1.sampleapi.CustomData;

interface ApiInterfaceV1 {
    /**
     * 用于检查数字是否为素数的简单远程方法
     */
    boolean isPrime(long value);
    
    /**
     * 检索 timestamp 以后的所有 CustomData 对象，至多获取 result.length 个对象
     */
    void getAllDataSince(long timestamp, out CustomData[] result);
    
    /**
     * 存储 CustomData 对象
     */
    void storeData(in CustomData data);
}
```

该例中的 AIDL 文件共有三个方法。**注意：** 原始类型参数不需要方向指示符（总是调用它们的值）。

切记，一旦实现了客户端代码，就不能再修改或者移除 AIDL 文件中的任何方法。可以在**文件末尾** 添加新的方法，但是因为 AIDL 编译器会为每个方法生成标识符，所以不能修改现存的方法，否则不能向后兼容老版本。需要处理新版本的 API 时，建议创建一个新的 AIDL 文件。这样做允许保持与老版本客户端的兼容。正如前例的 AIDL 文件名所示，可以在第一版的文件名后附加 V1 标识符来处理版本问题。再添加新方法就可以创建一个以 V2 结尾的文件，以此类推。

上面所示的版本处理方法是使用 AIDL 文件的缺点之一。解决该问题的一种方法是提供 Java 包装类，并以库工程或者 JAR 文件形式发布以便开发者使用。这样一来，客户端就不必实现多个 AIDL，但是可以下载最新版本的包装类，并确保它是兼容的。7.2.3 节会介绍如何创建这种包装类。

准备好 AIDL 文件后，需要同时在服务端和客户端实现它，如下所示：

```java
import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.os.RemoteException;

import androidx.annotation.Nullable;

import java.util.ArrayList;
import java.util.Date;

public class AidlService extends Service {

    private ArrayList<CustomData> mCustomDataCollection;

    @Override
    public void onCreate() {
        super.onCreate();
        mCustomDataCollection = new ArrayList<>();
        // 用于存储的数据填充列表
    }

    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        return mBinder;
    }

    public static boolean isPrimeImpl(long number) {
        // 略去具体的实现
        return false;
    }

    private void getDataSinceImpl(CustomData[] result, Date since) {
        int size = mCustomDataCollection.size();
        int pos = 0;
        for (int i = 0; i < size && pos < result.length; i++) {
            CustomData storedValue = mCustomDataCollection.get(i);
            if (since.after(storedValue.getCreated())) {
                result[pos++] = storedValue;
            }
        }
    }

    private void storeDataImpl(CustomData data) {
        int size = mCustomDataCollection.size();
        for (int i = 0; i < size; i++) {
            CustomData customData = mCustomDataCollection.get(i);
            if (customData.equals(data)) {
                mCustomDataCollection.set(i, data);
                return;
            }
        }
        mCustomDataCollection.add(data);
    }

    private final ApiInterfaceV1.Stub mBinder = new ApiInterfaceV1.Stub() {
        @Override
        public boolean isPrime(long value) throws RemoteException {
            return isPrimeImpl(value);
        }

        @Override
        public void getAllDataSince(long timestamp, CustomData[] result) throws RemoteException {
            getDataSinceImpl(result, new Date(timestamp));
        }

        @Override
        public void storeData(CustomData data) throws RemoteException {
            storeDataImpl(data);
        }
    };
}
```

前例中的 Service 在代码末尾实现了 ApiInterfaceV1.Stub。该对象也会在 onBind() 方法中返回给绑定到 Service 的客户端。注意，每次对 Service API 的调用都运行在自身的线程上，因为 Binder 提供了一个线程池用于执行所有的客户端调用。这以为这使用这种方法时，客户端不会阻塞 Service 所属的主线程。

下面的 Activity 展示了如何绑定到一个远程 Service 以及检索 ApiInterfaceV1 接口。如果是该 API 的唯一用户，可以同时管理客户端和服务端的版本（或者在同一个开发团队），那么这是首选的解决方案。

```java
package com.example.android.myapplication;

import android.app.Activity;
import android.content.ComponentName;
import android.content.Intent;
import android.content.ServiceConnection;
import android.os.Bundle;
import android.os.IBinder;
import android.os.RemoteException;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class MyApiClient extends Activity implements ServiceConnection {

    private ApiInterfaceV1 mService;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_my_api_client);
    }

    @Override
    protected void onResume() {
        super.onResume();
        bindService(new Intent("com.apt1.sampleapi.AIDL_SERVICE"), this,
                BIND_AUTO_CREATE);
    }

    public void onCheckForPrime(View view) throws RemoteException {
        EditText numberToCheck = findViewById(R.id.number_input);
        long number = Long.valueOf(numberToCheck.getText().toString());
        boolean isPrime = mService.isPrime(number);
        String message = isPrime ? getString(R.string.number_is_prime, number)
                : getString(R.string.number_not_prime, number);
        Toast.makeText(this, message, Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onPause() {
        super.onPause();
        unbindService(this);
    }

    @Override
    public void onServiceConnected(ComponentName name, IBinder service) {
        mService = ApiInterfaceV1.Stub.asInterface(service);
    }

    @Override
    public void onServiceDisconnected(ComponentName name) {
        mService = null;
    }
}
```

**AIDL回调**

客户端也可以实现 AIDL ，用做 Service 的回调接口。如果客户端项注册对 Service 的监听，比如从在线服务器更新了数据，这种方法会很有用。

下面的示例使用带有回调接口的新 AIDL 文件，注意 oneway 关键字，它告诉 AIDL 编译器该接口只是单向通信。对调用者（本例是 Service）的响应不是必需的。这样做会有轻微的性能提升。

```java
// AidlCallback.aidl
package com.example.android.myapplication;

import com.example.android.myapplication.CustomData;

oneway interface AidlCallback {

    void onDataUpdated(in CustomData[] data);
    
}
```

接下来，在客户端创建该接口的示例，如下所示。本例在收到 Service 的回调后只是展示一个 Toast：

```java
private AidlCallback.Stub mAidlCallback = new AidlCallback.Stub() {
    @Override
    public void onDataUpdated(CustomData[] data) throws RemoteException {
        Toast.makeText(MyApiClient.this, "Data was updated!", Toast.LENGTH_SHORT).show();
    }
};
```

在这之前所示的 Service AIDL 文件中，添加一行代码用于注册回调：

```java
void addCallback(in AidlCallback callback);
```

最后，在 Service 中实现 addCallback() 回调。这里同样使用 linkToDeath() 方法来接收通知，以防客户端 Binder 被杀死。

```java
@Override
public void addCallback(final AidlCallback callback) throws RemoteException {
    mCallbacks.add(callback);
    callback.asBinder().linkToDeath((DeathRecipient) () -> mCallbacks.remove(callback), 0);
}
```

> 通常，需要实现 addCallback() 和 removeCallback() 方法，留给读者作为练习。

前面的例子显示了如何在应用间创建回调接口。它还展示了如何在两个应用间传输 Binder 对象，而不需使用 ServiceManager 注册它。由于只有客户端和 Service 知道 Binder 的地址，因此它可以作为一种高效的 IPC 安全机制。

#### 7.2.2 Messager

也可以通过 Messager 类提供远程接口。当 Service 不需要支持并发操作时该类会非常有用。Messager 类使用 Handler 执行每个传入的消息，所有客户端的调用都按顺序运行在同一个线程上。使用 Messager 类还能避免 AIDL 文件带来的问题，并可以方便地为客户端提供异步消息 API。虽然没有那么强大，但该类有时候会很有效果，因为它更容易在客户端和 Service 端实现。

下面的例子展示了如何使用 Messager 类来提供异步 API。首先在 onCreate() 方法中创建 Messager，然后在 onBind() 方法中返回 Binder 对象。当 Messager 接收到消息时，它能够使用存储在 replyTo 成员变量里的 Messager 对象响应客户端的请求。

```java
import android.app.Service;
import android.content.Intent;
import android.graphics.Bitmap;
import android.os.Handler;
import android.os.HandlerThread;
import android.os.IBinder;
import android.os.Message;
import android.os.Messenger;
import android.os.RemoteException;
import android.util.Log;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

public class MessagerService extends Service {

    private Handler mMessageHandler;
    private Messenger mMessenger;

    @Override
    public void onCreate() {
        super.onCreate();
        HandlerThread handlerThread = new HandlerThread("MessengerService");
        handlerThread.start();
        mMessageHandler = new Handler(handlerThread.getLooper(), new MyHandlerCallback());
    }

    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        return mMessenger.getBinder();
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        mMessageHandler.getLooper().quit();
    }

    private class MyHandlerCallback implements Handler.Callback {

        @Override
        public boolean handleMessage(@NonNull Message msg) {
            boolean delivered = false;
            switch (msg.what) {
                case MessageAPI.SEND_TEXT_MSG:
                    delivered = sendTextMessage((String) msg.obj);
                    break;

                case MessageAPI.SEND_PHOTO_MSG:
                    delivered = sendPhotoMessage((Bitmap)msg.obj);
                    break;
            }
            Message reply = Message.obtain(null, MessageAPI.MESSAGE_DELIVERED_MSG,
                    delivered);
            try {
                msg.replyTo.send(reply);
            } catch (RemoteException e) {
                Log.e("MessengerService", "Error sending message reply!", e);
            }
            return true;
        }
    }

    // 分发后返回 true
    private boolean sendPhotoMessage(Bitmap photo) {
        // 略去具体实现
        return true;
    }

    // 分发后返回 true
    private boolean sendTextMessage(String textMessage) {
        // 略去具体实现
        return true;
    }
}
```

下例中，客户端首先绑定到 Service，然后使用 IBinder 作为参数构建一个 Messenger 对象，作为运行在远程 Service 中的 Messenger 的代理。当向 Service 发送消息时，也可以设置 Message 对象的 replyTo 属性。

```java
import android.app.Activity;
import android.content.ComponentName;
import android.content.Intent;
import android.content.ServiceConnection;
import android.os.Bundle;
import android.os.Handler;
import android.os.HandlerThread;
import android.os.IBinder;
import android.os.Message;
import android.os.Messenger;
import android.os.RemoteException;
import android.view.View;
import android.widget.EditText;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

public class MyMessengerClient extends Activity implements ServiceConnection {

    private ApiInterfaceV1 mService;
    private Messenger mRemoteMessenger;
    private Messenger mReplyMessenger;
    private Handler mReplyHandler;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        HandlerThread handlerThread = new HandlerThread("ReplyMessenger");
        handlerThread.start();
        mReplyHandler = new Handler(handlerThread.getLooper(), new ReplyHandlerCallback());
        mReplyMessenger = new Messenger(mReplyHandler);
    }

    @Override
    protected void onResume() {
        super.onResume();
        bindService(new Intent("com.apt1.sampleapi.MESSENGER_SERVICE"), this, BIND_AUTO_CREATE);
    }

    public void onSendTextPressed(View view) {
        String textMessage = (EditText) findViewById(R.id.message_input);
        Message message = Message.obtain();
        message.obj = textMessage;
        message.replyTo = mReplyMessenger;
        try {
            mRemoteMessenger.send(message);
        } catch (RemoteException e) {
            // 远程的 Service 已被销毁
        }
    }

    @Override
    protected void onPause() {
        super.onPause();
        unbindService(this);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        mReplyHandler.getLooper().quit();
    }

    @Override
    public void onServiceConnected(ComponentName name, IBinder service) {
        mRemoteMessenger = new Messenger(service);
    }

    @Override
    public void onServiceDisconnected(ComponentName name) {
        mRemoteMessenger = null;
    }

    private class ReplyHandlerCallback implements Handler.Callback {

        @Override
        public boolean handleMessage(@NonNull Message msg) {
            switch (msg.what) {
                case MessageAPI.MESSAGE_DELIVERED_MSG:
                    // 处理异步响应
                    break;
            }
            return true;
        }
    }
}
```

这种方法和第 6 章描述的 IntentService 非常类似，但本例没有使用 Intent，而是使用 Message 触发 Handler 上的操作（见第 2 章）。此外，Messenger 实现异步通信很方便，而不需要使用 BroadcastReceiver。

#### 7.2.3 使用库工程包装 API

不管是使用 AIDL 还是 Messenger 类来实现远程 API，最好把所有 API 相关的类和接口提取为一个库项目，并创建供客户端使用的纯 Java 包装类。因为很可能要在 API 中支持复杂的对象，只提供一个 AIDL 文件通常是不够的。开发者还需为客户端提供自定义的类。正如第 1 章描述的，当涉及发布和版本处理时，建立一个 Android 库项目来处理所有和远程 API 相关的问题是一个简单且有效的方法。也可以把编译好的包装类打包成一个 JAR 文件，以便方便地发布成第三方库。建议使用 Android 库项目，并把它们上传到在线的版本控制服务上（比如 GitHub），以便开发者能够简单地把代码集成到他们的应用中。

创建一个远程 API 库项目最简单的方式是把所有的 AIDL 文件和 Parcelable 类移到库项目中，接下来就可以在实现远程 API 的应用中引用它。但是，当有多个 AIDL 文件时（新的版本、客户端回调等），这样做很容易变得相当复杂，所以最好还是把它们包装成更容易使用的 Java 类，如下所示：

```java
import android.app.Activity;
import android.content.ComponentName;
import android.content.Intent;
import android.content.ServiceConnection;
import android.os.Bundle;
import android.os.Handler;
import android.os.HandlerThread;
import android.os.IBinder;
import android.os.Message;
import android.os.Messenger;
import android.os.RemoteException;
import android.view.View;
import android.widget.EditText;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

public class MyMessengerClient extends Activity implements ServiceConnection {

    private ApiInterfaceV1 mService;
    private Messenger mRemoteMessenger;
    private Messenger mReplyMessenger;
    private Handler mReplyHandler;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        HandlerThread handlerThread = new HandlerThread("ReplyMessenger");
        handlerThread.start();
        mReplyHandler = new Handler(handlerThread.getLooper(), new ReplyHandlerCallback());
        mReplyMessenger = new Messenger(mReplyHandler);
    }

    @Override
    protected void onResume() {
        super.onResume();
        bindService(new Intent("com.apt1.sampleapi.MESSENGER_SERVICE"), this, BIND_AUTO_CREATE);
    }

    public void onSendTextPressed(View view) {
        String textMessage = (EditText) findViewById(R.id.message_input);
        Message message = Message.obtain();
        message.obj = textMessage;
        message.replyTo = mReplyMessenger;
        try {
            mRemoteMessenger.send(message);
        } catch (RemoteException e) {
            // 远程的 Service 已被销毁
        }
    }

    @Override
    protected void onPause() {
        super.onPause();
        unbindService(this);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        mReplyHandler.getLooper().quit();
    }

    @Override
    public void onServiceConnected(ComponentName name, IBinder service) {
        mRemoteMessenger = new Messenger(service);
    }

    @Override
    public void onServiceDisconnected(ComponentName name) {
        mRemoteMessenger = null;
    }

    private class ReplyHandlerCallback implements Handler.Callback {

        @Override
        public boolean handleMessage(@NonNull Message msg) {
            switch (msg.what) {
                case MessageAPI.MESSAGE_DELIVERED_MSG:
                    // 处理异步响应
                    break;
            }
            return true;
        }
    }
}
```

上面的代码显示了如何为本章前面所示的 AIDL 示例创建包装类。该方法会给客户端提供一个更容易使用的接口。开发者甚至可以通过把它们包装成普通的 Java 接口来管理 AIDL 回调，见前面的 ApiCallback 示例。

此方法允许使用标准的 Java 代码对 API 进行版本控制。开发者可以为过时的方法添加 @deprecated 标签，还可以在包装类中添加新的方法。客户端不需要关心这些细节，可以很容易地保持向后兼容。

根据 Context.bindService() 中 Intent 内容的不同，返回不同的 IBinder 对象，开发者可以实现不同版本的 Service API。

```java
public IBinder onBind(Intent intent) {
    int apiVersionRequested = intent.getIntExtra(EXTRA_VERSION_TAG, 1);
    switch (apiVersionRequested) {
        case 1:
            return mBinderV1;
        case 2:
            return mBinderV2;
        case 3:
            return mBinderV3;
        default:
            return null;
    }
}
```

上面的示例显示了如何根据 Intent 中 int 值的不同来决定返回哪个版本的 API。该方法允许创建新的 AIDL 文件来更新 API。包装类现在会绑定所有的版本，并且每个绑定都保持一个本地的引用。

