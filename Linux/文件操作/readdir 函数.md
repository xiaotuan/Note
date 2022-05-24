`readdir` 函数返回一个指针，该指针指向的结构里保存着目录流 `dirp` 中下一个目录项的有关资料。后续的 `readdir` 调用将返回后续的目录项。如果发生错误或者达到目录尾，`readdir` 将返回 `NULL`。POSIX 兼容的系统在达到目录尾时会返回 `NULL`，但并不改变 `errno` 的值，只有在发生错误时才会设置 `errno`。其函数原型如下：

```c
#include <sys/types.h>
#include <dirent.h>

struct dirent *readdir(DIR *dirp);
```

> 注意：如果在 `readdir` 函数扫描目录的同时还有其他进程在该目录里创建或删除文件，`readdir` 将不保证能够列出该目录里的所有文件（和子目录）。

`dirent` 结构中包含的目录项内容包括以下部分：

+ `ino_t d_ino`：文件的 `inode` 节点号。
+ `char d_name[]`：文件的名字。

**示例代码**

```c
#include <unistd.h>
#include <stdio.h>
#include <dirent.h>
#include <string.h>
#include <sys/stat.h>
#include <stdlib.h>

void printdir(char *dir, int depth)
{
	DIR *dp;
	struct dirent *entry;
	struct stat statbuf;
	
	if ((dp = opendir(dir)) == NULL)
	{
		fprintf(stderr, "cannot open directory: %s\n", dir);
		return;
	}
	chdir(dir);
	while ((entry = readdir(dp)) != NULL)
	{
		lstat(entry->d_name, &statbuf);
		if (S_ISDIR(statbuf.st_mode))
		{
			/* Found a directory, but ignore . and .. */
			if (strcmp(".", entry->d_name) == 0 ||
				strcmp("..", entry->d_name) == 0)
			{
				continue;
			}
			printf("%*s%s/\n", depth, "", entry->d_name);
			/* Recurse at a new indent level */
			printdir(entry->d_name, depth + 4);
		} else {
			printf("%*s%s\n", depth, "", entry->d_name);
		}
	}
	chdir("..");
	closedir(dp);
}

int main(void)
{
	printf("Directory scan of /home:\n");
	printdir("/home", 0);
	printf("done.\n");
	
	exit(0);
}
```

