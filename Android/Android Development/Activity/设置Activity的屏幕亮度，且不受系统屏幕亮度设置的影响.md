可以在 `Activity` 的 `onCreate` 方法中添加如下代码，设置该 `Activity` 的屏幕亮度，且该亮度不受系统屏幕亮度设置的影响：

```java
android.view.Window window = getWindow();
android.view.WindowManager.LayoutParams lp = window.getAttributes();
lp.screenBrightness = 1.0f;
window.setAttributes(lp);
```

