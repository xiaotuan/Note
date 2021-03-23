#### 8.4.1　UNIX、Linux和DOS重定向

UNIX（运行命令行模式时）、Linux（ditto）和Window命令行提示（模仿旧式DOS命令行环境）都能重定向输入、输出。重定向输入让程序使用文件而不是键盘来输入，重定向输出让程序输出至文件而不是屏幕。

#### 1．重定向输入

假设已经编译了 `echo_eof.c` 程序，并生成了一个名为 `echo_eof` （或者在Windows系统中名为 `echo_eof.exe` ）的可执行文件。运行该程序，输入可执行文件名：

```c
./echo_eof
```

该程序的运行情况和前面描述的一样，获取用户从键盘输入的输入。现在，假设你要用该程序处理名为 `words` 的文本文件。文本文件（text file）是内含文本的文件，其中存储的数据是我们可识别的字符。文件的内容可以是一篇散文或者C程序。内含机器语言指令的文件（如存储可执行程序的文件）不是文本文件。由于该程序的操作对象是字符，所以要使用文本文件。只需用下面的命令代替上面的命令即可：

```c
./echo_eof < words
```

`<` 符号是UNIX和DOS/Windows的重定向运算符。该运算符使 `words` 文件与 `stdin` 流相关联，把文件中的内容导入 `echo_eof` 程序。 `echo_eof` 程序本身并不知道（或不关心）输入的内容是来自文件还是键盘，它只知道这是需要导入的字符流，所以它读取这些内容并把字符逐个打印在屏幕上，直至读到文件结尾。因为C把文件和I/O设备放在一个层面，所以文件就是现在的I/O设备。试试看！

> **注意　重定向**
> 对于UNIX、Linux和Windows命令提示，<两侧的空格是可选的。一些系统，如AmigaDOS（那些喜欢怀旧的人使用的系统），支持重定向，但是在重定向符号和文件名之间不允许有空格。

下面是一个特殊的 `words` 文件的运行示例， `$` 是UNIX和Linux的标准提示符。在Windows/DOS系统中见到的DOS提示可能是 `A>` 或 `C>` 。

```c
$ echo_eof < words
The world is too much with us: late and soon,
Getting and spending, we lay waste our powers:
Little we see in Nature that is ours;
We have given our hearts away, a sordid boon!
$

```

#### 2．重定向输出

现在假设要用 `echo_eof` 把键盘输入的内容发送到名为 `mywords` 的文件中。然后，输入以下命令并开始输入：

```c
./echo_eof>mywords
```

`>` 符号是第2个重定向运算符。它创建了一个名为 `mywords` 的新文件，然后把 `echo_eof` 的输出（即，你输入字符的副本）重定向至该文件中。重定向把 `stdout` 从显示设备（即，显示器）赋给 `mywords` 文件。如果已经有一个名为 `mywords` 的文件，通常会擦除该文件的内容，然后替换新的内容（但是，许多操作系统有保护现有文件的选项，使其成为只读文件）。所有出现在屏幕的字母都是你刚才输入的，其副本存储在文件中。在下一行的开始处按下Ctrl+D（UNIX）或Ctrl+Z（DOS）即可结束该程序。如果不知道输入什么内容，可参照下面的示例。这里，我们使用UNIX提示符 `$` 。记住在每行的末尾单击Enter键，这样才能把缓冲区的内容发送给程序。

```c
$./echo_eof > mywords
You should have no problem recalling which redirection
operator does what. Just remember that each operator points
in the direction the information flows. Think of it as
a funnel.
[Ctrl+D]
$

```

按下Ctrl+D或Ctrl+Z后，程序会结束，你的系统会提示返回。程序是否起作用了？UNIX的 `ls` 命令或Windows命令行提示模式的 `dir` 命令可以列出文件名，会显示 `mywords` 文件已存在。可以使用UNIX或Linux的 `cat` 或DOS的 `type` 命令检查文件中的内容，或者再次使用 `echo_eof` ，这次把文件重定向到程序：

```c
$ echo_eof < mywords
You should have no problem recalling which redirection
operator does what. Just remember that each operator points
in the direction the information flows. Think of it as a
funnel.
$

```

#### 3．组合重定向

现在，假设你希望制作一份 `mywords` 文件的副本，并命名为 `savewords` 。只需输入以下命令即可：

```c
./echo_eof < mywords > savewords
```

下面的命令也起作用，因为命令与重定向运算符的顺序无关：

