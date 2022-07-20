获取 GID 方法如下：

```c
#include <sys/types.h>
#include <unistd.h>

gid_t getgid(void);
gid_t getegid(void);
int setgid(gid_t gid);
```

`getgid` 函数返回调用进程的真实组 ID。`getegid` 函数返回调用进程的有效组ID。`setgid` 函数用于设置组 ID。

> 注意：调用 `setgid` 函数需要超级用户权限。

**示例代码：**

```c
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int main() {
    gid_t gid;
    gid_t egid;
    
    gid = getgid();
    egid = getegid();
   	printf("gid=%d, egid=%d\n", gid, egid);
   	setgid(130);
   	gid = getgid();
    egid = getegid();
   	printf("gid=%d, egid=%d\n", gid, egid);
    
    exit(0);
}
```

运行结果如下：

```shell
$ sudo ./a.out
gid=0, egid=0
gid=130, egid=130
```

