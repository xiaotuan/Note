`X/Open` 规范（可以在 <http://opengroup.org/> 上找到）定义了命令行选项的标志用法（工具语法指南），同时定义了在 C 语言程序中提供命令行开关的标准用法（工具语法指南），同时定义了在 C 语言程序中提供命令行开关的标志变成接口： `getopt` 函数。

`Linux` 提供了 `getopt` 函数，它支持需要关联值和不需要关联值的选项，而且简单易用：

```c
#include <unistd.h>

int getopt(int argc, char *const argv[], const char *optstring);
extern char *optarg;
extern int optind, opterr, optopt;
```

`getopt` 函数将传递给程序的 `main` 函数的 `argc` 和 `argv` 作为参数，同时接受一个选项指定符字符串 `optstring`，该字符串告诉 `getopt` 那些选项可用，以及它们是否有关联值。`optstring` 只是一个字符列表，每个字符代表一个单字符选项。如果一个字符后面紧跟一个冒号（`:`），则表明该选项有一个关联值作为下一个参数。`bash` 中的 `getopts` 命令执行类似的功能。

例如：

```c
getopt(argc, argc, "if:lr");
```

`getopt` 的返回值是 `argv` 数组中的下一个选项字符（如果有的话）。循环调用 `getopt` 就可以依次得到每个选项。`getopt` 有如下行为：

+ 如果选项有一个关联值，则外部变量 `optarg` 执行这个值。
+ 如果选项处理完毕，`getopt` 返回 `-1`，特殊参数 `--` 将使 `getopt` 停止扫描选项。
+ 如果遇到一个无法识别的选项，`getopt` 返回一个问号（`?`），并把它保存到外部变量 `optopt` 中。
+ 如果一个选项要求有一个关联值（例如例子中的 `-f`），但用户并未提供这个值，`getopt` 通常将返回一个问号（`?`）。如果我们将选项字符串的第一个字符设置为冒号（`:`），那么 `getopt` 将在用户未提供值的情况下返回冒号（`:`）而不是问号（`?`）。

外部变量 `optind` 被设置为下一个待处理参数的索引。`getopt` 利用它来记录自己的进度。

有些版本的 `getopt` 会在第一个非选项参数处停下来，返回 `-1` 并设置 `optind` 的值。而其他一些版本，如 `Linux` 提供的版本，能够处理出现程序参数中任意位置的选项。注意，在这种情况下，`getopt` 实际上重写了 `argv` 数组，把所有非选项参数都集中在一起，从 `argv[optind]` 位置开始。对 `GUN` 版本的 `getopt` 而言，这一行为是由环境变量 `POSIXLY_CORRECT` 控制的，如果它被设置，`getopt` 就会在第一个非选项参数处停下来。此外，还有些 `getopt` 版本会在遇到未知选项时打印出错信息。注意，根据 `POSIX` 规范的规定，如果 `opterr` 变量是非零值，`getopt` 就会向 `stderr` 打印一条出错信息。

例如：

```c
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	int opt;
	
	while ((opt = getopt(argc, argv, ": if:lr")) != -1)
	{
		switch (opt)
		{
			case 'i':
			case 'l':
			case 'r':
				printf("option: %c\n", opt);
				break;
				
			case 'f':
				printf("filename: %s\n", optarg);
				break;
				
			case ':':
				printf("option needs a value\n");
				break;
				
			case '?':
				printf("unknown option: %c\n", optopt);
				break;
		}
	}
	
	for (; optind < argc; optind++)
	{
		printf("argument: %s\n", argv[optind]);
	}
	
	exit(0);
}
```

运行结果如下：

```shell
$ ./a.out -i -lr 'hi there' -f fred.c -q
option: i
option: l
option: r
filename: fred.c
unknown option: q
argument: hi there
```

