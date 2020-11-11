接收 TR069_PROTOCOL 广播的代码在 `src/net/sunniwell/tms/CWMPBroadcastReceiver.java`，具体代码如下所示：

```java
private Handler doHandler = new Handler() {

    public void handleMessage(Message msg) {
        Intent intent = (Intent) msg.obj;
        String sAction = intent.getAction();
        log.d("======do====CWMPService=============" + sAction);
        ......
        } else if (sAction.equals(Constant.TR069_PROTOCOL)) {
            try {
                if(CWMPService.getInstance()!=null &&CWMPService.getInstance().getHandler()!=null )
                    CWMPService.getInstance().getHandler().sendEmptyMessage(intent.getIntExtra("eventCode", -1));
            } catch (NullPointerException e) {
                e.printStackTrace();
            }
        } else if (sAction.equals(MEDIA_CHANGED_BROADCAST)) {// 播控诊断，软探针逻辑
        ......
    }
}
```

可以看出它将会向 `src/net/sunniwell/tms/CWMPEventHandler.java` 发送消息，具体的消息是通过该广播 Intent 中的 eventCode 附带信息获取的。从上面的代码我们无法看出它将会发送什么样的消息，那就先看下会有谁发送该广播吧。通过搜索得到如下结果：

```console
./SWTR069_sd_sunniwell/src/net/sunniwell/tms/CWMPEventHandler.java:952:                 Intent intent = new Intent(Constant.TR069_PROTOCOL);
./SWTR069_sd_sunniwell/src/net/sunniwell/tms/CWMPEventHandler.java:953:                 intent.putExtra(Constant.TR069_PROTOCOL_EVENTCODE, CWMPEvent.EVENT_CWMP_PERIOD);
```

我们进到  `src/net/sunniwell/tms/CWMPEventHandler.java` 代码中看下，它发送的代码：

```java
public void refreshPeriodTimer(long period) {
    try {
        log.d("period=" + period);
        Intent intent = new Intent(Constant.TR069_PROTOCOL);
        intent.putExtra(Constant.TR069_PROTOCOL_EVENTCODE, CWMPEvent.EVENT_CWMP_PERIOD);
        PendingIntent pIntent = PendingIntent.getBroadcast(mContext, 0, intent, PendingIntent.FLAG_UPDATE_CURRENT);
        AlarmManager alarmManager = (AlarmManager) mContext.getSystemService(Context.ALARM_SERVICE);
        // 若已启动
        //			if (CWMPService.isConnectCPE)
        alarmManager.cancel(pIntent);
        alarmManager.setRepeating(AlarmManager.RTC_WAKEUP, System.currentTimeMillis()+period, period, pIntent);
    } catch (Exception e) {
        log.d("catch e" + e);
        e.printStackTrace();
    }
}
```

再来看下调用 refreshPeriodTimer() 方法的代码：

```java
/**
	 * 指示此次会话由第一次 CPE 安 装或ACS URL发生了变化而建 立的。 必 须 导 致 BOOTSTRAP EventCode 的特定条件：
	 * a) CPE 在出厂后第一次到 ACS 的连接 b) CPE 在恢复为出厂配置后 第一次到 ACS 的连接 c) CPE 在 ACS URL
	 * 被修改后 （通过任何方法） 第一次到 ACS 的连接 跟其他所有的 EventCode 值一 样， BOOTSTRAP EventCode 可
	 * 能跟其他的 EventCode 值一起 包含在事件数组（Event array） 中。这是可能发生的，例如， CPE 出厂后首次 boot
	 * 时，CPE 会同时包含 BOOTSTRAP 和 BOOT EventCode。
	 * 
	 * @param event
	 * 
	 * 
	 *            首先检测是否是 0 boot 在检测是否是 是否是 升级，恢复出厂设置，重启
	 * 
	 */
	private synchronized void onBoot() {
		log.d("======== TR069  onBoot=======");
		String mReboot = getPreference(DataPreferences.MREBOOT);
		String mDownload = getPreference(DataPreferences.MDOWNLOAD);
		log.d("==mReboot===" + mReboot + "=====mdownload==" + mDownload);
		try {
			......
			// 完成首次启动后，修改标志位
			// 按照InformResponse报文中约定的时间间隔触发心跳
			long period = Long.parseLong(DataResolver.getInstance().getParameterValue(Constant.FTP_UPGTADE_PERIOD)) * 1000;
			refreshPeriodTimer(period);
			// 更新syslog的Timer
			refreshSyslogTimer();
			......
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
```

可以看到这个方法是在接收到网络改变和认证广播的时候执行。

通过上面的分析，我们现在知道了接收到 TR069_PROTOCOL 广播时，将会发送 EVENT_CWMP_PERIOD 消息到  `src/net/sunniwell/tms/CWMPEventHandler.java` 。下面来分析 CWMPEventHandler.java 中的相关代码：

```java
@Override
public void handleMessage(Message msg) {
    log.d("msg====start====== " + msg.what);
    super.handleMessage(msg);
    switch (msg.what) {
		......
        case CWMPEvent.EVENT_CWMP_PERIOD:
            doPeriod();
            break;
        ......
    }
}
```

CWMPEventHandler 在接收到 EVENT_CWMP_PERIOD 消息后会执行 doPeriod() 方法：

```java
/**
 * 2 PERIODIC指示此次会话的建立是基于周 期性的 Inform 间隔 [pɪrɪ'ɑdɪk]
 */
private void doPeriod() { // 会话建立了定期通知间隔心跳
    log.d("======== TR069  onPeriod=======" + DataResolver.getInstance().getParameterValue(Constant.FTP_UPGTADE_PERIOD) + "s");
    try {
        ArrayList<ParameterValueStruct> mPeriodic = CWMPObserverManager.getmPeriodic();

        if (mPeriodic != null && mPeriodic.size() > 0) {
            for(ParameterValueStruct struct : mPeriodic){
                Log.d("VALUE-CHANGE", "doPeriod, struct.name = "+struct.name);
            }
            sendInform(new String[] { CWMPEvent.EVENT_CODE_STRING_PERIODIC, CWMPEvent.EVENT_CODE_STRING_VALUE_CHANGE }, mPeriodic);
            mPeriodic.clear();
        } else {
            sendInform(new String[] { CWMPEvent.EVENT_CODE_STRING_PERIODIC }, null);
        }
    } catch (IOException e) {
        e.printStackTrace();
    } catch (InterruptedException e) {
        e.printStackTrace();
    }
    CWMPObserverManager.getmPeriodic().clear();
}
```

通过上面代码的注释可以看出该方法是向服务器周期性发送心跳数据的，但是我们在这个方法中没有看到可以周期性发送的代码，那么它是怎么周期性发送的呢？其实它是在 refreshPeriodTimer() 方法中设置了定时闹钟实现的。

从上面的代码可以知道它通过 sendInform() 方法向网管平台发送消息的。