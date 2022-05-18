`unlink` 系统调用删除一个文件的目录项并减少它的链接数。它在成功时返回 0，失败时返回 -1。如果想通过调用这个函数来成功删除文件，你就必须拥有该文件所属目录的写和执行权限。

它们的函数原型如下所示：

```c
#include <unistd.h>

int unlink(const char *path);
int link(const char *path1, const char *path2);
int symlink(const char *path1, const char *path2);
```

如果一个文件的链接数减少到零，并且没有进程打开它，这个文件就会被删除。事实上，目录项总是被立刻删除，但文件所占用的空间要等到最后一个进程（如果有的话）关闭它之后才会被系统回收。`rm` 程序使用的就是这个调用。文件上其他的链接表示这个文件还有其他名字，这通常是由 `ln` 程序创建的。你可以使用 `link` 系统调用在程序中创建一个文件的新链接。

先用 `open` 创建一个文件，然后对其调用 `unlink` 是某些程序员用来创建临时文件的技巧。这些文件只有在被打开的时候才能被程序使用，当程序退出并且文件关闭的时候，它们就会被自动删除掉。

`link` 系统调用将创建一个指向已有文件 path1 的新链接。新目录项由 path2 给出。你可以通过 `symlink` 系统调用以类似的方式创建符号链接。注意，一个文件的福来链接并不会增加该文件的链接数，所以它不会像普通（硬）链接那样防止文件被删除。

> 提示：
>
> `link` 系统调用用于创建硬链接，链接的文件名不能与原文件同名。
>
> `symlink` 系统调用用于创建符号链接，链接的文件名可以与原文件同名。

例如：

```c
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <string.h>

int main(void)
{
    const char *FILE_NAME = "link.txt";
    const char *LINK_FILE = "../passwd.txt";
    const char *FILE_CONTENT = "这是测试文件，可以删除。";
	int fd;
	char ch;
	int result;
	size_t count;
	
	// 创建文件
	fd = open(FILE_NAME, O_CREAT | O_EXCL | O_WRONLY, S_IRUSR | S_IWUSR);
	if (fd == -1)
	{
	    printf("Unabled create %s file.\n", FILE_NAME);
	    return -1;
	}
	
	// 向文件写入内容
	count = write(fd, FILE_CONTENT, strlen(FILE_CONTENT));
	if (count != strlen(FILE_CONTENT))
	{
	    printf("Write file content failed./n");
	    close(fd);
	    return -2;
	}
	
	close(fd);
	
	// 创建文件硬链接
	result = link(FILE_NAME, LINK_FILE);
	if (result)
	{
	    printf("Create file link faile.\n");
	}
	
	printf("Please enter q to delete %s: ", FILE_NAME);
	ch = getchar();
	while (ch != 'q' && ch != 'Q')
    {
        printf("Please retry: ");
        ch = getchar();
    }
    
    // 删除 link.txt 文件
    unlink(FILE_NAME);
    
    // 创建 passwd.txt 符号链接
    result = symlink(LINK_FILE, "passwd.txt");
    if (result)
    {
        printf("Create passwd.txt symbolic link failed.\n");
    }
    
    printf("Please enter q to delete %s: ", LINK_FILE);
	ch = getchar();
	while (ch != 'q' && ch != 'Q')
    {
        printf("Please retry: ");
        ch = getchar();
    }
    
    // 删除 passwd.txt 文件
    unlink(LINK_FILE);
    
	return 0;
}
```

