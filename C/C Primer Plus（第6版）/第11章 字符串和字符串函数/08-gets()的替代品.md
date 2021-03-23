#### 11.2.3　 `gets()` 的替代品

过去通常用 `fgets()` 来代替 `gets()` ， `fgets()` 函数稍微复杂些，在处理输入方面与 `gets()` 略有不同。C11标准新增的 `gets_s()` 函数也可代替 `gets()` 。该函数与 `gets()` 函数更接近，而且可以替换现有代码中的 `gets()` 。但是，它是 `stdio.h` 输入/输出函数系列中的可选扩展，所以支持C11的编译器也不一定支持它。

#### 1． `fgets()` 函数（和 `fputs()` ）

`fgets()` 函数通过第2个参数限制读入的字符数来解决溢出的问题。该函数专门设计用于处理文件输入，所以一般情况下可能不太好用。 `fgets()` 和 `gets()` 的区别如下。

+ `fgets()` 函数的第2个参数指明了读入字符的最大数量。如果该参数的值是 `n` ，那么 `fgets()` 将读入 `n-1` 个字符，或者读到遇到的第一个换行符为止。
+ 如果 `fgets()` 读到一个换行符，会把它存储在字符串中。这点与 `gets()` 不同， `gets()` 会丢弃换行符。
+ `fgets()` 函数的第3个参数指明要读入的文件。如果读入从键盘输入的数据，则以 `stdin` （标准输入）作为参数，该标识符定义在 `stdio.h` 中。

因为 `fgets()` 函数把换行符放在字符串的末尾（假设输入行不溢出），通常要与 `fputs()` 函数（和 `puts()` 类似）配对使用，除非该函数不在字符串末尾添加换行符。 `fputs()` 函数的第2个参数指明它要写入的文件。如果要显示在计算机显示器上，应使用 `stdout` （标准输出）作为该参数。程序清单11.7演示了 `fgets()` 和 `fputs()` 函数的用法。

程序清单11.7　 `fgets1.c` 程序

```c
/*  fgets1.c  -- 使用 fgets() 和 fputs() */
#include <stdio.h>
#define STLEN 14
int main(void)
{
     char words[STLEN];
     puts("Enter a string, please.");
     fgets(words, STLEN, stdin);
     printf("Your string twice (puts(), then fputs()):\n");
     puts(words);
     fputs(words, stdout);
     puts("Enter another string, please.");
     fgets(words, STLEN, stdin);
     printf("Your string twice (puts(), then fputs()):\n");
     puts(words);
     fputs(words, stdout);
     puts("Done.");
     return 0;
}
```

下面是该程序的输出示例：

```c
Enter a string, please.
apple pie
Your string twice (puts(), then fputs()):
apple pie
apple pie
Enter another string, please.
strawberry shortcake
Your string twice (puts(), then fputs()):
strawberry sh
strawberry shDone.

```

第1行输入， `apple pie` ，比 `fgets()` 读入的整行输入短，因此， `apple pie\n\0` 被存储在数组中。所以当 `puts()` 显示该字符串时又在末尾添加了换行符，因此 `apple pie` 后面有一行空行。因为 `fputs()` 不在字符串末尾添加换行符，所以并未打印出空行。

第2行输入， `strawberry shortcake` ，超过了大小的限制，所以 `fgets()` 只读入了13个字符，并把 `strawberry sh\0` 存储在数组中。再次提醒读者注意， `puts()` 函数会在待输出字符串末尾添加一个换行符，而 `fputs()` 不会这样做。

`fgets()` 函数返回指向 `char` 的指针。如果一切进行顺利，该函数返回的地址与传入的第1个参数相同。但是，如果函数读到文件结尾，它将返回一个特殊的指针：空指针（null pointer）。该指针保证不会指向有效的数据，所以可用于标识这种特殊情况。在代码中，可以用数字 `0` 来代替，不过在C语言中用宏 `NULL` 来代替更常见（如果在读入数据时出现某些错误，该函数也返回 `NULL` ）。程序清单11.8演示了一个简单的循环，读入并显示用户输入的内容，直到 `fgets()` 读到文件结尾或空行（即，首字符是换行符）。

程序清单11.8　 `fgets2.c` 程序

```c
/*  fgets2.c  -- 使用 fgets() 和 fputs() */
#include <stdio.h>
#define STLEN 10
int main(void)
{
     char words[STLEN];
     puts("Enter strings (empty line to quit):");
     while (fgets(words, STLEN, stdin) != NULL && words[0] != '\n')
          fputs(words, stdout);
     puts("Done.");
     return 0;
}
```

