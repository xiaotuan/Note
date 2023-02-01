`FrameLayout` 主要用于动态显示单一视图，但可以向其中填充许多项，将一个项设置为可见，而将其与设置为不可见。

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content">

    <ImageView
        android:id="@+id/oneImgView"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:scaleType="fitCenter"
        android:src="@drawble/one"/>
    
    <ImageView
        android:id="@+id/twoImgView"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:scaleType="fitCenter"
        android:src="@drawable/two"
        android:visibility="gone" />

</FrameLayout>
```

`FrameLayout` 不会强制一次只显示一个控件。如果向布局中添加许多控件，那么 `FrameLayout` 会简单地将控件堆叠在一起，最后一个控件位于最顶部。

`FrameLayout` 的另一个有趣之外是，如果向该布局添加多个控件，布局的大小将按容器中最大项的大小来计算。

另请注意，如果在 `FrameLayout` 中放入了许多控件，而且一个或多个控件在最初时是不可见的，那么可以考虑对 `FrameLayout` 使用 `setMeasureAllChildren(true)`。因为最大的子控件确定了布局的大小，所以如果最大的子控件在开始时不可见，那么讲话遇到问题。也就是说，当它变得可见时，它将仅能显示一部分。为了确保所有项都正确地呈现，可以调用 `setMeasureAllChidren()` 并向其传入值 true。与 `FrameLayout` 等价的 XML 特性是 `android:measureAllChildren="true"`。