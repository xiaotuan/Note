超级用户可以使用 `chown` 系统调用来改变一个文件的属主。它的函数原型如下所示：

```c
#include <sys/types.h>
#include <unistd.h>

int chown(const char *path, uid_t owner, gid_t group);
```

这个调用使用的是用户 ID 和组 ID 的数字值（通过 `getuid` 和 `getgid` 调用获得）和一个用于限定谁可以修改文件属主的系统值。如果已经设置了适当的特权，文件的属主和所属组就会改变。

`POSIX` 规范实际上允许非超级用户改变文件的属主。虽然所有 “正确的” `POSIX` 系统都不允许这样做，但严格来说，这是它的一个扩展规定里要求的。

例如：

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>


int main(void)
{
	int result = chown("./printf.txt", getuid(), getgid());
	if (result) {
	    printf("Failed to execute chown method, result: %d.", result);
	}
	return 0;
}
```

> 注意：`getuid` 和 `getgid` 方法获取到的是当前执行给命令的用户 ID 和组 ID，如果使用 `sudo` 命令执行该程序，这两个方法获取到的是 `root` 用户 ID 和 `root` 用户组 ID。
