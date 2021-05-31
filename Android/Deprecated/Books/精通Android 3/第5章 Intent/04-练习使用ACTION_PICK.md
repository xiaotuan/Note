ACTION_PICK 的理念是启动一个活动来显示项列表。该活动然后应该允许用户从该列表中挑选一个项。用户挑选了项之后，活动应该项调用方返回所挑选项的 URI。

应该使用执行一个 Android 内容游标的 MIME 类型，以指明要从中选择的项集合。此 URI 的实际 MIME 类型应该类似于：

```
vnd.android.cursor.dir/vnd.google.note
```

如果希望 startActivity() 返回数据，可以使用 startActivityForResult()，它包含一个回调。我们看一下 Activity 类中 startActivityForResult() 方法的签名：

```java
public void startActivityForResult(Intent intent, int requestCode)
```

此方法启动希望从中获得结果的活动。当存在此活动时，将使用给定的 requestCode 调用源活动的 onActivityResult() 方法。此回调方法的签名为：

```java
protected void onActivityResult(int requestCode, int resultCode, Intent data)
```

requestCode 是调用 startActivityForResult() 时传入的 requestCode，resultCode 可以是 RESULT_OK、RESULT_CANCELED或自定义代码。自定义代码应该以 RESULT_FIRST_USER 开头。 Intent 参数包含所调用活动希望返回的任何附加数据。

**代码清单5-3** 在调用操作后返回数据

```java
public class SomeActivity extends Activity {
    ......
    public static void invokePick(Activity activity) {
        Intent pickIntent = new Intent(Intent.ACTION_PICK);
        int requestCode = 1;
        pickIntent.setData(Uri.parse("content://com.google.provider.NotePad/notes"));
        activity.startActivityForResult(pickIntent, requestCode);
    }
    
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        // This is to inform the parent class (Activity)
        // that the called activity has finished and the baseclass
        // can do the necessary clean up
        super.onActivityResult(requestCode, resultCode, data);
        parseResult(this, requestCode, resultCode, data);
    }
    
    public static void parseResult(Activity activity, int requestCode, int resultCode, Intent data) {
        if (requestCode != 1) {
            Log.d("Test", "Some one else called this. not us");
            return;
        }
        if (resultCode != Activity.RESULT_OK) {
            Log.d("Test", "Result code is not ok: " + resultCode);
            return;
        } 
        Log.d("Test", "Result code is ok: " + resultCode);
        Uri selectedUri = data.getData();
        Log.d("Test", "The output uri: " + selectedUri.toString());
        
        // Proceed to display the note
        data.setAction(Intent.ACTION_VIEW);
        startActivity(data);
    }
}
```

