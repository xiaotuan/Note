**代码清单5-1** 练习 Android 中预制的应用程序

```java
public class IntentsUtils {

    public static void invokeWebBrowser(Activity activity) {
        Intent intent = new Intent(Intent.ACTION_VIEW);
        intent.setData(Uri.parse("https://www.baidu.com"));
        activity.startActivity(intent);
    }

    public static void invokeWebSearch(Activity activity) {
        Intent intent = new Intent(Intent.ACTION_WEB_SEARCH);
        intent.setData(Uri.parse("https://www.baidu.com"));
        activity.startActivity(intent);
    }

    public static void dial(Activity activity) {
        Intent intent = new Intent(Intent.ACTION_DIAL);
        activity.startActivity(intent);
    }

    public static void call(Activity activity) {
        Intent intent = new Intent(Intent.ACTION_CALL);
        intent.setData(Uri.parse("tel:904-905-5646"));
        activity.startActivity(intent);
    }

    public static void showMapAtLatLong(Activity activity) {
        Intent intent = new Intent(Intent.ACTION_VIEW);
        // geo:lat, long?=z=zoomlevel&q=question-string
        intent.setData(Uri.parse("geo:0,0?z=4&q=business+near+city"));
        activity.startActivity(intent);
    }

    public static void tryOneOfThese(Activity activity) {
        IntentsUtils.call(activity);
    }
}
```

**代码清单5-2** 创建简单菜单的测试工具

```java
public class MainActivity extends Activity {
    
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        
        TextView tv = new TextView(this);
        tv.setText("Hello, Android. Say hello");
        setContentView(tv);
    }
    
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        super.onCreateOptionsMenu(menu);
        int base = Menu.FIRST;	// value is 1
        MenuItem item1 = menu.add(base, base, base, "Test");
        return true;
    }
    
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        if (item.getItemId() == 1) {
            IntentUtils.tryOneOfThese(this);
        } else {
            return super.onOptionsItemSelected(item);
        }
        return true;
    }
}
```

