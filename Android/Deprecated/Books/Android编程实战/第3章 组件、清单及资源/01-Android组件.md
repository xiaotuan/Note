[toc]

最常用的 Android 组件有四个，分别为 Activity、Service、BroadcastReceiver 以及 ContentProvider。

### 1. Service

建议每个任务都有一个对应的 Service。

### 2. Application

每个 Android 应用程序都会有一个 Application 组件，如果没有显示定义，系统会创建一个默认的 Application。可以通过 Context.getApplication() 方法获取对 Application 的引用。因为每个 Android 应用都只有一个 Application 实例，开发者可以使用它共享变量并和应用中的其他组件通信。虽然使用单例也可以共享全局状态，但是 Application 更有优势，因为它还实现了应用生命周期的回调。

```java
import android.app.Application;

import java.util.Collections;
import java.util.HashSet;
import java.util.Set;
import java.util.concurrent.ConcurrentHashMap;

public class MyApplication extends Application {

    private ConcurrentHashMap<String, String> mGlobalVariables;
    private Set<AppStateListener> mAppStateListeners;

    @Override
    public void onCreate() {
        super.onCreate();
        // 在其他组件创建之前调用
        mGlobalVariables = new ConcurrentHashMap<>();
        mAppStateListeners = Collections.synchronizedSet(new HashSet<AppStateListener>());
    }

    public String getGlobalVariable(String key) {
        return mGlobalVariables.get(key);
    }

    public String removeGlobalVariable(String key) {
        String value = mGlobalVariables.remove(key);
        notifyListeners(key, null);
        return value;
    }

    public void putGlobalVariable(String key, String value) {
        mGlobalVariables.put(key, value);
        notifyListeners(key, value);
    }

    public void addAppStateListener(AppStateListener appStateListener) {
        mAppStateListeners.add(appStateListener);
    }

    public void removeAppStateListener(AppStateListener appStateListener) {
        mAppStateListeners.remove(appStateListener);
    }

    private void notifyListeners(String key, String value) {
        for (AppStateListener appStateListener : mAppStateListeners) {
            appStateListener.onStateChanged(key, value);
        }
    }

    public interface AppStateListener {
        void onStateChanged(String key, String value);
    }
}
```

为了让 Android 系统识别自定义的 Application 组件而不是使用默认的，需要在 android:name 属性中声明自定义的 Application 组件。

```xml
<application android:label="@string/app_name"
             android:icon="@drawable/app_icon"
             android:name=".MyApplication">
	<!-- 所有其他组件都在这里声明 -->
</application>
```

可以像如下代码所示，在 Activity 中使用 Application 对象：

```java
public class MyActivity extends Activity implements MyApplication.AppStateListener {
    
    @Override
    protected void onResume() {
        super.onResume();
        MyApplication myApplication = (MyApplication) getApplication();
        myApplication.addAppStateListener(this);
    }
    
    @Override
    protected void onPause() {
        super.onPause();
        MyApplication myApplication = (MyApplication) getApplication();
        myApplication.removeAppStateListener(this);
    }
    
    @Override
    public void onStateChanged(String key, String value) {
        // 处理状态变化
    }
}
```

