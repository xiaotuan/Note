如果遇到需要立刻使用临时文件的情况，可以用 `tmpfile` 函数在给它命名的同时打开它。这点非常重要，因为一个程序可能会创建一个与 `tmpnam` 返回的文件名同名的文件。`tmpfile` 函数则完全避免了这个问题的发生：

```c
#include <stdio.h>

FILE *tmpfile(void);
```

`tmpfile` 函数返回一个文件流指针，它指向一个唯一的临时文件。该文件以读写方式打开（通过 `w+` 方式的 `fopen`），当对它的所有引用全部关闭时，该文件会被自动删除。

如果出错，`tmpfile` 返回空指针并设置 `errno` 的值。

> 注意：当编译一个使用 `tmpnam` 函数的程序时，`GNU C` 编译器会对它的使用给出警告信息。

**例如： tmpnam.c**

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>

int main()
{
    char tmpname[L_tmpnam];
    char content[256];
    char *filename;
    size_t count;
    int seek_result;
    FILE *tmpfp;
    
    filename = tmpnam(tmpname);
    
    printf("Temporary file name is: %s\n", filename);
    tmpfp = tmpfile();
    if (tmpfp) 
    {
        printf("Opened a temporary file OK\n");
    } else {
        printf("tmpfile\n");
    }
    fwrite("sdfksdlfjsd", sizeof(char), strlen("sdfksdlfjsd"), tmpfp);
    fflush(tmpfp);
    seek_result = fseek(tmpfp, 0, SEEK_SET);
	if (seek_result) {
		printf("移动读取位置失败。错误代码: %d\n", errno);
		exit(-3);
	}
	count = fread(content, sizeof(char), 256, tmpfp);
	if (count <= 0) {
		printf("没有读取到内容。错误代码: %d\n", errno);
	}
	printf("文件内容为：%s\n", content);
    sleep(20);
    exit(0);
}
```

