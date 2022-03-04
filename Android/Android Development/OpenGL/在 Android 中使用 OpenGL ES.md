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