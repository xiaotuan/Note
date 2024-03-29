[toc]

### 1. 根窗口

在 GUI 编程中，顶层的根窗口对象包含组成 GUI 应用的所有小窗口对象。在 Python 中，一般会写成如下语句：

```python
top = Tkinter.Tk()	# or just Tk() with "from Tkinter import *"
```

### 2. 事件驱动处理

当所有控件摆放好后，可以让应用进入无序主循环中。在 Tkinter 中，代码如下所示：

```python
Tkinter.mainloop()
```

一般这是程序运行的最后一段代码。当进入主循环后，GUI 就从这里开始接管程序的执行。所有其他行为都会通过回调来处理，甚至包括退出应用。

### 3. 布局管理器

Tk 有 3 种布局管理器来帮助控件集进行定位。最原始的一种称为 Placer。它的做法非常直接：你提供控件的大小和摆放位置，然后管理器就会将其摆放好。

第二种布局管理器会是你主要使用的，它叫做 Packer。它会把控件填充到正确的位置，然后对于之后的每个控件，会去寻找剩余的控件进行填充。

第三种布局管理器是 Grid。你可以基于网格坐标，使用 Grid 来指定 GUI 控件的放置。Grid 会在它们的网格位置上渲染 GUI 应用中的每个对象。