先来看是谁发出了该广播，通过搜索得到如下结果：

```console
./SWTR069_sd_sunniwell/src/net/sunniwell/tms/CWMPBroadcastReceiver.java:110:                    }else if("com.android.action.IPTV.AUTH_STATUS_CHANGE".equals(sAction)){
./SWGuide_sd/app/src/main/java/net/sunniwell/guide/iptvauth/service/HuaweiIPTVAuth.java:616:        intent.setAction("com.android.action.IPTV.AUTH_STATUS_CHANGE");
./SWGuide_sd/app/src/main/java/net/sunniwell/guide/receiver/SWGuideReceiver.java:27:                    if(intent.getAction().equals("com.android.action.IPTV.AUTH_STATUS_CHANGE")){
```

我们来看下 HuaweiIPTVAuth.java 发送广播的代码：

```java
public void sendAuthBroadcast() {
    Intent intent = new Intent();
    intent.setAction("com.android.action.IPTV.AUTH_STATUS_CHANGE");
    intent.putExtra("newStatus", "AuthSuccess");
    sendBroadcast(intent);
}
```

再看下是谁调用了该方法：

```java
/**
 * 处理认证状态
 * 
 * @param statusCode
 *            认证状态码
 * @param msg
 *            认证信息
 */
private void handleAuthenStatus(int statusCode, String msg) {
    log.d("statusCode===" + statusCode + "msg=" + msg);
    SWApplication.getInstance().getStatus().changeStatus(msg);
    mRedirectCount = 0;
    if(statusCode == SUCCESS && !isAgainAuth){
        setUserName();
        setUserPwd();
        setAuthStatus();
        sendAuthBroadcast();
        sendAuthSuccess();
    } else if (statusCode == FAILED) {
        startWarnningActivity();
        mAuthenHandler.sendEmptyMessage(AUTHEN_STOP);
    }
}
```

从上面的代码可以看出，它是在认证成功后发出该广播的。现在我们来看下处理该广播的代码，它位于 `src/net/sunniwell/tms/CWMPBroadcastReceiver.java` 类中：

```java
private Handler doHandler = new Handler() {

    public void handleMessage(Message msg) {
        Intent intent = (Intent) msg.obj;
        String sAction = intent.getAction();
        log.d("======do====CWMPService=============" + sAction);
        ......
        }else if("com.android.action.IPTV.AUTH_STATUS_CHANGE".equals(sAction)){
            Log.d("AUTH-TIME", "1111111!!!!!!!!!!!!!!!!!!!!!!!!!!sAction = "+sAction);
            final DataPreferences preferences = new DataPreferences(context.getApplicationContext());
            final String value = intent.getStringExtra("newStatus");
            Log.d("AUTH-TIME", "22222!!!!!!!!!!!!!!!!!!!!!!!!!!value = "+value);
            if(!Utility.isEmpty(value)&&value.trim().equalsIgnoreCase("AuthSuccess")){
                final long time = System.currentTimeMillis();
                Log.d("AUTH-TIME", "33333!!!!!!!!!!!!!!!!!!!!!!!!!!time = "+time);
                preferences.setPreferences(DataPreferences.IPTV_AUTH_TIME, time+"");
                reportIPTVAuthTime(time);
            }
        }else if("cn.10086.action.USERTOKEN_UPDATE".equals(sAction)){
        ......
    }
}
```

在接收到 com.android.action.IPTV.AUTH_STATUS_CHANGE 广播后，它将当前时间保存为认证时间，然后通过 reportIPTVAuthTime() 方法将认证时间上报给网管平台，reportIPTVAuthTime() 方法的代码如下：

```java
public void reportIPTVAuthTime(final long time){
    if(CWMPService.isConnectCPE){
        Log.d("SD-TMS", "report IPTVAuthTime start , time = "+time);
        final Parameter parameter = DataResolver.getInstance().getParameter("Device.X_CMCC_OTV.ServiceInfo.AuthSucTime");
        final ParameterValueStruct parameterValueStruct = new ParameterValueStruct();
        parameterValueStruct.name ="Device.X_CMCC_OTV.ServiceInfo.AuthSucTime";
        parameterValueStruct.value.content =time+"";
        parameterValueStruct.value.type = parameter.type;
        final ArrayList<ParameterValueStruct> values = new ArrayList<ParameterValueStruct>();
        values.add(parameterValueStruct);
        final Message msg = Message.obtain();
        msg.what = CWMPEvent.EVENT_CWMP_SOFTWATE_LIST_CHANGED;
        msg.obj = values;
        CWMPService.getInstance().getHandler().sendMessage(msg);
        Log.d("SD-TMS", "report IPTVAuthTime end , time = "+time);
    }
}
```

可以看出，它将认证时间封装成 ParameterValueStruct 对象，然后向 `src/net/sunniwell/tms/CWMPEventHandler.java` 发送 EVENT_CWMP_SOFTWATE_LIST_CHANGED 消息。下面我们来看下 CWMPEventHandler 是如何处理该消息的：

```java
@Override
public void handleMessage(Message msg) {
    log.d("msg====start====== " + msg.what);
    super.handleMessage(msg);
    switch (msg.what) {
		......
        case CWMPEvent.EVENT_CWMP_SOFTWATE_LIST_CHANGED:
            onSoftwareVersionListChanged((ArrayList<ParameterValueStruct>) msg.obj);
            break;
        ......
    }
}
```

CWMPEventHandler 将会调用 onSoftwareVersionListChanged() 方法进行处理，下面是改方法的代码：

```java
private void onSoftwareVersionListChanged(ArrayList<ParameterValueStruct> values) {
    log.d("======== TR069  onSoftwareVersionListChanged=======");
    try {
        if (values != null && values.size() > 0) {
            for(ParameterValueStruct struct : values){
                Log.d("VALUE-CHANGE", "11 onSoftwareVersionListChanged, struct.name = "+struct.name+" , struct.value = "+struct.value.content);
            }
            sendInform(new String[] { CWMPEvent.EVENT_CODE_STRING_VALUE_CHANGE }, values.size() > 0 ? values : null);
            values.clear();
        } else {
            Log.d("VALUE-CHANGE", "22 onSoftwareVersionListChanged");
            sendInform(new String[] { CWMPEvent.EVENT_CODE_STRING_VALUE_CHANGE }, null);
        }
    } catch (IOException e) {
        e.printStackTrace();
    } catch (InterruptedException e) {
        e.printStackTrace();
    }
}
```

它会调用 sendInform() 方法向网管平台发送数据，下面是 sendInform() 方法的代码：

```java
private void sendInform(final String[] codes, final ArrayList object) throws IOException, InterruptedException {
    log.i("========sendInform=======codes=" + codes.toString() + " object=" + (object == null ? "null" : object.toString()));
    // Auto-generated method stub
    ACSSession session = new ACSSession(mContext);
    InputStream input;
    try {
        input = CWMPService.getInstance().getTemplateInputStream("Inform");
        Envelope request = Inform.getInstance().buildRequest(codes, input, object);
        input.close();
        session.setRequest(mPreferences, request);
        session.start();
        session.join();
    } catch (Exception e) {
        e.printStackTrace();
    }
}
```

