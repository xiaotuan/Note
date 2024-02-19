使用 `vim` 指令创建一个名为 `main.c` 的文件，然后再里面输入如下代码：

```c
#include <stdio.h>

int main(int argc, char *argv[])
{
	printf("Hello World!\n");
}
```

使用 `gcc` 编译器来编译文件，输入如下命令：

```shell
$ gcc main.c
```

使用下面命令执行程序：

```shell
$ ./a.out 
Hello World!
```

`a.out` 这个文件的命名是 `GCC` 编译器自动命名的，可以在使用 `gcc` 命令的时候加上 `-o` 来指定生成的可执行文件名字，例如：

```shell
$ gcc main.c -o main
```

