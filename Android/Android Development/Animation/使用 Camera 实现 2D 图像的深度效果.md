[toc]

`Camera` 类可以将 3D 控件内移动的 2D 图像投影到 2D 表面，实现深度效果。下面是一个使用 `Camera` 类实现视图动画的示例代码：

**Kotlin 版本**

```kotlin
package com.ai.android.sampleviewanimation

import android.graphics.Camera
import android.util.Log
import android.view.animation.Animation
import android.view.animation.LinearInterpolator
import android.view.animation.Transformation

class ViewAnimation(
    private val centerX: Float,
    private val centerY: Float
): Animation() {

    private val cam = Camera()

    override fun initialize(width: Int, height: Int, parentWidth: Int, parentHeight: Int) {
        super.initialize(width, height, parentWidth, parentHeight)
        Log.d(TAG, "width: $width")
        Log.d(TAG, "height: $height")
        Log.d(TAG, "pwidth: $parentWidth")
        Log.d(TAG, "pheight: $parentHeight")
        duration = 2500
        fillAfter = true
        interpolator = LinearInterpolator()
    }

    override fun applyTransformation(interpolatedTime: Float, t: Transformation?) {
        applyTransformationNew(interpolatedTime, t)
    }

    private fun applyTransformationNew(interpolatedTime: Float, t: Transformation?) {
        Log.d(TAG, "transform: $interpolatedTime")
        t?.apply {
            matrix?.apply {
                cam.save()
                cam.translate(0.0f, 0.0f, (1300 - 1300.0f * interpolatedTime))
                cam.rotateY(360 * interpolatedTime)
                cam.getMatrix(this)

                preTranslate(-centerX, -centerY)
                postTranslate(centerX, centerY)
                cam.restore()
            }
        }
    }

    companion object {
        const val TAG = "ViewAnimation"
    }
}
```

**Java 版本**

```java
package com.ai.android.ExerciseSystemIntents;

import android.graphics.Camera;
import android.graphics.Matrix;
import android.util.Log;
import android.view.animation.Animation;
import android.view.animation.LinearInterpolator;
import android.view.animation.Transformation;

public class ViewAnimation extends Animation {

    private static final String TAG = ViewAnimation.class.getSimpleName();

    private float centerX;
    private float centerY;
    private Camera cam;

    public ViewAnimation(float cx, float cy) {
        cam = new Camera();
        centerX = cx;
        centerY = cy;
    }

    @Override
    public void initialize(int width, int height, int parentWidth, int parentHeight) {
        super.initialize(width, height, parentWidth, parentHeight);
        Log.d(TAG, "width: " + width);
        Log.d(TAG, "height: " + height);
        Log.d(TAG, "pwidth: " + parentWidth);
        Log.d(TAG, "pheight: " + parentHeight);
        setDuration(2500);
        setFillAfter(true);
        setInterpolator(new LinearInterpolator());
    }

    @Override
    protected void applyTransformation(float interpolatedTime, Transformation t) {
        applyTransformationNew(interpolatedTime, t);
    }

    protected void applyTransformationNew(float interpolatedTime, Transformation t) {
        Log.d(TAG, "transform: " + interpolatedTime);
        final Matrix matrix = t.getMatrix();
        cam.save();
        cam.translate(0.0f, 0.0f, (1300 - 1300.0f * interpolatedTime));
        cam.rotateY(360 * interpolatedTime);
        cam.getMatrix(matrix);

        matrix.preTranslate(-centerX, -centerY);
        matrix.postTranslate(centerX, centerY);
        cam.restore();
    }
}
```

> 提示：
>
> 可以使用 `Camera` 对象实现很多有趣的动画，这个可以自己试验。如果希望创建 3D 效果的动画，可以在使用 `Camera`对象时，设置其 `Z` 轴的值。