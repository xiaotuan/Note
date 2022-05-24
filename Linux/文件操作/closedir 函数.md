`closedir` 函数关闭一个目录流并释放与之关联的资源，它在执行成功时返回 0，发生错误时返回 -1。其函数原型如下：

```c
#include <sys/types.h>
#include <dirent.h>

int closedir(DIR *dirp);
```

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

