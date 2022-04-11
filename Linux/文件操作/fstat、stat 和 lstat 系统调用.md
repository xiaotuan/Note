[toc]

fstat 系统调用返回与打开的文件描述符相关的文件状态信息，该信息将会写到一个 buf 结构中， buf 的地址以参数形式传递给 fstat。

stat 和 lstat 返回的是通过文件名查到的状态信息。它们产生相同的结果，但当文件是一个符号链接时，lstat 返回的是该符号链接本身的信息，而 stat 返回的是该链接执行的文件的信息。

### 1. fstat 系统调用原型

下面是 fstat、stat 和 lstat 系统调用的原型：

```c
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>

int fstat(int fd, struct stat *statbuf);
int stat(const char *path, struct stat *buf);
int lstat(const char *path, struct stat *buf);
```

> 提示
>
> 包含头文件 `sys/types.h` 是可选的，但由于一些系统调用的定义针对那些某天可能会做出调整的标准类型使用了别名，所以但在程序中使用系统调用时，还是推荐将这个头文件包含进去。

### 2. stat 结构体

stat 结构体的成员在不同的类 UNIX 系统上会有所变化，但一般会包含下表的内容：

| stat 成员 | 说明                                         |
| --------- | -------------------------------------------- |
| st_mode   | 文件权限和文件类型信息                       |
| st_ino    | 与该文件关联的 inode                         |
| st_dev    | 报错文件的设备                               |
| st_uid    | 文件属性的 UID 号                            |
| st_gid    | 文件属性的 GID 号                            |
| st_atime  | 文件上一次被访问的时间                       |
| st_ctime  | 文件的权限、属主、组或内容上一次被改变的时间 |
| st_mtime  | 文件的内容上一次被修改的时间                 |
| st_nlink  | 该文件上硬链接的个数                         |

stat 结果中返回的 st_mode 标志还有一些与之关联的宏，它们定义在头文件 `sys/stat.h` 中。

#### 2.1 访问权限标志

+ `S_IRUSR`：读权限，文件属主
+ `S_IWUSR`：写权限，文件属主
+ `S_IXUSR`：执行权限，文件属主
+ `S_IRGRP`：读权限，文件所属组
+ `S_IWGRP`：写权限，文件所属组
+ `S_IXGRP`：执行权限，文件所属组
+ `S_IROTH`：读权限，其他用户
+ `S_IWOTH`：写权限，其他用户
+ `S_IXOTH`：执行权限，其他用户

#### 2.2 文件类型标志

+ `S_IFBLK`：文件是一个特殊的块文件。
+ `S_IFDIR`：文件是一个目录。
+ `S_IFCHR`：文件是一个特殊的字符设备。
+ `S_IFIFO`：文件是一个 FIFO （命名管道）。
+ `S_IFREG`：文件是一个普通文件。
+ `S_FLNK`：文件是一个符号链接。

#### 2.3 其他模式

+ `S_ISUID`：文件设置了 SUID 位。
+ `S_ISGID`：文件设置了 SGID 位。

#### 2.4 st_mode 标志的掩码

+ `S_IFMT`：文件类型
+ `S_IRWXU`：属主的读/写/执行权限。
+ `S_IRWXG`：属组的读/写/执行权限。
+ `S_IRWXO`：其他用户的读/写/执行权限。

#### 2.5 判断文件类型的宏定义

+ `S_ISBLK`：测试是否是特殊的块设备文件。
+ `S_ISCHR`：测试是否是特殊的字符设备文件。
+ `S_ISDIR`：测试是否是目录。
+ `S_ISFIFO`：测试是否是 FIFO。
+ `S_ISREG`：测试是否是普通文件。
+ `S_ISLNK`：测试是否是符号链接。

##### 2.5.1 示例代码

```c
#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <stdio.h>

int main() 
{
	int in;
	struct stat info;
	
	in = open("testDir", O_RDONLY);
	if (in == -1) {
		write(2, "Unable open file.\n", 18);
		exit(1);
	}
	fstat(in, &info);
	if (S_ISDIR(info.st_mode))
	{
		printf("file.in is a directory.\n");
	} else {
		printf("file.in is not a directory.\n");
	}
	close(in);
	exit(0);
}
```

### 3. 示例代码

```c
#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <stdio.h>

int main() 
{
	int in;
	struct stat info;
	
	in = open("testDir", O_RDONLY);
	if (in == -1) {
		write(2, "Unable open file.\n", 18);
		exit(1);
	}
	fstat(in, &info);
	if (info.st_mode & S_IFDIR)
	{
		printf("file.in is a directory.\n");
	} else {
		printf("file.in is not a directory.\n");
	}
	close(in);
	exit(0);
}
```

