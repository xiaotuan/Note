[toc]

### 1. 使用 GLSurfaceView 和相关类

下面给出了通常使用这些类进行绘制的步骤：

（1）实现 Renderer 接口。

（2）在呈现器的实现中提供绘图所必须的 Camera 设置。

（3）在实现的 onDrawFrame 方法中提供绘图代码。

（4）构造 GLSurfaceView。

（5）设置第 1 步 ~ 第 3 步在 GLSurfaceView 中实现的呈现器。

（6）指定是否需要将 GLSurfaceView 绘制成动画。

（7）在 Activity 中将 GLSurfaceView 设置

### 2. 实现 Renderer 接口

#### 2.1 Renderer 接口的签名

```java
public interface Renderer {
    void onSurfaceCreated(GL10 gl, EGLConfig config);
    void onSurfaceChanged(GL10 gl, int width, int height);
    void onDrawFrame(GL10 gl);
}
```

主要的绘制过程在 `onDrawFrame()` 方法中进行。只要为此视图创建了一个新表面，就会调用 `onSurfaceCreated()` 方法。档表面变化时，比如窗口的宽度和高度变化时，将调用 `onSurfaceChanged()` 方法。

#### 2.2 Renderer 接口的抽象实现

下面是一个 Renderer 的抽象类，有了它我们就可以将注意力集中在绘图方法上。

```java
import android.opengl.GLSurfaceView;
import android.opengl.GLU;

import javax.microedition.khronos.egl.EGLConfig;
import javax.microedition.khronos.opengles.GL10;

public abstract class AbstractRenderer implements GLSurfaceView.Renderer {

    @Override
    public void onSurfaceCreated(GL10 gl, EGLConfig config) {
        gl.glDisable(GL10.GL_DITHER);
        gl.glHint(GL10.GL_PERSPECTIVE_CORRECTION_HINT, GL10.GL_FASTEST);
        gl.glClearColor(.5f, .5f, .5f, 1);
        gl.glShadeModel(GL10.GL_SMOOTH);
        gl.glEnable(GL10.GL_DEPTH_TEST);
    }

    @Override
    public void onSurfaceChanged(GL10 gl, int width, int height) {
        gl.glViewport(0, 0, width, height);
        float ratio = (float) width / height;
        gl.glMatrixMode(GL10.GL_PROJECTION);
        gl.glLoadIdentity();
        gl.glFrustumf(-ratio, ratio, -1, 1, 3, 7);
    }

    @Override
    public void onDrawFrame(GL10 gl) {
        gl.glDisable(GL10.GL_DITHER);
        gl.glClear(GL10.GL_COLOR_BUFFER_BIT | GL10.GL_DEPTH_BUFFER_BIT);
        gl.glMatrixMode(GL10.GL_MODELVIEW);
        gl.glLoadIdentity();
        GLU.gluLookAt(gl, 0, 0, -5, 0f, 0f, 0f, 0f, 1.0f, 0.0f);
        gl.glEnableClientState(GL10.GL_VERTEX_ARRAY);
        draw(gl);
    }

    protected abstract void draw(GL10 gl);
}
```

#### 2.3 Renderer 的简单实现

```java
import android.content.Context;

import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.nio.FloatBuffer;
import java.nio.ShortBuffer;

import javax.microedition.khronos.opengles.GL10;

public class SimpleTriangleRenderer extends AbstractRenderer {

    // Number of points or vertices we want to use
    private final static int VERTS = 3;

    // A raw native buffer to hold the point coordinates
    private FloatBuffer mFVertexBuffer;

    // A raw native buffer to hold indices
    // allowing a reuse of points.
    private ShortBuffer mIndexBuffer;

    public SimpleTriangleRenderer(Context context) {
        ByteBuffer vbb = ByteBuffer.allocateDirect(VERTS * 3 * 4);
        vbb.order(ByteOrder.nativeOrder());
        mFVertexBuffer = vbb.asFloatBuffer();

        ByteBuffer ibb = ByteBuffer.allocateDirect(VERTS * 2);
        ibb.order(ByteOrder.nativeOrder());
        mIndexBuffer = ibb.asShortBuffer();

        float[] coords = {
                -0.5f, -0.5f, 0,    // (x1, y1, z1)
                0.5f, 0.5f, 0,
                0.0f, 0.5f, 0
        };
        for (int i = 0; i < VERTS; i++) {
            for (int j = 0; j < 3; j++) {
                mFVertexBuffer.put(coords[i * 3 + j]);
            }
        }
        short[] myIndecesArray = { 0, 1, 2 };
        for (int i = 0; i < 3; i++) {
            mIndexBuffer.put(myIndecesArray[i]);
        }
        mFVertexBuffer.position(0);
        mIndexBuffer.position(0);
    }

    @Override
    protected void draw(GL10 gl) {
        gl.glColor4f(1.0f, 0, 0, 0.5f);
        gl.glVertexPointer(3, GL10.GL_FLOAT, 0, mFVertexBuffer);
        gl.glDrawElements(GL10.GL_TRIANGLES, VERTS, GL10.GL_UNSIGNED_SHORT, mIndexBuffer);
    }
}
```

