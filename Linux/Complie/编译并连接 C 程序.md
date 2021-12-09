要运行的 C 源代码：

**hello.c**

```c
#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("Hello World\n");
    exit(0);
}
```

编译、链接和运行 C 源代码：

```shell
$ gcc -o hello hello.c
$ ./hello
Hello World
```

