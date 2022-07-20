`UNIX` 有另一种生成临时文件名的方式，就是使用 `mktemp` 和 `mkstemp` 函数 。`Linux` 也支持这两个函数，它们与 `tmpnam` 类似，不同之处在于可以为临时文件名指定一个模板，模板可以让你对文件的存放位置和名字有更多的控制：

```c
#include <stdlib.h>

char *mktemp(char *template);
int mkstemp(char *template);
```

`mktemp` 函数以给定的模板为基础创建一个唯一的文件名。`template` 参数必须是一个以 6 个 X 字符结尾的字符串。`mktemp` 函数用有效文件名字符的一个唯一组合来替换这些 X 字符。它返回一个指向生成的字符串的指针，如果不能生成一个唯一的名字，它就返回一个空指针。

`mkstemp` 函数类似于 `tmpfile`，它也是同时创建并打开一个临时文件。文件名的生成方法和 `mktemp` 一样，但是它的返回值是一个打开的、底层的文件描述符。

> 提示：你应该在程序中使用 "创建并打开" 函数 `tmpfile` 和 `mkstemp`，而不要使用 `tmpnam` 和 `mktemp`。

> 注意：`template` 参数会在调用 `mktemp` 或 `mkstemp` 函数后改变。

例如：

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
#include <fcntl.h>
#include <sys/stat.h>

int main()
{
    char tmpname[L_tmpnam] = "Xiaotuan-XXXXXX";
    char mktmpname[L_tmpnam] = "Xiaotuan-XXXXXX";
    char content[256];
    char *filename;
    size_t count;
    int seek_result;
    int fd;
    
    filename = mktemp(tmpname);
    
    printf("Temporary file name is: %s\n", filename);
    
    fd = mkstemp(mktmpname);
    if (fd != -1) 
    {
        printf("Opened a temporary file OK\n");
    } else {
        printf("tmpfile\n");
    }
    write(fd, "sdfksdlfjsd", strlen("sdfksdlfjsd"));
    
    seek_result = lseek(fd, 0, SEEK_SET);
	if (seek_result == -1) {
		printf("移动读取位置失败: %d。错误代码: %d\n", seek_result, errno);
		exit(-3);
	}
	
	count = read(fd, content, 256);
	if (count <= 0) {
		printf("没有读取到内容。错误代码: %d\n", errno);
	}
	printf("文件内容为：%s\n", content);

    sleep(20);
    close(fd);
    exit(0);
}
```

