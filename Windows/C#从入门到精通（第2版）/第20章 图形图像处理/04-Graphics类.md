### 20.1.2　Graphics类

我们在进行绘画之前必须指定画布，在绘图时，Graphics类封装一个GDI+绘图的表面，我们要进行绘图操作，首先需要创建代表绘图表面的Graphics对象，然后利用GDI+提供的绘图方法在绘图表面上绘制图形图像，Graphics与特定的设备上下文关联。画图方法都包括在Graphics类中，它是一切GDI+操作的基础类。

Graphics位于System.Drawing 命名空间下，图形图像处理相关的命名空间主要包括以下几种。

+ System.Drawing：提供了对 GDI+ 基本图形功能的访问支持。
+ System.Drawing.Drawing2D：提供高级的二维和矢量图形功能。
+ System.Drawing.Imaging：提供高级 GDI+ 图像处理功能。
+ System.Drawing.Text：提供高级 GDI+ 排版功能。

绘图程序的设计过程一般分为两个步骤：一是创建Graphics对象，二是使用Graphics对象的方法绘图、显示文本或处理图像。

创建一个Graphics对象的方式有三种。

（1）方式一：使用CreateGraphics()方法创建。

调用窗口或控件的CreateGraphics()方法，创建一个Graphics类的实例对象，这个实例对象代表调用CreateGraphics()方法的窗体或控件的表面，可以通过创建的Graphics对象在窗体和控件的表面上绘图。

例如，

```c
01  private void Form1_Load(object sender, EventArgs e)
02  {
03          Graphics g = this.CreateGraphics();
04  }
```

（2）方式二：在窗体或控件的Paint事件中引用Graphics对象。

在窗体或控件的Paint事件对象中包含对应窗体或控件的Graphics对象的引用，我们可以在Paint事件处理方法中通过PaintEventArgs参数获得Graphics对象，它代表事件源所对应的窗体或控件，在为控件创建绘制代码时，通常会使用此方法来获取对图形对象的引用。例如，

```c
//窗体的Paint事件的响应方法
01  private void form1_Paint(object sender, PaintEventArgs e) 
02  {
03          Graphics g = e.Graphics;
04  }
```

也可以直接重载控件或窗体的OnPaint方法，具体代码如下所示。

```c
01  protected override void OnPaint(PaintEventArgs e) 
02  {
03            Graphics g = e.Graphics;
04  }
```

Paint事件在重绘控件时发生。

（3）方式三：调用Graphics类的FromImage静态方法。

由从Image继承的任何对象都可以调用FromImage()方法创建Graphics对象。通过这种方式获得的Graphics对象代表图像的绘图区域，在需要更改已存在的图像时，通常会使用此方法。例如，

```c
//名为“g1.jpg”的图片位于当前路径下
01  Image img = Image.FromFile("g1.jpg");//建立Image对象
02  Graphics g = Graphics.FromImage(img);//创建Graphics对象
```

