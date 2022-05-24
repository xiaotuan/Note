`telldir` 函数的返回值记录着一个目录流里的当前位置。你可以在随后的 `seekdir` 调用中利用这个值来重置目录扫描到当前位置。其函数原型如下：

```c
#include <sys/types.h>
#include <dirent.h>

long int telldir(DIR *dirp);
```

**示例代码**

```c
#include <unistd.h>
#include <stdio.h>
#include <dirent.h>
#include <string.h>
#include <sys/stat.h>
#include <stdlib.h>

int main(void)
{
	const char *DIR_PATH = "/media/sf_Sharespace/QT5.9Samp2019/chap01Introduction/build-samp1_1-Desktop_Qt_5_9_1_MinGW_32bit-Debug";
	DIR *dp;
	struct dirent *entry;
	struct stat statbuf;
	long start_loc;
	int index = 0;
	
	if ((dp = opendir(DIR_PATH)) == NULL)
	{
		fprintf(stderr, "Count not open %s directory.\n", DIR_PATH);
		exit(-1);
	}
	
	start_loc = telldir(dp);
	chdir(DIR_PATH);
	while ((entry = readdir(dp)) != NULL)
	{
		lstat(entry->d_name, &statbuf);
		if (S_ISDIR(statbuf.st_mode))
		{
			if (strcmp(".", entry->d_name) == 0 ||
					strcmp("..", entry->d_name) == 0)
			{
				continue;
			}
			printf("%s/%4s", entry->d_name, " ");
		} else {
			printf("%s%4s", entry->d_name, " ");
		}
		
		index++;
		if (index % 5 == 0) {
			printf("\n");
		}
	}
	
	seekdir(dp, start_loc);
	entry = readdir(dp);
	while (entry != NULL && (strcmp(".", entry->d_name) == 0 || strcmp("..", entry->d_name) == 0))
	{
		entry = readdir(dp);
	}
	printf("\n\nFirst File name is %s.\n", entry->d_name);
	
	chdir("..");
	closedir(dp);
	
	return 0;
}
```

