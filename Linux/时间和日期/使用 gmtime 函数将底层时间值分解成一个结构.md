`gmtime`  函数把底层时间值分解为一个结构，该结构包含一些常用的成员：

```c
#include <time.h>

struct tm *gmtime(const time_t timeval);
```

`tm` 结构被定义为至少包含如下表的成员：

| tm 成员      | 说明                       |
| ------------ | -------------------------- |
| int tm_sec   | 秒，0 ~ 61                 |
| int tm_min   | 分，0 ~ 59                 |
| int tm_hour  | 小时，0 ~ 23               |
| int tm_mday  | 月份中的日期，1 ~ 31       |
| int tm_mon   | 月份，0 ~ 11（一月份为 0） |
| int tm_year  | 从 1990 年开始计算的年份   |
| int tm_wday  | 星期几，0 ~ 6 （周日为 0） |
| int tm_yday  | 年份中的日期，0 ~ 365      |
| int tm_isdst | 是否夏令时                 |

> 提示：`tm_sec` 的范围允许临时润秒或双润秒。

例如：

**gmtime.c**

```c
#include <time.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
    struct tm *tm_ptr;
    time_t the_time;
    (void) time(&the_time);
    tm_ptr = gmtime(&the_time);
    
    printf("Raw time is %ld\n", the_time);
    printf("gmtime gives: \n");
    printf("date: %02d/%02d/%02d\n", tm_ptr->tm_year, tm_ptr->tm_mon + 1, tm_ptr->tm_mday);
    printf("time: %02d:%02d:%02d\n", tm_ptr->tm_hour, tm_ptr->tm_min, tm_ptr->tm_sec);
    exit(0);
}
```

运行结果如下：

```shell
$ ./a.out
Raw time is 1657616531
gmtime gives: 
date: 122/07/12
time: 09:02:11
```

