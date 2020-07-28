[toc]

##### 1. 自定义 View 的 onMeasure 方法解析

**SquareFrameLayout.java的onMeasure()**

```java
@Override
protected void onMeasure(int widthMeasureSpec, int heightMeasureSpec) {
    final int widthSize = MeasureSpec.getSize(widthMeasureSpec);
    final int heightSize = MeasureSpec.getSize(heightMeasureSpec);

    if (widthSize == 0 && heightSize == 0) {
        // If there are no constraints on size, let FrameLayout measure
        super.onMeasure(widthMeasureSpec, heightMeasureSpec);

        // Now use the smallest of the measured dimensions for both dimensions
        final int minSize = Math.min(getMeasuredWidth(), getMeasuredHeight());
        setMeasuredDimension(minSize, minSize);
        return;
    }

    final int size;
    if (widthSize == 0 || heightSize == 0) {
        // If one of the dimensions has no restriction on size set both dimensions to be
        // on that does
        size = Math.max(widthSize, heightSize);
    } else {
        // Both dimensions have restrictions on size, set both dimensions to be the
        // smallest of the two
        size = Math.min(widthSize, heightSize);
    }
    final int newMeasureSpec = MeasureSpec.makeMeasureSpec(size, MeasureSpec.EXACTLY);
    super.onMeasure(newMeasureSpec, newMeasureSpec);
}
```

（1）`MeasureSpec.getSize(widthMeasureSpec)` 方法获取 `View` 的真实尺寸，如果 `View` 在布局文件中设置的是 `LayoutParams.MATCH_PARENT`，则该方法返回的值为 0。