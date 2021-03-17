[toc]

Toast 类似于包含一条消息的提醒对话框，会显示一定时间并消失。它是一种短暂的提醒消息。

**代码清单8-15** 提供了使用 Toast 显示消息的示例

```java
// Create a function to wrap a message as toast
// show the toast
public void reportToast(String message) {
    String s = tag + ":" + message;
    Toast mToast = Toast.makeText(activity, s, Toast.LENGHT_SHORT);
    mToast.show();
    Log.d(tag, message);
}

// You can invoke the function above
// multiple times if needed as below
private void testToast() {
    reportToast("Message1");
    reportToast("Message2");
    reportToast("Message3");
}
```

