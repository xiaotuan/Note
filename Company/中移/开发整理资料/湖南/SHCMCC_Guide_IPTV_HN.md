[toc]

### 1. 谁在启动我？

查看应用的 `AndroidManifest.xml` 文件可以知道该应用的启动界面是 `IptvMainActivity`：

```xml
<activity
          android:name="com.shcmcc.chinamobile.activity.IptvMainActivity"
          android:launchMode="singleInstance">
    <intent-filter>
        <action android:name="cn.cmvideo.action.IPTVGUIDE" />
        <action android:name="android.intent.action.MAIN" />

        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.LAUNCHER" />
        <category android:name="chinamobile.sdk.appinfo" />
    </intent-filter>
</activity>
```

通过搜索 `cn.cmvideo.action.IPTVGUIDE` 字符串得到如下结果：

```shell
$ grep -rn "ACTION_IPTV" .
./SHCMCC_CWMPService_HN/src/net/sunniwell/cwmp/protocol/cmd/IPTVPlayer.java:12:    private static final String ACTION_IPTV_PLAY = "com.chinamobile.action.IPTV_PLAY";
./SHCMCC_CWMPService_HN/src/net/sunniwell/cwmp/protocol/cmd/IPTVPlayer.java:13:    private static final String ACTION_IPTV_PLAY_STATE = "com.chinamobile.action.IPTV_PLAY_STATE";
./SHCMCC_CWMPService_HN/src/net/sunniwell/cwmp/protocol/cmd/IPTVPlayer.java:14:    private static final String ACTION_IPTV_STOP = "com.chinamobile.action.IPTV_STOP";
./SHCMCC_CWMPService_HN/src/net/sunniwell/cwmp/protocol/cmd/IPTVPlayer.java:66:            this.mContext.registerReceiver(this.mPlayBroadcastReceiver, new IntentFilter(ACTION_IPTV_PLAY_STATE));
./SHCMCC_CWMPService_HN/src/net/sunniwell/cwmp/protocol/cmd/IPTVPlayer.java:81:            intent.setAction(ACTION_IPTV_PLAY);
./SHCMCC_CWMPService_HN/src/net/sunniwell/cwmp/protocol/cmd/IPTVPlayer.java:90:            intent.setAction(ACTION_IPTV_STOP);
./SHCMCC_Startup_HN/src/com/chinamobile/startup/activity/StartUpMainActivity.java:37:    private static final String ACTION_IPTV = "cn.cmvideo.action.IPTVGUIDE";
./SHCMCC_Startup_HN/src/com/chinamobile/startup/activity/StartUpMainActivity.java:155:        return ACTION_IPTV;
```

> 提示：通过搜索发现 `IptvMainActivity` 界面只通过 `action` 方法启动，没有其他方式启动了。

#### 1.1 SHCMCC_Startup_HN 应用的 StartUpMainActivity.java

**SHCMCC_Startup_HN/src/com/chinamobile/startup/activity/StartUpMainActivity.java**

`StartUpMainActivity` 中定义了如下常量：

```java
private static final String ACTION_IPTV = "cn.cmvideo.action.IPTVGUIDE";
```

`getDefaultAction()` 方法会根据 `serviceType` 返回对应的 `action` 值：

```java
private String getDefaultAction() {
    String serviceType = STBManagerUtil.getInstance(this).getValue(Contants.SERVICE_TYPE);
    if (serviceType == null || !Contants.TYPE_IPTV.equals(serviceType)) {
        return ACTION_OTT;
    }
    return ACTION_IPTV;
}
```

在 `startGuideApp()` 方法中会调用 `getDefaultAction()` 启动 `SHCMCC_Guide_IPTV_HN` 应用的 `IptvMainActivity` 。

```java
private boolean startGuideApp() {
    boolean isStartApp = false;
    String pName = this.mPackageName;
    String aName = this.mAction;
    String cName = "";
    this.mDefaultAction = getDefaultAction();
    boolean flag = true;
    if ("null".equals(aName)) {
        aName = "";
    }
    if ("null".equals(pName)) {
        pName = "";
    }
    if (TextUtils.isEmpty(aName) && TextUtils.isEmpty(pName)) {
        aName = this.mSharePreference.getValue(this.mActionKey, this.mDefaultAction);
        pName = this.mSharePreference.getValue(this.mPackageNameKey, "");
        flag = false;
    }
    L.i("startGuideApp pName:" + pName + "---aName:" + aName + "---cName:" + cName);
    if (!TextUtils.isEmpty(pName)) {
        if (pName.contains("/")) {
            String[] tmp = pName.split("/");
            pName = tmp[0];
            if (tmp[1].startsWith(".")) {
                cName = tmp[0] + tmp[1];
            } else {
                cName = tmp[1];
            }
        }
        L.i("startGuideApp1  pName:" + pName + "---aName:" + aName + "---cName:" + cName);
        isStartApp = IntentUtils.startAppWithPackageName(this, pName, cName);
    }
    if (!(isStartApp || TextUtils.isEmpty(aName))) {
        isStartApp = IntentUtils.startAppWithAction(this, aName, "");
    }
    if (!isStartApp) {
        isStartApp = IntentUtils.startAppWithAction(this, this.mDefaultAction, "");
    }
    ...
    return isStartApp;
}
```

### 2. 启动界面：IptvMainActivity.java

#### 2.1 onCreate() 方法

在该方法中主要内容就是注册登录状态广播接收器。

```java
protected void onCreate(Bundle arg0) {
    ......
    RegisterBroadcastUtil.registerLoginBroadcast(this, this);
}
```

`registerLoginBroadcast()` 方法的实现代码如下：

```java
public static void registerLoginBroadcast(Context context, MessageInterface messageInterface) {
    L.i("============开机初始化，注册登录广播，用来接受登录的需求 registerLoginBroadcast=======");
    IntentFilter filter = new IntentFilter();
    filter.addAction(Constants.BROADCAST_OUT_LOGIN_SUCESS);
    filter.addAction(Constants.BROADCAST_OUT_LOGIN_FAILURE);
    filter.addAction(Constants.ACTION_LOGIN_DOWNLOADING);
    filter.addAction(Constants.ACTION_SHCMCC_XIRICHANNEL_REGIST);
    filter.setPriority(Integer.MAX_VALUE);
    if (mGuideLoginBroadcast == null) {
        mGuideLoginBroadcast = new GuideLoginBroadcast(messageInterface);
    }
    context.registerReceiver(mGuideLoginBroadcast, filter);
}
```

`GuideLoginBroadcast.java` 相关代码如下：

```java
public class GuideLoginBroadcast extends BroadcastReceiver {
	......
    public void onReceive(Context context, Intent intent) {
        L.i("=======登录广播接收者 action=" + intent.getAction());
        if (intent.getAction().equals(Constants.ACTION_SHCMCC_XIRICHANNEL_REGIST)) {
            String from = intent.getStringExtra("from");
            L.i("=======from=" + from);
            SystemProperties.set("epg.xiri.regist", "" + from);
            return;
        }
        this.mInterface.cancelLoginTimeOut();
        if (intent.getAction().equals(Constants.BROADCAST_OUT_LOGIN_SUCESS)) {
            String businessExpireTime = intent.getStringExtra("businessExpireTime");
            String businessExpireDesc = intent.getStringExtra("businessExpireDesc");
            L.i(" 收到广播cn.cmvideo.action.LOGIN_SUCESS");
            this.mInterface.onLoginSuccess(businessExpireTime, businessExpireDesc);
        } else if (intent.getAction().equals(Constants.ACTION_LOGIN_DOWNLOADING)) {
            L.i("======  接收登录失败广播，并处理登录失败广播业务 ======");
            String msg = intent.getStringExtra("msg");
            L.i(" 收到广播cn.cmvideo.action.LOGIN_DOWNLOADING： 展示信息：" + msg);
            this.mInterface.onMessageCallBack(msg);
        } else if (intent.getAction().equals(Constants.BROADCAST_OUT_LOGIN_FAILURE)) {
            Bundle bundle = intent.getExtras();
            String code = bundle.getString("code");
            String desc = bundle.getString("desc");
            L.i(" 收到广播cn.cmvideo.action.LOGIN_FAILURE： code=" + code);
            L.i(" 收到广播cn.cmvideo.action.LOGIN_FAILURE： desc=" + desc);
            this.mInterface.onLoginFail(code, desc);
        }
    }
}
```

再来看下 `MessageInterface` 接口方法：

```java
public interface MessageInterface {
    void cancelLoginTimeOut();

    void onLoginFail(String str, String str2);

    void onLoginResultCallBack(boolean z);

    void onLoginSuccess(String str, String str2);

    void onMessageCallBack(String str);

    void onStartApp();
}
```

