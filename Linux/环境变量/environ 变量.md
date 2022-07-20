程序的环境由一组格式为 "名字=值" 的字符串组成。程序可以通过 `environ` 变量直接访问这个字符串数组。`environ` 变量的声明如下所示：

```c
#include <stdlib.h>

extern char **environ;
```

例如：

```c
#include <stdlib.h>
#include <stdio.h>

extern char **environ;

int main()
{
    char **env = environ;
    
    while (*env) {
        printf("%s\n", *env);
        env++;
    }
    exit(0);
}
```

