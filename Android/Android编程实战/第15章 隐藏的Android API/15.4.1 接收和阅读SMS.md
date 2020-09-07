应用程序要想接收 SMS 必须声明使用 RECEIVE_SMS 权限，并且实现 BroadcastReceiver，以处理收到的短信。

```java
public class MySmsReceiver extends BroadcastReceiver {
    // Telephony.java 中隐藏的常量
    public static final String SMS_RECEIVED_ACTION = "android.provider.Telephony.SMS_RECEIVED";
    public static final String MESSAGE_SERVICE_NUMBER = "+461234567890";
    public static final String MESSAGE_SERVICE_PREFIX = "MYSERVICE";
    
    public void onReceive(Context context, Intent intent) {
        String action = intent.getAction();
        if (SMS_RECEIVED_ACTION.equals(action)) {
            // 通过 "pdus" 获取 SMS 数据的隐藏键
            Object[] messages = (Object[]) intent.getSerializableExtra("pdus");
            for (Object message : messages) {
                byte[] messageData = (byte[]) message;
                SmsMessage smsMessage = SmsMessage.createFromPdu(messageData);
                processSms(smsMessage);
            }
        }
    }
    
    private void processSms(SmsMessage smsMessage) {
        String from = smsMessage.getOriginationAddress();
        if (MESSAGE_SERVICE_NUMBER.equals(from)) {
            String messageBody = smsMessage.getMessageBody();
            if (messageBody.startsWith(MESSAGE_SERVICE_PREFIX)) {
                // TODO: 消息验证通过，开始处理
            }
        }
    }
}
```

要阅读已经收到的 SMS，需要查询一个隐藏的 `ContentProvider`，并声明使用 READ_SMS 权限。

```java
@Override
public void onActivityCreated(Bundle savedInstanceState) {
    super.onActivityCreated(savedInstanceState);
    mAdapter = new SimpleCursorAdapter(this, 
                                       R.layout.sms_list_item, 
                                       null, 
                                       new String[] { Telephony.Sms.ADDRESS, Telephony.Sms.BODY, Telephony.Sms.DATE },
                                      new int[] { R.id.sms_from, R.id.sms_body, R.id.sms_received},
                                      CursorAdapter.FLAG_REGISTER_CONTENT_OBSERVER);
    setListAdapter(mAdapter);
    getLoaderManager().initLoader(0, null, this);
}

public Loader<Cursor> onCreateLoader(int id, Bundle args) {
    Uri smsUri = Telephony.Sms.CONTENT_URI;
    return new CursorLoader(getActivity(), smsUri, new String[] {
        Telephony.Sms._ID,
        Telephony.Sms.ADDRESS,
        Telephony.Sms.BODY,
        Telephony.Sms.DATE },
        null, null, Telephony.Sms.DEFAULT_SORT_ORDER);
}
```

