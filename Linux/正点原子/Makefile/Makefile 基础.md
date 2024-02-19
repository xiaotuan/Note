我们完成这样一个小工程，通过键盘输入两个整型数字，然后计算他们的和并将结果显示在屏幕上，在这个工程中我们有 `main.c`、`input.c` 和 `calcu.c` 这三个 C 文件和 `input.h`、`calcu.h` 这两个头文件。其中 `main.c` 是主体，`input.c` 负责接收从键盘输入的数值，`calcu.c` 进行任意两个数相加，其中 `main.c` 文件的内容如下：

**main.c**

```c
#include <stdio.h>
#include "input.h"
#include "calcu.h"

int main(int argc, char *argv[])
{
	int a, b, num;
	
	input_int(&a, &b);
	num = calcu(a, b);
	printf("%d + %d = %d\r\n", a, b, num);
}
```

**input.c**

```c
#include <stdio.h>
#include "input.h"

void input_int(int *a, int *b)
{
	printf("input two num: ");
	scanf("%d %d", a, b);
	printf("\r\n");
}
```

**calcu.c**

```c
#include "calcu.h"

int calcu(int a, int b)
{
	return (a + b);
}
```

**input.h**

```c
#ifndef __INPUT_H
#define __INPUT_H

void input_int(int *a, int *b);

#endif
```

**calcu.h**

```c
#ifndef __CALCU_H
#define __CALCU_H

int calcu(int a, int b);

#endif
```

可以通过如下命令编译该程序：

```shell
$ gcc main.c calcu.c input.c -o main
$ ./main 
input two num: 5 6

5 + 6 = 11
```

假如我们现在修改了 `calcu.c` 这个文件，只需要将 `calcu.c` 这个文件重新编译成 `.o` 文件，然后再将所有的 `.o` 文件链接成可执行文件即可，例如：

```shell
$ gcc -c calcu.c
$ gcc main.o input.o calcu.o -o main
```

我们也可以通过 `Makefile` 文件来实现上面的操作，在 `C` 文件同一目录下创建一个名为 `Makefile` 的文件，其内容如下：

```makefile
main: main.o input.o calcu.o
	gcc -o main main.o input.o calcu.o
main.o: main.c
	gcc -c main.c
input.o: input.c
	gcc -c input.c
calcu.o: calcu.c
	gcc -c calcu.c

clean:
	rm *.o
	rm main
```

上述代码中所有行首需要空出来的地方一定要使用 `TAB` 键！不要使用空格键！这是 `Makefile` 的语法要求。

`Makefile` 编写好以后我们就可以使用 `make` 命令来编译我们的工程了，直接在命令行中输入 `make` 即可，`make` 命令会在当前目录下查找是否存在 `Makefile` 这个文件，如果存在的话就按照 `Makefile` 里面定义的编译方式进行编译：

```shell
$ ls
calcu.c  calcu.h  input.c  input.h  main.c  Makefile
$ make
gcc -c main.c
gcc -c input.c
gcc -c calcu.c
gcc -o main main.o input.o calcu.o
$ ls
calcu.c  calcu.h  calcu.o  input.c  input.h  input.o  main  main.c  main.o  Makefile
```

使用 `make` 命令编译工程的时候可能会提示如下错误：

```shell
$ make
Makefile:2: *** missing separator。停止。
```

一般是下面两个原因造成的：

1）`Makefile` 中命令缩进没有使用 `TAB` 键！

2）`VI/VIM` 编辑器使用空格代替了 `TAB` 键，修改文件 `/etc/vim/vimrc`，在文件最后面加上如下所示代码：

```
set noexpandtab
```



