C 语言程序可以通过 `putenv` 和 `getenv` 函数来访问环境变量。

```c
#include <stdlib.h>

char *getenv(const char *name);
int putenv(const char *string);
```

环境由一组格式为 "名字=值" 的字符串组成。`getenv` 函数以给定的名字搜索环境中的一个字符串，并返回与该名字相关的值。如果请求的变量不存在，它就返回 NULL。如果变量存在但无关联值，它将运行成功并返回一个空字符串，即该字符串的第一个字节是 null。由于 `getenv` 返回的字符串是存储在 `getenv` 提供的静态控件中，所以如果想进一步使用它，你就必须将它复制到另一个字符串中，以免它被后续的 `getenv` 调用所覆盖。

`putenv` 函数以一个格式为 "名字=值" 的字符串作为参数，并将该字符串加到当前环境中。如果由于可用内存不足而不能扩展环境，它会失败并返回 -1。此时，错误变量 errno 将被设置为 ENOMEM。

**environ.c**

```c
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) 
{
    char *var, *value;
    
    if (argc == 1 || argc > 3) 
    {
        fprintf(stderr, "usage: environ var [value]\n");
        exit(1);
    }
    
    var = argv[1];
    value = getenv(var);
    if (value)
    {
        printf("Variable %s has value %s\n", var, value);
    } else {
        printf("Variable %s has no value\n", var);
    }
    
    if (argc == 3)
    {
        char *string;
        value = argv[2];
        string = malloc(strlen(var)+strlen(value)+2);
        if (!string)
        {
            fprintf(stderr, "out of memory\n");
            exit(1);
        }
        strcpy(string, var);
        strcat(string, "=");
        strcat(string, value);
        printf("Calling putenv with: %s\n", string);
        if (putenv(string) != 0)
        {
            fprintf(stderr, "putenv failed\n");
            free(string);
            exit(1);
        }
        
        value = getenv(var);
        if (value)
        {
            printf("New value of %s is %s\n", var, value);
        } else {
            printf("New value of %s is null??\n", var);
        }
        
        free(string);
    }
    
    exit(0);
}
```

运行结果如下：

```shell
$ ./a.out HOME
Variable HOME has value /home/xiaotuan
$ ./a.out FRED
Variable FRED has no value
$ ./a.out FRED hello
Variable FRED has no value
Calling putenv with: FRED=hello
New value of FRED is hello
$ ./a.out FRED
Variable FRED has no value
```

> 注意：环境仅对程序本身有效。你在程序里做的改变不会反映到外部环境中，这是因为变量的值不会从子进程传播到父进程。

