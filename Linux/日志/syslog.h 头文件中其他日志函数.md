在头文件 `syslog.h` 中还定义了一些能够改变日志记录行为的其他函数。它们是：

```c
#include <syslog.h>

void closelog(void);
void openlog(const char *ident, int logopt, int facility);
int setlogmast(int maskpri);
```

你可以通过调用 `openlog` 函数来改变日志信息的表示方式。它可以设置一个字符串 `ident`，该字符串会添加在日志信息的前面。你可以通过它来指明是那个程序创建了这条信息。`facility` 参数记录一个将被用于后续 `syslog` 调用的默认设施值，其默认值是 `LOG_USER`。`logopt` 参数对后续 `syslog` 调用的行为进行配置，它是 0 个或多个参数的按位或：

| logopt 参数 | 说明                                                         |
| ----------- | ------------------------------------------------------------ |
| LOG_PID     | 在日志信息中包含进程标识符，这是系统分配给每个进程的一个唯一值 |
| LOG_CONS    | 如果信息不能被记录到日志文件中，就把它们发送到控制台         |
| LOG_ODELAY  | 在第一次调用 `syslog` 时才打开日志设施                       |
| LOG_NDELAY  | 立即打开日志设施，而不是等到第一次记录日志时                 |

`openlog` 函数会分配并打开一个文件描述符，并通过它来写日志。你可以调用 `closelog` 函数来关闭它。注意，在调用 `syslog` 之前无需调用 `openlog`，因为 `syslog` 会根据需要自行打开日志设施。

你可以使用 `setlogmask` 函数来设置一个日志掩码，并通过它来控制日志信息的有衔接。优先级未在日志掩码中置位的后续 `syslog` 调用都将被丢弃。所以你可以通过这个方法关闭 `LOG_DEBUG` 消息而不用改变程序主体。

你可以用 `LOG_MASK`（priority）为日志信息创建一个掩码，它的作用是创建一个只包含一个优先级的掩码。你还可以用 `LOG_UPTO`（priority）来创建一个由指定优先级之上的所有优先级（包括指定优先级）构成的掩码。

**示例代码：**

```c
#include <syslog.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main()
{
    int logmask;
    
    openlog("mask", LOG_PID | LOG_CONS, LOG_USER);
    syslog(LOG_INFO, "informative message, pid = %d", getpid());
    syslog(LOG_DEBUG, "debug message, should appear");
    logmask = setlogmask(LOG_UPTO(LOG_NOTICE));
    syslog(LOG_DEBUG, "debug message, should not appear");
    
    exit(0);
}
```

日志输出如下：

```
Jul 19 09:18:25 xiaotuan-VirtualBox mask[147446]: informative message, pid = 147446
Jul 19 09:18:25 xiaotuan-VirtualBox mask[147446]: debug message, should appear
```