下面是该程序的输出示例：

```c
Enter strings (empty line to quit):
By the way, the gets() function
By the way, the gets() function
also returns a null pointer if it
also returns a null pointer if it
encounters end-of-file.
encounters end-of-file.
Done.

```

有意思，虽然 `STLEN` 被设置为 `10` ，但是该程序似乎在处理过长的输入时完全没问题。程序中的 `fgets()` 一次读入 `STLEN - 1` 个字符（该例中为9个字符）。所以，一开始它只读入了“ `By the wa` ”，并存储为 `By the wa\0` ；接着 `fputs()` 打印该字符串，而且并未换行。然后 `while` 循环进入下一轮迭代， `fgets()` 继续从剩余的输入中读入数据，即读入“ `y, the ge` ”并存储为 `y, the ge\0` ；接着 `fputs()` 在刚才打印字符串的这一行接着打印第2次读入的字符串。然后 `while` 进入下一轮迭代， `fgets()` 继续读取输入、 `fputs()` 打印字符串，这一过程循环进行，直到读入最后的“ `tion\n` ”。 `fgets()` 将其存储为 `tion\n\0` ， `fputs()` 打印该字符串，由于字符串中的 `\n` ，光标被移至下一行开始处。

系统使用缓冲的I/O。这意味着用户在按下Return键之前，输入都被存储在临时存储区（即，缓冲区）中。按下Return键就在输入中增加了一个换行符，并把整行输入发送给 `fgets()` 。对于输出， `fputs()` 把字符发送给另一个缓冲区，当发送换行符时，缓冲区中的内容被发送至屏幕上。

`fgets()` 存储换行符有好处也有坏处。坏处是你可能并不想把换行符存储在字符串中，这样的换行符会带来一些麻烦。好处是对于存储的字符串而言，检查末尾是否有换行符可以判断是否读取了一整行。如果不是一整行，要妥善处理一行中剩下的字符。

首先，如何处理掉换行符？一个方法是在已存储的字符串中查找换行符，并将其替换成空字符：

```c
while (words[i] != '\n') // 假设\n在words中
     i++;
words[i] = '\0';
```

其次，如果仍有字符串留在输入行怎么办？一个可行的办法是，如果目标数组装不下一整行输入，就丢弃那些多出的字符：

```c
while (getchar() != '\n')    // 读取但不存储输入，包括\n
     continue;
```

程序清单11.9在程序清单11.8的基础上添加了一部分测试代码。该程序读取输入行，删除存储在字符串中的换行符，如果没有换行符，则丢弃数组装不下的字符。

程序清单11.9　 `fgets3.c` 程序

```c
/*  fgets3.c  -- 使用 fgets() */
#include <stdio.h>
#define STLEN 10
int main(void)
{
     char words[STLEN];
     int i;
     puts("Enter strings (empty line to quit):");
     while (fgets(words, STLEN, stdin) != NULL && words[0] != '\n')
     {
          i = 0;
          while (words[i] != '\n' && words[i] != '\0')
               i++;
          if (words[i] == '\n')
               words[i] = '\0';
          else    // 如果word[i] == '\0'则执行这部分代码
               while (getchar() != '\n')
                     continue;
          puts(words);
     }
     puts("done");
     return 0;
}
```

循环

```c
while (words[i] != '\n' && words[i] != '\0')
     i++;
```

遍历字符串，直至遇到换行符或空字符。如果先遇到换行符，下面的 `if` 语句就将其替换成空字符；如果先遇到空字符， `else` 部分便丢弃输入行的剩余字符。下面是该程序的输出示例：

```c
Enter strings (empty line to quit):
This
This
program seems
program s
unwilling to accept long lines.
unwilling
But it doesn't get stuck on long
But it do
lines either.
lines eit
done

```



**空字符和空指针**

程序清单11.9中出现了空字符和空指针。从概念上看，两者完全不同。空字符（或'\0'）是用于标记C字符串末尾的字符，其对应字符编码是0。由于其他字符的编码不可能是0，所以不可能是字符串的一部分。

空指针（或 `NULL` ）有一个值，该值不会与任何数据的有效地址对应。通常，函数使用它返回一个有效地址表示某些特殊情况发生，例如遇到文件结尾或未能按预期执行。

