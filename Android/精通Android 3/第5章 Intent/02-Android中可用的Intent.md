**代码清单5-1** 练习 Android 中预制的应用程序

```java
public class IntentsUtils {
    
    public static void invokeWebBrowser(Activity action) {
        Intent intent = new Intent(Intent.ACTION_VIEW);
        intent.setData(Uri.parse("http://www.google.com"));
        activity.startActivity(intent);
    }
    
    public static void invokeWebSearch(Activity activity) {
        Intent intent = new Intent(Intent.ACTION_WEB_SEARCH);
        intent.setData(Uri.parse("http://www.google.com"));
        activity.startActivity(intent);
    }
    
    public static void dial(Activity activity) {
        Intent intent = new Intent(Intent.ACTION_CALL);
        intent.setData(Uri.parse("tel:555-555-5555"));
        activity.startActivity(intent);
    }
    
}
```

