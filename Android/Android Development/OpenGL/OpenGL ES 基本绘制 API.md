[toc]

在 OpenGL 中，在 3D 空间中进行绘制。首先指定一系列点，这些点也成为顶点。每个点都具有 3 个值，分别对应于 x、y 和 z 坐标。

然后将这些点连接起来形成一个形状。可以连接这些点来形成各种形状，在 OpenGL ES 中这些形状称为原始形状，它们包括点、线和三角形。请注意在 OpenGL 中，原始形状还包括矩形和多边形。

OpenGL ES 提供了两个主要方法来帮助绘制：

+ glVertexPointer
+ glDrawElements

使用 glVertexPointer 来指定一系列点或顶点，使用 glDrawElements 并采用前面介绍的一种原始形状来绘制它们。

### 1. glVertexPointer 和指定图形顶点

glVertexPointer 方法指定由要绘制的点组成的数组。每个点从 3 个维度指定，所以每个点将包含 3 个值： x、y 和 z。例如：

```java
float[] coords = {
    -0.5f, -0.5f, 0,	// p1: (x1, y1, z1)
    0.5f, -0.5f, 0,	// p2: (x1, y1, z1)
    0.0f, 0.5f, 0	// p3: (x1, y1, z1)
};
```

glVertexPointer 仅接受与语言无关的本地缓存区，而不是 Java 浮点数组。出于此原因，需要将基于 Java 的浮点数组转换为可接受的类似 C 的本地缓存区。

```java
java.nio.ByteBuffer vbb = java.nio.ByteBuffer.allocateDirect(3 * 3 * 4);
vbb.order(ByteOrder.nativeOrder());
java.nio.FloatBuffer mFVertexBuffer = vbb.asFloatBuffer();
```

将这些值收集到本地缓冲区之后，可以调用 glVertexPointer：

```java
glVertexPointer(
	// Are we using (x,y) or (x,y,z) in each point
    3,
    // each value is a float value in the buffer
    GL10.GL_FLOAT,
    // Between two points there is no space
    0,
    // pointer to the start of the buffer
    mFVertexBuffer
);
```

第一个参数告诉 OpenGL ES 一个点或顶点有几维。在本例中，我们指定 3 来表示 x、y 和 z。也可以指定 2 来仅表示 x 和 y。对于这种情况，z 轴值将为 0。

第二个参数表示坐标需要解释为浮点值。第三个参数名为 stride，表示将每个点分开的字节数。在本例中，它为 0，因为一个点紧挨着一个点。有时可以在缓冲区中每个点之后添加颜色特性。如果希望添加颜色特性，可以在顶点规范中使用 stride 跳过这些部分。最后一个参数是包含点的缓冲区的指针。

### 2. glDrawElements

通过 glVertexPointer 指定了一系列点之后，可以使用 glDrawElements 方法，依照 OpenGL ES 所支持的一种原始形状来绘制这些点。请注意，OpenGL 是一种状态机。它在以累积方式调用下一个方法时，会记住一个方法所设置的值。所以无需显示地将 glVertexPointer 设置的点传递给 glDrawElements。glDrawElements 将隐式地使用这些点。

```java
glDrawElements(
	// type of shape
    GL10.GL_TRIANGLE_STRIP,
    // Number of indices
    3,
    // How big each index is 
    GL10.GL_UNSIGNED_SHORT,
    // buffer containing the 3 indices
    mIndexBuffer
);
```

第一个参数表示要绘制的集合形状的类型：GL_TRIANGLE_STRIP 表示三角形条带。此参数的其他可能选项包括：仅绘制点（GL_POINTS）、线带（GL_LINE_STRIP）、仅绘制线（GL_LINES）、线环（GL_LINE_LOOP）、仅绘制三角形（GL_TRIANGLES）和三角扇形（GL_TRIANGLE_FAN）。

GL_LINE_STRIP 和 GL_TRIANGLE_STRIP 中的 STRIP 概念用于在使用旧点时添加新点。这样，可以避免为每个新对象指定所有点。例如，如果再一个数组中指定 4 个点，可以使用条带来绘制第一个三角形（1, 2, 3）和第二个三角形（2, 3, 4）。每个新点会添加一个新三角形。

GL_TRIANGLE_FAN 中的 FAN 概念适用于这样一种三角形：它们的第一个点用作所有后续三角形的起点。所以实际上绘制的是一个类似扇形或圆形的对象，其中第一个顶点位于中间。假设数组中有 6 个点：（1,2,3,4,5,6）。使用 FAN，将在（1,2,3）、（1,3,4）、（1,4,5）、（1,5,6）位置绘制三角形。每个新点会添加一个新三角形，类似于打开扇子或展开一些卡片的过程。

第二个参数确定索引缓冲区中有多少个索引。

第三个参数执行索引数组中的值的类型，为无符号短整型（GL_UNSIGNED_SHORT）还是无符号字节型（GL_UNSIGNED_BYTE）。

glDrawElements 的最后一个参数指向索引缓冲区。要填充索引缓冲区，需要做的工作与填充顶点缓冲区类似。例如：

```java
// Figure out how you want to arrange your points
short[] myIndecesArray = {0, 1, 2};

// get a short buffer
java.nio.ShortBuffer mIndexBuffer;

// Allocate 2 bytes each for each index value
ByteBuffer ibb = ByteBuffer.allocateDirect(3 * 2);
ibb.order(ByteOrder.nativeOrder());
mIndexBuffer = ibb.asShortBuffer();

// stuff that into the buffer
for (int i = 0; i < 3; i++) {
    mIndexBuffer.put(myIndecesArray[i]);
}
```

> 说明：
>
> 无需创建任何新点，索引缓冲区仅对通过 glVertexPointer 指定的点数组建立索引。之所以可以这么做，是因为 OpenGL 会记住前面的调用所设置的资产状态。

### 3. glClear

使用 glClear 方法擦除绘图表面。使用此方法，不仅可以重置颜色，还可以重置所使用蜡纸（stencil）的深度和类型。要指定需要重置的原始，可以传入常量 GL_COLOR_BUFFER_BIT、GL_DEPTH_BUFFER_BIT 或 GL_STENCIL_BUFFER_BIT。

颜色缓冲区包含可见的像素，因此清除它就相当于擦除了具有任何颜色的表面。深度缓冲区指在 3D 场景中可见的所有像素，具体取决于对象的远近程度。

> 说明
>
> 蜡纸是一种绘图模板，可用于多次复制图形。

出于我们的目的，可以使用以下代码来清除颜色缓冲区：

```java
// Clear the surface of any color
gl.glClear(gl.GL_COLOR_BUFFER_BIT);
```

### 4. glColor

使用 glColor 设置接下来要绘制图形的默认颜色。例如：

```java
// Set the current color
glColor4f(1.0f, 0, 0, 0.5f);
```

4f 表示该方法接受 4 个参数，每个参数都为浮点值。这 4 个参数是红、绿、蓝和 alpha （颜色渐变）的分量。每个参数的起始值为（1,1,1,1）。



