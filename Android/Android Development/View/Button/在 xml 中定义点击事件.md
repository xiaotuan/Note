[toc]

可以在 XML 中定义 `Button` 的点击事件，而不需要调用 `setOnClickListener()` 方法设置点击方法了。

### 1. 在 xml 中定义点击方法

```xml
<Button
        android:id="@+id/ccbtn1"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:onClick="myClickHandler"
        android:text="@string/basicBtnLabel" />
```

### 2. 在代码中实现点击方法

#### 2.1 Kotlin

```kotlin
public fun myClickHandler(view: View) {
  when (view.id) {
    R.id.ccbtn1 -> {
      ......
    }
  }
}
```

#### 2.2 Java

```Java
public void myClickHandler(View view) {
  switch (view.getId()) {
    case R.id.ccbtn1:
      ......
  }
}
```

