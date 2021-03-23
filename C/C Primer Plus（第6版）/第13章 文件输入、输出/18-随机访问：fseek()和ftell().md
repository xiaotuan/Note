### 13.5　随机访问： `fseek()` 和 `ftell()` 

有了 `fseek()` 函数，便可把文件看作是数组，在 `fopen()` 打开的文件中直接移动到任意字节处。我们创建一个程序（程序清单13.4）演示 `fseek()` 和 `ftell()` 的用法。注意， `fseek()` 有3个参数，返回 `int` 类型的值； `ftell()` 函数返回一个 `long` 类型的值，表示文件中的当前位置。

程序清单13.4　 `reverse.c` 程序

```c
/* reverse.c -- 倒序显示文件的内容 */
#include <stdio.h>
#include <stdlib.h>
#define CNTL_Z '\032'        /* DOS文本文件中的文件结尾标记 */
#define SLEN 81
int main(void)
{
     char file[SLEN];
     char ch;
     FILE *fp;
     long count, last;
     puts("Enter the name of the file to be processed:");
     scanf("%80s", file);
     if ((fp = fopen(file, "rb")) == NULL)
     {                                    /* 只读模式    */
          printf("reverse can't open %s\n", file);
          exit(EXIT_FAILURE);
     }
     fseek(fp, 0L, SEEK_END);                /* 定位到文件末尾 */
     last = ftell(fp);
     for (count = 1L; count <= last; count++)
     {
          fseek(fp, -count, SEEK_END);        /* 回退        */
          ch = getc(fp);
          if (ch != CNTL_Z && ch != '\r')    /* MS-DOS 文件 */
               putchar(ch);
     }
     putchar('\n');
     fclose(fp);
     return 0;
}
```

下面是对一个文件的输出：

```c
Enter the name of the file to be processed:
Cluv
.C ni eno naht ylevol erom margorp a
ees reven llahs I taht kniht I

```

该程序使用二进制模式，以便处理MS-DOS文本和UNIX文件。但是，在使用其他格式文本文件的环境中可能无法正常工作。

> **注意**
> 如果通过命令行环境运行该程序，待处理文件要和可执行文件在同一个目录（或文件夹）中。如果在IDE中运行该程序，具体查找方案序因实现而异。例如，默认情况下，Microsoft Visual Studio 2012在源代码所在的目录中查找，而Xcode 4.6则在可执行文件所在的目录中查找。

接下来，我们要讨论3个问题： `fseek()` 和 `ftell()` 函数的工作原理、如何使用二进制流、如何让程序可移植。