从上面的代码可以看出 `IptvMainActivity ` 注册了登录状态的监听广播，而监听广播通过 `MessageInterface` 接口反馈给 `IptvMainActivity`。

#### 2.1 onResume() 方法

```java
protected void onResume() {
    super.onResume();
    L.i("==== onResume =====" + this);
    isActShow = true;
    this.isLoginSuccess = false;
    L.i("=== onResume isActShow:" + isActShow + "---isLoginSuccess:" + this.isLoginSuccess);
    initData();
}
```

在 `onResume()` 方法中调用了 `initData()` 方法。`initData()` 代码如下：

```java
private void initData() {
    Parameter pm = new Parameter(this);
    String stb_type = Parameter.getProp("ro.product.type", "");
    String flag = pm.getParameter("initialization_wizard");
    L.d("================= initialization_wizard = " + flag);
    if (flag == null || flag.equals("0")) {
        updateTs((int) R.string.checking);
        L.d("当前未开通，等待开通，时间为:60s--->stb_type:" + stb_type);
        if (stb_type.equals("1")) {
            IntentUtils.startPublicGuideActivity(this);
        } else {
            IntentUtils.startGuideActivity(this);
        }
        isWaitLogin = true;
        L.i("当前未开通，等待开通, 登录标记 isWaitLogin：" + isWaitLogin);
        this.myHandler.removeMessages(1);
        this.myHandler.sendEmptyMessageDelayed(1, 60000);
        return;
    }
    int isLogin = SystemProperties.getInt("epg.login", -1);
    L.d("校验当前登录情况，登录标记 isLogin=" + isLogin);
    if (isLogin == 1) {
        this.myHandler.removeMessages(1);
        isWaitLogin = false;
        runOnUiThread(new Runnable() {
            public void run() {
                ShowBusinessExpireModel.showBusinessExpireDlg(IptvMainActivity.this, IptvMainActivity.this, IptvMainActivity.this.mBusinessExpireTime, IptvMainActivity.this.mBusinessExpireDesc);
            }
        });
        return;
    }
    L.i("========= 启动登录服务 ========= false");
    updateTs((int) R.string.logining);
    IntentUtils.startLoginService(this, false);
    isWaitLogin = true;
    L.i("当前未登录，启动登录服务， 登录标记 isWaitLogin：" + isWaitLogin);
    L.d("当前未登录，启动登录服务，并等待登录响应，时间为：60s");
    this.myHandler.removeMessages(1);
    this.myHandler.sendEmptyMessageDelayed(1, 60000);
}
```

通过判断 Settings 数据库 secure 表中的 `initialization_wizard` 的值判断设备是否已经走完初始化，如果 `initialization_wizard` 的值不为 1 则启动向导页面引导用户走完向导设置。在 `IPTV` 设备中会调用 `IntentUtils.startGuideActivity(this);` 方法走完开机向导。

如果设备已经走完开机向导，则判断当前是否正在登录，如果正在登录，则只需要等待即可，否则启动登录服务：

```java
IntentUtils.startLoginService(this, false);
```

#### 2.3 登录成功回调：onLoginSuccess()

```java
public void onLoginSuccess(final String businessExpireTime, final String businessExpireDesc) {
    L.i("=== onLoginSuccess:" + this);
    L.i("登录成功的接口回调  查看登录状态 isWaitLogin:" + isWaitLogin + " isActShow:" + isActShow + "--isLoginSuccess:" + this.isLoginSuccess);
    if (isWaitLogin || isActShow || this.isLoginSuccess) {
        isActShow = true;
        this.myHandler.removeMessages(1);
        updateTs(getResources().getString(R.string.login_sucess));
        runOnUiThread(new Runnable() {
            public void run() {
                ShowBusinessExpireModel.showBusinessExpireDlg(IptvMainActivity.this, IptvMainActivity.this, businessExpireTime, businessExpireDesc);
            }
        });
    }
}
```

从代码中可以看出它只更新了界面提示，并弹出一个对话框。通过查看 `ShowBusinessExpireModel.showBusinessExpireDlg()` 方法，发现在用户点击确认按钮后会调用 `IptvMainActivity` 中 `MessageInterface` 接口的 `onStartApp()` 方法。

#### 2.4 登录失败回调：onLoginFail()

```java
public void onLoginFail(String code, String desc) {
    L.i("接口回调 返回登录失败...... 登录标记isWaitLogin:" + isWaitLogin);
    if (isWaitLogin) {
        ...
        new Thread(new Runnable() {
            public void run() {
                try {
                    Thread.sleep(5000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                Parameter pm = new Parameter(IptvMainActivity.this);
                String username = pm.getParameter("ntvuseraccount") + pm.getParameter("ntvusersuffix");
                String password = pm.getParameter("ntvuserpassword");
                IntentUtils.startDiagnoseApp(IptvMainActivity.this, "AUTHCHECK", IptvMainActivity.this.getResources().getString(R.string.authent_open_error, new Object[]{username, password}));
            }
        }).start();
    }
}
```

可以看出在登录失败后会启动设备诊断应用。

#### 2.5 登录成功启动桌面：onStartApp()

```java
public void onStartApp() {
    myHandler.sendEmptyMessage(0);
}
```

`onStartApp()` 方法发送个 Handler 消息，下面是 Handler 处理该消息的代码：

```java
Handler myHandler = new Handler() {
    public void handleMessage(Message msg) {
        switch (msg.what) {
            case MSG_START_APP:
                updateTs((int) R.string.login_sucess);
                if (mStartAppManager == null) {
                    mStartAppManager = new StartAppManager(IptvMainActivity.this, IptvMainActivity.this);
                }
                L.i("=== myHandler isActShow:" + isActShow);
                if (isActShow) {
                    mStartAppManager.startApp();
                } else {
                    L.d("启动第三方界面时候发现当前界面已经不存在 非法启动 isActShow" + isActShow);
                }
                break;
    ...
}
```

在消息处理中调用了 `StartAppManager` 类的 `startApp()` 方法，下面是 `startApp()` 方法的代码：

```java
public void startApp() {
    L.i("======startApp()=====");
    boolean b = false;
    if (null == null) {
        String epgActionName = SystemProperties.get("epg.action.name", "");
        L.i("======startApp()===== action : " + epgActionName);
        if (TextUtils.isEmpty(epgActionName) || "null".equals(epgActionName)) {
            String pageName = SystemProperties.get("epg.package.name", "");
            L.i("======startApp()===== pagename : " + pageName);
            if (!TextUtils.isEmpty(pageName)) {
                b = startAppWithPackageName(pageName, null, null);
            }
        } else {
            b = startAppWithAction(epgActionName, null);
        }
        if (!b && !startAppWithAction("cn.cmvideo.action.ITV", null)) {
            String epgPackageNameFlag = SystemProperties.get(Contants.EPG_PACKAGENAME_FLAG, "");
            L.i("======startApp()===== getprop [epg.packagename.flag]: " + epgPackageNameFlag);
            if (!"1".equals(epgPackageNameFlag)) {
                String desc = this.mContext.getResources().getString(R.string.initial_application_exception_upgrade, new Object[]{"android.app.chinamobile.ott.itv"});
                this.mMessageInterface.onMessageCallBack(desc);
                IntentUtils.startDiagnoseApp(this.mContext, "APKCHECK", desc);
            }
        }
    }
}
```

从日志输出中可以看出最后是通过 `startAppWithAction("cn.cmvideo.action.ITV", null)` 方法启动桌面应用的。

### 3. 登录服务：IptvLoginMainService.java

#### 3.1 谁启动我，怎么启动的

登录服务是在 `IptvMainActivity` 的  `initData()` 方法中启动的。通过 `IntentUtils` 类的 `startLoginService()` 方法启动。

#### 3.2 onCreate() 方法

```java
public void onCreate() {
    super.onCreate();
    L.i("LoginMainService====== onCreate( ======");
    APK_UPGRADE_URL = new Parameter(this).getParameter("upgrade_url");
    L.i("获取升级服务器地址：" + APK_UPGRADE_URL);
    RegisterBroadcastUtil.registerXmppBroadcast(this);
}
```

在 `onCreate()` 中通过 Settings 数据库 secure 表中的 `upgrade_url` 的值获取升级服务器地址，并注册了登录会话广播：

```java
public static void registerXmppBroadcast(Context context) {
    L.i("============开机初始化，注册登录广播，用来接受登录的需求 registerLoginBroadcast=======");
    IntentFilter filter = new IntentFilter();
    filter.addAction(Constants.BROADCAST_IN_PAIR_CONNECT);
    filter.addAction(Constants.BROADCAST_IN_PAIR_DISCONNECT);
    filter.addAction(Constants.BROADCAST_IN_GET_WAN_MATCHCODE);
    filter.addAction(Constants.BROADCAST_IN_VERIFY_WAN_MATCHCODE);
    filter.addAction(Constants.BROADCAST_CHECK_UPDATE_COMPLETE);
    filter.setPriority(Integer.MAX_VALUE);
    if (mLoginXmppBroadcast == null) {
        mLoginXmppBroadcast = new LoginXmppBroadcast();
    }
    context.registerReceiver(mLoginXmppBroadcast, filter);
}
```

