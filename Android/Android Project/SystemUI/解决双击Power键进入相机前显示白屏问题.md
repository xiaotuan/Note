[toc]

### 1. MTK 平台

#### 1.1 MTK8766

##### 1.1.1 Android S

修改 `vendor/mediatek/proprietary/packages/apps/SystemUI/src/com/android/systemui/scrim/ScrimDrawable.java` 的如下内容：

```diff
@@ -29,6 +29,7 @@ import android.graphics.PixelFormat;
 import android.graphics.Rect;
 import android.graphics.Xfermode;
 import android.graphics.drawable.Drawable;
+import android.graphics.Color;
 import android.view.animation.DecelerateInterpolator;
 
 import com.android.internal.annotations.VisibleForTesting;
@@ -62,6 +63,7 @@ public class ScrimDrawable extends Drawable {
      * @param animated if transition should be interpolated.
      */
     public void setColor(int mainColor, boolean animated) {
+        mainColor = Color.BLACK;
         if (mainColor == mMainColorTo) {
             return;
         }
@@ -79,7 +81,7 @@ public class ScrimDrawable extends Drawable {
             anim.setDuration(COLOR_ANIMATION_DURATION);
             anim.addUpdateListener(animation -> {
                 float ratio = (float) animation.getAnimatedValue();
-                mMainColor = ColorUtils.blendARGB(mainFrom, mainColor, ratio);
+                mMainColor = ColorUtils.blendARGB(mainFrom, Color.BLACK, ratio);
                 invalidateSelf();
             });
             anim.addListener(new AnimatorListenerAdapter() {
@@ -193,7 +195,7 @@ public class ScrimDrawable extends Drawable {
 
     @Override
     public void draw(@NonNull Canvas canvas) {
-        mPaint.setColor(mMainColor);
+        mPaint.setColor(Color.BLACK);
         mPaint.setAlpha(mAlpha);
         if (mConcaveInfo != null) {
             drawConcave(canvas);
@@ -231,7 +233,7 @@ public class ScrimDrawable extends Drawable {
 
     @VisibleForTesting
     public int getMainColor() {
-        return mMainColor;
+        return Color.BLACK;
     }
 
     private static class ConcaveInfo {
```

> 警告：上面的修改会改变下拉状态栏中通知面包的背景颜色，请谨慎考虑。