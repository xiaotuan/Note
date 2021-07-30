[toc]

### 1. MTK8168 Android R

#### 1.1 修改 `frameworks/base/core/res/res/values/strings.xml` 文件

在文件末尾添加如下字符串：

```xml
<string name="shutdown_password_dialog_title">关机密码</string>
```

#### 1.2 修改 `frameworks/base/core/res/res/values/symbols.xml` 文件

在文件末尾添加如下代码，使对话框使用的资源对外开放：

```xml
<java-symbol type="id" name="error_tip" />
<java-symbol type="id" name="password" />
<java-symbol type="layout" name="shutdown_password_dialog" />
<java-symbol type="string" name="shutdown_password_dialog_title" />
```

#### 1.3 添加对话框布局文件 `frameworks/base/core/res/res/layout/shutdown_password_dialog.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content">

    <TextView
        android:id="@+id/error_tip"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="4dp"
        android:layout_marginLeft="16dp"
        android:layout_marginRight="16dp"
        android:gravity="center"
        android:textSize="18sp"
        android:textColor="@color/holo_red_light"
        android:text="@string/passwordIncorrect" />

    <EditText
        android:id="@+id/password"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="4dp"
        android:layout_marginBottom="8dp"
        android:layout_marginLeft="16dp"
        android:layout_marginRight="16dp"
        android:inputType="textPassword"
        android:singleLine="true"
        android:textSize="18sp"/>

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginLeft="16dp"
        android:layout_marginRight="16dp"
        android:orientation="horizontal">

        <View
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1" />

        <Button
            android:id="@+id/ok"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textAllCaps="false"
            android:text="@string/ok" />

        <Button
            android:id="@+id/cancel"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textAllCaps="false"
            android:layout_marginRight="8dp"
            android:layout_marginLeft="8dp"
            android:text="@string/cancel" />
    </LinearLayout>

</LinearLayout>
```

#### 1.4 添加对话框实现文件 `vendor/mediatek/proprietary/packages/apps/SystemUI/src/com/android/systemui/globalactions/ShutdownPasswordDialog.java`

```java
package com.android.systemui.globalactions;

import android.content.Context;
import android.os.UserManager;
import com.android.internal.R;
import com.android.systemui.plugins.GlobalActions.GlobalActionsManager;

import android.app.Dialog;
import android.content.Context;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.Display;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.view.inputmethod.InputMethodManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.util.TypedValue;

public class ShutdownPasswordDialog {

    private Context mContext;
    private View mDialogView;
    private TextView mErrorTipTv;
    private EditText mPasswordEt;
    private Button mOkBtn;
    private Button mCancelBtn;
    private Dialog mPasswordDialog;

    private final GlobalActionsManager mWindowManagerFuncs;

