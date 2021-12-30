[toc]

在 `AlertDialog` 对话框中使用自定义视图的步骤如下：

+ 为提示对话框创建布局视图。
+ 将布局加载到 `View` 类中。
+ 构造 `Builder` 对象。
+ 在 `Builder` 对象中设置视图。
+ 设置按钮和它们用于捕获所输入文本的回调。
+ 使用提示对话框生成器创建对话框
+ 显示对话框

### 1. 创建对话框布局文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginStart="20dp"
        android:layout_marginEnd="20dp"
        android:text="Your text goes here"
        android:gravity="left"
        android:textAppearance="?android:attr/textAppearanceMedium" />

    <EditText
        android:id="@+id/editText_prompt"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginStart="20dp"
        android:layout_marginEnd="20dp"
        android:scrollHorizontally="true"
        android:autoText="false"
        android:capitalize="none"
        android:gravity="fill_horizontal"
        android:textAppearance="?android:attr/textAppearanceMedium" />

</LinearLayout>
```

### 2. 创建并显示对话框

#### 2.1 Kotlin 版本

```kotlin
import android.app.AlertDialog
import android.content.Context
import android.view.LayoutInflater
import android.widget.EditText
import android.widget.Toast

fun showCustomAlert(ctx: Context) {
    val inflater = LayoutInflater.from(ctx)
    val view = inflater.inflate(R.layout.prompt_layout, null)

    // get a builder and set the view
    val builder = AlertDialog.Builder(ctx)
    builder.setTitle("Prompt")
    builder.setView(view)

    builder.setPositiveButton("OK") { _, _ ->
        val et = view.findViewById<EditText>(R.id.editText_prompt)
        Toast.makeText(this, "Prompt text: ${et.text}", Toast.LENGTH_SHORT).show()
    }
    builder.setNegativeButton("Cancel") { _, _ ->
        Toast.makeText(this, "Your cancel operation", Toast.LENGTH_SHORT).show()
    }

    // get the dialog
    val dialog = builder.create()
    dialog.show()
}
```

#### 2.2 Java 版本

```java
import android.app.AlertDialog;
import android.content.Context;

import android.view.LayoutInflater;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public void showCustomAlert(Context ctx) {
    LayoutInflater inflater = LayoutInflater.from(ctx);
    View view = inflater.inflate(R.layout.prompt_layout, null);

    // get a builder and set the view
    AlertDialog.Builder builder = new AlertDialog.Builder(ctx);
    builder.setTitle("Prompt");
    builder.setView(view);

    builder.setPositiveButton("OK", (dialog, buttonId) -> {
        EditText et = view.findViewById(R.id.editText_prompt) ;
        Toast.makeText(this, "Prompt text: " + et.getText(), Toast.LENGTH_SHORT).show();
    });
    builder.setNegativeButton("Cancel", (dialog, buttonId) -> {
        Toast.makeText(this, "Your cancel operation", Toast.LENGTH_SHORT).show();
    });

    // get the dialog
    AlertDialog dialog = builder.create();
    dialog.show();
}
```

