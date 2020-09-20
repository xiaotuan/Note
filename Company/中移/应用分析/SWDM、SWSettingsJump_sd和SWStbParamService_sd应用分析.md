### SWDM 应用分析

由于SWDM 应用的业务代码已经进行混淆处理过，因此只能从中大概猜出这个应用应该是用于设备的注册和认证。其主要功能是监听网络连接广播，当网络连接后启动 SWService 服务，并在服务中调用 MTSdk 类的 init() 方法。由于 MTSdk 类封装在 terminal_sdk-v1.1.1_release_jdk1.7.jar 文件中，且该文件已进行混淆，故无法了解其具体功能。从 terminal_sdk-v1.1.1_release_jdk1.7.jar 的解开文件中可以看到在 MTSdk 的 init() 方法中主要是保存 IMEI 号和 IMSI 号，然后再启动 MTService 服务。具体代码如下：

```java
public static void init(Application paramApplication, String paramString1, String paramString2, String paramString3, String paramString4) {
    application = paramApplication;
    if (TextUtils.isEmpty(paramString1)) {
        MTLog.e(TAG, "imei is null");
        return;
    } 
    if (TextUtils.isEmpty(paramString4)) {
        MTLog.e(TAG, "appId is null");
        return;
    } 
    SPUtil.saveImei((Context)paramApplication, paramString1);
    if (!TextUtils.isEmpty(paramString2)) {
        SPUtil.saveImei2((Context)paramApplication, paramString2);
    } else {
        SPUtil.saveImei2((Context)paramApplication, "****");
    } 
    SPUtil.saveAppId((Context)paramApplication, paramString4);
    if (!TextUtils.isEmpty(paramString3)) {
        SPUtil.saveImsi((Context)paramApplication, paramString3);
    } else {
        SPUtil.saveImsi((Context)paramApplication, "****");
    } 
    initUpdateTime();
    LogToFile.init();
    application.startService(new Intent((Context)application, MTService.class));
    MyUnCatchExceptionHandler.init((Context)application);
}
```

对于 MTService 服务的具体功能是在每天或者网络连接（由于 MTBroadCastReceiver 为注册网络连接广播，因此这条分支永远不会执行）后进行设备认证。下面是相关代码片段：

**发送心跳定时器代码**

```java
public class MTService extends Service {
  public static String a = "MTService";
  
  private a b;
  
  @Nullable
  public IBinder onBind(Intent paramIntent) {
    return null;
  }
  
  public void onCreate() {
    MTLog.i(a, "onCreate");
    super.onCreate();
    SPUtil.saveSuccessReportTime((Context)this, 0L);
    this.b = a.a((Context)this);
    a();
  }
    
  private void a() {
    MTLog.i(a, "clientStart");
    MTSdk.getExecutor().execute(new Runnable(this) {
          public void run() {
            MTService.a(this.a).b((Context)this.a);
            UpdateUtil.resetHeartbeatAlarm((Context)this.a);
          }
        });
  }
}

public class UpdateUtil {
  public static String TAG = "UpdateUtil";
  
  public static void resetHeartbeatAlarm(Context paramContext) {
    long l = b.a;
    MTLog.i(TAG, "resetHeartbeatAlarm interval: " + l);
    Intent intent = new Intent();
    intent.setPackage(paramContext.getPackageName());
    intent.setAction("cn.richinfo.mutm.action.HEARTBEAT");
    PendingIntent pendingIntent = PendingIntent.getBroadcast(paramContext, 0, intent, 134217728);
    AlarmManager alarmManager = (AlarmManager)paramContext.getSystemService("alarm");
    alarmManager.cancel(pendingIntent);
    AlarmManagerUtil.setAlarm(paramContext, System.currentTimeMillis(), l, pendingIntent);
  }
}

public class b {
  public static long a = 86400000L;
}
```

**下面是设备认证相关代码**

