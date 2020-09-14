学习 Swift 最好的工具是：playground（游乐园）。首先，让我们创建一个新的 playground。启动 Xcode 并在菜单栏中打开 `File -> New -> Playground...` 选项。在打开的对话框中，为你的 playground 命名（如 SwiftBasics），并确保 Platform 是 iOS，然后按下 Next。选择你要保存的文件路径，然后按下 Create。

任何在 // 后且在回车符前的字符都会被编译器忽略。

```swift
var str = "Hello, playground"	// 这一行是我的注释
```

如果要编写超过一行的注释，可以将 /* 用作开头，*/ 用作结尾。

```swift
/*
 这是一段超过一行
 的注释
 */
```

有各种不同的方式来写一个多行注释。有些人喜欢表达清晰，每行的注释由一个 * 字符开始：

```swift
/*
 * 这是一段超过一行
 * 的注释
 */
```

`var` 关键字声明具有给定名称的新变量。

如果选择不提供初始化，那么必须将变量类型添加在变量名后，用冒号隔开：

```swift
var str2: String	// 一个未初始化的变量
```

在大多数情况下，最好将声明和初始化结合起来，并允许编译器来推断变量的类型。

```swift
var count = 2
```

输入以上代码到 playground，将鼠标悬停在 count 上，并按下 <kbd>Option</kbd> 键，鼠标光标将变为一个问号标记。现在点击鼠标，Swift 会在弹出框里显示推断此变量的类型。

与 JavaScript 这样的动态语言不同，你不能简单地通过指定一个新值改变一个变量的类型。请试着这样做：

```swift
var count = 2
count = "Two"
```

Swift 语言几乎没有必要以分号作为声明的结尾。当然，你可以输入分号，但很可能之后就不会再这样做了。只有一种情况下必须使用分号，即必须在同一行内写 2 个语句。下面的代码是无效的：

```swift
var count = 2 count = 3
```

添加一个分号，编译器会很顺利地再次执行：

```swift
var count = 2; count = 3
```

Swift 提供了 let 语句来创建一个常量，语法上，let 类似于 var，但你必须提供一个初始值：

```swift
let pi = 3.14159265
```

当然，你可以使用常量来为变量初始化：

```swift
let pi = 3.14159265
var value = pi
```

你可以调用 Swift 标准库的 print() 函数来创建输出结果。比如下面这个：

```swift
print("Hello, world")
```

如果你不希望字符串后面自动添加一个换行符，可以选择去除或者将其替换成另一个字符串，办法是使用稍微有些区别的另一种 print() 函数，它会获取一个额外的参数。试试下面的代码：

```swift
print("Hello, world", terminator: "")
```

这段代码使用一个空字符替换了换行符。

> print() 是 Swift 的标准库中的一个函数。可以在 <https://developer.apple.com/library/ios/documentation/General/Reference/SwiftStandardLibraryReference> 找到库的文档。另一种查看标准库内容的方法是在 playground 中添加 import Swift 语句，然后按住 <kbd>Command</kbd> 键并点击 Swift 文字。 Playground 会切换到一个包含标准库内容的列表。这里有非常多的信息，你需要更多地掌握 Swift 才能够全部理解，不过可以简单浏览了解存在哪些内容。