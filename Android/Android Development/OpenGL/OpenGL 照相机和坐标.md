[toc]

所绘制的图形将根据照相机的位置、照相机镜头的方向、照相机的朝向、缩放级别和拍照 “胶片” 的尺寸而变得可见。

在 OpenGL 中，将 3D照片投影到 2D 屏幕上的这些方面由 3 个方法控制：

+ gluLookAt：控制照相机的方向。
+ glFrustum：控制视体、缩放级别或靠近或远离你的距离。
+ glViewport：控制屏幕大小或照相机 ”胶片“ 的尺寸。

### 1. gluLookAt 和照相机类比手法

使用 gluLookAt 方法来指定三个点——眼点（照相机的位置）、注视点（照相机对准的方向）和向上矢量（照相机是朝上、朝下还是倾斜）：

```java
gluLookAt(gl, 0,0,0, 0,0,0, 0,1,0);
```

### 2. glFrustum 和视体

你可能已注意到，描述照相机位置的所有点都没有使用 gluLookAt 来处理大小。那么如何告诉照相机将焦点对准哪里？希望捕获的被摄物体有多远？拍摄区域有多宽和多高？可以使用 OpenGL 方法 glFrustum 来指定感兴趣的场景区域。

将场景区域想想为具有一个边界框，这个框也称为 **视锥体** 或 **视体**。这个框内的任何景象将被捕获，框外的任何景象将被裁剪和忽略。那么如何指定此视框？首先确定近点，或者照相机与视框最近处的距离。然后可以选择一个远点，也就是照相机与视框最远处的距离。近点与远点之间沿 z 轴的距离是视框的景深。如果指定近点为 50，远点为 200，那么将捕获这两点之间的任何景深，视框景深将为 150。还需要指定视框沿连接照相机与注视点的虚构射线的左边、右边、顶边和底边。

在 OpenGL 中，可以通过两种方式来想象此框。一种方式称为 **透视投影**，这种方式涉及前面介绍的视锥体。这种方式模拟自然的照相机功能，涉及一种凌锥结构，其中远平面相当于底面，照相机相当于顶点。近平面将凌锥的顶部裁剪掉，形成近平面到远平面之间的截头锥体。

想象视框的另一种方式是将它视为一个立方体。这种情况称为正摄投影，适用于尽管照相机与图形之间存在一定距离，但仍然需要保持大小的几何图形。

```java
// calculate aspect ratio first
float ratio = (float) w / h;

// indicate that we want a perspective projection
glMatrixMode(GL10.GL_PROJECTION);

// Specify the frustum: the viewing volume
gl.glFrustumf(
	-ratio,	// Left side of the viewing box
    ratio,	// right side of the viewing box
    1,		// top of the viewing box
    -1,		// bottom of the viewing box
    3,		// how far is the front of the box from the camera
    7		// how far is the back of the box from the camera
);
```

因为我们在前面这段代码中将视框的顶面设置为1，将底面设置为 -1，所以我们将视框前部高度设置为 2 个单位。使用比例数来指定视锥体左边和右边的大小。因此，这段代码使用了窗口高度和宽度来计算比例考虑窗口的长宽比。这段代码还假设操作区域为沿 z 轴 3 个单位到 7 个单位之间的部分。对照相机而言，在这些坐标以外的任何景象都将不可见。

现在已确定了视体的大小。需要使用另一个 API 将这些大小映射到屏幕上：glViewport。

### 3. glViewport 和屏幕大小

glViewport 负责指定视体将投影到屏幕上的哪个矩形区域。此方法接受 4 个参数来指定该矩形框：左下角的 x 和 y 坐标，以及宽度和高度。

```java
glViewport(
	0,	// lower left "x" of the rectangle on the screen
    0,	// lower left "y" of the rectangle on the screen
    width,	// width of the rectangle on the screen
    height	// height of the rectangle on the screen
);
```

如果窗口或试图的高度为 100 像素，而且视锥体高度为 10 个单位，那么世界坐标中的每个逻辑单位 1 将转换为屏幕坐标中的 10 像素。