    public ShutdownPasswordDialog(Context context, GlobalActionsManager windowManagerFuncs) {
        mContext = context;
        mWindowManagerFuncs = windowManagerFuncs;
        LayoutInflater inflater = (LayoutInflater) mContext.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
        mDialogView = inflater.inflate(R.layout.shutdown_password_dialog, null);
        mErrorTipTv = (TextView) mDialogView.findViewById(R.id.error_tip);
        mPasswordEt = (EditText) mDialogView.findViewById(R.id.password);
        mOkBtn = (Button) mDialogView.findViewById(R.id.ok);
        mCancelBtn = (Button) mDialogView.findViewById(R.id.cancel);
        mPasswordEt.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {
                mErrorTipTv.setVisibility(View.INVISIBLE);
            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
            }

            @Override
            public void afterTextChanged(Editable s) {
            }
        });
        mOkBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                hideKeyboard();
                String password = mPasswordEt.getText().toString();
                if ("510".equals(password)) {
                    mWindowManagerFuncs.shutdown();
                } else {
                    mErrorTipTv.setVisibility(View.VISIBLE);
                }
            }
        });
        mCancelBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                hideKeyboard();
                mPasswordDialog.dismiss();
            }
        });
        mPasswordDialog = createDialog();
    }

    private Dialog createDialog() {
        Dialog dialog = new Dialog(mContext, getDialogTheme(mContext));
        dialog.setTitle(R.string.shutdown_password_dialog_title);
        Window window = dialog.getWindow();
        window.setContentView(mDialogView);
        //设置dialog大小，这里是一个小赠送，模块好的控件大小设置
        Window dialogWindow = dialog.getWindow();
        WindowManager manager = (WindowManager) mContext.getSystemService(Context.WINDOW_SERVICE);
        WindowManager.LayoutParams params = dialogWindow.getAttributes(); // 获取对话框当前的参数值
        dialogWindow.setGravity(Gravity.CENTER);//设置对话框位置
        Display d = manager.getDefaultDisplay(); // 获取屏幕宽、高度
        params.width = (int) (d.getWidth() * 0.65); // 宽度设置为屏幕的0.65，根据实际情况调整
        params.height = 230;
        dialogWindow.setAttributes(params);
        dialog.setCanceledOnTouchOutside(false); // Handled by the custom class.
        dialog.getWindow().setType(WindowManager.LayoutParams.TYPE_KEYGUARD_DIALOG);
        return dialog;
    }

    public void show() {
        mErrorTipTv.setVisibility(View.INVISIBLE);
        mPasswordEt.setText("");
        mPasswordDialog.show();
    }

    public void dismiss() {
        mErrorTipTv.setVisibility(View.INVISIBLE);
        mPasswordEt.setText("");
        mPasswordDialog.dismiss();
    }

    private void hideKeyboard() {
        InputMethodManager imm = (InputMethodManager) mContext.getSystemService(Context.INPUT_METHOD_SERVICE);
        imm.hideSoftInputFromWindow(mPasswordEt.getWindowToken(), 0);
    }

    private static int getDialogTheme(Context context) {
        TypedValue outValue = new TypedValue();
        context.getTheme().resolveAttribute(com.android.internal.R.attr.alertDialogTheme,
                outValue, true);
        return outValue.resourceId;
    }
}
```

#### 1.5 修改 `vendor/mediatek/proprietary/packages/apps/SystemUI/src/com/android/systemui/globalactions/GlobalActionsDialog.java` 文件

将如下代码：

```java
final class ShutDownAction extends SinglePressAction implements LongPressAction {
    private ShutDownAction() {
        super(R.drawable.ic_lock_power_off,
              R.string.global_action_power_off);
    }

    @Override
    public boolean onLongPress() {
        if (!mUserManager.hasUserRestriction(UserManager.DISALLOW_SAFE_BOOT)) {
            mWindowManagerFuncs.reboot(true);
            return true;
        }
        return false;
    }

    @Override
    public boolean showDuringKeyguard() {
        return true;
    }

    @Override
    public boolean showBeforeProvisioning() {
        return true;
    }

    @Override
    public void onPress() {
        // shutdown by making sure radio and power are handled accordingly.
        mWindowManagerFuncs.shutdown();
    }
}
```

修改成：

```java
final class ShutDownAction extends SinglePressAction implements LongPressAction {
    private ShutDownAction() {
        super(R.drawable.ic_lock_power_off,
              R.string.global_action_power_off);
    }

    @Override
    public boolean onLongPress() {
        if (!mUserManager.hasUserRestriction(UserManager.DISALLOW_SAFE_BOOT)) {
            mWindowManagerFuncs.reboot(true);
            return true;
        }
        return false;
    }

    @Override
    public boolean showDuringKeyguard() {
        return true;
    }

    @Override
    public boolean showBeforeProvisioning() {
        return true;
    }

    @Override
    public void onPress() {
        // shutdown by making sure radio and power are handled accordingly.
        //mWindowManagerFuncs.shutdown();
        mPasswordDialog.show();
    }
}
```