`LoginXmppBroadcast` 广播代码如下：

```java
public class LoginXmppBroadcast extends BroadcastReceiver {
    public void onReceive(Context paramContext, Intent paramIntent) {
        String action = paramIntent.getAction();
        L.i("====处理广播LoginXmppBroadcast === Action=" + action);
        if (action != null && !"".equals(action)) {
            Bundle bundle;
            if (Constants.BROADCAST_IN_PAIR_CONNECT.equalsIgnoreCase(action) || Constants.BROADCAST_IN_PAIR_DISCONNECT.equalsIgnoreCase(action)) {
                bundle = paramIntent.getExtras();
                if (bundle != null) {
                    String userId = bundle.getString("userid", "");
                    String deviceId = bundle.getString("deviceid", "");
                    String token = bundle.getString("token", "");
                    String deviceType = bundle.getString("deviceType", "");
                    String connectType = bundle.getString("connectType", "");
                    L.i("===userId=" + userId + ",deviceId=" + deviceId + ",token=" + token + ",deviceType=" + deviceType + ",connectType=" + connectType);
                    ImplicitLoginModel.startImplicitLogin(paramContext, IptvLoginMainService.mStb, action, userId, deviceId, token, deviceType, connectType);
                }
            } else if (action.equalsIgnoreCase(Constants.BROADCAST_IN_GET_WAN_MATCHCODE)) {
                GetWanMatchCodeModel.getWanMatchCode(paramContext, IptvLoginMainService.mStb);
            } else if (action.equalsIgnoreCase(Constants.BROADCAST_IN_VERIFY_WAN_MATCHCODE)) {
                bundle = paramIntent.getExtras();
                if (bundle != null) {
                    VerifyMatchCodeModel.verifyMatchCode(paramContext, bundle.getString("matchCode", ""), bundle.getString("terminalId", ""), IptvLoginMainService.mStb);
                }
            } else if (action.equalsIgnoreCase(Constants.BROADCAST_CHECK_UPDATE_COMPLETE)) {
                CheckCmccApkUtils.isCmccApkCompleted = true;
                int result = paramIntent.getIntExtra(Constant.KEY_RESULT, -1);
                L.i("==cmccAPK check completed:result=" + result + ",message=" + paramIntent.getStringExtra("message "));
            }
        }
    }
}
```

#### 3.3 onStartCommand() 方法

```java
public int onStartCommand(Intent intent, int flags, int startId) {
    L.i("LoginMainService ====== onStartCommand===intent：" + intent + ",flags：" + flags + ",startId：" + startId);
    if (intent == null) {
        L.d("intent is null, the service maybe be killed by system, so reload data");
        reload();
    } else {
        Bundle bundle = intent.getExtras();
        String account = bundle.getString("username", "");
        String password = bundle.getString("password", "");
        L.i("LoginMainService====== 启动登录 ===== account：1" + account + "3,password:os" + password);
        login(account, password);
    }
    return 1;
}
```

当 `intent` 为 null 时，调用 `reload()` 方法从存储中获取数据封装 `IdentityBean` 对象。如果 `intent` 不为空，则调用 `login()` 方法执行登录操作。

```java
private void login(String account, String password) {
    if (this.isLogining) {
        L.i("当前有登录任务在执行 isLogining：" + this.isLogining);
        return;
    }
    this.isLogining = true;
    if (account.equals("") || password.equals("")) {
        L.d("登录参数错误，服务无法正常运行");
        this.isLogining = false;
        return;
    }
    LoginModel.login(this, this, account, password);
}
```

`login()` 方法中调用 `LoginModel` 的静态方法 `login()` 执行登录。

```java
public class LoginModel {
    public static void login(Context context, final LoginResultProcessInterface loginResultProcess, String account, final String password) {
        ...
        new LoginManager(context).login(attrs, new LoginCallback() {
            public void finish(LoginBeen login) {
                if (login == null) {
                    L.i("登陆返回结果发现登录实体类为null");
                } else {
                    L.i("登陆返回结果查看最终组装的信息:" + login.toString());
                }
                loginResultProcess.loginResultProcessCallBack(stbid, password, login);
            }
        });
    }
}
```

从上面的代码中可以看出最后执行登录的是 `LoginManager` 的 `login()` 方法。

```java
public void login(final Map<String, Object> attrs, final LoginCallback callback) {
    if (this.mThread != null && this.mThread.isAlive()) {
        this.mThread.interrupt();
    }
    this.mThread = new Thread(new Runnable() {
        public void run() {
            LoginBeen mLoginBeen = null;
            try {
                L.i("------ 开始请求登录服务器 ------");
                String loginRespXml = request(attrs, true);
                L.d("请求登录服务器返回的结果 loginRespXml:" + loginRespXml);
                Document document = LoginManager.xml2Doc(loginRespXml);
                if (document == null) {
                    L.i(" 登录服务器返回的结果为null");
                } else {
                    L.i(" 登录服务器返回的结果不为null");
                    mLoginBeen = ParseLogin.parseLoginAuth(document);
                    mLoginBeen.setLoginRespXml(loginRespXml);
                }
            } catch (Exception e) {
                L.e(e, "");
            } finally {
                callback.finish(mLoginBeen);
            }
        }
    });
    mThread.start();
}
```

在 `login()` 方法中通过调用 `request` 方法进行登录请求。从下面的代码中可以看出登录请求使用了两个地址，一个地址不行，则换另一个地址。

```java
private String request(Map<String, Object> attrs, boolean needxml) {
    String result = null;
    for (int i = 0; i < 2; i++) {
        result = netRequest(this.SCSP_URL, attrs);
        if (!TextUtils.isEmpty(result)) {
            return result;
        }
    }
    return netRequest(this.SCSP_URL_2, attrs);
}

private String netRequest(String url, Map<String, Object> attrs) {
    return netRequest(url, getLoginXml(attrs));
}

private String netRequest(String url, String loginXml) {
    L.d("request SCSP_URL/bak_SCSP_URL=" + url);
    HttpParams httpParameters = new BasicHttpParams();
    HttpConnectionParams.setConnectionTimeout(httpParameters, 5000);
    HttpConnectionParams.setSoTimeout(httpParameters, 30000);
    HttpClient client = new DefaultHttpClient(httpParameters);
    HttpPost post = new HttpPost(url);
    try {
        L.d("====== 请求的报文 ======：" + loginXml);
        post.setEntity(new StringEntity(loginXml, "UTF-8"));
        HttpResponse response = client.execute(post);
        L.i("response code=" + response.getStatusLine().getStatusCode());
        if (response.getStatusLine().getStatusCode() == CMD.PAY_NEXT) {
            String data = EntityUtils.toString(response.getEntity(), "UTF-8");
            L.d("====== 返回的报文 ======：" + data);
            if (data != null && !"".equals(data)) {
                return data;
            }
        }
        Thread.sleep(1000);
        post.abort();
        client.getConnectionManager().shutdown();
    } catch (Exception e) {
        L.i(e + "");
        post.abort();
    } finally {
        post.abort();
        client.getConnectionManager().shutdown();
    }
    SystemClock.sleep(1000);
    return null;
}
```

登录请求地址获取方法如下：

```java
public LoginManager(Context context) {
    this.SCSP_URL = Contants.homePase(context);
    this.SCSP_URL_2 = Contants.homePase2(context);
}

public static String homePase(Context context) {
    String homepage = new Parameter(context).getParameter("iptv_home_page");
    return homepage + (homepage.endsWith("/") ? "" : "/") + "scspProxy";
}

public static String homePase2(Context context) {
    String homepage_2 = new Parameter(context).getParameter("iptv_home_page2");
    return homepage_2 + (homepage_2.endsWith("/") ? "" : "/") + "scspProxy";
}

public String getParameter(String name) {
    try {
        String value = Secure.getString(this.mContext.getContentResolver(), name);
        if (!name.equals("ntvuserpassword")) {
            return value;
        }
        if (AESTools.isEncrypt(value)) {
            return AESTools.Decrypt(value);
        }
        setParameter(name, value);
        return value;
    } catch (Throwable e) {
        CMCCLogger.error(e);
        return null;
    }
}
```

当登录操作完成后会调用 `LoginCallback` 接口的 `finish()` 方法返回到 `LoginModel` 类的回调中。

