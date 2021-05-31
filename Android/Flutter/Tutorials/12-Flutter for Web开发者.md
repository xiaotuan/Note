# Flutter for Web开发者

- 执行基本布局操作
  - [给文本添加样式](https://flutterchina.club/web-analogs/#给文本添加样式)
  - [设置背景颜色](https://flutterchina.club/web-analogs/#设置背景颜色)
  - [居中组件](https://flutterchina.club/web-analogs/#居中组件)
  - [设置容器宽度](https://flutterchina.club/web-analogs/#设置容器宽度)
- 控制位置和大小
  - [设置绝对位置](https://flutterchina.club/web-analogs/#设置绝对位置)
  - [旋转组件](https://flutterchina.club/web-analogs/#旋转组件)
  - [缩放组件](https://flutterchina.club/web-analogs/#缩放组件)
  - 应用线性渐变
    - [垂直渐变](https://flutterchina.club/web-analogs/#垂直渐变)
    - [水平渐变](https://flutterchina.club/web-analogs/#水平渐变)
- 处理形状
  - [圆角](https://flutterchina.club/web-analogs/#圆角)
  - [添加阴影](https://flutterchina.club/web-analogs/#添加阴影)
  - [圆和椭圆](https://flutterchina.club/web-analogs/#圆和椭圆)
- 操作文本
  - [调整文本间距](https://flutterchina.club/web-analogs/#调整文本间距)
  - [转换文本](https://flutterchina.club/web-analogs/#转换文本)
  - [进行内联格式更改](https://flutterchina.club/web-analogs/#进行内联格式更改)
  - [创建文本摘要](https://flutterchina.club/web-analogs/#创建文本摘要)

此页面适用于熟悉HTML和CSS语法的用户。它将HTML / CSS代码片段映射到的Flutter / Dart代码片段。

这些例子假定:

- HTML文档以HTML DOCTYPE开始, 并且所有HTML的

  ```
  box-sizing
  ```

  为

   

  border-box

  , 以便与Flutter模型一致.

  ```css
  <!DOCTYPE html>
  
   {
     box-sizing: border-box;
   }
  ```

- 在Flutter中，“Lorem ipsum”文本的默认样式由

  ```
  bold24Roboto
  ```

  变量定义 如下，以保持简单的语法:

  ```dart
  TextStyle bold24Roboto = new TextStyle(
    color: Colors.white,
    fontSize: 24.0,
    fontWeight: FontWeight.w900,
  );
  ```

## 执行基本布局操作

以下示例显示如何执行最常见的UI布局任务。

### 给文本添加样式

CSS中的字体样式, 大小, 和一些其它文本属性在Flutter中对应了[Text](https://docs.flutter.io/flutter/widgets/Text-class.html) 的[TextStyle](https://docs.flutter.io/flutter/painting/TextStyle-class.html)属性。

在 HTML 和 Flutter中, 默认情况下，子元素或widget都固定在左上角

```css
<div class="greybox">
    Lorem ipsum
</div>

.greybox {
      background-color: #e0e0e0; /* grey 300 */
      width: 320px;
      height: 240px;
      font: 900 24px Georgia;
    }
var container = new Container( // grey box
  child: new Text(
    "Lorem ipsum",
    style: new TextStyle(
      fontSize: 24.0
      fontWeight: FontWeight.w900,
      fontFamily: "Georgia",
    ),
  ),
  width: 320.0,
  height: 240.0,
  color: Colors.grey[300],
);
```

### 设置背景颜色

在Flutter中，您可以在[Container](https://docs.flutter.io/flutter/widgets/Container-class.html)的 `decoration` 属性中设置背景颜色.

下面CSS示例中使用的十六进制颜色值与Flutter Material调色板中所对应的颜色相同：

```css
<div class="greybox">
  Lorem ipsum
</div>

.greybox {
      background-color: #e0e0e0;  /* grey 300 */
      width: 320px;
      height: 240px;
      font: 900 24px Roboto;
    }
var container = new Container( // grey box
    child: new Text(
      "Lorem ipsum",
      style: bold24Roboto,
    ),
    width: 320.0,
    height: 240.0,
    color: Colors.grey[300],
  );
```

### 居中组件

[Center](https://docs.flutter.io/flutter/widgets/Center-class.html) widget 可以使其子widget在水平和垂直方向居中.

为了在CSS中实现类似效果，父元素使用flex或table-cell。此页面上的示例使用了flex布局。

```css
<div class="greybox">
  Lorem ipsum
</div>

.greybox {
  background-color: #e0e0e0; /* grey 300 */
  width: 320px;
  height: 240px;
  font: 900 24px Roboto;
  display: flex;
  align-items: center;
  justify-content: center; 
}
var container = new Container( // grey box
  child:  new Center(
    child:  new Text(
      "Lorem ipsum",
      style: bold24Roboto,
    ),
  ),
  width: 320.0,
  height: 240.0,
  color: Colors.grey[300],
);
```

### 设置容器宽度

要指定[Container](https://docs.flutter.io/flutter/widgets/Container-class.html)的宽度，请设置其`width`属性。 这是一个固定的宽度，不像CSS中max-width属性，它可以设置容器宽度最大值。要在Flutter中模拟这种效果，请使用容器的`constraints`属性。 创建一个新的[BoxConstraints](https://docs.flutter.io/flutter/rendering/BoxConstraints-class.html)来设置`minWidth`或`maxWidth`。

对于嵌套容器，如果父级的宽度小于子级宽度，则子级容器将自行调整大小以匹配父级。

```css
<div class="greybox">
  <div class="redbox">
    Lorem ipsum
  </div>
</div>

.greybox {
  background-color: #e0e0e0; /* grey 300 */
  width: 320px; 
  height: 240px;
  font: 900 24px Roboto;
  display: flex;
  align-items: center;
  justify-content: center;
}
.redbox {
  background-color: #ef5350; /* red 400 */
  padding: 16px;
  color: #ffffff;
    width: 100%;
  max-width: 240px; 
}
var container = new Container( // grey box
  child: new Center(
    child: new Container( // red box
      child: new Text(
        "Lorem ipsum",
        style: bold24Roboto,
      ),
      decoration: new BoxDecoration(
        color: Colors.red[400],
      ),
      padding: new EdgeInsets.all(16.0),
      width: 240.0, //max-width is 240.0
    ),
  ),
  width: 320.0, 
  height: 240.0,
  color: Colors.grey[300],
);
```

## 控制位置和大小

以下示例显示如何在widget的位置、大小和背景上执行更复杂的操作。

### 设置绝对位置

默认情况下，widget相对于其父widget定位。

要将widget的绝对位置指定为x-y坐标，请将其嵌套在[Positioned](https://docs.flutter.io/flutter/widgets/Positioned-class.html)widget中， 该widget又嵌套在[Stack](https://docs.flutter.io/flutter/widgets/Stack-class.html) widget中。

```css
<div class="greybox">
  <div class="redbox">
    Lorem ipsum
  </div>
</div>

.greybox {
  background-color: #e0e0e0; /* grey 300 */
  width: 320px;
  height: 240px;
  font: 900 24px Roboto;
  position: relative; 
}
.redbox {
  background-color: #ef5350; /* red 400 */
  padding: 16px;
  color: #ffffff;
  position: absolute;
  top: 24px;
  left: 24px; 
}
var container = new Container( // grey box
  child: new Stack(
    children: [
      new Positioned( // red box
        child:  new Container(
          child: new Text(
            "Lorem ipsum",
            style: bold24Roboto,
          ),
          decoration: new BoxDecoration(
            color: Colors.red[400],
          ),
          padding: new EdgeInsets.all(16.0),
        ),
        left: 24.0,
        top: 24.0,
      ),
    ],
  ), 
  width: 320.0,
  height: 240.0,
  color: Colors.grey[300],
);
```

### 旋转组件

要旋转一个widget，将它嵌套在一个[Transform](https://docs.flutter.io/flutter/widgets/Transform-class.html)中。 使设置其`alignment`和`origin`属性分别以相对和绝对值指定变换原点。

对于简单的2D旋转，widget在Z轴上旋转。（度数×π/ 180）

```css
<div class="greybox">
  <div class="redbox">
    Lorem ipsum
  </div>
</div>

.greybox {
  background-color: #e0e0e0; /* grey 300 */
  width: 320px;
  height: 240px;
  font: 900 24px Roboto;
  display: flex;
  align-items: center;
  justify-content: center;
}
.redbox {
  background-color: #ef5350; /* red 400 */
  padding: 16px;
  color: #ffffff;
  transform: rotate(15deg); 
}
var container = new Container( // gray box
  child: new Center(
    child:  new Transform(
      child:  new Container( // red box
        child: new Text(
          "Lorem ipsum",
          style: bold24Roboto,
          textAlign: TextAlign.center,
        ),
        decoration: new BoxDecoration(
          color: Colors.red[400],
        ),
        padding: new EdgeInsets.all(16.0),
      ),
      alignment: Alignment.center,
      transform: new Matrix4.identity()
        ..rotateZ(15 * 3.1415927 / 180),
    ), 
  ),
  width: 320.0,
  height: 240.0,
  color: Colors.grey[300],
);
```

### 缩放组件

要向上或向下缩放widget，请将其嵌套在[Transform](https://docs.flutter.io/flutter/widgets/Transform-class.html)中。 并设置其`alignment`和`origin`属性分别以相对和绝对值指定变换原点。

对于沿x轴的简单缩放操作，请创建一个新的[Matrix4](https://docs.flutter.io/flutter/vector_math_64/Matrix4-class.html)， 标识对象并使用其`scale（）`方法指定缩放因子。

当缩放父widget时，所有子widget都会相应地缩放。

```css
<div class="greybox">
  <div class="redbox">
    Lorem ipsum
  </div>
</div>

.greybox {
  background-color: #e0e0e0; /* grey 300 */
  width: 320px;
  height: 240px;
  font: 900 24px Roboto;
  display: flex;
  align-items: center;
  justify-content: center;
}
.redbox {
  background-color: #ef5350; /* red 400 */
  padding: 16px;
  color: #ffffff;
  transform: scale(1.5); 
}
var container = new Container( // gray box
  child: new Center(
    child:  new Transform(
      child:  new Container( // red box
        child: new Text(
          "Lorem ipsum",
          style: bold24Roboto,
          textAlign: TextAlign.center,
        ),
        decoration: new BoxDecoration(
          color: Colors.red[400],
        ),
        padding: new EdgeInsets.all(16.0),
      ),
      alignment: Alignment.center,
      transform: new Matrix4.identity()
        ..scale(1.5),
     ), 
  width: 320.0,
  height: 240.0,
  color: Colors.grey[300],
);
```

### 应用线性渐变

要将线性渐变应用于widget的背景，请将其嵌套到[Container](https://docs.flutter.io/flutter/widgets/Container-class.html)widget中。 然后使用Container的`decoration`属性来创建[BoxDecoration](https://docs.flutter.io/flutter/painting/BoxDecoration-class.html)对象， 并使用BoxDecoration的`gradient`属性来转换背景填充。

渐变“角度”基于Alignment（x，y）值:

- | 如果开始和结束的x值相等，则渐变是垂直的（0° | 180°）。 |
  | ------------------------------------------- | -------- |
  |                                             |          |

- | 如果开始和结束的y值相等，则渐变为水平（90° | 270°） |
  | ------------------------------------------ | ------ |
  |                                            |        |

#### 垂直渐变

```css
<div class="greybox">
  <div class="redbox">
    Lorem ipsum
  </div>
</div>

.greybox {
  background-color: #e0e0e0; /* grey 300 */
  width: 320px;
  height: 240px;
  font: 900 24px Roboto;
  display: flex;
  align-items: center;
  justify-content: center;
}
.redbox {
  padding: 16px;
  color: #ffffff;
  background: linear-gradient(180deg, #ef5350, rgba(0, 0, 0, 0) 80%); 
}
var container = new Container( // grey box
  child: new Center(
    child: new Container( // red box
      child: new Text(
        "Lorem ipsum",
        style: bold24Roboto,
      ),
      decoration: new BoxDecoration(
        gradient: new LinearGradient(
          begin: const Alignment(0.0, -1.0),
          end: const Alignment(0.0, 0.6),
          colors: <Color>[
            const Color(0xffef5350),
            const Color(0x00ef5350)
          ],
        ),
      ), 
      padding: new EdgeInsets.all(16.0),
    ),
  ),
  width: 320.0,
  height: 240.0,
  color: Colors.grey[300],
);
```

#### 水平渐变

```css
<div class="greybox">
  <div class="redbox">
    Lorem ipsum
  </div>
</div>

.greybox {
  background-color: #e0e0e0; /* grey 300 */
  width: 320px;
  height: 240px;
  font: 900 24px Roboto;
  display: flex;
  align-items: center;
  justify-content: center;
}
.redbox {
  padding: 16px;
  color: #ffffff;
  background: linear-gradient(90deg, #ef5350, rgba(0, 0, 0, 0) 80%); 
}
var container = new Container( // grey box
  child: new Center(
    child: new Container( // red box
      child: new Text(
        "Lorem ipsum",
        style: bold24Roboto,
      ),
      decoration: new BoxDecoration(
        gradient: new LinearGradient(
          begin: const Alignment(-1.0, 0.0),
          end: const Alignment(0.6, 0.0),
          colors: <Color>[
            const Color(0xffef5350),
            const Color(0x00ef5350)
          ],
        ),
      ), 
      padding: new EdgeInsets.all(16.0),
    ),
  ),
  width: 320.0,
  height: 240.0,
  color: Colors.grey[300],
);
```

## 处理形状

以下示例显示如何自定义形状。

### 圆角

要给矩形添加圆角请使用[BoxDecoration](https://docs.flutter.io/flutter/painting/BoxDecoration-class.html)对象的`borderRadius`属性 。 创建一个新的[BorderRadius](https://docs.flutter.io/flutter/painting/BorderRadius-class.html)对象，给该对象指定一个的半径（会四舍五入）。

```css
<div class="greybox">
  <div class="redbox">
    Lorem ipsum
  </div>
</div>

.greybox {
  background-color: #e0e0e0; /* gray 300 */
  width: 320px;
  height: 240px;
  font: 900 24px Roboto;
  display: flex;
  align-items: center;
  justify-content: center;
}
.redbox {
  background-color: #ef5350; /* red 400 */
  padding: 16px;
  color: #ffffff;
  border-radius: 8px; 
}
var container = new Container( // grey box
  child: new Center(
    child: new Container( // red circle
      child: new Text(
        "Lorem ipsum",
        style: bold24Roboto,
      ),
      decoration: new BoxDecoration(
        color: Colors.red[400],
        borderRadius: new BorderRadius.all(
          const Radius.circular(8.0),
        ), 
      ),
      padding: new EdgeInsets.all(16.0),
    ),
  ),
  width: 320.0,
  height: 240.0,
  color: Colors.grey[300],
);
```

### 添加阴影

在CSS中，您可以使用box-shadow属性来快速指定阴影偏移和模糊。

在Flutter中，每个属性和值都单独指定。使用BoxDecoration的`boxShadow`属性创建[BoxShadow](https://docs.flutter.io/flutter/painting/BoxShadow-class.html)列表。 您可以定义一个或多个BoxShadow，它们可以叠加出自定义阴影深度、颜色等。

```css
<div class="greybox">
  <div class="redbox">
    Lorem ipsum
  </div>
</div>

.greybox {
  background-color: #e0e0e0; /* grey 300 */
  width: 320px;
  height: 240px;
  font: 900 24px Roboto;
  display: flex;
  align-items: center;
  justify-content: center;
}
.redbox {
  background-color: #ef5350; /* red 400 */
  padding: 16px;
  color: #ffffff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.8),
              0 6px 20px rgba(0, 0, 0, 0.5);
}
var container = new Container( // grey box
  child: new Center(
    child: new Container( // red box
      child: new Text(
        "Lorem ipsum",
        style: bold24Roboto,
      ),
      decoration: new BoxDecoration(
        color: Colors.red[400],
        boxShadow: <BoxShadow>[
          new BoxShadow (
            color: const Color(0xcc000000),
            offset: new Offset(0.0, 2.0),
            blurRadius: 4.0,
          ),
          new BoxShadow (
            color: const Color(0x80000000),
            offset: new Offset(0.0, 6.0),
            blurRadius: 20.0,
          ),
        ], 
      ),
      padding: new EdgeInsets.all(16.0),
    ),
  ),
  width: 320.0,
  height: 240.0,
  decoration: new BoxDecoration(
    color: Colors.grey[300],
  ),
  margin: new EdgeInsets.only(bottom: 16.0),
);
```

### 圆和椭圆

在CSS中制作一个圆需要将矩形的四条边的`border-radius`设置为50%。

虽然[BoxDecoration](https://docs.flutter.io/flutter/painting/BoxDecoration-class.html)的`borderRadius`属性支持此方法， 但Flutter为此提供了一个shape属性, 值为[BoxShape枚举](https://docs.flutter.io/flutter/painting/BoxShape-class.html) 。

```css
<div class="greybox">
  <div class="redcircle">
    Lorem ipsum
  </div>
</div>

.greybox {
  background-color: #e0e0e0; /* gray 300 */
  width: 320px;
  height: 240px;
  font: 900 24px Roboto;
  display: flex;
  align-items: center;
  justify-content: center;
}
.redcircle {
  background-color: #ef5350; /* red 400 */
  padding: 16px;
  color: #ffffff;
  text-align: center;
  width: 160px;
  height: 160px;
  border-radius: 50%; 
}
var container = new Container( // grey box
  child: new Center(
    child: new Container( // red circle
      child: new Text(
        "Lorem ipsum",
        style: bold24Roboto,
        textAlign: TextAlign.center, 
      ),
      decoration: new BoxDecoration(
        color: Colors.red[400],
        shape: BoxShape.circle, 
      ),
      padding: new EdgeInsets.all(16.0),
      width: 160.0,
      height: 160.0, 
    ),
  ),
  width: 320.0,
  height: 240.0,
  color: Colors.grey[300],
);
```

## 操作文本

以下示例显示如何指定字体和其他文本属性。他们还展示了如何变换文本字符串，自定义间距和创建摘要。

### 调整文本间距

在CSS中，通过分别给出letter-spacing和word-spacing属性的长度值，指定每个字母或单词之间的空白间距。长度单位可以是px，pt，cm，em等。

在Flutter中，您将空白区域指定为Text的[TextStyle](https://docs.flutter.io/flutter/painting/TextStyle-class.html)的`letterSpacing`和`wordSpacing`属性， 值为逻辑像素（允许为负值）

```css
<div class="greybox">
  <div class="redbox">
    Lorem ipsum
  </div>
</div>

.greybox {
  background-color: #e0e0e0; /* grey 300 */
  width: 320px;
  height: 240px;
  font: 900 24px Roboto;
  display: flex;
  align-items: center;
  justify-content: center;
}
.redbox {
  background-color: #ef5350; /* red 400 */
  padding: 16px;
  color: #ffffff;
  letter-spacing: 4px; 
}
var container = new Container( // grey box
  child: new Center(
    child: new Container( // red box
      child: new Text(
        "Lorem ipsum",
        style: new TextStyle(
          color: Colors.white,
          fontSize: 24.0,
          fontWeight: FontWeight.w900,
          letterSpacing: 4.0, 
        ),
      ),
      decoration: new BoxDecoration(
        color: Colors.red[400],
      ),
      padding: new EdgeInsets.all(16.0),
    ),
  ),
  width: 320.0,
  height: 240.0,
  color: Colors.grey[300],
);
```

### 转换文本

在HTML / CSS中，您可以使用text-transform属性执行简单大小写转换

在Flutter中，使用 dart:core库中的[String 类](https://docs.flutter.io/flutter/dart-core/String-class.html)的方法来转换Text的内容。

```css
<div class="greybox">
  <div class="redbox">
    Lorem ipsum 
  </div>
</div>

.greybox {
  background-color: #e0e0e0; /* grey 300 */
  width: 320px;
  height: 240px;
  font: 900 24px Roboto;
  display: flex;
  align-items: center;
  justify-content: center;
}
.redbox {
  background-color: #ef5350; /* red 400 */
  padding: 16px;
  color: #ffffff;
  text-transform: uppercase; 
}
var container = new Container( // grey box
  child: new Center(
    child: new Container( // red box
      child: new Text(
        "Lorem ipsum".toUpperCase(), 
        style: bold24Roboto,
      ),
      decoration: new BoxDecoration(
        color: Colors.red[400],
      ),
      padding: new EdgeInsets.all(16.0),
    ),
  ),
  width: 320.0,
  height: 240.0,
  color: Colors.grey[300],
);
```

### 进行内联格式更改

[Text](https://docs.flutter.io/flutter/widgets/Text-class.html) widget控件，可以用相同的格式显示文本。 要显示使用多个样式的文本（在本例中为带有重点的单个单词），请改用[RichText](https://docs.flutter.io/flutter/widgets/RichText-class.html)。 它的text属性可以指定一个或多个可单独设置样式的[TextSpan](https://docs.flutter.io/flutter/painting/TextSpan-class.html)widget。

在以下示例中，“Lorem”位于具有默认（继承）文本样式的TextSpan小部件中，“ipsum”位于具有自定义样式的单独TextSpan中。

```css
<div class="greybox">
  <div class="redbox">
    Lorem <em>ipsum</em> 
  </div>
</div>

.greybox {
  background-color: #e0e0e0; /* grey 300 */
  width: 320px;
  height: 240px;
  font: 900 24px Roboto; 
  display: flex;
  align-items: center;
  justify-content: center;
}
.redbox {
  background-color: #ef5350; /* red 400 */
  padding: 16px;
  color: #ffffff;
}
 .redbox em {
  font: 300 48px Roboto;
  font-style: italic;
} 
var container = new Container( // grey box
  child: new Center(
    child: new Container( // red box
      child:  new RichText(
        text: new TextSpan(
          style: bold24Roboto,
          children: <TextSpan>[
            new TextSpan(text: "Lorem "),
            new TextSpan(
              text: "ipsum",
              style: new TextStyle(
                fontWeight: FontWeight.w300,
                fontStyle: FontStyle.italic,
                fontSize: 48.0,
              ),
            ),
          ],
        ),
      ), 
      decoration: new BoxDecoration(
        backgroundColor: Colors.red[400],
      ),
      padding: new EdgeInsets.all(16.0),
    ),
  ),
  width: 320.0,
  height: 240.0,
  color: Colors.grey[300],
);
```

### 创建文本摘要

摘录显示段落中文本的最初行，并且通常使用省略号处理溢出文本。在HTML / CSS中，摘要不能超过一行。截断多行需要一些JavaScript代码。

在Flutter中，使用Text小部件的`maxLines`属性来指定要包含在摘要中的行数，以及用于处理溢出文本的属性`overflow`。

```css
<div class="greybox">
  <div class="redbox">
    Lorem ipsum dolor sit amet, consec etur
  </div>
</div>

.greybox {
  background-color: #e0e0e0; /* grey 300 */
  width: 320px;
  height: 240px;
  font: 900 24px Roboto;
  display: flex;
  align-items: center;
  justify-content: center;
}
.redbox {
  background-color: #ef5350; /* red 400 */
  padding: 16px;
  color: #ffffff;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap; 
}
var container = new Container( // grey box
  child: new Center(
    child: new Container( // red box
      child: new Text(
        "Lorem ipsum dolor sit amet, consec etur",
        style: bold24Roboto,
        overflow: TextOverflow.ellipsis,
        maxLines: 1, 
      ),
      decoration: new BoxDecoration(
        backgroundColor: Colors.red[400],
      ),
      padding: new EdgeInsets.all(16.0),
    ),
  ),
  width: 320.0,
  height: 240.0,
  color: Colors.grey[300],
);
```