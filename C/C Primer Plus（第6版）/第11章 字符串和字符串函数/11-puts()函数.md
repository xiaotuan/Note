#### 11.3.1　 `puts()` 函数

`puts()` 函数很容易使用，只需把字符串的地址作为参数传递给它即可。程序清单11.12演示了 `puts()` 的一些用法。

程序清单11.12　 `put_out.c` 程序

```c
/* put_out.c -- 使用 puts() */
#include <stdio.h>
#define DEF "I am a #defined string."
int main(void)
{
     char str1[80] = "An array was initialized to me.";
     const char * str2 = "A pointer was initialized to me.";
     puts("I'm an argument to puts().");
     puts(DEF);
     puts(str1);
     puts(str2);
     puts(&str1[5]);
     puts(str2 + 4);
     return 0;
}
```

该程序的输出如下：

```c
I'm an argument to puts().
I am a #defined string.
An array was initialized to me.
A pointer was initialized to me.
ray was initialized to me.
inter was initialized to me.
```

如上所示，每个字符串独占一行，因为 `puts()` 在显示字符串时会自动在其末尾添加一个换行符。

该程序示例再次说明，用双引号括起来的内容是字符串常量，且被视为该字符串的地址。另外，存储字符串的数组名也被看作是地址。在第5个 `puts()` 调用中，表达式 `&str1[5]` 是 `str1` 数组的第6个元素（ `r` ）， `puts()` 从该元素开始输出。与此类似，第6个 `puts()` 调用中， `str2+4` 指向存储 `"pointer"` 中 `i` 的存储单元， `puts()` 从这里开始输出。

`puts()` 如何知道在何处停止？该函数在遇到空字符时就停止输出，所以必须确保有空字符。不要模仿程序清单11.13中的程序！

程序清单11.13　 `nono.c` 程序

```c
/* nono.c -- 千万不要模仿！ */
#include <stdio.h>
int main(void)
{
     char side_a[] = "Side A";
     char dont[] = { 'W', 'O', 'W', '!' };
     char side_b[] = "Side B";
     puts(dont); /* dont 不是一个字符串 */
     return 0;
}
```

由于 `dont` 缺少一个表示结束的空字符，所以它不是一个字符串，因此 `puts()` 不知道在何处停止。它会一直打印 `dont` 后面内存中的内容，直到发现一个空字符为止。为了让 `puts()` 能尽快读到空字符，我们把 `dont` 放在 `side_a` 和 `side_b` 之间。下面是该程序的一个运行示例：

```c
WOW!Side A
```

我们使用的编译器把 `side_a` 数组存储在 `dont` 数组之后，所以 `puts()` 一直输出至遇到 `side_a` 中的空字符。你所使用的编译器输出的内容可能不同，这取决于编译器如何在内存中存储数据。如果删除程序中的 `side_a` 和 `side_b` 数组会怎样？通常内存中有许多空字符，如果幸运的话， `puts()` 很快就会发现一个。但是，这样做很不靠谱。