```java
public class MTService extends Service {
  public static String a = "MTService";
  
  private a b;
  
  public int onStartCommand(Intent paramIntent, int paramInt1, int paramInt2) {
    MTLog.i(a, "onStartCommand");
    a(paramIntent, paramInt1, paramInt2);
    return super.onStartCommand(paramIntent, paramInt1, paramInt2);
  }
    
  private void a(Intent paramIntent, int paramInt1, int paramInt2) {
    if (null == paramIntent || null == paramIntent.getStringExtra("MT_ACTION"))
      return; 
    String str = paramIntent.getStringExtra("MT_ACTION");
    if (str.equals("cn.richinfo.mutm.action.HEARTBEAT")) {
      c();
    } else if (str.equals("android.richinfo.net.conn.CONNECTIVITY_CHANGE")) {
      long l1 = System.currentTimeMillis();
      long l2 = SPUtil.getSuccessReportTime((Context)this);
      if (l1 - l2 > b.a + 300000L)
        this.b.b((Context)this); 
    } 
  }
    
  private void c() {
    MTLog.i(a, "clientUpdate ");
    UpdateUtil.resetHeartbeatAlarm((Context)this);
    MTSdk.getExecutor().execute(new Runnable(this) {
          public void run() {
            String str1 = SPUtil.getImsi((Context)this.a);
            String str2 = MobileUtil.getIMSI((Context)this.a);
            MTLog.i(MTService.a, "regImsi: " + str1);
            MTLog.i(MTService.a, "currentImsi: " + str2);
            if (str1.equals(str2)) {
              MTLog.i(MTService.a, "update regImsi: " + str1);
              MTService.a(this.a).a().b();
            } else {
              MTService.a(this.a).b((Context)this.a);
              SPUtil.saveImsi((Context)this.a, str2);
            } 
          }
        });
  }
}

public class a {
  private static b a;
  
  private static final String[] b = new String[] { "3303.xml" };
  
  private Context c;
  
  private static a d;
  
  private static org.a.b.a.a.a e = null;
  
  private a(Context paramContext) {
    this.c = paramContext;
  }
  
  public static final synchronized a a(Context paramContext) {
    if (d == null)
      d = new a(paramContext); 
    return d;
  }
  
  public void b(Context paramContext) {
    MTLog.i("LeshanSdk", "leshanStart ");
    String str1 = "coap://localhost:5683";
    byte[] arrayOfByte1 = null;
    byte[] arrayOfByte2 = null;
    String str2 = null;
    boolean bool1 = false;
    String str3 = null;
    boolean bool2 = false;
    Float float_1 = null;
    Float float_2 = null;
    Float float_3 = Float.valueOf(1.0F);
    String str4 = SPUtil.getImei(paramContext) + "-" + SPUtil.getImei2(paramContext) + "-" + SPUtil.getImsi(paramContext) + "-" + "1.1.1";
    if (MTSdk.isDebugMode()) {
      str1 = "coap://shipei.fxltsbl.com:5683";
    } else {
      str1 = "coap://m.fxltsbl.com:5683";
    } 
    try {
      String str = AesCoder.getInstance().encrypt(str4);
      Log.i("LeshanSdk", "endpoint " + str);
      a(paramContext, str, str2, bool1, str3, bool2, false, str1, arrayOfByte1, arrayOfByte2, float_1, float_2, float_3.floatValue());
    } catch (Exception exception) {
      Log.i("LeshanSdk", "Exception " + exception.getMessage());
    } 
  }
    
}
```

**下面是注册相关代码**

```java
public class c {
  
  private boolean d() {
    MTLog.i(a, "begin register");
    e e = f.a(this.e);
    b b = e.b.values().iterator().next();
    if (b == null)
      return false; 
    MTLog.i(a, "Trying to register to {} ..." + b.b());
    r r = new r(this.c, Long.valueOf(b.a), "1.0", b.b, null, org.a.b.a.g.a.a(this.e.values(), null), this.j);
    n n = (n)this.d.a(b.a(), b.c(), (t)r, 120000L);
    if (n == null) {
      this.i = null;
      if (this.g != null)
        this.g.a(b); 
    } else if (n.d()) {
      this.i = n.c();
      MTLog.i(a, "Registered with location: " + this.i);
      MTLog.i(a, "check if MainLooper: " + ((Looper.getMainLooper() == Looper.myLooper()) ? 1 : 0));
      if (this.g != null)
        this.g.a(b, n.c()); 
    } else {
      this.i = null;
      if (this.g != null)
        this.g.a(b, n.a(), n.b()); 
    } 
    return (this.i != null);
  }
}
```



### SWSettingsJump_sd 应用分析

SWSettingsJump_sd 应用的主要功能是实现一个和原始 Settings 应用一样的包名的应用，当第三方应用调用原始 Settings 应用时，将通过该应用跳转到朝歌的设置应用。

核心代码如下所示：

```java
@Override
protected void onResume() {
    startSetting();	
    super.onResume();
}

// 启动设置界面
private void startSetting() {
    Intent intent = new Intent();
    intent.setAction("android.settings.SETTINGS");
    intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
    startActivity(intent);
    finish();
}
```



### SWStbParamService_sd 应用分析

SWStbParamService_sd 应用主要功能是提供第三方调用 DevInfoManager 对象的 getValue() 方法的远程调用接口。

其核心代码如下所示：

```java
private final IStbParmService.Stub mBinder = new IStbParmService.Stub() {

    @Override
    public String getStbParameter(String parmName) throws RemoteException {
        String parmValue = null;
        Log.d(TAG, "======================parmName:"+parmName);
        parmValue = mDevInfoManager.getValue(parmName);
        Log.d(TAG, "============parmValue="+parmValue);
        return parmValue;
    }
};
```