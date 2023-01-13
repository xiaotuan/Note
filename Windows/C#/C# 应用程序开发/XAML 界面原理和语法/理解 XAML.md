`XAML` 文件中的每个元素代表 `.NET` 中的一个类，并且 `XAML` 文件中的每个属性代表 `.NET` 类中的一个属性、方法或事件。例如，若要在 Windows 10 的界面上创建一个按钮，可以用下面的 `XAML` 代码来实现：

```xml
<Button x:Name="button 1" BorderThickness="1" Click="OnClick1" Content="按钮" />
```

上面的 `XAML` 代码中的按钮 `Button` 实际上是 Windows 10 中的 `Windows.UI.Xaml.Controls.Button` 类。`XAML` 的属性是相应类中的相关属性，如上例中的 `Name`、`BorderThickness` 实际上是 `Button` 类中相应的相关属性。在这句 `XAML` 语句中，还实现了事件处理程序，`Click="OnClick1"`，即 `XAML` 支持声明事件处理程序，具体逻辑在其对应的 `.xaml.cs` 的后台代码文件的 `OnClick1` 方法中。`XAML` 文件可以映射到一个扩展名为 `.xaml.cs` 的后台代码文件。

编写 `XAML` 代码时需要注意，声明一个 `XAML` 元素时，可以用 `Name` 属性为该元素指定一个名称，这样在 `C#` 代码里面才可以访问到此元素。

下面是声明一个 `XAML` 编程必须遵循的 4 大原则：

+ `XAML` 是大小写区分的，元素和属性的名称必须严格区分大小写，例如对于 `Button` 元素来说，其在 `XAML` 中的声明应该为 `<Button>`，而不是 `<button>`；
+ 所有的属性值，无论它是什么数据类型，都必须包含在双引号中；
+ 所有的元素都必须是封闭的，例如 `<Button.../>`，或者是有一个起始标记和一个结束标记，例如 `<Button>...</Button>`；
+ 最终的 `XAML` 文件也必须是合适的 XML 文档。