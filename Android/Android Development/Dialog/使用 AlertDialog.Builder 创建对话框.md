[toc]

使用 `AlertDialog.Builder` 创建对话框的步骤如下：

+ 构建 Builder 项目。
+ 设置显示参数，比如按钮数量、项列表等。
+ 设置按钮的回调方法。
+ 告诉 Builder 构建对话框。所构建对话框的类型取决于在 Builder 对象的设置。
+ 使用 `dialog.show()` 显示对话框。

### 1. Kotlin 版本

```kotlin
import android.app.AlertDialog
import android.content.Context
import android.content.DialogInterface
import android.widget.Toast

fun showAlert(message: String, ctx: Context) {
    // Create a builder
    val builder = AlertDialog.Builder(ctx)
    builder.setTitle("Alert Window")
    builder.setMessage(message)

    // add buttons and listener
    builder.setPositiveButton("OK") { v: DialogInterface, buttonId: Int ->
       Toast.makeText(this, "Button id $buttonId clicked.", Toast.LENGTH_SHORT).show()
        v.dismiss()
    }

    // Create the dialog
    val dialog = builder.create()

    // show
    dialog.show()
}
```

### 2. Java 版本

```java
import android.app.AlertDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.widget.Toast;

public void showAlert(String message, Context ctx) {
    // Create a builder
    AlertDialog.Builder builder = new AlertDialog.Builder(ctx);
    builder.setTitle("Alert Window");
    builder.setMessage(message);

    // add buttons and listener
    builder.setPositiveButton("OK", (DialogInterface v, int buttonId) -> {
        Toast.makeText(this, "Button id $buttonId clicked.", Toast.LENGTH_SHORT).show();
        v.dismiss();
    });

    // Create the dialog
    AlertDialog dialog = builder.create();

    // show
    dialog.show();
}
```

> 注意
>
> `DialogInterface` 接口有两个重要方法：
>
> + `cancel()`
> + `dismiss()`
>
> 通常不需要调用这些方法，因为按钮单击操作会在必要时自动调用它们。