空字符是整数类型，而空指针是指针类型。两者有时容易混淆的原因是：它们都可以用数值0来表示。但是，从概念上看，两者是不同类型的 `0` 。另外，空字符是一个字符，占 `1` 字节；而空指针是一个地址，通常占 `4` 字节。



#### 2． `gets_s()` 函数

C11新增的 `gets_s()` 函数（可选）和 `fgets()` 类似，用一个参数限制读入的字符数。假设把程序清单11.9中的 `fgets()` 换成 `gets_s()` ，其他内容不变，那么下面的代码将把一行输入中的前9个字符读入 `words` 数组中，假设末尾有换行符：

`gets_s(words, STLEN);`

`gets_s()` 与 `fgets()` 的区别如下。

+ `gets_s()` 只从标准输入中读取数据，所以不需要第3个参数。
+ 如果 `gets_s()` 读到换行符，会丢弃它而不是存储它。
+ 如果 `gets_s()` 读到最大字符数都没有读到换行符，会执行以下几步。首先把目标数组中的首字符设置为空字符，读取并丢弃随后的输入直至读到换行符或文件结尾，然后返回空指针。接着，调用依赖实现的“处理函数”（或你选择的其他函数），可能会中止或退出程序。

第2个特性说明，只要输入行未超过最大字符数， `gets_s()` 和 `gets()` 几乎一样，完全可以用 `gets_s()` 替换 `gets()` 。第3个特性说明，要使用这个函数还需要进一步学习。

我们来比较一下 `gets()` 、 `fgets()` 和 `gets_s()` 的适用性。如果目标存储区装得下输入行，3个函数都没问题。但是 `fgets()` 会保留输入末尾的换行符作为字符串的一部分，要编写额外的代码将其替换成空字符。

如果输入行太长会怎样？使用 `gets()` 不安全，它会擦写现有数据，存在安全隐患。 `gets_s()` 函数很安全，但是，如果并不希望程序中止或退出，就要知道如何编写特殊的“处理函数”。另外，如果打算让程序继续运行， `gets_s()` 会丢弃该输入行的其余字符，无论你是否需要。由此可见，当输入太长，超过数组可容纳的字符数时， `fgets()` 函数最容易使用，而且可以选择不同的处理方式。如果要让程序继续使用输入行中超出的字符，可以参考程序清单11.8中的处理方法。如果想丢弃输入行的超出字符，可以参考程序清单11.9中的处理方法。

所以，当输入与预期不符时， `gets_s()` 完全没有 `fgets()` 函数方便、灵活。也许这也是 `gets_s()` 只作为C库的可选扩展的原因之一。鉴于此， `fgets()` 通常是处理类似情况的最佳选择。

#### 3． `s_gets()` 函数

程序清单11.9演示了 `fgets()` 函数的一种用法：读取整行输入并用空字符代替换行符，或者读取一部分输入，并丢弃其余部分。既然没有处理这种情况的标准函数，我们就创建一个，在后面的程序中会用得上。程序清单11.10提供了一个这样的函数。

程序清单11.10　 `s_gets()` 函数

```c
char * s_gets(char * st, int n)
{
     char * ret_val;
     int i = 0;
     ret_val = fgets(st, n, stdin);
     if (ret_val)    // 即，ret_val != NULL
     {
          while (st[i] != '\n' && st[i] != '\0')
               i++;
          if (st[i] == '\n')
               st[i] = '\0';
          else<ins>
</ins>               while (getchar() != '\n')
                     continue;
     }
     return ret_val;
}
```

如果 `fgets()` 返回 `NULL` ，说明读到文件结尾或出现读取错误， `s_gets()` 函数跳过了这个过程。它模仿程序清单11.9的处理方法，如果字符串中出现换行符，就用空字符替换它；如果字符串中出现空字符，就丢弃该输入行的其余字符，然后返回与 `fgets()` 相同的值。我们在后面的示例中将讨论 `fgets()` 函数。

也许读者想了解为什么要丢弃过长输入行中的余下字符。这是因为，输入行中多出来的字符会被留在缓冲区中，成为下一次读取语句的输入。例如，如果下一条读取语句要读取的是 `double` 类型的值，就可能导致程序崩溃。丢弃输入行余下的字符保证了读取语句与键盘输入同步。

我们设计的 `s_gets()` 函数并不完美，它最严重的缺陷是遇到不合适的输入时毫无反应。它丢弃多余的字符时，既不通知程序也不告知用户。但是，用来替换前面程序示例中的 `gets()` 足够了。

