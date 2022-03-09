[toc]

### 1. 绘制矩形

```java
import android.content.Context;

import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.nio.FloatBuffer;
import java.nio.ShortBuffer;

import javax.microedition.khronos.opengles.GL10;

public class SimpleTriangleRenderer extends AbstractRenderer {

    // Number of points or vertices we want to use
    private final static int VERTS = 4;

    // A raw native buffer to hold the point coordinates
    private FloatBuffer mFVertexBuffer;

    // A raw native buffer to hold indices
    // allowing a reuse of points.
    private ShortBuffer mIndexBuffer;

    public SimpleTriangleRenderer(Context context) {
        ByteBuffer vbb = ByteBuffer.allocateDirect(VERTS * 3 * 4);
        vbb.order(ByteOrder.nativeOrder());
        mFVertexBuffer = vbb.asFloatBuffer();

        ByteBuffer ibb = ByteBuffer.allocateDirect(6 * 2);
        ibb.order(ByteOrder.nativeOrder());
        mIndexBuffer = ibb.asShortBuffer();

        float[] coords = {
                -0.5f, -0.5f, 0,    // (x1, y1, z1)
                0.5f, -0.5f, 0,
                0.5f, 0.5f, 0,
                -0.5f, 0.5f, 0
        };
        for (int i = 0; i < VERTS; i++) {
            for (int j = 0; j < 3; j++) {
                mFVertexBuffer.put(coords[i * 3 + j]);
            }
        }
        short[] myIndecesArray = { 0, 1, 2, 0, 2, 3};
        for (int i = 0; i < 6; i++) {
            mIndexBuffer.put(myIndecesArray[i]);
        }
        mFVertexBuffer.position(0);
        mIndexBuffer.position(0);
    }

    @Override
    protected void draw(GL10 gl) {
        gl.glColor4f(1.0f, 0, 0, 0.5f);
        gl.glVertexPointer(3, GL10.GL_FLOAT, 0, mFVertexBuffer);
        gl.glDrawElements(GL10.GL_TRIANGLES, 6, GL10.GL_UNSIGNED_SHORT, mIndexBuffer);
    }
}
```

在 Activity 中显示矩形：

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

### 2. 使用形状

下面以绘制正多边形为例：

#### 2.1  定义形状接口

**Shape.java**

```java
import java.nio.FloatBuffer;
import java.nio.ShortBuffer;

public interface Shape {
    FloatBuffer getVertexBuffer();
    ShortBuffer getIndexBuffer();
    int getNumberofIndices();
}
```

#### 2.2 实现 RegularPolygon 形状

我们使用正多边形的边数和中心到顶点的距离来定义它。我们将此距离称为半径，因为正多边形的顶点都在一个与它具有相同中心的圆周上。所以，这个圆的半径和边数可以表示我们所需的多边形。

**RegularPolygon.java**

