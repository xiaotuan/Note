在代码中，可以使用如下代码设置 `RelativeLayout` 布局中元素的 `android:layout_alignParentLeft`、`android:layout_alignParentTop`、`android:layout_alignParentRight`、`android:layout_alignParentBottom` 和 `android:layout_centerInParent` 属性：

```java
view = mView.findViewById(R.id.lockscreen_clock_view_large);
lp = (RelativeLayout.LayoutParams) view.getLayoutParams();
lp.addRule(RelativeLayout.CENTER_IN_PARENT, 1);
view.setLayoutParams(lp);
```

如果要删除 `android:layout_below` 属性，可以使用如下代码：

```java
lp.removeRule(RelativeLayout.CENTER_IN_PARENT);
```

