[toc]

### 1. MTK

#### 1.1 MT8788

##### 1.1.1 Android T

修改 `sys/packages/apps/Launcher3/src/com/android/launcher3/util/DisplayController.java` 文件中 `isTablet()` 方法将其返回 `false` 即可：

```java
/**
 * Returns {@code true} if the bounds represent a tablet.
 */
public boolean isTablet(WindowBounds bounds) {
    // return smallestSizeDp(bounds) >= MIN_TABLET_WIDTH;
    return false;
}
```