```java
import android.util.Log;

import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.nio.FloatBuffer;
import java.nio.ShortBuffer;

public class RegularPolygon implements Shape {

    // Space to hold (x, y, z) of the center: cx, cy, cz
    // and the radius "r"
    private float cx, cy, cz, r;

    private int sides;

    // coordinate array: (x, y) vertex points
    private float[] xarray = null;
    private float[] yarray = null;

    // texture array: (x, y) also called (s, t) points
    // where the figure is going to be mapped to a texture bitmap
    private float[] sarray = null;
    private float[] tarray = null;

    //****************************************
    // Constructor
    //****************************************
    public RegularPolygon(float incx, float incy, float incz /* (x, y, z) center */,
                            float inr /* radius */,
                            int insides /* number of sides */) {
        cx = incx;
        cy = incy;
        cz = incz;
        r = inr;
        sides = insides;

        // allocate memory for the arrays
        xarray = new float[sides];
        yarray = new float[sides];

        // allocate memory for texture point arrays
        sarray = new float[sides];
        tarray = new float[sides];

        // calculate vertex points
        calcArrays();

        // calculate texture points
        calcTextureArrays();
    }

    //******************************************************************
    // Get and convert the vertex coordinates
    // based on origin and radius.
    // Real logic of angles happen inside getMultiplierArray() functions
    //******************************************************************
    private void calcArrays() {
        // Get the vertex points assuming a circle
        // with a radius of "1" and located at "origin" zero
        float[] xmarray = getXMultiplierArray();
        float[] ymarray = getYMultiplierArray();

        // calc xarray: get the vertex
        // by adding the "x" portion of the origin
        // multiply the coordinate with radius (scale)
        for (int i = 0; i < sides; i++) {
            float curm = xmarray[i];
            float xcoord = cx + r * curm;
            xarray[i] = xcoord;
        }
        printArray(xarray, "xarray");

        // calc yarray: do the same for y coordinates
        for (int i = 0; i < sides; i++) {
            float curm = ymarray[i];
            float ycoord = cy + r * curm;
            yarray[i] = ycoord;
        }
        printArray(yarray, "yarray");
    }

    //*********************************************************
    // Calculate texture arrays
    // See Texture subsection for more discussion on this
    // very similay approach.
    // Here the polygon has to map into a space
    // that is a square
    //*********************************************************
    private void calcTextureArrays() {
        float[] xmarray = getXMultiplierArray();
        float[] ymarray = getYMultiplierArray();

        // calc xarray
        for (int i = 0; i < sides; i++) {
            float curm = xmarray[i];
            float xcoord = 0.5f + 0.5f * curm;
            sarray[i] = xcoord;
        }
        printArray(sarray, "sarray");

        // calc yarray
        for (int i = 0; i < sides; i++) {
            float curm = ymarray[i];
            float ycoord = 0.5f + 0.5f * curm;
            tarray[i] = ycoord;
        }
        printArray(tarray, "tarray");
    }

    //***************************************************
    // Covert the java array of vertices
    // into an nio float buffer
    //***************************************************
    @Override
    public FloatBuffer getVertexBuffer() {
        int vertices = sides + 1;
        int coordinates = 3;
        int floatsize = 4;
        int spacePerVertex = coordinates * floatsize;

        ByteBuffer vbb = ByteBuffer.allocateDirect(spacePerVertex * vertices);
        vbb.order(ByteOrder.nativeOrder());
        FloatBuffer mFVertexBuffer = vbb.asFloatBuffer();

        // Put the first coordinate (x, y, z: 0, 0, 0)
        mFVertexBuffer.put(cx); // x
        mFVertexBuffer.put(cy); // y
        mFVertexBuffer.put(0.0f);   // z

        int totalPuts = 3;
        for (int i = 0; i < sides; i++) {
            mFVertexBuffer.put(xarray[i]);  // x
            mFVertexBuffer.put(yarray[i]);  // y
            mFVertexBuffer.put(0.0f);   // z
            totalPuts += 3;
        }
        Log.d("total puts:", Integer.toString(totalPuts));
        return mFVertexBuffer;
    }

    //****************************************************
    // Convert texture buffer to an nio buffer
    //****************************************************
    public FloatBuffer getTextureBuffer() {
        int vertices = sides + 1;
        int coordinates = 2;
        int floatsize = 4;
        int spacePerVertex = coordinates * floatsize;

        ByteBuffer vbb = ByteBuffer.allocateDirect(spacePerVertex * vertices);
        vbb.order(ByteOrder.nativeOrder());
        FloatBuffer mFTextureBuffer = vbb.asFloatBuffer();

        // Put the first coordinate (x, y (s, t): 0, 0)
        mFTextureBuffer.put(0.5f);  // x or s
        mFTextureBuffer.put(0.5f);  // y or t

        int totalPuts = 2;
        for (int i = 0; i < sides; i++) {
            mFTextureBuffer.put(sarray[i]); // x
            mFTextureBuffer.put(tarray[i]); // y
            totalPuts += 2;
        }
        Log.d("total texture puts:", Integer.toString(totalPuts));
        return mFTextureBuffer;
    }

    //*****************************************************
    // Calculate indices forming multiple triangles.
    // Start with the center vertex which is at 0
    // The count them in a clockwise direction such as
    // 0, 1, 2,  0, 2, 3,  0, 3, 4 and so on.
    //*****************************************************
    @Override
    public ShortBuffer getIndexBuffer() {
        short[] iarray = new short[sides * 3];
        ByteBuffer ibb = ByteBuffer.allocateDirect(sides * 3 * 2);
        ibb.order(ByteOrder.nativeOrder());
        ShortBuffer mIndexBuffer = ibb.asShortBuffer();
        for (int i = 0; i < sides; i++) {
            short index1 = 0;
            short index2 = (short)(i + 1);
            short index3 = (short)(i + 2);
            if (index3 == sides + 1) {
                index3 = 1;
            }
            mIndexBuffer.put(index1);
            mIndexBuffer.put(index2);
            mIndexBuffer.put(index3);

            iarray[i * 3 + 0] = index1;
            iarray[i * 3 + 1] = index2;
            iarray[i * 3 + 2] = index3;
        }
        printShortArray(iarray, "index array");
        return mIndexBuffer;
    }

    //*******************************************************
    // This is where you take the angle array
    // for each vertex and calculate their projection multiplier
    // on the x axis
    //*******************************************************
    private float[] getXMultiplierArray() {
        float[] angleArray = getAngleArrays();
        float[] xmultiplierArray = new float[sides];
        for (int i = 0; i < angleArray.length; i++) {
            float curAngle = angleArray[i];
            float sinvalue = (float) Math.cos(Math.toRadians(curAngle));
            float absSinValue = Math.abs(sinvalue);
            if (isXPositiveQuadrant(curAngle)) {
                sinvalue = absSinValue;
            } else {
                sinvalue = -absSinValue;
            }
            xmultiplierArray[i] = getApproxValue(sinvalue);
        }
        printArray(xmultiplierArray, "xmultiplierArray");
        return xmultiplierArray;
    }

    //************************************************************
    // This is where you take the angle array
    // for each vertex and calculate their rojection multiplier
    // on the y axis
    //************************************************************
    private float[] getYMultiplierArray() {
        float[] angleArray = getAngleArrays();
        float[] ymultiplierArray = new float[sides];
        for (int i = 0; i < angleArray.length; i++) {
            float curAngle = angleArray[i];
            float sinvalue = (float) Math.sin(Math.toRadians(curAngle));
            float absSinValue = Math.abs(sinvalue);
            if (isYPositiveQuadrant(curAngle)) {
                sinvalue = absSinValue;
            } else {
                sinvalue = -absSinValue;
            }
            ymultiplierArray[i] = getApproxValue(sinvalue);
        }
        printArray(ymultiplierArray, "ymultiplierArray");
        return ymultiplierArray;
    }

    //******************************************************
    // This function may not be needed
    // Test it yourself and discard it if you dont need
    //******************************************************
    private boolean isXPositiveQuadrant(float angle) {
        if ((0 <= angle) && (angle <= 90)) {
            return true;
        }
        if ((angle < 0) && (angle >= -90)) {
            return true;
        }
        return false;
    }

    //*******************************************************
    // This function may not be needed
    // Test it yourself and discard it if you dont need
    //*******************************************************
    private boolean isYPositiveQuadrant(float angle) {
        if ((0 <= angle) && (angle <= 90)) {
            return true;
        }
        if ((angle < 180) && (angle >= 90)) {
            return true;
        }
        return false;
    }

    //*******************************************************
    // This is where you calculate angles
    // for each line going from center to each vertex
    //*******************************************************
    private float[] getAngleArrays() {
        float[] angleArray = new float[sides];
        float commonAngle = 360.0f/sides;
        float halfAngle = commonAngle / 2.0f;
        float firstAngle = 360.0f - (90 + halfAngle);
        angleArray[0] = firstAngle;

        float curAngle = firstAngle;
        for (int i = 1; i < sides; i++) {
            float newAngle = curAngle - commonAngle;
            angleArray[i] = newAngle;
            curAngle = newAngle;
        }
        printArray(angleArray, "angleArray");
        return angleArray;
    }

    //********************************************************
    // Some rounding if needed
    //********************************************************
    private float getApproxValue(float f) {
        return (Math.abs(f) < 0.001) ? 0 : f;
    }

    //*******************************************************
    // Return how many Indices you will need
    // given the number of sides
    // This is the count of number of triangles needed
    // to make the polygon multiplied by 3
    // It just happens that the number of triangles is
    // same as the number of sides
    //******************************************************
    @Override
    public int getNumberofIndices() {
        return sides * 3;
    }

    public static void test() {
        RegularPolygon triangle = new RegularPolygon(0, 0, 0, 1, 3);
    }

    private void printArray(float array[], String tag) {
        StringBuilder sb = new StringBuilder(tag);
        for (int i = 0; i < array.length; i++) {
            sb.append(";").append(array[i]);
        }
        Log.d("hh", sb.toString());
    }

    private void printShortArray(short array[], String tag) {
        StringBuilder sb = new StringBuilder(tag);
        for (int i = 0; i < array.length; i++) {
            sb.append(";").append(array[i]);
        }
        Log.d(tag, sb.toString());
    }
}
```

