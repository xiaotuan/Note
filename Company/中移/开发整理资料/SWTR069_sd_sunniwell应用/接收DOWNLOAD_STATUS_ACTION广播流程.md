应用是在 `src/net/sunniwell/tms/CWMPBroadcastReceiver.java` 类中接收 `DownLoadEvent.DOWNLOAD_STATUS_ACTION广播。代码如下：

```java
private Handler doHandler = new Handler() {

    public void handleMessage(Message msg) {
        Intent intent = (Intent) msg.obj;
        String sAction = intent.getAction();
        log.d("======do====CWMPService=============" + sAction);
  		......
        } else if (sAction.equals(DownLoadEvent.DOWNLOAD_STATUS_ACTION)) {
            Log.d("ZHG-TMS", "!!!!!!!!!!!!!!!!!!!!!!!!!!HTTP_CHECK_STATUS_ACTION");
            handleUpgradeInfo(intent, DOWN_UPGRADE);
        } else if (sAction.equals(Constant.TR069_PROTOCOL)) {
        ......
    }
}
```

先来看下 DownLoadEvent.DOWNLOAD_STATUS_ACTION 广播是从哪里发出来的，通过搜索关键字后等到如下信息：

```console
./SWUpgrade_sd/app/src/main/java/net/sunniwell/app/upgradebase/download/FileDownloader.java:491:                mIntent.setAction(ConstantInfo.DOWNLOAD_STATUS_ACTION);
```

接收到 DOWNLOAD_STATUS_ACTION 广播后会执行 handleUpgradeInfo() 方法：

```java
private void handleUpgradeInfo(Intent intent, String type) {
    DataPreferences dataPreferences = new DataPreferences(this.context);
    final String flag = dataPreferences.getPreferences(DataPreferences.MDOWNLOAD);
    if(Utility.isEmpty(flag)) return;
    Bundle b = intent.getExtras();
    if (b != null) {
		......
        } else if (type.equals(DOWN_UPGRADE)) {
            log.d("=========down handleUpgradeInfo==download error what=" + infoType);
            switch (infoType) {
                case DownLoadEvent.DownloadInfo.FILE_RENAME_ERROR: // 文件重命名失败
                case DownLoadEvent.DownloadInfo.FILE_MD5_CHECK_ERROR:// md5
                case DownLoadEvent.DownloadInfo.DOWNLOAD_EXCEPTION:// 下载异常结束
                case DownLoadEvent.DownloadInfo.DOWNLOAD_FAILE:// 下载失败
                    Log.d("ZHG-TMS", "!!!!!!!!!!!!!!!!!!!!!!!!!!111 DOWN_UPGRADE , infoType = "+infoType);
                    log.d("====sendMessage==DOWNLOAD_FAILE==" + infoType);
                    if (lastErrorTime == 0) {
                        lastErrorTime = System.currentTimeMillis();
                        int errorCode = DownLoadEvent.DownloadFaultCode.FAILE;
                        if (infoType == DownLoadEvent.DownloadInfo.FILE_MD5_CHECK_ERROR) {
                            errorCode = DownLoadEvent.DownloadFaultCode.FAILE_CHECKFAILED;
                        }
                        sendMessage(errorCode, DownLoadEvent.DownloadEvent.DOWNLOAD_FAILE);
                    }
                    if (System.currentTimeMillis() - lastErrorTime < 3000) {

                    } else {
                        Log.d("ZHG-TMS", "!!!!!!!!!!!!!!!!!!!!!!!!!!2222 DOWN_UPGRADE , infoType = "+infoType);
                        lastErrorTime = System.currentTimeMillis();
                        sendMessage(DownLoadEvent.DownloadFaultCode.FAILE, DownLoadEvent.DownloadEvent.DOWNLOAD_FAILE);
                    }
                    break;
                case DownLoadEvent.DownloadInfo.DOWNLOAD_SUCCESS:// 下载成功//
                case DownLoadEvent.DownloadInfo.DOWNLOAD_FILE_WAS_DOWNLOADED:
                    log.d("====sendMessage==DOWNLOAD_SUCCESS==" + infoType);
                    //						sendMessage(DownLoadEvent.DownloadFaultCode.SECUESS, DownLoadEvent.DownloadEvent.DOWNLOAD_SECUESS);
                    break;
            }
        }
    }
}
```

可以看到，上面的代码只对下载失败的信息进行处理，当下载失败后，会调用 sendMessage() 方法向 CWMPService 服务发送消息：

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

最终消息会由 `src/net/sunniwell/tms/CWMPEventHandler.java` 进行处理，它的处理流程与 [接收HTTP_CHECK_STATUS_ACTION广播流程](.\接收HTTP_CHECK_STATUS_ACTION广播流程.md) 中的处理一致，只是传递的信息不一样而已。