### 3. 通过 Activity 使用 GLSurfaceView

```java
import android.opengl.GLSurfaceView;
import android.os.Bundle;
import android.util.Log;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "qty";

    private GLSurfaceView mTestHarness;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Log.v(TAG, "in onCreate");
        // 实例化 GLSurfaceView 
        mTestHarness = new GLSurfaceView(this);
        // 告诉视图，无需特殊的 EGL 配置选择程序，采用默认配置即可
        mTestHarness.setEGLConfigChooser(false);
        // 设置呈现器
        mTestHarness.setRenderer(new SimpleTriangleRenderer(this));
       // 在需要绘制时调用
        mTestHarness.setRenderMode(GLSurfaceView.RENDERMODE_WHEN_DIRTY);
        // 绘图代码将被反复调用，以便为图形创造动画效果
        // mTestHarness.setRenderMode(GLSurfaceView.RENDERMODE_CONTINUOUSLY);
        setContentView(mTestHarness);
    }

    @Override
    protected void onResume() {
        super.onResume();
        mTestHarness.onResume();
    }

    @Override
    protected void onPause() {
        super.onPause();
        mTestHarness.onPause();
    }
}
```

### 4. 为简单的 OpenGL 三角形制作动画

实现原理是在 Renderer 接口中不断的改变图形的属性，在 GLSurfaceView 中将 GLSurfaceView.RENDERMODE_CONTINUOUSLY 传递给 `setRenderMode()` 方法。

#### 4.1 Renderer 接口的实现

```java
import android.content.Context;
import android.os.SystemClock;

import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.nio.FloatBuffer;
import java.nio.ShortBuffer;

import javax.microedition.khronos.opengles.GL10;

public class SimpleTriangleRenderer extends AbstractRenderer {

    // Number of points or vertices we want to use
    private final static int VERTS = 3;

    // A raw native buffer to hold the point coordinates
    private FloatBuffer mFVertexBuffer;

    // A raw native buffer to hold indices
    // allowing a reuse of points.
    private ShortBuffer mIndexBuffer;

    public SimpleTriangleRenderer(Context context) {
        ByteBuffer vbb = ByteBuffer.allocateDirect(VERTS * 3 * 4);
        vbb.order(ByteOrder.nativeOrder());
        mFVertexBuffer = vbb.asFloatBuffer();

        ByteBuffer ibb = ByteBuffer.allocateDirect(VERTS * 2);
        ibb.order(ByteOrder.nativeOrder());
        mIndexBuffer = ibb.asShortBuffer();

        float[] coords = {
                -0.5f, -0.5f, 0,    // (x1, y1, z1)
                0.5f, 0.5f, 0,
                0.0f, 0.5f, 0
        };
        for (int i = 0; i < VERTS; i++) {
            for (int j = 0; j < 3; j++) {
                mFVertexBuffer.put(coords[i * 3 + j]);
            }
        }
        short[] myIndecesArray = { 0, 1, 2 };
        for (int i = 0; i < 3; i++) {
            mIndexBuffer.put(myIndecesArray[i]);
        }
        mFVertexBuffer.position(0);
        mIndexBuffer.position(0);
    }

    @Override
    protected void draw(GL10 gl) {
        long time = SystemClock.uptimeMillis() % 4000L;
        float angle = 0.090f * ((int) time);
        gl.glRotatef(angle, 0, 0, 1.0f);
        gl.glColor4f(1.0f, 0, 0, 0.5f);
        gl.glVertexPointer(3, GL10.GL_FLOAT, 0, mFVertexBuffer);
        gl.glDrawElements(GL10.GL_TRIANGLES, VERTS, GL10.GL_UNSIGNED_SHORT, mIndexBuffer);
    }
}
```

#### 4.2 通过 Activity 使用 GLSurfaceView

```java
import android.opengl.GLSurfaceView;
import android.os.Bundle;
import android.util.Log;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "qty";

    private GLSurfaceView mTestHarness;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Log.v(TAG, "in onCreate");
        mTestHarness = new GLSurfaceView(this);
        mTestHarness.setEGLConfigChooser(false);
        mTestHarness.setRenderer(new SimpleTriangleRenderer(this));
        mTestHarness.setRenderMode(GLSurfaceView.RENDERMODE_CONTINUOUSLY);
        setContentView(mTestHarness);
    }

    @Override
    protected void onResume() {
        super.onResume();
        mTestHarness.onResume();
    }

    @Override
    protected void onPause() {
        super.onPause();
        mTestHarness.onPause();
    }
}
```

