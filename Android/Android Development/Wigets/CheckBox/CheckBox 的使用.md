[toc]

`CheckBox` （复选框）是一种具有 2 种状态的按钮，允许用户切换它的状态。

### 1. 在 xml 中定义 CheckBox

```xml
<CheckBox
          android:id="@+id/chickenCB"
          android:layout_width="wrap_content"
          android:layout_height="wrap_content"
          android:checked="true"
          android:text="Chicken" />
```

### 2. 在代码中使用 CheckBox

#### 2.1 Kotlin

```kotlin
import android.widget.CheckBox

val cb = findViewById<CheckBox>(R.id.chickenCB)

if (cb.isChecked) {
  cb.toggle()	// flips the checkbox to unchecked if it was checked
}

cb.setOnCheckedChangeListener { checkBox, isChecked -> {
  Log.v("CheckBoxActivity", "The cb checkbox is now "
       + (isChecked ? "checked" : "not checked"));
}}
```

#### 2.2 Java

```java
import android.widget.CheckBox;

CheckBox cb = findViewById(R.id.chickenCB);

if (cb.isChecked()) {
  cb.toggle();	// flips the checkbox to unchecked if it was checked
}

cb.setOnCheckedChangeListener((checkBox, isChecked) -> {
  Log.v("CheckBoxActivity", "The cb checkbox is now "
       + (isChecked ? "checked" : "not checked"));
});
```

>   注意：如果使用 `onClick()` 方法，你需要适当地转换按钮来自行确定它的状态，然后对它调用 `isChecked()`。

