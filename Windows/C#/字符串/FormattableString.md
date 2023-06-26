把字符串赋值给 `FormattableString`，就很容易看到插值字符串被翻译成什么。可以把插值字符串直接赋值给这种类型，因为它比正常的字符串更适合这种类型。该类型定义了 `Format` 属性（返回得到的格式字符串）、`ArguumentCount` 属性和方法 `GetArgument()` （返回实参值）：

```c#
using System;

UsingFormattableString();

void UsingFormattableString()
{
    int x = 3, y = 4;
    FormattableString s = $"The result of {x} + {y} is {x + y}";
    Console.WriteLine($"format: {s.Format}");
    for (int i = 0; i < s.ArgumentCount; i++)
    {
        Console.WriteLine($"argument: {i}:{s.GetArgument(i)}");
    }
    Console.WriteLine();
}
```

运行结果如下：

```
format: The result of {0} + {1} is {2}
argument: 0:3
argument: 1:4
argument: 2:7
```