#### 2.3 使用 RegularPolygon 呈现正方形

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

**SquareRenderer.java**

```java
package com.android.androidtest;

import android.content.Context;

import java.nio.FloatBuffer;
import java.nio.ShortBuffer;

import javax.microedition.khronos.opengles.GL10;

public class SquareRenderer extends AbstractRenderer {

    // A raw native buffer to hold the point coordinates
    private FloatBuffer mFVertexBuffer;

    // A raw native buffer to hold indices
    // allowing a reuse of points.
    private ShortBuffer mIndexBuffer;

    private int numOfIndices = 0;

    private int sides = 4;

    public SquareRenderer(Context context) {
        prepareBuffers(sides);
    }

    private void prepareBuffers(int sides) {
        RegularPolygon t = new RegularPolygon(0, 0, 0, 0.5f, sides);
        // RegularPolygon t = new RegularPolygon(1, 1, 0, 1, sides);
        mFVertexBuffer = t.getVertexBuffer();
        mIndexBuffer = t.getIndexBuffer();
        numOfIndices = t.getNumberofIndices();
        mFVertexBuffer.position(0);
        mIndexBuffer.position(0);
    }

    // overriden method
    @Override
    protected void draw(GL10 gl) {
        prepareBuffers(sides);
        gl.glVertexPointer(3, GL10.GL_FLOAT, 0, mFVertexBuffer);
        gl.glDrawElements(GL10.GL_TRIANGLES, numOfIndices, GL10.GL_UNSIGNED_SHORT, mIndexBuffer);
    }
}
```

#### 2.4 在 Activity 中显示形状

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
        mTestHarness.setRenderer(new SquareRenderer(this));
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

