`scanf` 系列函数的作用是从一个文件流里读取数据，并把数据值放到以指针参数形式传递过来的地址处的变量中。它们也使用一个格式字符串来控制输入数据的转换，它们使用的许多转换控制符都与 `printf` 系列函数一样。

它们的原型如下所示：

```c
#include <stdio.h>

int scanf(const char *format, ...);
int fscanf(FILE *stream, const char *format, ...);
int sscanf(const char *s, const char *format, ...);
```

`scanf` 函数读入的值将保存在对应的变量里，这些变量的类型必须正确，并且它们必须精确匹配格式字符串。否则，内存数据就可能会遭到破坏，从而使程序崩溃。例如：

```c
int num;
scanf("Hello %d", &num);
```

这个 `scanf` 调用只有在标准输入中接下来的五个字符匹配 "Hello" 的情况下才会成功。然后，如果后面的字符构成了一个可识别的十进制数字，该数字就将被读入并赋值给变量 num。格式字符串中的空格用于忽略输入数据中位于转换控制符之间的各种空白字符（空格、制表符、换页符合换行符）。这意味着在下面两种输入情况下，这个 `scanf` 调用都会执行成功，并把 1234 放到变量 num 里：

```
Hello   1234
Hello1234
```

> 注意：如果用户在输入中应该出现一个整数的地方放的是一个非数字字符，就可能在程序里导致一个无限循环。

下面是一些转换控制符：

+ `%d`：读取一个十进制整数。
+ `%o`、`%x`：读取一个八进制或十六进制整数。
+ `%f`、`%e`、`%g`：读取一个浮点数。
+ `%c` ：读取一个字符（不会忽略空格）。
+ `%s` ：读取一个字符串。
+ `%[]`：读取一个字符集合。
+ `%%`：读取一个 % 字符。

`scanf` 的转换控制符里也可以加上对输入数据字段宽度的限制。长度限定符（h 对应于短，`l` 对应于长）指明接收参数的长度是否比默认情况更短或更长。这意味着，`%hd` 表示要读入一个短整数，`%ld` 表示要读入一个长整数，而 `%lg` 表示要读入一个双精度浮点数。

以星号（`*`）开头的控制符表示对应位置上的输入数据将被忽略。这意味着，这个数据不会被保存，因此不需要使用一个变量来接收它。

我们使用 `%c` 控制符从输入中读取一个字符。它不会跳过起始的空白字符。

我们使用 `%s` 控制符来扫描字符串，但使用时必须小心。它会跳过起始的空白符，并且会在字符串里出现的第一个空白符处停下来，所以你最好用它来读取单词而不是一般意义上的字符串。此外，如果没有使用字段宽度限定符，它能够读取的字符串的长度是没有限制的，所以接收字符串必须有足够的空间来容纳输入流中可能的最长字符串。较好的选择是使用一个字段限定符，或者结合使用 `fgets` 和 `sscanf` 从输入中读入一行数据，再对它进行扫描。这样可以避免可能被恶意用户利用的缓冲区溢出。

我们使用 `%[]` 控制符读取由一个字符集合中的字符构成的字符串。格式字符串`%[A-Z]` 将读取一个由大写字母构成的字符串。如果字符集中的第一个字符是 `^`，就表示将读取一个由不属于该字符集合中的字符构成的字符串。因此，读取一个其中带空格的字符串，并且在遇到第一个逗号时停止，你可以用 `%[^,]`。

给定下面输入行：

```
Hello, 1234, 5.678, X, string to the end of the line
```

下面的 `scanf` 调用会正确读入 4 个数据项：

```c
char s[256];
int n;
float f;
char c;

scanf("Hello, %d, %g, %c, %[^\n]", &n, &f, &c, s)
```

`scanf` 函数的返回值是它成功读取的数据项个数，如果再读第一个数据项时失败了，它的返回值就将是零。如果再匹配第一个数据项之前就已经到达了输入的结尾，它就返回 EOF。如果文件流发生读错误，流错误标志就会被设置并且错误变量 errno 将被设置以指明错误类型。

一般来说，scanf 系列函数有下面 3 个问题：

+ 从历史来看，它们的具体实现都有漏洞。
+ 它们的使用不够灵活。
+ 使用它们编写的代码不容易看出究竟正在解析什么。