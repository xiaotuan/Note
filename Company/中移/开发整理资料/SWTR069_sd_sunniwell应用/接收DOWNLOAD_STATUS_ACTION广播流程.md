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