```c
./echo_eof > savewords < mywords
```

注意：在一条命令中，输入文件名和输出文件名不能相同。

```c
./echo_eof < mywords > mywords....<--错误
```

原因是 `> mywords` 在输入之前已导致原 `mywords` 的长度被截断为 `0` 。

总之，在UNIX、Linux或Windows/DOS系统中使用两个重定向运算符（ `<` 和 `>` ）时，要遵循以下原则。

+ 重定向运算符连接一个可执行程序（包括标准操作系统命令）和一个数据文件，不能用于连接一个数据文件和另一个数据文件，也不能用于连接一个程序和另一个程序。
+ 使用重定向运算符不能读取多个文件的输入，也不能把输出定向至多个文件。
+ 通常，文件名和运算符之间的空格不是必须的，除非是偶尔在UNIX shell、Linux shell或Windows命令行提示模式中使用的有特殊含义的字符。例如，我们用过的./ `echo_eof<words` 。

以上介绍的都是正确的例子，下面来看一下错误的例子， `addup` 和 `count` 是两个可执行程序， `fish` 和 `beets` 是两个文本文件：

```c
./fish > beets                ←违反第1条规则
./addup < count               ←违反第1条规则
./addup < fish < beets        ←违反第2条规则
./count > beets fish          ←违反第2条规则
```

UNIX、Linux或Windows/DOS还有>>运算符，该运算符可以把数据添加到现有文件的末尾，而 | 运算符能把一个文件的输出连接到另一个文件的输入。欲了解所有相关运算符的内容，请参阅UNIX的相关图书，如UNIX Primer Plus，Third Edition（Wilson、Pierce和Wessler合著）。

#### 4．注释

重定向让你能使用键盘输入程序文件。要完成这一任务，程序要测试文件的末尾。例如，第7章演示的统计单词程序（程序清单7.7），计算单词个数直至遇到第1个|字符。把 `ch` 的 `char` 类型改成 `int` 类型，把循环测试中的 `|` 替换成 `EOF` ，便可用该程序来计算文本文件中的单词量。

重定向是一个命令行概念，因为我们要在命令行输入特殊的符号发出指令。如果不使用命令行环境，也可以使用重定向。首先，一些集成开发环境提供了菜单选项，让用户指定重定向。其次，对于Windows系统，可以打开命令提示窗口，并在命令行运行可执行文件。Microsoft Visual Studio的默认设置是把可执行文件放在项目文件夹的子文件夹，称为Debug。文件名和项目名的基本名相同，文件名的扩展名为.exe。默认情况下，Xcode在给项目命名后才能命名可执行文件，并将其放在Debug文件夹中。在UNIX系统中，可以通过Terminal工具运行可执行文件。从使用上看，Terminal比命令行编译器（GCC或Clang）简单。

如果用不了重定向，可以用程序直接打开文件。程序清单8.3演示了一个注释较少的示例。我们学到第13章时再详细讲解。待读取的文件应该与可执行文件位于同一目录。

程序清单8.3　 `file_eof.c` 程序

```c
// file_eof.c --打开一个文件并显示该文件
#include <stdio.h>
#include <stdlib.h>            // 为了使用exit()
int main()
{
     int ch;
     FILE * fp;
     char fname[50];            // 存储文件名
     printf("Enter the name of the file: ");
     scanf("%s", fname);
     fp = fopen(fname, "r");    // 打开待读取文件
     if (fp == NULL)            // 如果失败
     {
          printf("Failed to open file. Bye\n");
          exit(1);              // 退出程序
     }
     // getc(fp)从打开的文件中获取一个字符
     while ((ch = getc(fp)) != EOF)
          putchar(ch);
     fclose(fp);                // 关闭文件
     return 0;
}
```



**小结：如何重定向输入和输出**

绝大部分C系统都可以使用重定向，可以通过操作系统重定向所有程序，或只在C编译器允许的情况下重定向C程序。假设 `prog` 是可执行程序名， `file1` 和 `file2` 是文件名。

**把输出重定向至文件：>**

```c
./prog >file1
```

**把输入重定向至文件：<**

```c
./prog <file2
```

**组合重定向：**

```c
./prog <file2 >file1
./prog >file1 <file2
```

这两种形式都是把file2作为输入、file1作为输出。

**留白：**

一些系统要求重定向运算符左侧有一个空格，右侧没有空格。而其他系统（如，UNIX）允许在重定位运算符两侧有空格或没有空格。



