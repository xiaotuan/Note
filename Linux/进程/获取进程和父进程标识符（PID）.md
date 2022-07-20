`getpid` 函数用于获取调用进程的进程标识符（PID）。`getppid` 函数用于获取调用进程的父进程标识符（PID）：

```c
#include <sys/types.h>
#include <unistd.h>

pid_t getpid(void);
pid_t getppid(void);
```

**示例代码：**

```c
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
    pid_t pid;
    pid_t ppid;
    
    pid = getpid();
    ppid = getppid();
    printf("PID = %d, PPID = %d\n", pid, ppid);
    
    exit(0);
}
```