```java
new LoginManager(context).login(attrs, new LoginCallback() {
    public void finish(LoginBeen login) {
        if (login == null) {
            L.i("登陆返回结果发现登录实体类为null");
        } else {
            L.i("登陆返回结果查看最终组装的信息:" + login.toString());
        }
        loginResultProcess.loginResultProcessCallBack(stbid, password, login);
    }
});
```

在 `LoginModel` 类中通过 `LoginCallback` 接口的回调方法 `loginResultProcessCallBack` 返回到 `IptvLoginMainService` 类中。

```java
public void loginResultProcessCallBack(final String stbid, final String password, final LoginBeen login) {
    L.i("++++ =========  --- 进入容灾流程---  ========= ++++");
    new Thread(new Runnable() {
        public void run() {
            if (IptvLoginMainService.this.mDisasterRecoveryManager == null) {
                IptvLoginMainService.this.mDisasterRecoveryManager = new DisasterRecoveryManager(IptvLoginMainService.this.getApplicationContext());
            }
            boolean isEncountDisasterRecovery = IptvLoginMainService.this.mDisasterRecoveryManager.checkDisasterRecovery(login);
            L.i("  本次登录的容灾标记：" + isEncountDisasterRecovery);
            LoginBeen loginEnd = IptvLoginMainService.this.mDisasterRecoveryManager.dealDisasterRecovery(IptvLoginMainService.this, login, isEncountDisasterRecovery, stbid, password);
            L.i("  上一次登录的容灾标记 isLastDisasterRecovery=" + IptvLoginMainService.isLastDisasterRecovery);
            if (loginEnd != null) {
                L.i(" 处理完容灾后，login实体信息变更为：" + loginEnd.toString());
            }
            if (!IptvLoginMainService.isLastDisasterRecovery || (loginEnd != null && !loginEnd.isEncountDisasterRecovery())) {
                if (IptvLoginMainService.this.mRetry_login_timer != null) {
                    IptvLoginMainService.this.mRetry_login_timer.cancel();
                }
                if (loginEnd != null) {
                    IptvLoginMainService.this.loginHaveMessage(stbid, password, loginEnd);
                } else {
                    IptvLoginMainService.this.loginNoMessage();
                }
                IptvLoginMainService.this.isLogining = false;
            } else {
                L.i("上次登录为容灾，本次登录仍然失败，忽略后续处理！");
                IptvLoginMainService.this.isLogining = false;
            }
        }
    }).start();
}
```

通过分析 `loginResultProcessCallBack()` 方法可以知道如果登录不成功，会调用 `loginHaveMessage()` 方法，登录成功则调用 `loginNoMessage()`。先来看下 `loginHaveMessage()` 方法：

```java
private void loginHaveMessage(String stbid, String password, LoginBeen login) {
    long time = System.currentTimeMillis();
    if (login.getResult().equals("0")) {
        CmccApkResult cmccApkResult = CmccApkResult.checkCmccApk(this, login);
        if (!cmccApkResult.isResultOk()) {
            Tools.startDiagnoseOrSetting(this, "APKCHECK", cmccApkResult.combineDisplayString().replace("\n", ""));
        }
        this.isReopenAcount = false;
        this.mReopenAcountCount = 0;
        mStb = new IdentityBean();
        mStb.setUserId(login.getUserId());
        mStb.setToken(login.getToken());
        mStb.setDeviceId(stbid);
        CheckCmccApkUtils.checkCmccApk(this, login.getPackagename(), login.getActionname(), APK_UPGRADE_URL);
        UpdatePropUtils.updateStbProp(this, this.mHandler, "1", mStb.getUserId(), mStb.getToken(), login.getMessageJID(), login.getUserLocal(), login.getIndexWSUrl(), login.getECCode(), login.getCopyrighteId(), login.getCmccIndexUrl(), login.getAuthCode(), login.getECCoporationCode(), login.getPackagename(), login.getActionname(), login.getCpCode(), login.getCityCode(), login.getUserGroup(), login.getAccountIdentity(), login.getBusinessParam(), login.isEncountDisasterRecovery());
        L.i("login send broadcast cn.cmvideo.action.LOGIN_SUCESS ");
        IntentUtils.startLoginSuccessBroadcast(this, login);
        L.i("login analytical Duration : " + (System.currentTimeMillis() - time));
        if (login.isEncountDisasterRecovery()) {
            this.mRetry_login_timer = new Timer();
            this.mRetry_login_timer.schedule(new TimerTask() {
                public void run() {
                    L.i("登录容灾，定时重试登录！");
                    Parameter mParam = new Parameter(IptvLoginMainService.this);
                    String stbAccount = mParam.getParameter("ntvuseraccount");
                    String stbAcountSuffix = mParam.getParameter("ntvusersuffix");
                    IptvLoginMainService.this.login(stbAccount + stbAcountSuffix, mParam.getParameter("ntvuserpassword"));
                }
            }, DisasterRecoveryRetryInterval, DisasterRecoveryRetryInterval);
        }
        isLastDisasterRecovery = login.isEncountDisasterRecovery();
    } else if (this.isReopenAcount || this.mReopenAcountCount > 10 || !(login.getResult().equals("8027") || login.getResult().equals("900000") || login.getResult().equals("900056"))) {
        L.i("登录失败，原因是:" + login.getResultDesc() + ",请重新登录!");
        UpdatePropUtils.updateStbProp(this, this.mHandler, "0", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", false);
        IntentUtils.startLoginFaliBroadcast(this, login.getResult(), login.getResultDesc());
    } else {
        this.mReopenAcountCount++;
        L.i("login: 密码错误，重新验证帐号!");
        StbOpen.validateSTBID(this, new StbOpenCallBack() {
            public void onFinish(boolean isOK, int errorcode, String errMsg) {
                IptvLoginMainService.this.isReopenAcount = true;
                Parameter mParam = new Parameter(IptvLoginMainService.this);
                if (errorcode == 0) {
                    IptvLoginMainService.this.isReopenAcount = false;
                    String stbAccount = mParam.getParameter("ntvuseraccount");
                    String stbAcountSuffix = mParam.getParameter("ntvusersuffix");
                    IptvLoginMainService.this.login(stbAccount + stbAcountSuffix, mParam.getParameter("ntvuserpassword"));
                    return;
                }
                IptvLoginMainService.this.isReopenAcount = false;
                L.i("验证失败，需要重新开通!");
                mParam.setParameter("ntvuseraccount", "");
                mParam.setParameter("ntvusersuffix", "");
                mParam.setParameter("ntvuserpassword", "");
                mParam.setParameter("initialization_wizard", "0");
                IntentUtils.startGuideAppActivity(IptvLoginMainService.this);
            }
        });
    }
    L.i("通知升级模块执行升级请求 to notify start rom upgrade");
    String rightChange = login.getRightChange();
    if ("1".equals(rightChange)) {
        SystemProperties.set("epg.product.model", login.getChangeTerminalModel());
    } else {
        SystemProperties.set("epg.product.model", "");
    }
    IntentUtils.sendStopRomUpgradeBroadcast(this);
    IntentUtils.sendStartRomUpgradeBroadcast(this, rightChange);
    AlarmManagerUtil.setAlarm(getApplicationContext());
}
```

在 `loginHaveMessage()` 方法中，登录成功后会发送登录成功广播，并定时重新登录；登录失败则会发送登录失败广播；其他错误时，则会跳转到开机向导界面 `GuideMainActivity`。

### 4. 获取账号信息：GuideMainActivity

`GuideMainActivity` 界面主要是为了获取如下信息：

```java
Parameter mParam = new Parameter(this.mContext);
mParam.setParameter("ntvuseraccount", stbAccount);
mParam.setParameter("ntvusersuffix", stbAcountSuffix);
mParam.setParameter("ntvuserpassword", stbPassword);
mParam.setParameter("initialization_wizard", "1");
```

#### 4.1 onResume() 方法

```java
protected void onResume() {
    super.onResume();
    L.i("============= GuideMainActivity onResume()====== isRunning:" + this.isRunning);
    if (!this.isRunning) {
        this.isRunning = true;
        this.mWebTvSubEngine.excuteWebTv(this);
    }
}
```

在 `onResume()` 方法中调用了 `WebTvSubEngine` 类的 `excuteWebTv()` 方法:

```java
public void excuteWebTv(Context context) {
    this.mContext = context;
    HashMap<String, Object> attrs = new HashMap();
    attrs.put("stbId", SystemProperties.get("ro.serialno", ""));
    attrs.put("openType", "3");
    String xml = new WebTvRequest().getWebTVXml(attrs);
    L.i("手机开通机顶盒 c:" + xml);
    Log.d("desaco", "SHCMCC_Guide_IPTV_HN_0430, WebTvSubEngine 手机开通机顶盒 xml:" + xml);
    doAsynPostRequest(this.mContext, xml);
}
```

