如果需要再字符串输出中显示反斜杠，则可以使用两个反斜杠 `\\` 进行转义。如果需要多次用到反斜杠，这种写法令人厌烦，因为它们可能降低代码的可读性。对于这种场景，例如在使用正则表达式的时候，就可以使用 `verbatim` 字符串。`verbatim` 字符串带有 `@` 前缀：

```c#
string s = @"a tab: \t, a carriage return: \r, a newline: \n";
Console.WriteLine(s);
```

运行结果如下：

```
a tab: \t, a carriage return: \r, a newline: \n
```

