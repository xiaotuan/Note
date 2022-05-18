`chmod` 系统调用可以用来改变文件或目录的访问权限。该函数原型如下所示：

```c
#include <sys/stat.h>

int chmod(const char *path, mode_t mode);
```

`path` 参数指定的文件被修改为具有 `mode` 参数给出的访问权限。参数 `mode` 的定义与 `open` 系统调用中的一样，也是对所要求的访问权限进行按位 OR 操作。除非程序被赋予适当的特权，否则只有文件的属主或超级用户可以修改它的权限。

参数 `mode` 是几个标志按位或后得到的，这些标志在头文件 `sys/stat.h` 中定义，如下所示：

+ `S_IRUSR`：读权限，文件属主
+ `S_IWUSR`：写权限，文件属主
+ `S_IXUSR`：执行权限，文件属主
+ `S_IRGRP`：读权限，文件所属组
+ `S_IWGRP`：写权限，文件所属组
+ `S_IXGRP`：执行权限，文件所属组
+ `S_IROTH`：读权限，其他用户
+ `S_IWOTH`：写权限，其他用户
+ `S_IOTH`：执行权限，其他用户

例如：

```c
#include <stdio.h>
#include <sys/stat.h>

int main(void)
{
	chmod("./printf.txt", S_IRUSR | S_IRGRP | S_IROTH);
	return 0;
}
```

