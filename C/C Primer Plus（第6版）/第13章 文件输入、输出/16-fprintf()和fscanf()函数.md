#### 13.4.1　 `fprintf()` 和 `fscanf()` 函数

文件I/O函数 `fprintf()` 和 `fscanf()` 函数的工作方式与 `printf()` 和 `scanf()` 类似，区别在于前者需要用第1个参数指定待处理的文件。我们在前面用过 `fprintf()` 。程序清单13.3演示了这两个文件I/O函数和 `rewind()` 函数的用法。

程序清单13.3　 `addaword.c` 程序

```c
/* addaword.c -- 使用 fprintf()、fscanf() 和 rewind() */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 41
int main(void)
{
     FILE *fp;
     char words[MAX];
     if ((fp = fopen("wordy", "a+")) == NULL)
     {
          fprintf(stdout, "Can't open \"wordy\" file.\n");
          exit(EXIT_FAILURE);
     }
     puts("Enter words to add to the file; press the #");
     puts("key at the beginning of a line to terminate.");
     while ((fscanf(stdin, "%40s", words) == 1) && (words[0] != '#'))
          fprintf(fp, "%s\n", words);
     puts("File contents:");
     rewind(fp);        /* 返回到文件开始处 */
     while (fscanf(fp, "%s", words) == 1)
          puts(words);
     puts("Done!");
     if (fclose(fp) != 0)
          fprintf(stderr, "Error closing file\n");
     return 0;
}
```

该程序可以在文件中添加单词。使用 `"a+"` 模式，程序可以对文件进行读写操作。首次使用该程序，它将创建 `wordy` 文件，以便把单词存入其中。随后再使用该程序，可以在 `wordy` 文件后面添加单词。虽然 `"a+"` 模式只允许在文件末尾添加内容，但是该模式下可以读整个文件。 `rewind()` 函数让程序回到文件开始处，方便 `while` 循环打印整个文件的内容。注意， `rewind()` 接受一个文件指针作为参数。

下面是该程序在UNIX环境中的一个运行示例（可执行程序已重命名为 `addword` ）：

```c
$ ./addaword
Enter words to add to the file; press the Enter
key at the beginning of a line to terminate.
The fabulous programmer
#
File contents:
The
fabulous
programmer
Done!
$ ./addaword
Enter words to add to the file; press the Enter
key at the beginning of a line to terminate.
enchanted the
large
#
File contents:
The
fabulous
programmer
enchanted
the
large
Done!

```

如你所见， `fprintf()` 和 `fscanf()` 的工作方式与 `printf()` 和 `scanf()` 类似。但是，与 `putc()` 不同的是， `fprintf()` 和 `fscanf()` 函数都把 `FILE` 指针作为第1个参数，而不是最后一个参数。

