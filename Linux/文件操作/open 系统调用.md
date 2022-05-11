[toc]

open 系统调用建立了一条到文件或设备的访问路径。如果调用成功，它将返回一个可以被 read、write 和其他系统调用使用的文件描述符。这个文件描述符是唯一的，它不会与任何其他运行中的进程共享。如果两个程序同事打开同一个文件，它们会分别得到两个不同的文件描述符。如果它们都对文件进行写操作，那么它们会各写各的，它们分别接着上次离开的位置继续往下写。它们的数据不会交织在一起，而是彼此相互覆盖。两个程序对文件的读写位置（偏移值）不同。你可以通过文件锁功能来防止出现冲突。

open 调用在成功时返回一个新的文件描述符（它总是一个非负整数），在失败时返回 -1 并设置全局表里 errno 来指明失败原因。

POSIX 规范还标准化了一个 cteat 调用，但它并不常用。这个调用不仅会像我们预期的那样创建文件，还会打开文件。它的作用相当于以 oflags 标志 `O_CREAT|O_WRONLY|O_TRUNC` 来调用 open。

任何一个运行中的程序能够同时打开的文件数是有限制的。这个限制通常是由 `limits.h` 头文件中的常量 `OPEN_MAX` 定义的。在 Linux 系统中，这个限制可以在系统运行时调整，所以 `OPEN_MAX` 并不是一个常量。它通常一开始被设置为 256。

### 1. open 系统调用原型

下面是 open 系统调用的原型：

```c
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>

int open(const char *path, int oflags);
int open(const char *path, int oflags, mode_t mode);
```

> 提示
>
> 严格来说，在遵循 POSIX 规范的系统上，使用 open 系统调用并不需要包括头文件 `sys/types.h` 和 `sys/stat.h` ，但在某些 UNIX 系统上，它们可能是必不可少的。

### 2. oflags 参数可用值

| 模式     | 说明           |
| -------- | -------------- |
| O_RDONLY | 以只读方式打开 |
| O_WRONLY | 以只写方式打开 |
| O_RDWR   | 以读写方式打开 |

open 调用还可以在 oflags 参数中包括下列可选模式的组合（用 “按位或” 操作）：

+ O_APPEND：把写入数据追加在文件的末尾。
+ O_TRUNC：把文件长度设置为零，丢弃已有的内容。
+ O_CREAT：如果需要，就按参数 mode 中给出的访问模式创建文件。
+ O_EXCL：与 O_CREAT 一起使用，确保调用者创建出文件。open 调用是一个原子操作，也就是说，它值执行一个函数调用。使用这个可选模式可以防止两个程序同时创建同一个文件。如果文件已经存在，open 调用将失败。

> 提示
>
> 其他可用使用的 oflag 值，可以使用 `man 2 open` 命令查看。

### 3. mode 参数可用值

参数 mode 是几个标志按位或后得到的，这些标志在头文件 `sys/stat.h` 中定义，如下所示：

+ `S_IRUSR`：读权限，文件属主
+ `S_IWUSR`：写权限，文件属主
+ `S_IXUSR`：执行权限，文件属主
+ `S_IRGRP`：读权限，文件所属组
+ `S_IWGRP`：写权限，文件所属组
+ `S_IXGRP`：执行权限，文件所属组
+ `S_IROTH`：读权限，其他用户
+ `S_IWOTH`：写权限，其他用户
+ `S_IOTH`：执行权限，其他用户

### 4. umask

umask 是一个系统变量，它的作用是：当文件被创建时，为文件的访问权限设定一个掩码。执行 umask 命令可以修改这个变量的值。它是一个由 3 个八进制数字组成的值。每个数字都是八进制值 1、2、4 的 OR 操作结果。它们的具体含义见下表，这 3 个数字分别对应这用户 (user)、组 (group) 和其他用户 (other) 的访问权限。

| 数字 | 取值 | 含义                   |
| ---- | ---- | ---------------------- |
| 1    | 0    | 禁止属主任何权限       |
|      | 4    | 允许属主的读权限       |
|      | 2    | 允许属主的写权限       |
|      | 1    | 允许属主的执行权限     |
| 2    | 0    | 禁止组任何权限         |
|      | 4    | 允许组的读权限         |
|      | 2    | 允许组的写权限         |
|      | 1    | 允许组的执行权限       |
| 3    | 0    | 禁止其他用户任何权限   |
|      | 4    | 允许其他用户的读权限   |
|      | 2    | 允许其他用户的写权限   |
|      | 1    | 允许其他用户的执行权限 |

### 5. 示例代码

```c
#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>

int main() 
{
    int fd = open("myfile", O_CREAT|O_EXCL|O_WRONLY|O_APPEND, S_IRUSR|S_IWUSR|S_IRGRP|S_IWGRP|S_IROTH);
	if (fd == -1)
	{
		write(2, "Unable create myfile file\n", 26);
		exit(1);
	}
	if ((write(fd, "This is new file content.\n", 26)) != 26) {
		write(2, "Write content failed.\n", 22);
	}
    close(fd);
	exit(0);
}
```

