#### 11.2.2　不幸的 `gets()` 函数

在读取字符串时， `scanf()` 和转换说明 `%s` 只能读取一个单词。可是在程序中经常要读取一整行输入，而不仅仅是一个单词。许多年前， `gets()` 函数就用于处理这种情况。 `gets()` 函数简单易用，它读取整行输入，直至遇到换行符，然后丢弃换行符，存储其余字符，并在这些字符的末尾添加一个空字符使其成为一个C字符串。它经常和 `puts()` 函数配对使用，该函数用于显示字符串，并在末尾添加换行符。程序清单11.6中演示了这两个函数的用法。

程序清单11.6　 `getsputs.c` 程序

```c
/*  getsputs.c  -- 使用 gets() 和 puts() */
#include <stdio.h>
#define STLEN 81
int main(void)
{
     char words[STLEN];
     puts("Enter a string, please.");
     gets(words);  // 典型用法
     printf("Your string twice:\n");
     printf("%s\n", words);
     puts(words);
     puts("Done.");
     return 0;
}
```

下面是该程序在某些编译器（或者至少是旧式编译器）中的运行示例：

```c
Enter a string, please.
I want to learn about string theory!
Your string twice:
I want to learn about string theory!
I want to learn about string theory!
Done.

```

整行输入（除了换行符）都被存储在 `words` 中， `puts(words)` 和 `printf("%s\n", words)` 的效果相同。

下面是该程序在另一个编译器中的输出示例：

```c
Enter a string, please.
warning: this program uses gets(), which is unsafe.
Oh, no!
Your string twice:
Oh, no!
Oh, no!
Done.

```

编译器在输出中插入了一行警告消息。每次运行这个程序，都会显示这行消息。但是，并非所有的编译器都会这样做。其他编译器可能在编译过程中给出警告，但不会引起你的注意。

这是怎么回事？问题出在 `gets()` 唯一的参数是 `words` ，它无法检查数组是否装得下输入行。上一章介绍过，数组名会被转换成该数组首元素的地址，因此， `gets()` 函数只知道数组的开始处，并不知道数组中有多少个元素。

如果输入的字符串过长，会导致缓冲区溢出（buffer overflow），即多余的字符超出了指定的目标空间。如果这些多余的字符只是占用了尚未使用的内存，就不会立即出现问题；如果它们擦写掉程序中的其他数据，会导致程序异常中止；或者还有其他情况。为了让输入的字符串容易溢出，把程序中的 `STLEN` 设置为 `5` ，程序的输出如下：

```c
Enter a string, please.
warning: this program uses gets(), which is unsafe.
I think I'll be just fine.
Your string twice:
I think I'll be just fine.
I think I'll be just fine.
Done.
Segmentation fault: 11

```

“ `Segmentation fault` ”（分段错误）似乎不是个好提示，的确如此。在UNIX系统中，这条消息说明该程序试图访问未分配的内存。

C提供解决某些编程问题的方法可能会导致陷入另一个尴尬棘手的困境。但是，为什么要特别提到 `gets()` 函数？因为该函数的不安全行为造成了安全隐患。过去，有些人通过系统编程，利用 `gets()` 插入和运行一些破坏系统安全的代码。

不久，C编程社区的许多人都建议在编程时摒弃 `gets()` 。制定C99标准的委员会把这些建议放入了标准，承认了 `gets()` 的问题并建议不要再使用它。尽管如此，在标准中保留 `gets()` 也合情合理，因为现有程序中含有大量使用该函数的代码。而且，只要使用得当，它的确是一个很方便的函数。

好景不长，C11标准委员会采取了更强硬的态度，直接从标准中废除了 `gets()` 函数。既然标准已经发布，那么编译器就必须根据标准来调整支持什么，不支持什么。然而在实际应用中，编译器为了能兼容以前的代码，大部分都继续支持 `gets()` 函数。不过，我们使用的编译器，可没那么大方。