在 `excuteWebTv()` 会调用父类 `BaseEngine` 的 `doAsynPostRequest()` 方法：

```java
protected void doAsynPostRequest(Context context, String xml) {
    NetService netService = this.mNetService;
    int i = this.requestId + 1;
    this.requestId = i;
    netService.doAsynXmlPostRequest(context, i, xml);
}
```

在 `doAsynPostRequest()` 方法中调用了 `NetService` 的 `doAsynXmlPostRequest()` 方法：

```java
public void doAsynXmlPostRequest(final Context context, int id, final String xml) {
    this.mExecutor.submit(new Runnable() {
        public void run() {
            L.i("开始请求升级服务器=====");
            NetService.this.mXmlRequest.request(context, NetService.this.resultListener, xml);
        }
    });
}
```

在 `doAsynXmlPostRequest()` 方法中调用 `XmlDocumentRequest` 类的 `request()` 方法：

```java
public class XmlDocumentRequest {
    public void request(Context context, ApiInfoCallback resultListener, String xml) {
        HttpParams httpParameters = new BasicHttpParams();
        HttpConnectionParams.setConnectionTimeout(httpParameters, 5000);
        HttpConnectionParams.setSoTimeout(httpParameters, 30000);
        HttpClient client = new DefaultHttpClient(httpParameters);
        L.i("开始请求升级服务器");
        for (int i = 0; i < 2; i++) {
            Document result = netRequest(client, Contants.homePase(context), xml);
            if (result != null) {
                resultListener.onApiFinish(result);
                return;
            }
        }
        resultListener.onApiFinish(netRequest(client, Contants.homePase2(context), xml));
    }

    private Document netRequest(HttpClient client, String url, String body) {
        L.i("request SCSP_URL/bak_SCSP_URL=" + url);
        HttpPost post = new HttpPost(url);
        try {
            post.setEntity(new StringEntity(body, "UTF-8"));
            HttpResponse response = client.execute(post);
            L.i("response code=" + response.getStatusLine().getStatusCode());
            if (response.getStatusLine().getStatusCode() == CMD.PAY_NEXT) {
                String data = EntityUtils.toString(response.getEntity(), "UTF-8");
                L.i("请求服务器返回数据  s:" + data);
                return DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(new ByteArrayInputStream(data.getBytes()));
            }
            Thread.sleep(1000);
            return null;
        } catch (Exception e) {
            L.e(e);
        }
        return null;
    }

}
```

当请求完成后，`request()` 方法会调用 `ApiInfoCallback` 接口的 `onApiFinish()` 方法返回到 `BaseEngine` 类中：

```java
public void onApiFinish(Document doc) {
    onHandleDocumentComplete(doc);
}
```

在 `onApiFinish()` 方法中会调用 `WebTvSubEngine` 类的 `onHandleDocumentComplete()` 方法：

```java
protected void onHandleDocumentComplete(Document document) {
    ResponseBeen mResponseBeen;
    L.i("====== 验证机顶盒ID返回结果====== document:" + document);
    if (document == null) {
        mResponseBeen = errorNetworkProcess(this.mContext);
    } else {
        mResponseBeen = new ResponseBeen();
        NodeList nodeList = document.getElementsByTagName("webTVAuth");
        if (nodeList.getLength() > 0) {
            Element mElement = (Element) nodeList.item(0);
            if (mElement.hasAttribute(Constant.KEY_RESULT)) {
                mResponseBeen.setResult(mElement.getAttribute(Constant.KEY_RESULT));
            }
            if (mElement.hasAttribute("resultDesc")) {
                mResponseBeen.setResultDesc(mElement.getAttribute("resultDesc"));
            }
            if (mElement.hasAttribute("stbAccount")) {
                mResponseBeen.setStbAccount(mElement.getAttribute("stbAccount"));
            }
            if (mElement.hasAttribute("stbPassword")) {
                mResponseBeen.setStbPassword(mElement.getAttribute("stbPassword"));
            }
        }
    }
    parseData(mResponseBeen);
}
```

在 `onHandleDocumentComplete()` 方法中会调用 `parseData()` 方法来解析结果：

```java
private void parseData(ResponseBeen response) {
    int code = -1;
    try {
        code = Integer.parseInt(response.getResult());
    } catch (Exception e) {
        e.printStackTrace();
    }
    switch (code) {
        case 0:
            String stbAccount = response.getStbAccount();
            String stbPassword = response.getStbPassword();
            String stbAcountSuffix = "";
            if (stbAccount == null || stbAccount.equals("")) {
                onFinish(false, 2, "");
                return;
            }
            if (stbAccount.contains("@")) {
                stbAcountSuffix = stbAccount.substring(stbAccount.indexOf("@"));
                stbAccount = stbAccount.substring(0, stbAccount.indexOf("@"));
            }
            try {
                Parameter mParam = new Parameter(this.mContext);
                mParam.setParameter("ntvuseraccount", stbAccount);
                mParam.setParameter("ntvusersuffix", stbAcountSuffix);
                mParam.setParameter("ntvuserpassword", stbPassword);
                mParam.setParameter("initialization_wizard", "1");
            } catch (Exception e2) {
                e2.printStackTrace();
            }
            onFinish(true, 0, "");
            return;
        case 900056:
        case 901004:
        case 901021:
            onFinish(false, code, response.getResultDesc());
            return;
        default:
            String hint = response.getResultDesc();
            if (TextUtils.isEmpty(hint)) {
                hint = this.mContext.getResources().getString(R.string.protocol_data_error);
            }
            onFinish(false, -1, hint);
            return;
    }
}
```

可以看出当请求成功后会对如下值进行设置：

```java
Parameter mParam = new Parameter(this.mContext);
mParam.setParameter("ntvuseraccount", stbAccount);
mParam.setParameter("ntvusersuffix", stbAcountSuffix);
mParam.setParameter("ntvuserpassword", stbPassword);
mParam.setParameter("initialization_wizard", "1");
```

不管成功还是失败都会调用 `GuideMainActivity ` 中的 `onFinish()` 方法：

```java
WebTvSubEngine mWebTvSubEngine = new WebTvSubEngine() {
    protected void onFinish(boolean isOK, int errorcode, String errorDesc) {
        if (isOK) {
            L.i("===============swguide  success ==================isLogin=" + SystemProperties.getInt("epg.login", -1));
            GuideMainActivity.this.startActivity(new Intent(GuideMainActivity.this, IptvMainActivity.class));
            GuideMainActivity.this.finish();
        } else if (-1 == errorcode || 2 == errorcode) {
            GuideMainActivity.this.mErrorDescription = errorDesc + " (" + errorcode + ") ";
            L.i(" 出现了小概率性的协议数据错误 ：" + GuideMainActivity.this.mErrorDescription);
            GuideMainActivity.this.runOnUiThread(GuideMainActivity.this);
        } else {
            L.i(" 没有出现协议数据错误但是没有开通 errorCode:" + errorcode);
            L.i(" 没有出现协议数据错误但是没有开通 errorDesc:" + errorDesc);
            IntentUtils.startFailureActivity(GuideMainActivity.this, errorcode, errorDesc);
            GuideMainActivity.this.finish();
        }
        GuideMainActivity.this.isRunning = false;
    }
};
```

从代码中可以看出，当请求成功会启动 `IptvMainActivity` 界面。如果错误代码为 1 或 2 则会调用 `GuideMainActivity` 的 `run()` 方法启动设备诊断应用程序。其他错误则会启动失败界面：

```java
public static void startFailureActivity(Context context, int errorcode, String errorDesc) {
    Intent intent = new Intent(context, GuideFailureActivity.class);
    intent.putExtra(Constant.KEY_ERRORCODE, errorcode);
    intent.putExtra("errorDesc", errorDesc);
    context.startActivity(intent);
}
```

### 5. 展示登录错误信息：GuideFailureActivity

`GuideFailureActivity ` 界面主要用于获取登录错误的详细信息，并展示给用户。

#### 5.1 onResume() 方法

```java
protected void onResume() {
    super.onResume();
    L.i("====== GuideFailureActivity onResume ======");
    this.mWebTVControlEngine.excuteWebTvControl(this);
}
```

在 `onResume()` 方法中调用了 `WebTVControlEngine` 类的 `excuteWebTvControl()` 方法：

```java
public void excuteWebTvControl(Context context) {
    this.mContext = context;
    HashMap<String, Object> attrs = new HashMap();
    attrs.put("stbId", SystemProperties.get("ro.serialno", ""));
    doAsynPostRequest(this.mContext, new WebTVControlRequest().getWebTVControlXml(attrs));
}
```

在 `excuteWebTvControl()` 方法中会调用父类 `BaseEngine` 类的 `doAsynPostRequest()` 方法，调用了 `doAsynPostRequest()` 方法后的流程就不再次介绍了，可以参考 `GudieMainActivity` 类的相关介绍。最终请求完成后会调用 `WebTVControlEngine` 类的 `onHandleDocumentComplete()` 方法：

