应用是在 `src/net/sunniwell/tms/CWMPBroadcastReceiver.java` 类中接收 `DownLoadEvent.HTTP_CHECK_STATUS_ACTION` 广播。代码如下：

```java
private Handler doHandler = new Handler() {

    public void handleMessage(Message msg) {
        Intent intent = (Intent) msg.obj;
        String sAction = intent.getAction();
        log.d("======do====CWMPService=============" + sAction);
        
        ......
            
        } else if (sAction.equals(DownLoadEvent.HTTP_CHECK_STATUS_ACTION)) {
            Log.d("ZHG-TMS", "!!!!!!!!!!!!!!!!!!!!!!!!!!HTTP_CHECK_STATUS_ACTION");
            handleUpgradeInfo(intent, CHECK_UPGRADE);
        } else if (sAction.equals(DownLoadEvent.DOWNLOAD_STATUS_ACTION)) {
        
        ......
          
    }
}
```

那 `DownLoadEvent.HTTP_CHECK_STATUS_ACTION` 广播是从哪里发出来的呢？通过搜索广播 Action ，我们可以看到如下结果：

```console
./packages/cmdc/SWUpgrade_sd/app/src/main/java/net/sunniwell/app/upgradebase/server/CheckVersionService.java:889:               mIntent.setAction(ConstantInfo.HTTP_CHECK_STATUS_ACTION);
./packages/cmdc/SWUpgrade_sd/app/src/main/java/net/sunniwell/app/upgradebase/server/extension/XMLParseCls.java:297:             mIntent.setAction(ConstantInfo.HTTP_CHECK_STATUS_ACTION);
```

现在回到广播接收器的代码，我们可以看到当接收到该广播后，会执行 `handleUpgradeInfo(intent, CHECK_UPGRADE)` 代码：

```java
private void handleUpgradeInfo(Intent intent, String type) {
    DataPreferences dataPreferences = new DataPreferences(this.context);
    final String flag = dataPreferences.getPreferences(DataPreferences.MDOWNLOAD);
    if(Utility.isEmpty(flag)) return;
    Bundle b = intent.getExtras();
    if (b != null) {
        int infoType = b.getInt("status");
        if (type.equals(CHECK_UPGRADE)) {
            switch (infoType) {
                case DownLoadEvent.CheckInfo.SERVER_CHECKE_FAILE:// 服务器升级配置信息错误
                case DownLoadEvent.CheckInfo.SERVER_ERROR:// 服务器错误
                case DownLoadEvent.CheckInfo.THE_SAME_VERSION:
                case DownLoadEvent.CheckInfo.UPGRADE_URL_ERROR:
                case DownLoadEvent.CheckInfo.UPGRADE_SERVER_CONNECTION_FAILURE:// 服务器错误
                case DownLoadEvent.CheckInfo.DOWNLOAD_FILE_NO_EXIST:
                case DownLoadEvent.CheckInfo.PARAMETERS_ARE_INCORRECT:
                case DownLoadEvent.CheckInfo.GRADE_INFORMATION_IS_NOT:
                    Log.d("ZHG-TMS", "!!!!!!!!!!!!!!!!!!!!!!!!!!111 CHECK_UPGRADE , infoType = "+infoType);
                    log.d("============error================" + infoType);
                    if (lastErrorTime == 0 || System.currentTimeMillis() - lastErrorTime >= 3000) {
                        Log.d("ZHG-TMS", "!!!!!!!!!!!!!!!!!!!!!!!!!!222 CHECK_UPGRADE , infoType = "+infoType);
                        lastErrorTime = System.currentTimeMillis();
                        sendMessage(DownLoadEvent.DownloadFaultCode.FAILE, DownLoadEvent.DownloadEvent.DOWNLOAD_FAILE);
                    }
                    break;
            }
        } else if (type.equals(DOWN_UPGRADE)) {
           ......
        }
    }
}
```

从上面的代码可以看出，它只处理升级失败问题。当检测到升级失败后，会调用 sendMessage() 方法发送失败消息给 CWMPService 服务：

```java
private void sendMessage(final int faultCode, final String faultString) {
    new Thread() {
        @Override
        public void run() {
            //log.d("=========!CWMPService.isConnectCPE=" + (!CWMPService.isConnectCPE));
            while (!CWMPService.isConnectCPE) {
                SystemClock.sleep(1000);
            }
            // 使用同一个msg发送过快，handler未处理完将出现Runtime异常
            FaultStruct fault = new FaultStruct();
            fault.faultCode = faultCode;
            fault.faultString = faultString;
            ArrayList<Object> list = new ArrayList<Object>();
            list.add(fault);
            String commandKey = new DataPreferences(CWMPService.getInstance().getApplicationContext()).getPreferences(DataPreferences.CommandKey);
            list.add(commandKey);
            Message msg = CWMPService.getInstance().getHandler().obtainMessage(CWMPEvent.EVENT_CWMP_TRANSFERCOMPLETE, 0, 0, list);
            try {
                CWMPService.getInstance().getHandler().sendMessage(msg);
            } catch (Exception e) {
                e.printStackTrace();
            }
            super.run();
        }
    }.start();

}
```

通过上面的代码可以看出，最终它是将消息发送给  `src/net/sunniwell/tms/CWMPEventHandler.java` 来处理：

```java
@Override
public void handleMessage(Message msg) {
    log.d("msg====start====== " + msg.what);
    super.handleMessage(msg);
    switch (msg.what) {
		......
        case CWMPEvent.EVENT_CWMP_TRANSFERCOMPLETE:
            if (hasMessages(CWMPEvent.EVENT_CWMP_TRANSFERCOMPLETE))
                removeMessages(CWMPEvent.EVENT_CWMP_TRANSFERCOMPLETE);
            log.d((msg.arg1 == 1 ? "upload" : "download") + " " + (msg.obj == null ? "null" : "have obj"));
            doTransferComplete(msg.obj, msg.arg1);
            break;
        case CWMPEvent.EVENT_CWMP_STARTCPELISTEN:
            ......
    }
}
```

当 CWMPEventHandler 接收到消息后会执行 doTransferComplete() 方法：

```java
/**
 * 指示此会话是为了指示一个早 先请求的上载或下载的完成 （不管是成功的或不成功的） ， TransferComplete 方式会在这个
 * 会话期间被调用一次或多次。 这 个 事 件 码 必 须 只 跟 “ M Download”和／或“M Upload” 事件码（ “M
 * Download”和“M Upload”见下面） 。
 */
private void doTransferComplete(Object object, int arg1) { // 表明会话完完成下载或上传(成功或失败)
    // 上报,TransferComplete方法将调用一个或多个次在此会话
    try {
        if (object != null && object instanceof ArrayList) {
            log.d("arg1=" + arg1);
            if (arg1 == 1) {
                sendInform(new String[] { CWMPEvent.EVENT_CODE_STRING_TRANSFER_COMPLETE, CWMPEvent.EVENT_CODE_STRING_M_UPLOAD }, (ArrayList) object);
            } else {
                sendInform(new String[] { CWMPEvent.EVENT_CODE_STRING_TRANSFER_COMPLETE, CWMPEvent.EVENT_CODE_STRING_M_DOWNLOAD }, (ArrayList) object);
            }
        } else
            sendInform(new String[] { CWMPEvent.EVENT_CODE_STRING_TRANSFER_COMPLETE }, null);
    } catch (IOException e) {
        e.printStackTrace();
    } catch (InterruptedException e) {
        e.printStackTrace();
    }
    ACSSession.isDoingOtherSession = false;
}
```

doTransferComplete() 会调用 sendInform() 方法与网管服务器进行会话：

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

