可以通过 `VelocityTracker` 类来获取手指在屏幕上的移动速度。

要使用 `VelocityTracker`，首先调用静态方法 `VelocityTracker.obtain()` 来创建一个 `VelocityTracker` 实例，然后可以使用 `addMovement(MotionEvent ev)` 方法向实例中添加 `MotionEvent` 对象。

两个 `VelocityTracker` 方法 `getXVelocity()` 和 `getYVelocity()` 分别返回手指在 X 和 Y 方向上的对应速度。从这两个方法返回的值将表示每个时间单位内移动的像素数。这可以是每毫秒像素数或每秒像素数，或者你希望使用的任何单位。要告诉 `VelocityTracker` 使用何种时间单位，需要在调用这个两个方法之前调用 `VelocityTracker` 的 `computeCurrentVelocity(int units)` 方法。units 的值表示用于测量速度的时间单位包含多少毫秒。如果移动方向是朝右（X）或朝下（Y），`getXVelocity()` 和 `getYVelocity()` 方法返回的值将为正数。如果移动方向是朝左（X）或朝上（Y），返回的值将为负数。

处理完通过 `obtain()` 方法获取的 `VelocityTracker` 对象时，可调用 `VelocityTracker` 对象的 `recycle()` 方法。

例如：

**Kotlin**

```kotlin
import android.content.Context
import android.util.AttributeSet
import android.util.Log
import android.view.MotionEvent
import android.view.VelocityTracker
import android.view.View

class MyView : View {

    private var vTracker: VelocityTracker? = null

    constructor(context: Context) : super(context) {
        init(null, 0)
    }

    constructor(context: Context, attrs: AttributeSet) : super(context, attrs) {
        init(attrs, 0)
    }

    constructor(context: Context, attrs: AttributeSet, defStyle: Int) : super(
        context,
        attrs,
        defStyle
    ) {
        init(attrs, defStyle)
    }

    private fun init(attrs: AttributeSet?, defStyle: Int) {
    }

    override fun onTouchEvent(event: MotionEvent?): Boolean {
        event?.apply {
            when (action) {
                MotionEvent.ACTION_DOWN -> {
                    if (vTracker == null) {
                        vTracker = VelocityTracker.obtain();
                    } else {
                    	vTracker?.clear()
                    }
                    vTracker?.addMovement(event)
                }
                MotionEvent.ACTION_MOVE -> {
                    vTracker?.addMovement(event)
                    vTracker?.computeCurrentVelocity(1000)
                    for (i in 0 until pointerCount) {
                        Log.v(TAG, "onTouchEvent=>i: $i, id: ${getPointerId(i)}, " +
                                "x velocity: ${vTracker?.getXVelocity(i)}, " +
                                "y velocity: ${vTracker?.getYVelocity(i)}")
                    }
                }
                MotionEvent.ACTION_UP -> {
                    vTracker?.clear()
                }
            }
        }
        return true
    }

    override fun onDetachedFromWindow() {
        vTracker?.recycle()
        vTracker = null
        super.onDetachedFromWindow()
    }

    companion object {
        const val TAG = "MyView"
    }
}
```

**Java**

```java
import android.content.Context;
import android.os.Build;
import android.util.AttributeSet;
import android.util.Log;
import android.view.MotionEvent;
import android.view.VelocityTracker;
import android.view.View;

import androidx.annotation.Nullable;

public class MyView extends View {

    private static final String TAG = "MyView";

    private VelocityTracker vTracker;

    public MyView(Context context) {
        super(context);
    }

    public MyView(Context context, @Nullable AttributeSet attrs) {
        super(context, attrs);
    }

    public MyView(Context context, @Nullable AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
    }

    @Override
    public boolean onTouchEvent(MotionEvent event) {
        int pointId = -1;
        switch (event.getAction()) {
            case MotionEvent.ACTION_DOWN:
                if (vTracker == null) {
                    vTracker = VelocityTracker.obtain();
                } else {
                    vTracker.clear();
                }
                vTracker.addMovement(event);
            break;

            case MotionEvent.ACTION_MOVE:
                vTracker.addMovement(event);
                vTracker.computeCurrentVelocity(1000);
                for (int i = 0; i < event.getPointerCount(); i++) {
                    Log.v(TAG, "onTouchEvent=>i: " + i + ", id: " + event.getPointerId(i)
                            + ", x velocity: " + vTracker.getXVelocity(i)
                            + ", y velocity: " + vTracker.getYVelocity(i));
                }
                break;

            case MotionEvent.ACTION_UP:
                vTracker.clear();
                break;
        }
        return true;
    }

    @Override
    protected void onDetachedFromWindow() {
        vTracker.recycle();
        vTracker = null;
        super.onDetachedFromWindow();
    }
}
```

