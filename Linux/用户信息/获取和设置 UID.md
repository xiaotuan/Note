当一个程序的 `SUID` 位被置位时，它的运行就好像是由该可执行文件的数组启动的。当 `su` 命令被执行时，程序的运行就好像它是由超级用户启动的，它随后验证用户的访问权限，将 `UID` 改为目标账户的 `UID` 值并执行该账户的登录 shell。采用这种方式还可以允许一个程序的运行就好像是由另一个用户启动的，它经常被系统管理员用来执行一些维护任务。

`UID` 有它自己的类型——`uid_t`，它定义在头文件 `sys/types.h` 中。它通常是一个小整数。有些 `UID` 是系统预定义的，其他的则是系统管理员在添加新用户时创建的。一般情况下，用户的 `UID` 值都大于 100。

```c
#include <sys/types.h>
#include <unistd.h>

uid_t getuid(void);
```

`getuid` 函数返回程序关联的 `UID`，它通常是启动程序的用户的 `UID`。`geteuid` 函数返回调用进程的有效用户ID。

例如：

```c
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int main()
{
    uid_t uid;
    uid_t euid;
    
    uid = getuid();
    euid = geteuid();
    printf("UID: %d, effective UID: %d\n", uid, euid);
    
    exit(0);
}
```

`setuid` 函数用于设置程序关联的用户 ID。

> 注意：只有超级用户才能调用 `setuid` 函数。

**示例代码：**

```c
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int main()
{
    uid_t uid;
    uid_t euid;
    
    uid = getuid();
    printf("UID: %d\n", uid);
    setuid(998);
    uid = getuid();
    printf("UID: %d\n", uid);
    
    exit(0);
}
```

