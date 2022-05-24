`opendir`函数的作用是打开一个目录并建立一个目录流。如果成功，它返回一个指向 `DIR` 结构的指针，该指针用于读取目录数据项。其函数原型如下：

```c
#include <sys/types.h>
#include <dirent.h>

DIR *opendir(const char *name);
```

`opendir` 在失败时返回一个空指针。注意，目录流使用一个底层文件描述符来访问目录本身，所以如果打开的文件过多，`opendir` 可能会失败。

> 注意：使用 `opendir` 函数打开目录后，需要调用 `chdir` 函数切换当前工作目录到打开目录。如果未进行该操作，使用 `lstat` 函数获取文件属性将会无效。

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

