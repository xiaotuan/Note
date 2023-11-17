[toc]

### 1. MTK

#### 1.1 MT8788

##### 1.1.1 Android T

1. 修改 `sys/packages/apps/Launcher3/src/com/android/launcher3/util/DisplayController.java` 文件中 `isTablet()` 方法将其返回 `false` 即可：

   ```java
   /**
    * Returns {@code true} if the bounds represent a tablet.
    */
   public boolean isTablet(WindowBounds bounds) {
       // return smallestSizeDp(bounds) >= MIN_TABLET_WIDTH;
       return false;
   }
   ```

2. 修改 `packages/apps/Launcher3/src/com/android/launcher3/util/window/WindowManagerProxy.java` 文件中 `normalizeWindowInsets()` 和 `estimateWindowBounds()` 方法的如下代码：

   ```diff
   @@ -153,7 +153,7 @@ public class WindowManagerProxy implements ResourceBasedOverride {
            Resources systemRes = context.getResources();
            Configuration config = systemRes.getConfiguration();
    
   -        boolean isTablet = config.smallestScreenWidthDp > MIN_TABLET_WIDTH;
   +        boolean isTablet = false;//config.smallestScreenWidthDp > MIN_TABLET_WIDTH;
            boolean isGesture = isGestureNav(context);
            boolean isPortrait = config.screenHeightDp > config.screenWidthDp;
           
   @@ -240,7 +240,7 @@ public class WindowManagerProxy implements ResourceBasedOverride {
                systemRes = context.createConfigurationContext(conf).getResources();
            }
    
   -        boolean isTablet = swDp >= MIN_TABLET_WIDTH;
   +        boolean isTablet = false;//swDp >= MIN_TABLET_WIDTH;
            boolean isTabletOrGesture = isTablet
                    || (Utilities.ATLEAST_R && isGestureNav(context));
    
   ```

   

