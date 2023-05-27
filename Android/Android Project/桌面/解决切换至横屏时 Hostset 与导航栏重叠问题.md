[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android T

Android 12 风格下允许桌面旋转，在旋转至横屏时，桌面底部的 Hostset 与导航栏重叠。可以通过修改 `vendor/mediatek/proprietary/packages/apps/Launcher3/src/com/android/launcher3/util/window/WindowManagerProxy.java` 文件中 `normalizeWindowInsets()` 和 `estimateWindowBounds()` 两个方法的如下代码：

```diff
@@ -156,7 +156,9 @@ public class WindowManagerProxy implements ResourceBasedOverride {
         boolean isTablet = config.smallestScreenWidthDp > MIN_TABLET_WIDTH;
         boolean isGesture = isGestureNav(context);
         boolean isPortrait = config.screenHeightDp > config.screenWidthDp;
-
+       
+               // Solve the overlap problem between Hostset and NavigationBar by qty {{&&
+               /*
         int bottomNav = isTablet
                 ? 0
                 : (isPortrait
@@ -164,6 +166,18 @@ public class WindowManagerProxy implements ResourceBasedOverride {
                         : (isGesture
                                 ? getDimenByName(systemRes, NAVBAR_HEIGHT_LANDSCAPE)
                                 : 0));
+               */
+               boolean navBarCanMove = ResourceUtils.getBoolByName("config_navBarCanMove", systemRes, true);
+               int bottomNav = isTablet
+                ? 0
+                : (isPortrait
+                        ? getDimenByName(systemRes, NAVBAR_HEIGHT)
+                        : (isGesture
+                                ? getDimenByName(systemRes, NAVBAR_HEIGHT_LANDSCAPE)
+                                : (navBarCanMove
+                                                                       ? 0
+                                                                       : getDimenByName(systemRes, NAVBAR_HEIGHT))));
+               // &&}}
         Insets newNavInsets = Insets.of(navInsets.left, navInsets.top, navInsets.right, bottomNav);
         insetsBuilder.setInsets(WindowInsets.Type.navigationBars(), newNavInsets);
         insetsBuilder.setInsetsIgnoringVisibility(WindowInsets.Type.navigationBars(), newNavInsets);
@@ -242,11 +256,22 @@ public class WindowManagerProxy implements ResourceBasedOverride {
                         ? 0 : systemRes.getDimensionPixelSize(R.dimen.taskbar_size))
                 : getDimenByName(systemRes, NAVBAR_HEIGHT);
 
+               // Solve the overlap problem between Hostset and NavigationBar by qty {{&&
+               /*
         navBarHeightLandscape = isTablet
                 ? (mTaskbarDrawnInProcess
                         ? 0 : systemRes.getDimensionPixelSize(R.dimen.taskbar_size))
                 : (isTabletOrGesture
                         ? getDimenByName(systemRes, NAVBAR_HEIGHT_LANDSCAPE) : 0);
+               */
+               boolean navBarCanMove = ResourceUtils.getBoolByName("config_navBarCanMove", systemRes, true);
+               navBarHeightLandscape = isTablet
+                ? (mTaskbarDrawnInProcess
+                        ? 0 : systemRes.getDimensionPixelSize(R.dimen.taskbar_size))
+                : (isTabletOrGesture
+                        ? getDimenByName(systemRes, NAVBAR_HEIGHT_LANDSCAPE) : (navBarCanMove
+                                                       ? 0 : getDimenByName(systemRes, NAVBAR_HEIGHT)));
+               // &&}}
         navbarWidthLandscape = isTabletOrGesture
                 ? 0
                 : getDimenByName(systemRes, NAVBAR_LANDSCAPE_LEFT_RIGHT_SIZE);
@@ -275,6 +300,8 @@ public class WindowManagerProxy implements ResourceBasedOverride {
             insets.top = Math.max(insets.top, statusBarHeight);
             insets.bottom = Math.max(insets.bottom, navBarHeight);
 
+                       // Solve the overlap problem between Hostset and NavigationBar by qty {{&&
+                       /*
             if (i == Surface.ROTATION_270 || i == Surface.ROTATION_180) {
                 // On reverse landscape (and in rare-case when the natural orientation of the
                 // device is landscape), navigation bar is on the right.
@@ -282,6 +309,17 @@ public class WindowManagerProxy implements ResourceBasedOverride {
             } else {
                 insets.right = Math.max(insets.right, navbarWidth);
             }
+                       */
+                       if (navBarCanMove) {
+                               if (i == Surface.ROTATION_270 || i == Surface.ROTATION_180) {
+                                       // On reverse landscape (and in rare-case when the natural orientation of the
+                                       // device is landscape), navigation bar is on the right.
+                                       insets.left = Math.max(insets.left, navbarWidth);
+                               } else {
+                                       insets.right = Math.max(insets.right, navbarWidth);
+                               }
+                       }
+                       // &&}}
             result[i] = new WindowBounds(bounds, insets, i);
         }
         return result;
(END)
```

> 注意：如果默认允许桌面旋转，可能会导致最近任务栏显示异常。这是因为 `RecentsOrientedState.java` 类的 `updateHomeRotationSetting()` 会读取允许桌面旋转的开关值，该值默认是 false：
>
> ```java
> private void updateHomeRotationSetting() {
>     boolean homeRotationEnabled = mSharedPrefs.getBoolean(ALLOW_ROTATION_PREFERENCE_KEY, false);
>     setFlag(FLAG_HOME_ROTATION_ALLOWED_IN_PREFS, homeRotationEnabled);
>     SystemUiProxy.INSTANCE.get(mContext).setHomeRotationEnabled(homeRotationEnabled);
> }
> ```
>
> 可以通过将其改成 true 来解决。