```java
protected void onHandleDocumentComplete(Document result) {
    if (result == null) {
        errorNetworkProcess(this.mContext);
        return;
    }
    ResponseBeen mResponseBeen = new ResponseBeen();
    NodeList nodeList = result.getElementsByTagName("webTVControl");
    if (nodeList.getLength() > 0) {
        Element mElement = (Element) nodeList.item(0);
        if (mElement.hasAttribute(Constant.KEY_RESULT)) {
            mResponseBeen.setResult(mElement.getAttribute(Constant.KEY_RESULT));
        }
        if (mElement.hasAttribute("resultDesc")) {
            mResponseBeen.setResultDesc(mElement.getAttribute("resultDesc"));
        }
        if (mElement.hasAttribute("openMode")) {
            mResponseBeen.setOpenMode(mElement.getAttribute("openMode"));
        }
        NodeList versionNodeList = mElement.getChildNodes();
        for (int j = 0; j < versionNodeList.getLength(); j++) {
            Node versionNode = versionNodeList.item(j);
            String vname = versionNode.getNodeName();
            String value = versionNode.getTextContent();
            L.i("====:j=" + j + ",vname=" + vname + ",value=" + value);
            if ("copyRightId".equals(vname)) {
                mResponseBeen.setCopyRightId(value);
            } else if ("copyRightName".equals(vname)) {
                mResponseBeen.setCopyRightName(value);
            } else if ("copyRightProductInfo".equals(vname)) {
                mResponseBeen.setCopyRightProductInfo(value);
            }
        }
    }
    finish(mResponseBeen);
}
```

在 `onHandleDocumentComplete()` 方法中会调用 `GuideFailureActivity` 类的 `finish()` 方法：

```java
WebTVControlEngine mWebTVControlEngine = new WebTVControlEngine() {
    public void finish(ResponseBeen response) {
        L.i("=============response========" + response.getOpenMode());
        L.i("====== mWebTVAuthErrorCode:" + GuideFailureActivity.this.mWebTVAuthErrorCode);
        switch (GuideFailureActivity.this.mWebTVAuthErrorCode) {
            case 900056:
            case 901004:
            case 901021:
                GuideFailureActivity.this.checkResultCode(response, GuideFailureActivity.this.mWebTVAuthErrorDesc);
                return;
            default:
                L.i(" 错误码不在服务器返回的范畴，故执行错误信息为：" + response.getResultDesc());
                GuideFailureActivity.this.checkResultCode(response, response.getResultDesc());
                return;
        }
    }
};
```

在 `finish()` 方法中都会调用 `checkResultCode()` 方法：

```java
private void checkResultCode(ResponseBeen response, String unsupportOpenDesc) {
    int resultCode = -1;
    try {
        resultCode = Integer.parseInt(response.getResult());
    } catch (Exception e) {
    }
    L.i(" 根据错误码进行不同地处理 当前错误码为：" + resultCode);
    L.i(" 根据错误码进行不同地处理  unsupportOpenDesc " + unsupportOpenDesc);
    switch (resultCode) {
        case 0:
        case 2:
            L.i(" 当前开通方式为：" + response.getOpenMode());
            if (String.valueOf(1).equals(response.getOpenMode()) || String.valueOf(5).equals(response.getOpenMode())) {
                L.i(" 查看机顶盒管控信息 符合互联网开通条件");
                this.mResponseBeen = response;
                runOnUiThread(this);
                return;
            }
            L.i(" 查看机顶盒管控信息 不符合互联网开通条件 展示对话框 描述信息为：" + unsupportOpenDesc);
            showUnsupportOpenDlg(this.mWebTVAuthErrorCode + "  " + unsupportOpenDesc);
            return;
        default:
            String msg = getResources().getString(R.string.error_result_code) + resultCode + "";
            L.i("  查看机顶盒管控信息,并启动展示开通数据协议错误界面 msg:" + msg);
            IntentUtils.startDialogActivity(this, msg);
            finish();
            return;
    }
}
```

在 `checkResultCode()` 方法中根据不同的返回值，向用户展示错误信息。`runOnUiThread()` 方法会调用 `run()` 方法：

```java
public void run() {
    if (mResponseBeen == null || TextUtils.isEmpty(mWebTVAuthErrorDesc)) {
        L.i(" 刷新ui线程发现 不能执行开通流程，缺少必要的开通条件======");
        return;
    }
    L.i(" 执行开通流程界面======");
    IntentUtils.startPayWelcomeActivity(this, mResponseBeen.getOpenMode(), mWebTVAuthErrorDesc, mResponseBeen.getCopyRightId(), mResponseBeen.getCopyRightName(), mResponseBeen.getCopyRightProductInfo());
    if (mAlert != null && mAlert.isWinIsShow()) {
        mAlert.destroyWin();
    }
    mAlert = null;
    if (!isFinishing()) {
        finish();
    }
}
```

可以看出在 `run()` 方法中会通过 `IntentUtils` 类的 `startPayWelcomeActivity()` 方法启动 `GuidePayWelcomeActivity`。

```java
public static void startPayWelcomeActivity(Context context, String openMode, String errorDesc, String copyRightId, String copyRightName, String copyRightProductInfo) {
    Intent intent = new Intent();
    intent.setClass(context, GuidePayWelcomeActivity.class);
    intent.putExtra("openMode", openMode);
    intent.putExtra("errorDesc", errorDesc);
    intent.putExtra("copyRightId", copyRightId);
    intent.putExtra("copyRightName", copyRightName);
    intent.putExtra("copyRightProductInfo", copyRightProductInfo);
    context.startActivity(intent);
}
```

### 6. 开通流程界面：GuidePayWelcomeActivity

在 `GuidePayWelcomeActivity` 可以选择手机、验证码方式和选择牌照方方式开通。

#### 6.1 onClick() 方法

```java
public void onClick(View view) {
    switch (view.getId()) {
        case R.id.btn_next:
            L.i(" === 执行下一步");
            if ("1".equals(mOpenMode)) {
                L.i("执行手机、验证码开通");
                IntentUtils.startPhoneNumberValidateActivity(this, mCopyRightId, mCopyRightName, mCopyRightProductInfo);
            } else {
                L.i("执行选择牌照开通");
                IntentUtils.startPaySelectCopyRightActivity(this, mCopyRightId, mCopyRightName, mCopyRightProductInfo);
            }
            break;
    }
}
```

在 `onClick()` 方法中选择手机、验证码开通将启动 `GuidePhoneNumberValidateActivity` 界面；选择牌照方开通，将启动 `GuidePaySelectCopyRightActivity` 界面。

### 7. 手机验证码开通界面：GuidePhoneNumberValidateActivity

#### 7.1 onClick() 方法

当点击 `next` 按钮后，将会执行手机验证码开通请求。

```java
public void onClick(View paramView) {
    switch (paramView.getId()) {
        case R.id.validatemobile:
            if (this.mUsername.getText().toString().trim().equals("")) {
                this.mAlert.showPowerWin();
                this.mAlert.changeText(getResources().getString(R.string.ts_phone_null));
                this.mPhoneNumberHandler.setTimeOut(2, 3000);
            } else if (RegexUtils.isMobileSimple(this.mUsername.getText().toString().trim())) {
                sendState(Boolean.valueOf(false));
                L.i("====== send validate mobile  and goto get sms!!");
                this.mSmsEngine.excuteSms(this, this.mUsername.getText().toString().trim());
                new Thread(new Runnable() {
                    public void run() {
                        try {
                            mTime = 60;
                            do {
                                mPhoneNumberHandler.sendEmptyMessage(0);
                                Thread.sleep(1000);
                                mTime--;
                            } while (mTime > 0);
                        } catch (Exception e) {
                            e.printStackTrace()
                        }
                    }
                }).start();
            } else {
                mAlert.showPowerWin();
                mAlert.changeText(getResources().getString(R.string.ts_phone_error));
                mPhoneNumberHandler.setTimeOut(2, 3000);
            }
            break;
        case R.id.before:
            finish();
            break;
        case R.id.next:
            L.i("====  执行下一步的 配置 ======");
            if (mConnectOver) {
                String changeMsg;
                if (mFromResultCode == 0 && mCopyRightId != null) {
                    mAlert.showPowerWin();
                    changeMsg = getResources().getString(R.string.select_license);
                    L.i("====== act 1 更新对话框显示信息 msg：" + changeMsg);
                    mAlert.changeText(changeMsg);
                    mPhoneNumberHandler.setTimeOut(2, 3000);
                }
                if (!RegexUtils.isMobileSimple(mUsername.getText().toString().trim()) || mPassword.getText().toString().trim().equals("")) {
                    String changeMessage = getResources().getString(R.string.ts_check_phone_or_password);
                    L.i("====== 3 更新对话框显示信息 msg：" + changeMessage);
                    mAlert.showPowerWin();
                    mAlert.changeText(changeMessage);
                    mPhoneNumberHandler.setTimeOut(2, 3000);
                    return;
                } else {
                    mAlert.showPowerWin();
                    changeMsg = getResources().getString(R.string.ts_validating);
                    L.i("====== act 2 更新对话框显示信息 msg：" + changeMsg);
                    mAlert.changeText(changeMsg);
                    mPhoneNum = mUsername.getText().toString().trim();
                    L.i("========准备验证stbid===phoneNum:" + mPhoneNum);
                    mCode = mPassword.getText().toString().trim();
                    L.i("========准备验证stbid===mCode :" + mCode);
                    mConnectOver = false;
                    mPhoneNumberHandler.setTimeOut(2, 2000);
                    mLastErrorInfo = "";
                    mWebTvAuthEngine.excuteWebTvAuth(this, mPhoneNum, mCode, isPppoe_invisible, mPppoe.getText().toString().trim(), mProvinceID, mCopyRightId);
                    mSend.setClickable(false);
                }
            }
            break;
    }
}
```

