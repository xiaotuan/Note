[toc]

### 1. 设计提醒对话框

下面给出了创建提醒对话框需要执行的步骤：

（1）构造 Builder 项目。

（2）设置显示参数，比如按钮数量、项列表等。

（3）设置按钮的回调方法。

（4）告诉 Builder 构建对话框。所构建对话框的类型取决于在Builder 对象的设置。

（5）使用 dialog.show() 显示对话框。

**代码清单8-1** 构建和显示提醒对话框

```java
public class Alerts {
    
    public static void showAlert(String message, Context ctx) {
        // Create a builder
        AlertDialog.Builder builder = new AlertDialog.Builder(ctx);
        builder.setTitle("Alert Window");
        
        // add buttons and listener
        EmptyOnClickListener el = new EmptyOnClickListener();
        builder.setPositiveButton("OK", el);
        
        // Create the dialog
        AlertDialog ad = builder.create();
        
        // show
        ad.show();
    }
   
}

public class EmptyOnClickListener implements android.content.DialogInterface.OnClickListener {
    
    public void onClick(DialogInterface v, int buttonId) {
        
    }
    
}
```

### 2. 设计提示对话框

下面给出了创建提示对话框需要执行的步骤。

（1）为提示对话框创建布局视图。

（2）将布局加载到 View 类中。

（3）构造 Builder 对象。

（4）在 Builder 对象中设置视图。

（5）设置按钮和他们勇于捕获所输入文本的回调。

（6）使用提醒对话框生成器创建对话框。

（7）显示对话框。

#### 2.1 提示对话框的 XML 布局文件

**代码清单8-2** prompt_layout.xml 文件

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical">
	
    <TextView
        android:id="@+id/promptmessage"
        android:layout_height="wrap_content"
        android:layout_width="wrap_content"
        android:layout_marginLeft="20dp"
        android:layout_marginRight="20dp"
        android:text="Your text goes here"
        android:gravity="left"
        android:textAppearance="?android:attr/textAppearanceMedium" />
    
    <EditText
        android:id="@+id/editText_prompt"
        android:layout_height="wrap_content"
        android:layout_width="match_parent"
        android:layout_marginLeft="20dp"
        android:layout_marginRight="20dp"
        android:scrollHorizontally="true"
        android:autoText="false"
        android:capitalize="none"
        android:gravity="fill_horizontal"
        android:textAppearance="?android:attr/textAppearanceMedium" />
    
</LinearLayout>
```

#### 2.2 设置提醒对话框生成器和用户视图

**代码清单8-3** 将布局填充到对话框中

```java
LayoutInflater li = LayoutInflater.from(activity);
// the 'activity' variable is a reference to your activity or context
View view = li.inflate(R.layout.prompt_layout, null);

// get a builder and set the view
AlertDialog.Builder builder = new AlertDialog.Builder(ctx);
builder.setTitle("Prompt");
builder.setView(view);
```

#### 2.3 设置按钮和监听器

**代码清单8-4** 设置 OK 和 Cancel 按钮

```java
// add buttons and listener
PromptListener pl = new PromptListener(view);
builder.setPositiveButton("OK", pl);
builder.setNegativeButton("Cancel", pl);
```

#### 2.4 创建和显示提示对话框

**代码清单8-5** 告诉提醒对话框生成器创建对话框

```java
// get the dialog
AlertDialog ad = builder.create();
ad.show();

// return the prompt
return pl.getPromptReply();
```

#### 2.5 提示对话框监听器

**代码清单8-6** 监听器回调类 PromptListener

```java
public class PromptListener implements android.content.DialogInterface.OnClickListener {
    // local variable to return the prompt reply value
    private String promptReply = null;
    
    // Keep a variable for the view to retrieve the prompt value
    View proptDialogView = null;
    
    // Take in the view in the constructor
    public PromptListener(View inDialogView) {
        promptDialogView = inDialogView;
    }
    
    // Call back method from dialogs
    public void onClick(DialogInterface v, int buttonId) {
        if (buttonId == DialogInterface.BUTTON_POSITIVE) {
            // ok button
            promptReply = getPromptText();
        } else {
            // cancel button
            promptReply = null;
        }
    }
    
    // Just an access method for what is in the edit box
    private String getPromptText() {
        EditText et = (EditText) promptDialogView.findViewById(R.id.editText_prompt);
        return et.getText().toString();
    }
    
    public String getPromptReply() {
        return promptReply;
    }
    
}
```

#### 2.6 组合各部分

**代码清单8-7** 测试提示对话框的代码

```java
public class Alerts {
    
    public static String prompt(String message, Context ctx) {
        // load some kind of a view
        LayoutInflater li = LayoutInflater.from(ctx);
        View view = li.inflate(R.layout.prompt_layout, null);
        
        // get a builder and set the view
        AlertDialog.Builder builder = new AlertDialog.Builder(ctx);
        builder.setTitle("Prompt");
        builder.setView(view);
        
        // add buttons and listener
        PromptListener pl = new PromptListener(view);
        builder.setPositiveButton("OK", pl);
        builder.setNegativeButton("Cancel", pl);
        
        // get the dialog
        AlertDialog ad = builder.create();
        
        // show
        ad.show();
        
        return pl.getPromptReply();
    }
    
}
```

### 3. Android 对话框的特性

在 Android 中显示对话框是一个异步过程。显示对话框以后，调用对话框的主线程将返回并继续执行剩余代码。这并不是说对话框不是**模态**对话框。对话框仍然是模态的。鼠标单击仅适用于对话框，而父活动会回到其消息循环中。

### 4. 重新设计提示对话框

我们再看看前面的提示对话框实现中存在问题的代码：

```java
if (item.getItemId() == R.id.your_menu_id) {
    String reply = Alerts.showPrompt("Your goes here", this);
}
```

我们已经证明，字符串变量 reply 的值将为 null，因为由 Alerts.showPrompt() 发起的提示对话框无法在相同线程上返回值。解决此问题的唯一方法是，让活动直接实现回调方法：

```java
public class SampleActivity extends Activity implements android.content.DialogInterface.OnClickListener {
    
    ... other code
    if (item.getItemId() == R.id.your_menu_id) {
        Alerts.showPrompt("Your text goes here", this);
    }
    ...
    public void onClick(DialogInterface v, int buttonId) {
        // figure out a way here to read the reply string from the dialog
    }
}
```

