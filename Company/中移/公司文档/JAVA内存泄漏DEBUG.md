JAVA内存泄漏DEBUG
===
tag:[[debug]][[memory]]


> 内存泄漏：对于JAVA来说，就是new 出来的Object放在堆上无法被GC回收。

### Java中内存分配：
- 静态储存区：编译时候就分配好，在程序整个运行期间都存在，主要存放静态数据和常量
- 栈区：方法执行时，会在栈区内存中创建方法内部中的局部变量，方法结束后自动释放内存
- 堆区：通常存放 new 出来的对象，由Java垃圾回收器回收

参见附录[java中的static](#java中的static)

### 四种引用类型的介绍
- 强引用(Strong Reference) ：JVM宁可抛出OOM(out of memory)， 也不会让GC回收具有强引用的对象。
- 软引用(Soft Reference)
- 弱引用(Weak Reference)
- 虚引用(Phantom Reference)

所以这里的内存泄漏则为：new出来的对象无法被GC回收，即为强引用


### 内存泄漏分析工具
1. 可以用Android Studio中的Android Monitor观察内存抖动的情况 （被Android profilter取代）
2. MAT (Memory Analyzer Tools) eclipse的插件，快速分析方法
    - 被Android Profilter取代，具体见下[链接](https://developer.android.com/studio/profile/monitor) (Dalvik Debug Monitor Server (DDMS) :This tool is deprecated. Instead, use Android Profiler in Android Studio 3.0 and higher to profile your app's CPU, memory, and network usage.)
3. leakcanary
    - www.liaohuqiu.net/cn/posts/leak-canary

综上，现在可以用Android profilter工具来分析CPU MEMORY NET USE等。

---
### 内存泄漏具体例子
以下内容为摘取[链接](https://mp.weixin.qq.com/s/Q7aKsPqVKO7g2ofF81zThA)实例来讲android中内存泄漏分析解法和编写代码应注意的事项。

#### 1. 单例模式引起的内存泄露

由于单例模式的静态特性，使得它的生命周期和我们的应用一样长，如果让单例无限制的持有Activity的强引用就会导致内存泄漏。

**解决方案**
- 将该属性的引用方式改为弱引用;
- 如果传入Context，使用ApplicationContext;

1. 泄漏代码片段：
```java
public class UserInfoBean {
    private static UserInfoBean userInfoBean;
    private Context mContext;
    private UserInfoBean(Context context) {
        this.mContext = context;
    }
    public static UserInfoBean getUserInfoBean(Context context) {
        if (userInfoBean == null) {
            synchronized (UserInfoBean.class) {
                if (userInfoBean == null) {
                    userInfoBean = new UserInfoBean(context);
                }
            }
        }
        return userInfoBean;
    }
}
```
使用ApplicationContext：
```java
public class UserInfoBean {
    private static UserInfoBean userInfoBean;
    private Context mContext;
    private UserInfoBean(Context context) {
        this.mContext = context.getApplicationContext();
    }
    public static UserInfoBean getUserInfoBean(Context context) {
        if (userInfoBean == null) {
            synchronized (UserInfoBean.class) {
                if (userInfoBean == null) {
                    userInfoBean = new UserInfoBean(context);
                }
            }
        }
        return userInfoBean;
    }
}
```
或者代码中用到的Context可以使用自己定义的MyApplication中的MyApplication.getInstance获取。

2. 泄漏代码片段:
```java
private static CommonViewHelper mInstance;
private CommonViewHelper() {
}
public static CommonViewHelper getInstance() {
    if (mInstance == null) {
        synchronized (CommonViewHelper.class) {
            if (mInstance == null) {
                mInstance = new CommonViewHelper();
            }
        }
    }
    return mInstance;
}
private View mView = null;
public void setScrolledView(View scrolledView) {
    mView = scrolledView;
}
```

使用WeakReference:
```java
private static CommonViewHelper mInstance;
private CommonViewHelper() {
}
public static CommonViewHelper getInstance() {
    if (mInstance == null) {
        synchronized (CommonViewHelper.class) {
            if (mInstance == null) {
                mInstance = new CommonViewHelper();
            }
        }
    }
    return mInstance;
}
//使用弱引用 防止内存泄漏
private WeakReference<View> mViewWeakRef = null;
public void setScrolledView(View scrolledView) {
    mViewWeakRef = new WeakReference<View>(scrolledView);
}
```
#### 2. Handler引起的内存泄漏
Handler引起的内存泄漏在开发中最为常见的。Handler、Message、MessageQueue都是相互关联在一起的，如果Handler发送的Message尚未被处理，那么该Message以及发送它的Handler对象都会被线程MessageQueue一直持有，保持到消息得到处理，而导致了Activity无法被垃圾回收器回收，而导致了内存泄露。由于Handler属于TLS（Thread Local Storage）变量，生命周期和Activity是不一致的，因此这种实现方式很难保证跟Activity的生命周期一直，所以很容易无法释放内存。

**解决方案**
- 可以把Handler类放在单独的类文件中，或者使用静态内部类便可以避免泄露;
- 如果想在Handler内部去调用所在的Activity,那么可以在handler内部使用弱引用的方式去指向所在Activity.使用Static + WeakReference的方式来达到断开Handler与Activity之间存在引用关系的目的。

泄漏代码片段:
```java
private final Handler mHandler = new Handler() {  
    @Override  
    public void handleMessage(Message msg) {  
        // ...  
    }  
};  

@Override  
public void onCreate(Bundle savedInstanceState) {  
    super.onCreate(savedInstanceState);  
    setContentView(R.layout.activity_main);  
    mHandler.sendMessageDelayed(Message.obtain(), 60000*5);  
}
```

在上面的代码中发送了一个延时5分钟执行的Message，当该Activity退出的时候，延时任务（Message）还在主线成的MessageQueue中等待，此时的Message持有Handler的强引用，并且由于Handler是我们的Activity类的非静态内部类，所以Handler会持有该Activity的强引用，此时该Activity退出时无法进行内存回收，造成内存泄漏。

**解决办法：**
- 将Handler声明为静态内部类，这样它就不会持有外部类的引用了，Handler的的生命周期就与Activity无关了。不过倘若用到Context等外部类的非static对象，还是应该通过使用Application中与应用同生命周期的Context比较合适。
```java
private final MyHandler mHandler = new MyHandler(this);
@Override  
public void onCreate(Bundle savedInstanceState) {  
    super.onCreate(savedInstanceState);  
    setContentView(R.layout.activity_main);  
    mHandler.sendMessageDelayed(Message.obtain(), 60000*5);
}

private static final class MyHandler extends Handler {
    private WeakReference<HomeMainActivity> mActivity;
    public MyHandler(HomeMainActivity mainActivity) {
        mActivity = new WeakReference<>(mainActivity);
　　　　//or
　　　　//mActivity=mainActivity.getApplicationContext;
    }
    
    @Override
    public void handleMessage(Message msg) {
        super.handleMessage(msg);
        HomeMainActivity mainActivity = mActivity.get();
        if (null != mActivity) {
            //相关处理
        }
    }
}
```
虽然我们结束了Activity的内存泄漏问题，但是经过Handler发送的延时消息还在MessageQueue中，Looper也在等待处理消息，所以我们要在Activity销毁的时候处理掉队列中的消息。
```java
@Override
protected void onDestroy() {
    super.onDestroy();
    //传入null，就表示移除所有Message和Runnable
    if (mHandler != null) {
        mHandler.removeCallbacksAndMessages(null);
    }
    mHandler = null;
}
```

#### 3. InnerClass匿名内部类引起的内存泄漏（非静态内部类、匿名内部类、线程 ）
在Java中，非静态内部类 和 匿名类 都会潜在的引用它们所属的外部类，但是，静态内部类却不会。如果这个==非静态内部类==实例做了一些耗时的操作，就会造成外围对象不会被回收，从而==导致内存泄漏==。

匿名内部类的类型可以是如下几种方式。
- 接口匿名内部类
- 抽象类匿名内部类
- 类匿名内部类

**解决方案**
- 将内部类变成静态内部类;
- 如果有强引用Activity中的属性，则将该属性的引用方式改为弱引用;
- 在业务允许的情况下，当Activity执行onDestory时，结束这些耗时任务;

1. 泄漏代码片段:
```java
public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        test();
    }
    //这儿发生泄漏
    public void test() {
        new Thread(new Runnable() {
            @Override
            public void run() {
                while (true) {
                    try {
                        Thread.sleep(1000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        }).start();
    }
}
```

正确代码片段:
```java
public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        test();
    }
    //加上static，变成静态匿名内部类
    public static void test() {
        new Thread(new Runnable() {
            @Override
            public void run() {
                while (true) {
                    try {
                        Thread.sleep(1000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        }).start();
    }
}
```

2. Android开发经常会继承实现 Activity 或者 Fragment 或者 View。如果使用==了匿名类==，而又被异步线程所引用，如果==没有任何措施同样会导致内存泄漏==的：
```java
public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_inner_bad);
        Runnable runnable1 = new MyRunnable();
        Runnable runnable2 = new Runnable() {
            @Override
            public void run() {
            }
        };
    }
    private static class MyRunnable implements Runnable{
        @Override
        public void run() {
        }
    }
}
```
runnable1 和 runnable2的区别就是，runnable2使用了匿名内部类，runnable1是没有什么特别的。是个静态内部类。但runnable2多出了一个MainActivity的引用，若是这个引用再传入到一个异步线程，此线程在和Activity生命周期不一致的时候，也就造成了Activity的泄露。

3. 泄漏代码片段:
```java
public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        timer();
    }
    //这儿发生泄漏
    void timer(){
        new Timer().schedule(new TimerTask() {
          @Override
          public void run() {
            while(true);
          }
        },1000 ); // 1秒后启动一个任务
      }
}
```
正确代码片段:
```java
private TimerTask timerTask ;
public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        timer();
    }
    void timer(){
        timerTask = new MyTimerTask() ;
        new Timer().schedule( timerTask ,1000 ); // 1秒后启动一个任务
      }
      private static class MyTimerTask extends TimerTask{
        @Override
        public void run() {
          while(true){
            Log.d( "ttttttttt" , "timerTask" ) ;
          }
        }
      }
  @Override
  protected void onDestroy() {
    super.onDestroy();
    //取消定时任务
    if ( timerTask != null ){
      timerTask.cancel() ;
    }
  }
}
```
**注意**：在网上看到一些资料说，解决TimerTask内存泄漏可以使用在适当的时机进行Cancel。经过测试，证明单单使用在适当的时机进行Cancel，还是有内存泄漏的问题。==所以一定要用静态内部类配合使用==。

#### 4. 集合引发的内存泄漏
我们通常把一些对象的引用加入到了集合容器（比如ArrayList）中，当我们不需要该对象时，并没有把它的引用从集合中清理掉，这样这个集合就会越来越大。如果这个集合是static的话，那情况就更严重了。所以要在退出程序之前，将集合里的东西clear，然后置为null，再退出程序。

**解决方案**
- 在Activity退出之前，将集合里的东西clear，然后置为null，再退出程序。

正确代码片段:
```java
private List<String> nameList;
private List<Fragment> list;
@Override
public void onDestroy() {
    super.onDestroy();
    if (nameList != null){
        nameList.clear();
        nameList = null;
    }
    if (list != null){
        list.clear();
        list = null;
    }
}
```

#### 5. Activity Context 的不正确使用引起的内存泄漏
在Android应用程序中通常可以使用两种Context对象：Activity和Application。当类或方法需要Context对象的时候常见的做法是使用第一个作为Context参数。这样就意味着View对象对整个Activity保持引用，因此也就保持对Activty的所有的引用。

假设一个场景，当应用程序有个比较大的Bitmap类型的图片，每次旋转是都重新加载图片所用的时间较多。为了提高屏幕旋转时Activity的创建速度，最简单的方法时将这个Bitmap对象使用Static修饰。 当一个Drawable绑定在View上，实际上这个View对象就会成为这份Drawable的一个Callback成员变量。而静态变量的生命周期要长于Activity。导致了当旋转屏幕时，Activity无法被回收，而造成内存泄露。

**解决方案**
- 使用ApplicationContext代替Activity#Context，因为ApplicationContext会随着应用程序的存在而存在，而不依赖于activity的生命周期；
- 对Context的引用不要超过它本身的生命周期，慎重的对Context使用“static”关键字。Context里如果有线程，一定要在onDestroy()里及时停掉。

泄漏代码片段：
```java
private static Drawable sBackground;
@Override
protected void onCreate(Bundle state) {  
    super.onCreate(state);
    TextView tv = new TextView(this);
    tv.setText("引起的内存泄漏");  
    if (sBackground == null) {
        sBackground = getDrawable(R.drawable.large_bitmap);
    }
    tv.setBackgroundDrawable(sBackground);
    setContentView(tv);
}
```

正确代码片段：
```java
private static Drawable sBackground;
@Override
protected void onCreate(Bundle state) {  
    super.onCreate(state);
    TextView tv = new TextView(this);
    tv.setText("引起的内存泄漏");  
    if (sBackground == null) {
        sBackground = getApplicationContext().getDrawable(R.drawable.large_bitmap);
    }
    tv.setBackgroundDrawable(sBackground);
    setContentView(tv);
}
```

#### 6. 构造Adapter时，没有使用缓存的ConvertView引起的内存泄漏
初始时ListView会从Adapter中根据当前的屏幕布局实例化一定数量的View对象，同时ListView会将这些View对象缓存起来。

当向上滚动ListView时，原先位于最上面的List Item的View对象会被回收，然后被用来构造新出现的最下面的Item。

这个构造过程就是由getView()方法完成的，getView()的第二个形参View ConvertView就是被缓存起来的List Item的View对象(初始化时缓存中没有View对象则ConvertView是null)。

#### 7. BroadcastReceiver、ContentObserver、File、Cursor、Stream、Bitmap等资源引起的内存泄漏
资源性对象比如(Cursor，File文件等)往往都用了一些缓冲，我们在不使用的时候，应该及时关闭它们，以便它们的缓冲及时回收内存。它们的缓冲不仅存在于 java虚拟机内，还存在于java虚拟机外。如果我们仅仅是把它的引用设置为null,而不关闭它们，往往会造成内存泄漏。因为有些资源性对象，比如SQLiteCursor(在析构函数finalize(),如果我们没有关闭它，它自己会调close()关闭)，如果我们没有关闭它，系统在回收它时也会关闭它，但是这样的效率太低了。因此对于资源性对象在不使用的时候，应该调用它的close()函数，将其关闭掉，然后才置为null. 在我们的程序退出时一定要确保我们的资源性对象已经关闭。

调用onRecycled()：
```java
@Override
public void onRecycled() {
    reset();
    mSinglePicArea.onRecycled();
}
在View中调用reset()
public void reset() {
    if (mHasRecyled) {            
        return;
    }
    ...
    SubAreaShell.recycle(mActionBtnShell);
    mActionBtnShell = null;
    ...
    mIsDoingAvatartRedPocketAnim = false;        
    if (mAvatarArea != null) {
            mAvatarArea.reset();
    }        
    if (mNickNameArea != null) {
        mNickNameArea.reset();
    }
}
```
在自定义 View中取属性值，调用recycle()：
```java
TypedArray a  = context.getTheme().obtainStyledAttributes(attrs, R.styleable.ArcMenu,defStyleAttr,0);
a.recycle();
```
#### 8. 注册监听器的泄漏引起的内存泄漏
系统服务可以通过Context.getSystemService 获取，它们负责执行某些后台任务，或者为硬件访问提供接口。如果Context 对象想要在服务内部的事件发生时被通知，那就需要把自己注册到服务的监听器中。然而，这会让服务持有Activity的引用，如果在Activity onDestory时没有释放掉引用就会内存泄漏。

**解决方案**
- 使用ApplicationContext代替ActivityContext;
- 在Activity执行onDestory时，调用反注册;

泄漏代码片段::
```java
mSensorManager = (SensorManager) this.getSystemService(Context.SENSOR_SERVICE);
```

正确代码片段:
```java
mSensorManager = (SensorManager) getApplicationContext().getSystemService(Context.SENSOR_SERVICE);
```

下面是容易造成内存泄漏的系统服务:

泄漏代码片段:
```java
InputMethodManager imm = (InputMethodManager) context.getApplicationContext().getSystemService(Context.INPUT_METHOD_SERVICE);
```

正确代码片段:
```java
protected void onDetachedFromWindow() {        
       if (this.mActionShell != null) {
           this.mActionShell.setOnClickListener((OnAreaClickListener)null);
       }        
       if (this.mButtonShell != null) { 
           this.mButtonShell.setOnClickListener((OnAreaClickListener)null);
       }        
       if (this.mCountShell != this.mCountShell) {
           this.mCountShell.setOnClickListener((OnAreaClickListener)null);
       }
       super.onDetachedFromWindow();
}
```

#### 9. WebView引起的内存泄漏
当我们不要使用WebView对象时，应该调用它的destory()函数来销毁它，并释放其占用的内存，否则其占用的内存长期也不能被回收，从而造成内存泄露。

**解决方案**
- 为webView开启另外一个进程，通过AIDL与主线程进行通信，WebView所在的进程可以根据业务的需要选择合适的时机进行销毁，从而达到内存的完整释放。

使用中遇到问题可以参考该链接：[Android之Android WebView常见问题及解决方案汇总]( http://www.cnblogs.com/lee0oo0/p/4026774.html)


#### 10. 其他常见的引起内存泄漏原因：
- Bitmap在不使用的时候没有使用recycle()释放内存。
- 非静态内部类的静态实例容易造成内存泄漏：即一个类中如果你不能够控制它其中内部类的生命周期（譬如Activity中的一些特殊Handler等），则尽量使用静态类和弱引用来处理（譬如ViewRoot的实现）。
- 警惕线程未终止造成的内存泄露；譬如在Activity中关联了一个生命周期超过Activity的Thread，在退出Activity时切记结束线程。一个典型的例子就是HandlerThread的run方法是一个死循环，它不会自己结束，线程的生命周期超过了Activity生命周期，我们必须手动在Activity的销毁方法中调用thread.getLooper().quit();才不会泄露。
- 对象的注册与反注册没有成对出现造成的内存泄露；譬如注册广播接收器、注册观察者（典型的譬如数据库的监听）等。
- 创建与关闭没有成对出现造成的泄露；譬如Cursor资源必须手动关闭，WebView必须手动销毁，流等对象必须手动关闭等。
- 不要在执行频率很高的方法或者循环中创建对象（比如onMeasure），可以使用HashTable等创建一组对象容器从容器中取那些对象，而不用每次new与释放。
- 对Context持有一个过长的引用。对Context的引用超过它本身的生命周期。Android应用程序限制使用的堆内存是16M 。
- 注意对Context的引用不要超过它本身的生命周期 。
- Context里假设有线程，一定要在onDestory()里及时停掉。
- 当类成员变量声明为static后，它属于类而不是属于对象。假设我们将非常大的资源对象（Bitmap。context等待）声明static。那么这些资源不会被回收的回收目标。它会一直存在。因此，使用statickeyword成员变量定义时要小心。


---
## 附录
### java中的static
![image](https://pics3.baidu.com/feed/024f78f0f736afc33409f1471839eec1b74512b4.jpeg?token=33db0ecbe211c671b69179720b8e41d4&s=ED9CAA528ACE3EC846392E6303003066)
![image](https://pics3.baidu.com/feed/359b033b5bb5c9ea023ba6fe7e19b3053bf3b38c.jpeg?token=9fa34aec0b4a582efc233aefa0763daf&s=01906C32990BD04D5C5D80DA0000C0B2)
![image](https://pics2.baidu.com/feed/f3d3572c11dfa9ec028d9199c8f0f206908fc147.jpeg?token=2a78319a30f2dfd3eebeaea669541f68&s=2FA67D228BEF410B12F085D3000090B3)

成员变量随着对象的创建而存在随着对象的回收而释放。

静态变量随着类的加载而存在随着类的消失而消失。

FROM:[src](https://baijiahao.baidu.com/s?id=1636927461989417537&wfr=spider&for=pc)