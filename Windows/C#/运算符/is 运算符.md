`C#` 支持一种名为 `模式匹配` 的特性，可以通过 `if` 语句和 `is` 运算符使用这种特性：

```c#
void PatternMatching(object o) 
{
    if (o is null) 
    {
        throw new ArgumentNullException(nameof(o));
    } else {
        Console.WriteLine($"received a book: {b.Title}");
    }
}
```

> 注意：本例在抛出 `ArgumentNullException` 的时候使用了 `nameof` 表达式。编译器将把 `nameof` 表达式解析为其实参的名称（如变量 `o`），然后将结果作为一个字符串进行传递。`throw new ArgumentNullException(nameof(o));` 解析得到的代码与 `throw new ArgumentNullException("o");` 相同。

下面的代码片段显示了常量模型和类型模式的更多例子：

```c#
if (o is 42)	// const pattern
if (o is "42")	// const pattern
if (o is int i)	// type pattern
```

> 注意：可以在 `is` 运算符、`switch` 语句与 `switch` 表达式中使用模式匹配。