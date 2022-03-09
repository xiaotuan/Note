[toc]

### 1. 纹理

OpenGL 纹理是一种位图，可以将它粘贴到 OpenGL 中的表面上。例如，可以获取一张邮票的图像并粘贴到正方形中，使正方形看起来像一张邮票。或者可以获取一块砖头的位图并粘贴到矩形中，重复此操作多次，使矩形看起来像一面砖墙。

将纹理位图附加到 OpenGL 表面的过程类似于将墙纸粘贴到规则或不规则形状物体的表面上。表面的形状无关紧要，只要选择的墙纸足以覆盖住表面即可。

但是，要使墙纸保持合适的方向，以便图形井然有序地排列，则必须获得形状的每个顶点并在墙纸上标记出来，以便墙纸和对象的形状保持一致。如果形状比较独特且包含大量顶点，那么也需要在墙纸上标记出每个顶点。

### 2. 标准化纹理坐标

一个还未解决或明确说明的细节是物体和墙纸有多大。OpenGL 使用一种标准化方法来解决此问题。OpenGL 假设墙纸始终为 1 x 1 的正方形，其原点位于（0, 0）处，右上角的坐标为（1, 1）。然后 OpenGL 希望你缩小物体表面，使它位于这些 1 x 1 边界内。那么，程序员的任务是在 1 x 1 的正方形中计算出物体表面的顶点。

### 3. 抽象场景纹理处理操作

因为加载纹理的过程是通用的，所以我们抽象出了此过程，创建了派生自 AbstractRenderer 的抽象类 SingleAbstractTextureRenderer。

**AbstractRenderer.java**

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

**AbstractSingleTexturedRenderer.java**

```java
package com.android.androidtest;

import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.opengl.GLU;
import android.opengl.GLUtils;

import java.io.IOException;
import java.io.InputStream;

import javax.microedition.khronos.egl.EGLConfig;
import javax.microedition.khronos.opengles.GL10;

public abstract class AbstractSingleTexturedRenderer extends AbstractRenderer {

    private int mTextureId;
    private int mImageResourceId;
    private Context mContext;

    public AbstractSingleTexturedRenderer(Context ctx, int imageResourceId) {
        mImageResourceId = imageResourceId;
        mContext = ctx;
    }

    @Override
    public void onSurfaceCreated(GL10 gl, EGLConfig config) {
        super.onSurfaceCreated(gl, config);
        gl.glEnable(GL10.GL_TEXTURE_2D);
        prepareTexture(gl);
    }

    @Override
    public void onDrawFrame(GL10 gl) {
        gl.glDisable(GL10.GL_DITHER);
        gl.glTexEnvf(GL10.GL_TEXTURE_ENV, GL10.GL_TEXTURE_ENV_MODE, GL10.GL_MODULATE);

        gl.glClear(GL10.GL_COLOR_BUFFER_BIT | GL10.GL_DEPTH_BUFFER_BIT);
        gl.glMatrixMode(GL10.GL_MODELVIEW);
        gl.glLoadIdentity();
        GLU.gluLookAt(gl, 0, 0, -5, 0f, 0f, 0f, 0f, 1.0f, 0.0f);

        gl.glEnableClientState(GL10.GL_VERTEX_ARRAY);
        gl.glEnableClientState(GL10.GL_TEXTURE_COORD_ARRAY);

        gl.glActiveTexture(GL10.GL_TEXTURE0);
        gl.glBindTexture(GL10.GL_TEXTURE_2D, mTextureId);
        gl.glTexParameterf(GL10.GL_TEXTURE_2D, GL10.GL_TEXTURE_WRAP_S, GL10.GL_REPEAT);
        gl.glTexParameterf(GL10.GL_TEXTURE_2D, GL10.GL_TEXTURE_WRAP_T, GL10.GL_REPLACE);

        draw(gl);
    }

    private void prepareTexture(GL10 gl) {
        int[] textures = new int[1];
        gl.glGenTextures(1, textures, 0);

        mTextureId = textures[0];
        gl.glBindTexture(GL10.GL_TEXTURE_2D, mTextureId);

        gl.glTexParameterf(GL10.GL_TEXTURE_2D, GL10.GL_TEXTURE_MIN_FILTER, GL10.GL_NEAREST);
        gl.glTexParameterf(GL10.GL_TEXTURE_2D, GL10.GL_TEXTURE_MAG_FILTER, GL10.GL_LINEAR);

        gl.glTexParameterf(GL10.GL_TEXTURE_2D, GL10.GL_TEXTURE_WRAP_S, GL10.GL_CLAMP_TO_EDGE);
        gl.glTexParameterf(GL10.GL_TEXTURE_2D, GL10.GL_TEXTURE_WRAP_T, GL10.GL_CLAMP_TO_EDGE);

        gl.glTexEnvf(GL10.GL_TEXTURE_ENV, GL10.GL_TEXTURE_ENV_MODE, GL10.GL_REPLACE);

        InputStream is = mContext.getResources().openRawResource(mImageResourceId);
        Bitmap bitmap;
        try {
            bitmap = BitmapFactory.decodeStream(is);
        } finally {
            try {
                is.close();
            } catch (IOException ignore) {}
        }
        GLUtils.texImage2D(GL10.GL_TEXTURE_2D, 0, bitmap, 0);
        bitmap.recycle();
    }
}
```

