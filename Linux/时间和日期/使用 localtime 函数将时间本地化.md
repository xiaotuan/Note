不同时区同一时刻创建的文件都会有相同的创建时间。要看当地时间，需要使用 `localtime` 函数：

```c
#include <time.h>

struct tm *localtime(const time_t * timeval);
```

> 提示：`tm` 结构请参阅 《[使用 gmtime 函数将底层时间值分解成一个结构.md](./使用 gmtime 函数将底层时间值分解成一个结构.md)》。

例如：

```c
#include <time.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
    struct tm *tm_ptr;
    time_t the_time;
    (void) time(&the_time);
    tm_ptr = localtime(&the_time);
    
    printf("Raw time is %ld\n", the_time);
    printf("gmtime gives: \n");
    printf("date: %02d/%02d/%02d\n", tm_ptr->tm_year, tm_ptr->tm_mon + 1, tm_ptr->tm_mday);
    printf("time: %02d:%02d:%02d\n", tm_ptr->tm_hour, tm_ptr->tm_min, tm_ptr->tm_sec);
    exit(0);
}
```

