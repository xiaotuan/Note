[toc]

### 1. 命名空间

`XAML` 里面的元素都是对应着 `.NET` 里面的类，但是只提供类名是不够的。`XAML` 解析器还不知道这个类位于哪个 `.NET` 命名空间，这样解析器才能够正确地识别 `XAML` 的元素。首先来看一个最简单的 `Windows 10` 界面的 `XAML` 代码：

```xml
<Page
    x:Class="BackButtonDemo.MainPage"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:local="using:BackButtonDemo"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    mc:Ignorable="d"
    Background="{ThemeResource ApplicationPageBackgroundThemeBrush}">

    <Grid>
    </Grid>
</Page>
```

上面的代码声明了若干个 XML 命名空间，`XAML` 文档也是一个完整的 `XAML` 的文档。`xmlns` 特性是 XML 中的一个特殊特性，它专门用来声明命名空间。一旦声明一个命名空间，在文档中的任何地方都可以使用该命名空间。`using:HelloworldDemo` 表示引用的是应用程序里的 `HelloworldDemo` 空间，表示可以在 `XAML` 里面通过 `local` 标识符来使用 `HellowordDemo` 空间下的控件或者其他类。

先来看一下两个特别的命名空间：

```
xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
```

+ `http://schemas.microsoft.com/winfx/2006/xaml/presentation` 是 Windows 10 的核心命名空间。它包含了大部分用来构建用户界面的控件类。
+ `http://schemas.microsoft.com/winfx/2006/xaml` 是 `XAML` 命名空间。它包含各种 `XAML` 实用特性，这些特性可影响文档的解析方式。该名称空间被映射为前缀 `x`。这意味着可通过在元素名称之前放置名称空间前缀 `x` 来使用该命名空间，例如上面代码中的 `x:Name="LayoutRoot"`。

### 2. 设置属性

`XAML` 中的属性也是可以使用多种语法设置的，不同的属性类型也会有不同的设置方式，并不是全部的属性设置都是通用的。总的来说，可以通过下面的 4 种方式来设置对象元素的属性：

+ 使用属性语法；
+ 使用属性元素语法；
+ 使用内容元素语法；
+ 使用集合语法（通常是隐式集合语法）。

#### 2.1 使用属性语法设置属性

大部分的对象都可以使用属性元素语法来设置，这也是最常用的属性设置的语法。使用属性语法设置属性的语法格式如下所示：

```xml
<objcetName propertyName="propertyValue" .../>
```

或者

```xml
<objectName propertyName="propertyValue">
...
</objectName>
```

下面的示例使用属性语法来设置 `Rectangle` 对象的 `Name`、`Width`、`Height` 和 `Fill` 属性。

```xml
<Rectangle Name="rectangle1" Width="100" Height="100" Fill="Blue" />
```

下面的 `C#` 代码可以实现等效的效果：

```csharp
Rectangle rectangle1 = new Rectangle();
rectangle1.Width = 100.0;
rectangle1.Height = 100.0;
rectangle1.Fill = new SolidColorBrush(Colors.Blue);
```

#### 2.2 使用属性元素语法设置属性

属性元素语法是指把属性当作一个独立的元素来进行设置，如果要用属性元素语法设置属性，该属性的值也必须是一个 XAML 的对象元素。使用属性元素语法，就需要为要设置的属性创建 XML 元素。这些元素的形式为 `<Object.Property>`，Object 表示对象元素，Property 表示对象元素的属性。

下面用伪代码来表示属性元素语法设置属性的写法：

```xml
<Object>
	<Object.property>
    	PropertyValueAsObjectElement
    </Object.property>
</Object>
```

下面的示例使用属性语法来设置 `Rectangle` 对象元素的 `Fill` 属性：

```xml
<Rectangle Name="rectangle1" Width="100" Height="100">
	<Rectangle.Fill>
    	<SolidColorBrush Color="Blue" />
    </Rectangle.Fill>
</Rectangle>
```

如果使用属性语法来编写上面的代码，则等同于下面的代码：

```xml
<Rectangle Name="rectangle1" Width="100" Height="100" Fill="Blue">
</Rectangle>
```

#### 2.3 使用内容语法设置属性

使用内容语法设置属性是指直接在对象元素节点内容中设置改属性，忽略该属性的属性元素，相当于把该属性的值看作是当前对象元素的内容。内容语法需要较为特殊的属性才能支持，例如常见的 `Child` 属性、`Content` 属性都可以使用内容语法进行设置。下面的示例使用内容语法设置 `Border` 的 `Content` 属性：

```xml
<Border>
	<Button Content="按钮" />
</Border>
```

如果内容属性也支持 "松散" 的对象模型，在此模型中，属性类型为 `Object` 类型或者 `String` 类型，则可以使用内容语法将纯字符串作为内容放入开始对象标记与结束对象标记之间。下面的示例使用内容语法直接用字符串来设置 `TextBlock` 的 `Text` 属性：

```xml
<TextBlock>你好！</TextBlock>
```

#### 2.4 使用集合语法设置属性

如果属性的值是一个集合，就需要使用集合语法设置该属性。使用集合语法设置元素实际上是向对象集合中添加属性项，如下所示：

