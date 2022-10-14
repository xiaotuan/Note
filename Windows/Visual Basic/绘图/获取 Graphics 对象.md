[toc]

### 1. 为窗体或控件创建 Graphics 对象

如果要直接绘制到窗体或控件上，可调用该对象的 `CreateGraphics()` 方法获得对图形表面的引用。例如：

```vb
Dim objGraphics As Graphics = TextBox1.CreateGraphics
```

> 注意：直接绘制到窗体或控件上时，对象并不会持久化绘制在它上面的图形。如果窗体被遮掩，如果被其他窗体覆盖或将窗体最小化，下次窗体绘制时，将不会包含已绘制在它上面的图形。

### 2. 为新位图创建 Graphics 对象

不一定要将 `Graphics` 对象设置为窗体或控件的客户区域；也可将其设置为只存在于内存中的位图。

要创建新位图，可使用如下语法，声明一个存储新位图引用的变量：

```vb
variable = New Bitmap(width, height, pixelformat)
```

参数 width 和 height 是新位图的宽度和高度，pixelformat 参数指定位图的颜色深度，也可能指定位图是否有 alpha 图层。pixelformat 的一些常见取值有：

| 值                   | 说明                                                         |
| -------------------- | ------------------------------------------------------------ |
| Format16bppGrayScale | 像素格式为每像素 16 位，该颜色信息指定 65536 中颜色          |
| Format16bppRgb555    | 像素格式为每像素 16 位，该颜色信息指定 32768 中颜色，其中 5 位是红色，5 位是绿色，5 位是蓝色 |
| Format24bppRgb       | 像素格式为每像素 24 位，该颜色信息指定了 16777216 种颜色，其中 8 位是红色，8 位是绿色，8 位是蓝色 |

例如：

```vb
objMyBitmap = New Bitmap(640, 480, Drawing.Imaging.PixelFormat.Format24bppRgb)
```

创建位图后，可以使用 `FromImage()` 方法创建一个引用位图的 Graphics 对象，如下所示：

```vb
objGraphics = Graphics.FromImage(objMyBitMap)
```

> 注意：不再需要 `Graphics` 对象时，应调用它的 `Dispose()` 方法，确保 `Graphics` 对象占用的所有资源都被释放。

