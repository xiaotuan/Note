我们先来看下接收到 MEDIA_CHANGED_BROADCAST 的处理代码，它位于  `src/net/sunniwell/tms/CWMPBroadcastReceiver.java` 下：

```java
private Handler doHandler = new Handler() {

    public void handleMessage(Message msg) {
        Intent intent = (Intent) msg.obj;
        String sAction = intent.getAction();
        log.d("======do====CWMPService=============" + sAction);
        ......
        } else if (sAction.equals(MEDIA_CHANGED_BROADCAST)) {// 播控诊断，软探针逻辑
            int what = intent.getIntExtra("arg1", -1);
            log.d("what=" + what);
            // 过滤需要处理的消息
            if (what == MediaLog.MEDIA_ERROR_UNKNOWN || what == MediaLog.MEDIA_ERROR_SERVER_DIED || what == MediaLog.MEDIA_INFO_BUFFERING_START || what == MediaLog.MEDIA_INFO_BUFFERING_END || what == MediaLog.MEDIA_INFO_DOWNLOAD_ERROR) {
                Message mediaMsg = new Message();
                mediaMsg.what = HANDLE_SAVELOG;
                mediaMsg.obj = intent;
                mediaHandler.sendMessage(mediaMsg);
            }
        }else if("com.android.action.IPTV.AUTH_STATUS_CHANGE".equals(sAction)){
        ......
    }
}
```

那这个广播是从哪里发出来的呢？通过搜索，我没有找到发送该广播的地方，但是通过下面的分析，我们可以了解到这个广播的功能是将广播附带的日志存储到日志文件中。

我们继续分析，通过接收代码可以看出它会向 MediaHandler 发送 HANDLE_SAVELOG 的消息，下面来看 MediaHandler 的代码，它位于 `src/net/sunniwell/tms/CWMPBroadcastReceiver.java` 类中，是其内部类。

```java
private Handler mediaHandler = new Handler() {
    public void handleMessage(Message msg) {
        switch (msg.what) {
            case HANDLE_SAVELOG: {
                MediaLog mediaLog = MediaLog.getInstance();
                mediaLog.dealEvent((Intent) msg.obj);
                break;
            }
        }
    };
};
```

我们可以看到，它将调用 MediaLog 类的 dealEvent() 方法处理消息携带的对象，具体代码如下：

```java
// 处理消息
public void dealEvent(Intent intent) {
    String url = intent.getStringExtra("url");
    String type = intent.getStringExtra("type");
    int playtime = intent.getIntExtra("playtime", -1);
    int arg1 = intent.getIntExtra("arg1", -1);
    int arg2 = intent.getIntExtra("arg2", -1);
    String obj = intent.getStringExtra("obj");
    // log.d("url=" + url );
    log.d("type=" + type + ",playtime=" + playtime + ",arg1=" + arg1 + ",arg2=" + arg2 + ",obj=" + obj);
    if (type == null) {
        log.d("type is null.");
        return;
    }
    StringBuffer buf = new StringBuffer();
    if (type.equals("onInfo") || type.equals("onError")) {
        int what = arg1;
        DateTime dt = new DateTime();
        buf.append("#systemtime:" + dt.getFormattedDateTime("yyyyMMddHHmmss") + SEPARATOR);
        buf.append("url:" + url + SEPARATOR);
        buf.append("playtime:" + playtime + SEPARATOR);
        //buf.append("status:" + what + SEPARATOR);

        // 过滤需要处理的消息
        if (what == MEDIA_ERROR_UNKNOWN || what == MEDIA_ERROR_SERVER_DIED || what == MEDIA_INFO_BUFFERING_START || what == MEDIA_INFO_BUFFERING_END || what == MEDIA_INFO_BUFFERING_ERROR) {
            String desc = "";
            switch (what) {
                case MEDIA_ERROR_UNKNOWN:
                    buf.append("status:" + what + SEPARATOR);
                    break;
                case MEDIA_ERROR_SERVER_DIED:
                    buf.append("status:" + what + SEPARATOR);
                    break;
                case MEDIA_INFO_BUFFERING_START:
                    buf.append("status:" + 701 + SEPARATOR);
                    desc = "No data can play.";
                    break;
                case MEDIA_INFO_BUFFERING_END:
                    buf.append("status:" + 702 + SEPARATOR);
                    desc = "The data can play.";
                    break;
                case MEDIA_INFO_BUFFERING_ERROR:
                    buf.append("status:" + what + SEPARATOR);
                    desc = "No data,requet url is '" + obj + "'";
                    break;
            }
            buf.append("desc:" + desc + SEPARATOR);
            buf.append(SEPARATOR);
            writeLog(buf.toString());
        }
    }
}
```

通过上面的代码，可以看到它是将广播携带的日志信息写入到 `/tmp/playLog/` 目录下的日志文件中。