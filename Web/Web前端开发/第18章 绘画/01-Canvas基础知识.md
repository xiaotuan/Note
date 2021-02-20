[toc]

### 1. Canvas

在 HTML 页面上定义 Canvas 元素除了可以指定 id、style、class、hidden 等通用属性之外，还可以指定以下两个属性。

height：设置画布组件的高度。

width：设置画布组件的宽度。

在画布上绘制图形必须经过以下三个步骤：

① 获取 Canvas 对应的 DOM 对象，得到一个 Canvas 对象。

② 调用 Canvas 对象的 getContext() 方法，得到 CanvasRenderingCantext2D 对象（可绘制图形）。

③ 调用 CanvasRenderingContext2D 对象方法绘图。

**案例：示例 18-01：第一个 Canvas 图形**

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta keywords="Canvas" />
        <meta content="第一个Canvas图形" />
        <title>第一个Canvas图形</title>
    </head>

    <body>
        <canvas id="demo" width="300" height="200" style="border:1px solid #CCCCCC;"></canvas>
        <script type="text/javascript">
            //获取canvas元素对应的DOM对象
            var canvas = document.getElementById("demo");
            //获取在canvas上绘图的canvasRenderingContext2D对象
            var ctx = canvas.getContext("2d");
            //设置填充颜色
            ctx.fillStyle = '#007ACC';
            //绘制矩形
            ctx.fillRect(50, 50, 200, 100);
        </script>
    </body>
</html>
```

### 2. 绘图方法

<center><b>表 18-1 CanvasRenderingContext2D 绘图方法</b></center>

| 方法                                                         | 简要说明                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| void arc(float x, float y, float radius, float startAngel, float endAngle, boolean counterclockwise) | 向 Canvas 的当前路径上添加一段弧                             |
| var arcTo(float x1, float y1, float x2, float y2, float radius) | 向 Canvas 的当前路径上添加一段弧，与前一个方法相比，只是定义弧的方式不同 |
| void beginPath()                                             | 开始定义路径                                                 |
| void closePath()                                             | 关闭前面定义的路径                                           |
| void bezierCurveTo(float cpX1, float cpY1, float cpX2, float cpY2, float x, float y) | 向 Canvas 的当前路径上添加一段贝塞尔曲线                     |
| void clearRect(float x, float y, float width, float height)  | 擦除指定区域上绘制的图形                                     |
| void clip()                                                  | 从画布上裁切一块出来                                         |
| CanvasGradient createLinearGradient(float xStart, float yStart, float xEnd, float yEnd) | 创建一个线性渐变                                             |
| CanvasPattern createPattern(image image, string style)       | 创建一个图形平铺                                             |
| CanvasGradient createLinearGradient(float xStart, float yStart, float radiusStart, float xEnd, float yEnd, float radiusEnd) | 创建一个圆形渐变                                             |
| void drawImage(Image image, float x, float y)<br />void drawImage(Image image, float x, float y, float width, float height)<br />void drawImage(Image image, integer sx, integer xy, integer sw, integer sh, float dx, float dy, float dw, float dh) | 绘制位图                                                     |
| void fill()                                                  | 填充 Canvas 的当前路径                                       |
| void fillRect(float x, float y, float width, float height)   | 填充一个矩形区域                                             |
| void fillText(String text, float x, float y[, float maxWidth]) | 填充字符串                                                   |
| void lineTo(float x, float y)                                | 把 Canvas 的当前路径从当前结束点连接到 x、y 的对应点         |
| void moveTo(float x, float y)                                | 把 Canvas 的当前路径结束点移动到 x、y 的对应点               |
| void quadraticCurveTo(float cpX, float cpY, float x, float y) | 向 Canvas 当前路径上添加一段二次曲线                         |
| void rect(float x, float y, float width, float height)       | 向 Canvas 当前路径上添加一个矩形                             |
| void stroke()                                                | 沿着 Canvas 当前路径绘制边框                                 |
| void strokeRect(float x, float y, float width, float height) | 绘制一个矩形边框                                             |
| void strokeText(string text, float x, float y, float width[, float maxWidth]) | 绘制字符串边框                                               |
| void save()                                                  | 保存当前绘图状态                                             |
| void restore()                                               | 恢复之前保存的绘图状态                                       |
| void rotate(float angle)                                     | 旋转坐标系统                                                 |
| void scale(float sx, float sy)                               | 缩放坐标系统                                                 |
| void translate(float dx, float dy)                           | 平移坐标系统                                                 |

### 3. 绘图属性

<center><b>表18-2 CanvasRenderingContext2D 属性</b></center>

| 属性名                   | 简要说明                                                     |
| ------------------------ | ------------------------------------------------------------ |
| fillStyle                | 设置填充路径时所用的填充风格，该属性支持三种类型的值：<br />符合颜色格式的字符串值，表明使用纯色填充：<br />CanvasGradient，表明使用渐变填充<br />CanvasPattern，表明填充绘图的模式 |
| strokeStyle              | 设置绘制路径时所用的填充风格，该属性支持三种类型的值：<br />符合颜色格式的字符串值，表明使用纯色填充<br />CanvasGradient，表明使用渐变填充<br />CanvasPattern，表明填充路径的模式 |
| Font                     | 设置绘制字符串时所用的字体                                   |
| globalAlpha              | 设置全局透明度                                               |
| globalCompositeOperation | 设置全局叠加效果                                             |
| lineCap                  | 设置线段端点的绘图形状。该属性支持如下是三个值：<br />butt，默认的属性值，该属性值指定不绘制端点，在线条结尾处直接结束<br />round，该属性值指定绘制圆形端点。在线条结尾处绘制一个直径为线条宽度的半圆<br />square，该属性值指定绘制正方形端点。在线条结尾处绘制半个边长为线条宽度的正方形。这种形状的端点与 butt 形状端点相似，但线条略长。 |
| lineJoin                 | 设置线条连接点的风格。该属性支持如下三个值：<br />meter，默认属性值，线条连接点形如箭头<br />round，线条连接点形如圆角<br />bevel，线条连接点形如平角 |
| miterLimit               | 把 lineJoin 树形设置为 meter 风格时，该属性控制锐角箭头的长度 |
| lineWidth                | 设置笔触线条宽度                                             |
| shadowBlur               | 设置阴影的模糊程度                                           |
| shadowColor              | 设置阴影的颜色                                               |
| shadowOffsetX            | 设置阴影在 X 方向上的偏移                                    |
| shadowOffsetY            | 设置阴影在 Y 方向上的偏移                                    |
| textAlign                | 设置绘制字符串的水平对齐方式，该属性支持 start、end、left、right、center 等属性值 |
| textBaseAlign            | 设置绘制字符串的垂直对齐方式，该属性支持 top、hanging、middle、alphabetic、idecgraphic、bottom 等属性值 |

