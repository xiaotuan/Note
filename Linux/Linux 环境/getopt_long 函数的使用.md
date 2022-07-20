`GNU C` 函数库包含 `getopt` 的另一个版本，称作 `getopt_long`，它接受以双划线（`--`）开始的**长参数**。

```c
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

#define _GNU_SOURCE
#include <getopt.h>

int main(int argc, char *argv[])
{
	int opt;
	struct option longopts[] = {
		{ "initialize", 0, NULL, 'i' },
		{ "file", 1, NULL, 'f' },
		{ "list", 0, NULL, 'l' },
		{ "restart", 0, NULL, 'r' },
		{ 0, 0, 0, 0 }
	};
	
	while ((opt = getopt_long(argc, argv, ": if:lr", longopts, NULL)) != -1) 
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
$ ./a.out --initialize --list 'hi there' --file fred.c -q
option: i
option: l
filename: fred.c
unknown option: q
argument: hi there
$ ./a.out --init -l --file=fred.c 'hi there'
option: i
option: l
filename: fred.c
argument: hi there
```

`getopt_long` 函数比 `getopt` 多两个参数。第一个附加参数是一个结构数组，它描述了每个长选项并告诉 `getopt_long` 如何处理它们。第二个附加参数是一个变量指针，它可以作为 `optind` 的长选项版本使用。

长选项结构在头文件 `getopt.h` 中定义，并且该头文件必须与常量 `_GNU_SOURCE` 一同包含进来，该常量启用 `getopt_long` 功能。

```c
struct option {
    const char *name;
    int has_arg;
    int *flag;
    int val;
};
```

该结构的成员说明如下：

| 选项成员 | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| name     | 长选项的名字。缩写也可以接受，只要不与其他选项混淆           |
| has_arg  | 该选项是否带参数。0 表示不带参数， 1 表示必须有一个参数，2 表示有一个可选参数 |
| flag     | 设置为 NULL 表示当找到该选项时，`getopt_long` 返回在成员 `val` 里给出的值。否则，`getopt_long` 返回 0，并将 `val` 的值写入`flag` 指向的变量。 |
| val      | `getopt_long` 为该选项返回的值                               |

