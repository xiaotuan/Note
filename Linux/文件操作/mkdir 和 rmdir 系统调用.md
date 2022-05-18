可以使用 `mkdir` 和 `rmdir` 系统调用来建立和删除目录。

`mkdir` 的函数原型如下所示：

```c
#include <sys/types.h>
#include <sys/stat.h>

int mkdir(const char *path, mode_t mode);
```

`mkdir` 系统调用用于创建目录，它相当于 `mkdir` 程序。`mkdir` 调用将参数 `path` 作为新建目录的名字。目录的权限由参数 `mode` 设定，其含义与 `open` 系统调用的 `mode` 参数一样。

`rmdir` 函数原型如下所示：

```c
#include <unistd.h>

int rmdir(const char *path);
```

`rmdir` 系统调用用于删除目录，但只有在目录为空时才行。`rmdir` 程序就是用这个系统调用来完成工作的。

例如：

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/stat.h>

int main(void)
{
    const char *DIR_NAME = "Android SDK";
    int result;
    char ch;
    
    result = mkdir(DIR_NAME, S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP);
    if (result) 
    {
        printf("Create %s directory failed.\n", DIR_NAME);
        return -1;
    }
    
    printf("Please enter d to delete %s directory: ", DIR_NAME);
    ch = getchar();
    while (ch != 'q' && ch != 'Q')
    {
        printf("Please retry: ");
        ch = getchar();
    }
    
    rmdir(DIR_NAME);
    
	return 0;
}
```

