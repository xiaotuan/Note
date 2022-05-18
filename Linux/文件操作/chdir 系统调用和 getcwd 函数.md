`chdir` 系统调用可以用来改变当前工作目录，就像用户在文件系统里那样来浏览目录。它的函数原型如下所示：

```c
#include <unistd.h>

int chdir(const char *path);
```

程序可以通过调用 `getcwd` 函数来确定自己的当前工作目录。它的函数原型如下所示：

```c
#include <unistd.h>

char *getcwd(char *buf, size_t size);
```

`getcwd` 函数把当前目录的名字写到给定的缓冲区 buf 里。如果目录名的长度超出了参数 size 给出的缓冲区长度（一个 ERANGE 错误），它就返回 NULL。如果成功，它返回指针 buf。

如果再程序运行过程中，目录被删除（EINVAL 错误）或者有关权限发生了变化（EACCESS 错误），`getcwd` 也可能会返回 NULL。

例如：

```c
#include <stdio.h>
#include <unistd.h>

int main(void)
{
    char current_dir[2048];
    int result;
    char *dir;
    
    dir = getcwd(current_dir, sizeof(current_dir) / sizeof(char));
    if (!dir)
    {
        printf("Failed to get current working directory.\n");
    } else {
        printf("Current working directory is %s\n", dir);
    }
    
    printf("Switch current working directory to /etc.\n");
    result = chdir("/etc");
    if (result)
    {
        printf("Failed to switch current working directory.\n");
    }
    
    dir = getcwd(current_dir, sizeof(current_dir) / sizeof(char));
    if (!dir)
    {
        printf("Failed to get current working directory.\n");
    } else {
        printf("Current working directory is %s\n", dir);
    }
    
	return 0;
}
```

