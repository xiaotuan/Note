为了得到更 "友好" 的时间和日期表示，像 `date` 命令输出的那样，你可以使用 `asctime` 函数和 `ctime` 函数：

```c
#include <time.h>

char *asctime(const struct tm *timeptr);
char *ctime(const time_t *timeval);
```

`asctime` 函数返回一个字符串，它表示由 `tm` 结构 `timeptr` 所给出的时间和日期。这个返回的字符串有类似下面的格式：

```
Sun Jun 9 12:34:56 2007\n\0
```

它总是这种长度为 26 个字符的固定格式。`ctime` 函数等效于调用下面这个函数：

```c
asctime(localtime(timeval));
```

它以原始时间值作为参数，并将它转换为一个更易读的本地时间。

例如：

**ctime.c**

```c
#include <time.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
    time_t timeval;
    
    (void)time(&timeval);
    printf("The date is: %s", asctime(gmtime(&timeval)));
    printf("The local date is %s", ctime(&timeval));
    exit(0);
}
```

运行结果如下：

```shell
$ ./a.out
The date is: Tue Jul 12 09:43:40 2022
The local date is Tue Jul 12 17:43:40 2022
```

