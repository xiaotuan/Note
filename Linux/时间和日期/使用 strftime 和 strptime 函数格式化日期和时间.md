为了对时间和日期字符串的格式有更多控制，`Linux` 和现代的类 `UNIX` 系统提供了 `strftime` 函数。它很像是一个针对时间和日期的 `sprintf` 函数，工作方式也很类似：

```c
#include <time.h>

size_t strftime(char *s, size_t maxsize, const char *format, struct tm *timeptr);
```

`strftime` 函数格式化 `timeptr` 指针指向的 `tm` 结构所表示的时间和日期，并将结果放在字符串 `s` 中。字符串被指定（至少）`maxsize` 个字符长度。`format` 字符串用于控制写入字符串 `s` 的字符。与 `printf` 一样，它包含将被传给字符串的普通字符和用于格式化时间和日期元素的转换控制符。

| 转换控制符 | 说明                        | 转换控制符 | 说明                                          |
| ---------- | --------------------------- | ---------- | --------------------------------------------- |
| %a         | 星期几的缩写                | %u         | 星期几，1 ~ 7（周一为 1）                     |
| %A         | 星期几的全称                | %U         | 一年中的第几周，01 ~ 53（周日是一周的第一天） |
| %b         | 月份的缩写                  |            |                                               |
| %B         | 月份的全称                  | %V         | 一年中的第几周，01 ~ 53（周一是一周的第一天） |
| %c         | 日期和时间                  |            |                                               |
| %d         | 月份中的日期，01 ~ 31       | %w         | 星期几，0 ~ 6（周日为 0）                     |
| %H         | 小时，00 ~ 23               | %x         | 本地格式的日期                                |
| `%I`       | 12 小时制中的小时，01 ~ 12  | %X         | 本地格式的时间                                |
| %j         | 年份中的日期，001 ~ 366     | %y         | 年份减去 1900                                 |
| %m         | 年份中的月份，01 ~ 12       | %Y         | 年份                                          |
| %M         | 分钟，00 ~ 59               | %Z         | 时区名                                        |
| %p         | a.m. (上午) 或 p.m.（下午） | %%         | 字符 %                                        |
| %S         | 秒，00 ~ 61                 |            |                                               |

`strptime` 函数以一个代表日期和时间的字符串为参数，并创建表示同一日期和时间的 `tm` 结构：

```c
#define _XOPEN_SOURCE 
#include <time.h>

char *strptime(const char *buf, const char *format, struct tm *timeptr);
```

> 注意：需要在 `#include <time.h>` 语句前加上如下一行代码：
>
> ```c
> #define _XOPEN_SOURCE 
> ```

`format` 字符串的构建方式和 `strftime` 的 `format` 字符串往前一样。`strptime` 在字符串扫描方面类似于 `sscanf` 函数，也是查找可识别字段，并把它们写入对于的变量中。只是这里是根据 `format` 字符串来填充 `tm` 结构的成员。不过，`strptime` 的转换控制符与 `strftime` 的相比，限制要稍微松一些，因为 `strptime` 中的星期几和月份用缩写和全称都行，两者都匹配 `strptime` 中的 `%a` 控制符，此外，`strftime` 对小于 10 的数字总以 0 开头，而 `strptime` 则把它看作是可选的。

`strftime` 返回一个指针，执行转换过程处理的最后一个字符后面的那个字符。如果碰到不能转换的字符，转换过程就在该处停下来。调用程序需要检查是否已从传递的字符串中读入了足够多的数据，以确保 `tm` 结构中写入了有意义的值。

例如：

**strftime.c**

```c
#define _XOPEN_SOURCE 
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    struct tm *tm_ptr, timestruct;
    time_t the_time;
    char buf[256];
    char *result;
    
    (void) time(&the_time);
    tm_ptr = localtime(&the_time);
    strftime(buf, 256, "%A %d %B, %I:%S %p", tm_ptr);
    
    printf("strftime give: %s\n", buf);
    
    strcpy(buf, "Thu 26 July 2007, 17:53 will do fine");
    
    printf("calling strptime with: %s\n", buf);
    tm_ptr = &timestruct;
    
    result = strptime(buf, "%a %d %b %Y, %R", tm_ptr);
    printf("strptime consumed up to: %s\n", result);
    
    printf("strptime gives:\n");
    printf("date: %02d/%02d/%02d\n", tm_ptr->tm_year % 100, tm_ptr->tm_mon + 1, tm_ptr->tm_mday);
    printf("time: %02d:%02d\n", tm_ptr->tm_hour, tm_ptr->tm_min);
    exit(0);
}
```

运行结果如下：

```shell
$ ./a.out
strftime give: Tuesday 12 July, 06:20 PM
calling strptime with: Thu 26 July 2007, 17:53 will do fine
strptime consumed up to:  will do fine
strptime gives:
date: 07/07/26
time: 17:53
```

> 注意：要成功地扫描日期，`strptime` 需要一个准确的格式字符串，这一点非常重要。一般来说，该函数不会准确扫描读自用户的日期，除非用户输入的格式非常严格。