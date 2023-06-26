`C#` 还有一个非常出色的功能：根据特定的注释自动创建 `XML` 格式的文档说明。这些注释都是单行注释，但都以 3 条斜杠（`//`）开头，而不是通常的两条斜杠。在这些注释中，可以把包含类型和类型成员的文档说明的 `XML` 标记放在代码中。

| 标记             | 说明                                              |
| ---------------- | ------------------------------------------------- |
| `<c>`            | 把行中的文本标记为代码，例如 `<c>int i = 10;</c>` |
| `<code>`         | 把多行标记为代码                                  |
| `<example>`      | 标记一个代码示例                                  |
| `<exception>`    | 说明一个异常类（编译器要验证其语法）              |
| `<include>`      | 包含其他文档说明文件的注释（编译器要验证其语法）  |
| `<list>`         | 把列表插入文档中                                  |
| `<para>`         | 建立文本的结构                                    |
| `<param>`        | 标记方法的参数（编译器要验证其语法）              |
| `<paramref>`     | 表明一个单词是方法的参数（编译器要验证其语法）    |
| `<permission>`   | 说明对成员的访问（编译器要验证其语法）            |
| `<remarks>`      | 给成员添加描述                                    |
| `<returns>`      | 说明方法的返回值                                  |
| `<see>`          | 提供对另一个参数的交叉引用（编译器要验证其语法）  |
| `<seealso>`      | 提供描述中的 “参见” 部分（编译器要验证其语法）    |
| `<summary>`      | 提供类型或成员的简短小结                          |
| `<typeparam>`    | 用在泛型类型的注释中，以说明一个类型参数          |
| `<typeparamref>` | 类型参数的名称                                    |
| `<value>`        | 描述属性                                          |

下面的代码片段显示了 `Calculator` 类，并为该类和 `Add()` 方法指定了文档说明：

```C#
using System;

namespace ProCSharp.MathLib
{
    ///<summary>
    /// ProCsharp.MathLib.Calculator class.
    /// Provides a method to add two doubles.
    ///</summary>
    public static class Calculator
    {
        ///<summary>
        /// The Add method allows us to add two doubles.
        /// </summary>
        /// <returns>Result of the addition (double)</returns>
        /// <param name="x">First number to add</param>
        /// <param name="y">Second number to add</param>
        public static double Add(double x, double y) => x + y;
    }
}
```

要生成 `XML` 文档，可以在项目文件中添加 `GenerateDocumentationFile`：

```xml
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net7.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
	<GenerateDocumentationFile>true</GenerateDocumentationFile>
  </PropertyGroup>

</Project>
```

添加了这个设置后，将在程序的二进制文件所在的目录中生成文档文件。也可以指定 `DocumentationFile` 元素，定义一个与项目文件不同的名称，还可以指定在一个绝对目录中生成文档文件。