在上面的代码中，需要以下 API 来解决纹理问题：

+ glGenTextures：此 OpenGL 方法负责为纹理生成唯一 ID，使这些纹理可在以后引用。通过 GLUtils.texImage2D 加载了纹理位图之后，将该纹理绑定到特定的 ID。在将纹理绑定到 glGenTextures 生成的 ID 之前，这个 ID 只是 ID，没有其他用途。OpenGL 文献将这些整数 ID 用作纹理名称。
+ glBindTexture：使用此 OpenGL 方法将当前加载的纹理绑定到从 glGenTextures 获得的纹理 ID。
+ glTexParameter：在应用纹理时，有许多可选参数可以设置。此 API 可用于定义这些选项。一些例子包括 GL_REPEAT、GL_CLAMP 等。例如，如果对象较大，可以使用 GL_REPEAT 多次重复粘贴位图。可以从以下 URL 获得更加完整的参数列表：<www.khronos.org/opengles/documentation/opengles1_0/html/glTexParameter.html>。
+ glTexEnv：其他一些与纹理相关的选项可通过 glTexEnv 方法指定。
+ GLUtils.texImage2D：这是一个 Android API，可用于加载位图以用作纹理。在内部，这个 API 会调用 OpenGL 的 glTexImage2D。
+ glActiveTexture：此 API 将给定的纹理 ID 设置为活动结构。
+ glTexCoordpointer：此 OpenGL 方法用于指定纹理坐标。每个坐标必须与在 glVertexPointer 中指定的坐标相匹配。

### 4. 使用纹理绘制

```java
import android.content.Context;

import java.nio.FloatBuffer;
import java.nio.ShortBuffer;

import javax.microedition.khronos.opengles.GL10;

public class TexturedSquareRenderer extends AbstractSingleTexturedRenderer {

    // Number of points or vertices we want to use
    private final static int VERTS = 4;

    // A raw native buffer to hold the point coordinates
    private FloatBuffer mFVertexBuffer;

    // A raw native buffer to hold the point coordinates
    private FloatBuffer mFTextureBuffer;

    // A raw native buffer to hold indices
    // allowing a reuse of points.
    private ShortBuffer mIndexBuffer;

    private int numOfIndices = 0;

    private int sides = 4;

    public TexturedSquareRenderer(Context context) {
        super(context, R.drawable.robot);
        prepareBuffers(sides);
    }

    private void prepareBuffers(int sides) {
        RegularPolygon t = new RegularPolygon(0, 0, 0, 0.5f, sides);
        mFVertexBuffer = t.getVertexBuffer();
        mFTextureBuffer = t.getTextureBuffer();
        mIndexBuffer = t.getIndexBuffer();
        numOfIndices = t.getNumberofIndices();
        mFVertexBuffer.position(0);
        mIndexBuffer.position(0);
        mFTextureBuffer.position(0);
    }

    // overriden method
    @Override
    protected void draw(GL10 gl) {
        prepareBuffers(sides);
        gl.glEnable(GL10.GL_TEXTURE_2D);
        gl.glVertexPointer(3, GL10.GL_FLOAT, 0, mFVertexBuffer);
        gl.glTexCoordPointer(2, GL10.GL_FLOAT, 0, mFTextureBuffer);
        gl.glDrawElements(GL10.GL_TRIANGLES, numOfIndices, GL10.GL_UNSIGNED_SHORT, mIndexBuffer);
    }
}
```

### 5. 在 Activity 显示

```java
package com.android.androidtest;

import android.content.res.Configuration;
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
        mTestHarness.setRenderer(new TexturedSquareRenderer(this));
        mTestHarness.setRenderMode(GLSurfaceView.RENDERMODE_WHEN_DIRTY);
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