在 `onClick()` 方法中调用 `WebTvAuthEngine` 类的 `excuteWebTvAuth()` 方法进行验证。

```java
public void excuteWebTvAuth(Context context, String phoneNum, String code, boolean isPppoe_invisible, String pppoe, String provinceID, String copyRightId) {
    this.mContext = context;
    HashMap<String, Object> attrs = new HashMap();
    attrs.put("phoneNum", phoneNum);
    attrs.put("password", code);
    attrs.put("stbId", SystemProperties.get("ro.serialno", ""));
    if (isPppoe_invisible) {
        attrs.put("openType", "4");
        attrs.put("broadAccount", pppoe);
    } else {
        attrs.put("openType", "1");
    }
    if (provinceID == null) {
        provinceID = "";
    }
    attrs.put("provinceID", provinceID);
    attrs.put("operators", "");
    attrs.put("token", "");
    if (copyRightId == null) {
        copyRightId = "";
    }
    attrs.put("copyRightId", copyRightId);
    String xml = new WebTvRequest().getWebTVXml(attrs);
    L.i(" 对应调用AAA 互联网侧发起开通接口 c:" + xml);
    doAsynPostRequest(this.mContext, xml);
}
```

在 `excuteWebTvAuth()` 方法中会调用父类的 `doAsynPostRequest()` ，调用 `doAsynPostRequest()` 后的流程可以参考 `GuideMainActivity` 中的相关描述。最后会调用 `WebTvAuthEngine` 的 `onHandleDocumentComplete()` 回调方法。

```java
protected void onHandleDocumentComplete(Document result) {
    L.i("====== 验证机顶盒ID返回结果======");
    if (result == null) {
        errorNetworkProcess(this.mContext);
        return;
    }
    ResponseBeen mResponseBeen = new ResponseBeen();
    NodeList nodeList = result.getElementsByTagName("webTVAuth");
    if (nodeList.getLength() > 0) {
        Element mElement = (Element) nodeList.item(0);
        if (mElement.hasAttribute(Constant.KEY_RESULT)) {
            mResponseBeen.setResult(mElement.getAttribute(Constant.KEY_RESULT));
        }
        if (mElement.hasAttribute("resultDesc")) {
            mResponseBeen.setResultDesc(mElement.getAttribute("resultDesc"));
        }
        if (mElement.hasAttribute("stbAccount")) {
            mResponseBeen.setStbAccount(mElement.getAttribute("stbAccount"));
        }
        if (mElement.hasAttribute("stbPassword")) {
            mResponseBeen.setStbPassword(mElement.getAttribute("stbPassword"));
        }
    }
    onFinish(mResponseBeen);
}
```

通过调用 `doFinish()` 返回 `GuidePhoneNumberValidateActivity`。

```java
WebTvAuthEngine mWebTvAuthEngine = new WebTvAuthEngine() {
    protected void onFinish(ResponseBeen response) {
        String code = response.getResult();
        L.i(" mWebTvAuthEngine result code:" + code);
        if ("0".equals(code)) {
            GuidePhoneNumberValidateActivity.this.mStbAccount = response.getStbAccount();
            GuidePhoneNumberValidateActivity.this.mStbPassword = response.getStbPassword();
            String stbAcountSuffix = "";
            if (GuidePhoneNumberValidateActivity.this.mStbAccount.contains("@")) {
                stbAcountSuffix = GuidePhoneNumberValidateActivity.this.mStbAccount.substring(GuidePhoneNumberValidateActivity.this.mStbAccount.indexOf("@"));
                GuidePhoneNumberValidateActivity.this.mStbAccount = GuidePhoneNumberValidateActivity.this.mStbAccount.substring(0, GuidePhoneNumberValidateActivity.this.mStbAccount.indexOf("@"));
            }
            GuidePhoneNumberValidateActivity.this.mParam.setParameter("ntvuseraccount", GuidePhoneNumberValidateActivity.this.mStbAccount);
            GuidePhoneNumberValidateActivity.this.mParam.setParameter("ntvusersuffix", stbAcountSuffix);
            GuidePhoneNumberValidateActivity.this.mParam.setParameter("ntvuserpassword", GuidePhoneNumberValidateActivity.this.mStbPassword);
            GuidePhoneNumberValidateActivity.this.mParam.setParameter("initialization_wizard", "1");
            GuidePhoneNumberValidateActivity.this.mPhoneNumberHandler.setTimeOut(3, 0);
        } else if ("54".equals(code)) {
            Message msg = new Message();
            msg.what = 10;
            msg.obj = response;
            GuidePhoneNumberValidateActivity.this.mPhoneNumberHandler.sendMessage(msg);
            GuidePhoneNumberValidateActivity.this.isPppoe_invisible = true;
        } else {
            if (TextUtils.isEmpty(code)) {
                GuidePhoneNumberValidateActivity.this.mLastErrorInfo = GuidePhoneNumberValidateActivity.this.getResources().getString(R.string.protocol_data_error);
            } else {
                GuidePhoneNumberValidateActivity.this.mLastErrorInfo = response.getResultDesc();
            }
            GuidePhoneNumberValidateActivity.this.mPhoneNumberHandler.setTimeOut(6, 0);
        }
        GuidePhoneNumberValidateActivity.this.mConnectOver = true;
    }
};
```

在 `onFinish()` 方法中，如果请求成功的话会设置相关值，然后退出当前界面，最后显示 `IptvMainActivity`。如果请求失败的话，则只更改错误提示信息。

### 8. 选择牌照方开通：GuidePaySelectCopyRightActivity

#### 8.1 onClick() 方法

```java
public void onClick(View paramView) {
    switch (paramView.getId()) {
        case R.id.before:
            finish();
            return;
        case R.id.next:
            this.mAlert.showPowerWin();
            String changeMessage = getResources().getString(R.string.gaining_data);
            L.i("更新对话框显示信息：" + changeMessage);
            changeAltText(changeMessage);
            setCheckProductOK(false);
            setCheckDepositAmountOK(false);
            this.mReSubInfoEngine.excuteReSubInfo(this, this.mCopyRightId);
            this.mQueryBalanceEngine.excuteQueryBalance(this);
            return;
        default:
            return;
    }
}
```

在 `onClick()` 方法中，会调用 `ReSubInfoEngine` 类的 `excuteReSubInfo()` 方法和 `QueryBalanceEngine` 类的 `excuteQueryBalance()` 方法。具体流程可以参阅 `GuideMainActivity` 相关描述。最终会回调这两个类在 `GuidePaySelectCopyRightActivity` 中的 `onFinish()` 方法。