```xml
<Rectangle Width="200" Height="150">
	<Rectangle.Fill>
    	<LinearGradientBrush>
        	<LinearGradientBrush.GradientStops>
                <GradientStopCollection>
                	<GradientStop Offset="0.0" Color="Coral" />
                	<GradientStop Offset="1.0" Color="Green" />
                </GradientStopCollection>
            </LinearGradientBrush.GradientStops>
        </LinearGradientBrush>
    </Rectangle.Fill>
</Rectangle>
```

`XAML` 分析器可根据集合所属的属性隐式知道集合的后备类型。因此，可以省略集合本身的对象属性，上面的代码页可以省略掉 `GradientStopCollection`，如下所示：

```xml
<Rectangle Width="200" Height="150">
	<Rectangle.Fill>
    	<LinearGradientBrush>
        	<LinearGradientBrush.GradientStops>
            	<GradientStop Offset="0.0" Color="Coral" />
                <GradientStop Offset="1.0" Color="Green" />
            </LinearGradientBrush.GradientStops>
        </LinearGradientBrush>
    </Rectangle.Fill>
</Rectangle>
```

另外，有一些属性不但是集合属性，同时还是内容属性。前面示例中以及许多其他属性中使用的 `GradientStops` 属性就是这种情况，在这些语法中，也可以省略属性元素，如下所示：

```xml
<Rectangle Width="200" Height="150">
	<Rectangle.Fill>
    	<LinearGradientBrush>
        	<GradientStop Offset="0.0" Color="Coral" />
            <GradientStop Offset="1.0" Color="Green" />
        </LinearGradientBrush>
    </Rectangle.Fill>
</Rectangle>
```

集合属性语法最常见于布局控件中，例如 `Grid`、`StackPanel` 等布局控件的属性设置。下面的示例演示 `StackPanel` 面板的属性设置，分别由显示属性设置和最简洁的属性设置。

显示的 `StackPanel` 属性设置：

```xml
<StackPanel>
	<StackPanel.Children>
    	<TextBlock>Hello</TextBlock>
        <TextBlock>World</TextBlock>
    </StackPanel.Children>
</StackPanel>
```

最简洁的 `StackPanel` 的属性设置：

```xml
<StackPanel>
	<TextBlock>Hello</TextBlock>
    <TextBlock>World</TextBlock>
</StackPanel>
```

### 3. 附加属性

附加属性是一种特定类型的属性，和普通属性的作用并不一样。这种属性的特殊之处在于，其属性值受到 `XAML` 中专用属性系统的跟踪和影响。附加属性可用于多个控件，但却在另一个类中定义。在 `Windows 10 中，附加属性常用于控件布局。

下面来看一下一个附加属性使用的示例，如下所示：

```xml
<Canvas>
	<Button Canvas.Left="50">Hello</Button>
</Canvas>
```

上面使用了附加属性 `Canvas.Left="50"` 表示按钮放置在距离 `Canvas` 面板左边 50 像素的位置。当然如果对象元素并不在 `Canvas` 面板里面，设置 `Canvas.Left` 附加属性不好产生任何的影响。

### 4. 标记扩展

常用的 `XAML` 标记扩展功能包括以下 5 种：

+ `Binding`（绑定）标记扩展，实现在 `XAML` 载入时，将数据绑定到 `XAML` 对象；
+ `StaticResource`（静态资源）标记扩展，实现引用数据字典（ResourceDictionary）中定义的静态资源；
+ `ThemeResource`（主题资源）标记扩展，表示系统内置的静态资源；
+ `TemplateBinding`（模板绑定）标记扩展，实现在 XAML 页面中，对象模板绑定调用。
+ `RelativeSource`（绑定关联源）标记扩展，实现对特定数据源的绑定；

在语法上，`XAML` 使用大括号 `{}` 来表示扩展。例如，下面这句 `XAML`：

```xml
<TextBlock Text="{Binding Source={StaticResource myDataSource}, Path=PersonName}" />
```

这里有两处使用了 `XAML` 扩展，一处是 `Binding`，另一处是 `StaticResources`，这种用法又称为嵌套扩展，`TextBlock` 元素的 `Text` 属性的值为 `{}` 中的结果。当 `XAML` 编译器看到大括号 `{}` 时，把大括号中的内容解释为 `XAML` 标记扩展。

`XAML` 本身也定义了一些内置的标记扩展，这类扩展包括：`x:Type`、`x:Static`、`x:null` 和 `x:Array`。`x:null` 是一种最简单的扩展，其作用就是把目标属性设置为 `null`。`x:Type` 在 `XAML` 中取对象的类型，相当于 `C#` 中的 `typeof` 操作，这种操作发生在编译的时候。`x:Static` 是用来把某个对象中的属性或域的值赋给目标对象的相关属性。`x:Array` 表示一个 `.NET` 数组，`x:Array` 元素的子元素都是数组元素，它必须与 `x:Type` 一起使用，用于定义数组类型。使用 `x:null` 扩展标记把 `TextBlock` 的 `Background` 属性设置为 `null`，如下所示：

```xml
<TextBlock Text="你好" Background="{x:null}" />
```

#### 5. 事件

事件在 `XAML` 中基础语法如下：

```xml
<元素对象 事件名称="事件处理" />
```

例如，使用按钮控件的 `Click` 事件，响应按钮点击效果，代码如下：

```xml
<Button Content="按钮" Click="Button_Click" />
```

其中，`Button_Click` 连接后台代码中的同名事件处理程序：

```csharp
Private void Button_Click(object sender, RoutedEventArgs e) {
    // 在这里可以添加事件处理的逻辑程序
}
```