```java
QueryBalanceEngine mQueryBalanceEngine = new QueryBalanceEngine() {
    public void onFinish(ResponseBeen response) {
        L.i("=============response========" + response.getResult());
        int resultCode = -1;
        try {
            resultCode = Integer.parseInt(response.getResult());
        } catch (Exception e) {
        }
        L.i("=============resultCode========" + resultCode);
        if (resultCode == 0) {
            GuidePaySelectCopyRightActivity.this.mDepositAmount = Integer.parseInt(response.getBalance());
            GuidePaySelectCopyRightActivity.this.setCheckDepositAmountOK(true);
            if (GuidePaySelectCopyRightActivity.this.isCheckProductOK() && GuidePaySelectCopyRightActivity.this.isCheckDepositAmountOK()) {
                L.i("根据 SCSP提供查询余额接口 返回的数据发现 符合启动 选择支付方式条件");
                IntentUtils.startPaySelectTypeActivity(GuidePaySelectCopyRightActivity.this, GuidePaySelectCopyRightActivity.this.mProductInfos, GuidePaySelectCopyRightActivity.this.mDepositAmount);
                GuidePaySelectCopyRightActivity.this.setTimeOut(0, 0);
                return;
            }
            return;
        }
        StringBuffer msg = new StringBuffer();
        String resultDesc = response.getResultDesc();
        L.i("SCSP提供查询余额接口  响应更新对话框信息 原始：" + resultDesc.toString());
        if (TextUtils.isEmpty(resultDesc)) {
            String changeMessage = GuidePaySelectCopyRightActivity.this.getResources().getString(R.string.protocol_data_error);
            L.i("SCSP提供查询余额接口  响应更新对话框信息 采用默认信息：" + changeMessage.toString());
            msg.append(changeMessage);
        } else {
            msg.append(resultDesc);
        }
        L.i("SCSP提供查询余额接口  响应更新对话框信息 ：" + msg.toString());
        GuidePaySelectCopyRightActivity.this.changeAltText(msg.toString());
        GuidePaySelectCopyRightActivity.this.setTimeOut(0, 5000);
    }
};
ReSubInfoEngine mReSubInfoEngine = new ReSubInfoEngine() {
    public void onFinish(ResponseBeen response) {
        L.i("=============response========" + response.getResult());
        int resultCode = -1;
        try {
            resultCode = Integer.parseInt(response.getResult());
        } catch (Exception E) {
            L.e(E);
        }
        L.i("=============resultCode========" + resultCode);
        if (resultCode == 0) {
            GuidePaySelectCopyRightActivity.this.mProductInfos = response.getProductInfos();
            GuidePaySelectCopyRightActivity.this.setCheckProductOK(true);
            if (GuidePaySelectCopyRightActivity.this.isCheckProductOK() && GuidePaySelectCopyRightActivity.this.isCheckDepositAmountOK()) {
                L.i("根据 基本包续订信息查询接口 返回的数据发现 符合启动 选择支付方式条件");
                IntentUtils.startPaySelectTypeActivity(GuidePaySelectCopyRightActivity.this, GuidePaySelectCopyRightActivity.this.mProductInfos, GuidePaySelectCopyRightActivity.this.mDepositAmount);
                GuidePaySelectCopyRightActivity.this.setTimeOut(0, 0);
                return;
            }
            return;
        }
        StringBuffer msg = new StringBuffer();
        String resultDesc = response.getResultDesc();
        L.i("基本包续订信息查询接口  响应更新对话框信息 原始：" + resultDesc.toString());
        if (TextUtils.isEmpty(resultDesc)) {
            L.i("基本包续订信息查询接口  响应更新对话框信息 采用默认信息：" + GuidePaySelectCopyRightActivity.this.getResources().getString(R.string.protocol_data_error).toString());
            msg.append(GuidePaySelectCopyRightActivity.this.getResources().getString(R.string.protocol_data_error));
        } else {
            msg.append(resultDesc);
        }
        GuidePaySelectCopyRightActivity.this.changeAltText(msg.toString());
        GuidePaySelectCopyRightActivity.this.setTimeOut(0, 5000);
    }
};
```

因为这个两个类都是同时执行的，所以在 `onFinish()` 方法中它们相互依赖，只有两个请求都执行完成后才会执行最终的方法 `IntentUtils.startPaySelectTypeActivity(GuidePaySelectCopyRightActivity.this, GuidePaySelectCopyRightActivity.this.mProductInfos, GuidePaySelectCopyRightActivity.this.mDepositAmount);`。该方法会启动 `GuidePaySelectTypeActivity` 界面。

### 9. 付款界面：GuidePaySelectTypeActivity

#### 9.1 onActivityResult() 方法

付款流程就不分析了，这里只分析下付款成功后的操作。付款成功后会向 `PaySelectTypeHandler` 发送 `CMD.RESUB` 消息：

```java
protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    Object obj;
    StringBuilder append = new StringBuilder().append("requestCode=").append(requestCode).append(",resultCode=").append(resultCode).append(",data=");
    if (data == null) {
        obj = "null";
    } else {
        obj = data.getExtras();
    }
    L.i(append.append(obj).toString());
    if (resultCode != -1 || data == null) {
        this.mPaySelectTypeHandler.sendEmptyMessage(CMD.PAY_BY_ACCOUNT_FAIL);
    } else {
        String result = "" + data.getExtras().get(Constant.KEY_RESULT);
        String errorCode = "" + data.getExtras().get(Constant.KEY_ERRORCODE);
        String errorMsg = "" + data.getExtras().get(Constant.KEY_ERRORMSG);
        String orderCode = "" + data.getExtras().get(Constant.KEY_ORDERCODE);
        L.i("result=" + result + ",errorCode=" + errorCode + ",errorMsg=" + errorMsg + ",orderCode=" + orderCode + ",orderAmt=" + ("" + data.getExtras().get(Constant.KEY_ORDERAMT)));
        if ("0".equals(result)) {
            this.mPaySelectTypeHandler.sendMessage(this.mPaySelectTypeHandler.obtainMessage(CMD.RESUB));
        } else {
            if (errorCode == null || "null".equals(errorCode)) {
                errorCode = "";
            }
            if (errorMsg == null || "null".equals(errorMsg)) {
                errorMsg = "";
            }
            Message msg = this.mPaySelectTypeHandler.obtainMessage(CMD.PAY_BY_ACCOUNT_FAIL);
            msg.obj = errorCode + errorMsg;
            this.mPaySelectTypeHandler.sendMessage(msg);
        }
    }
    super.onActivityResult(requestCode, resultCode, data);
}
```

`PaySelectTypeHandler` 会调用 `GuidePaySelectTypeActivity` 的 `onReSubCallBack()` 方法：

```java
public void onReSubCallBack(HashMap<String, Object> attrs) {
    this.mReSubEngine.excuteResub(this, attrs);
}
```

`excuteResub()` 方法的执行流程请参阅 `GuideMainActivity` 相关描述。最终会回调 `GuidePaySelectTypeActivity` 中的 `onFinish()` 方法：

```java
ReSubEngine mReSubEngine = new ReSubEngine() {
    public void onFinish(ResponseBeen response) {
        L.i("=============response========" + response);
        int resultCode = -1;
        try {
            resultCode = Integer.parseInt(response.getResult());
        } catch (Exception e) {
        }
        L.i("=============resultCode========" + resultCode);
        if (resultCode == 0) {
            GuidePaySelectTypeActivity.this.mPaySelectTypeHandler.sendEmptyMessage(CMD.RESUB_OK);
            return;
        }
        Message msg = Message.obtain();
        msg.what = CMD.RESUB_FAIL;
        msg.obj = response;
        GuidePaySelectTypeActivity.this.mPaySelectTypeHandler.sendMessage(msg);
    }
};
```

在 `onFinish()` 方法中会向 `PaySelectTypeHandler` 发送 `CMD.RESUB_OK` 消息。

```java
case CMD.RESUB_OK /*303*/:
    this.mAlert.showPowerWin();
    this.mAlert.changeText(this.mAct.getResources().getString(R.string.renew_success));
    sendEmptyMessage(CMD.VALIDATE_STBID);
    return;
```

在 `CMD.RESUB_OK` 消息中又发送了 `CMD.VALIDATE_STBID` 消息：

```java
case CMD.VALIDATE_STBID /*401*/:
    this.mWebTvSubEngine.excuteWebTv(this.mAct);
    return;
```

在 `CMD.VALIDATE_STBID` 消息中调用了 `mWebTvSubEngine.excuteWebTv)`，该方法的具体流行请参阅 `GuideMainActivity` 中的相关描述。最后它会回调 `onFinish()` 方法回到 `PaySelectTypeHandler` 中。

```java
WebTvSubEngine mWebTvSubEngine = new WebTvSubEngine() {
    protected void onFinish(boolean isOK, int errorcode, String errorDesc) {
        PaySelectTypeHandler.this.sendEmptyMessage(1);
        if (!isOK) {
            Message msg = Message.obtain();
            msg.what = CMD.VALIDATE_STBID_FAIL;
            msg.obj = errorDesc;
            PaySelectTypeHandler.this.sendMessage(msg);
        }
    }
};
```

如果请求成功，则会发送消息 `1`。

```java
case 1:
    if (this.mAlert.isWinIsShow()) {
        this.mAlert.destroyWin();
        return;
    }
    return;
```

在消息处理代码中，它会隐藏当前界面，重新显示 `IptvMainActivity` 界面。

> 至此，整个 SHCMCC_Guide_IPTV_HN 应用就分析完成了。

### 10. 总结

![SHCMCC_Guide_IPTV_HN](./images/SHCMCC_Guide_IPTV_HN.png)
