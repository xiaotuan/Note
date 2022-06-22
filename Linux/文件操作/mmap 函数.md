[toc]

### 1. mmap 函数

`mmap` （内存映射）函数的作用是建立一段可以被两个或更多程序读写的内存。一个程序对它所做出的修改可以被其他程序看见。

`mmap` 函数创建一个指向一段内存区域的指针，该内存区域与可以通过一个打开的文件描述符访问的文件的内容相关联。该函数原型如下：

```c
#include <sys/mman.h>

void *mmap(void *addr, size_t len, int prot, int flags, int fildes, off_t off);
```

你可以通过传递 `off` 参数来改变经共享内存段访问的文件中数据的起始偏移值。打开的文件描述符由 `fildes` 参数给出。可以访问的数据量（即内存段的长度）由 `len` 参数设置。

你可以通过 `addr` 参数来请求使用某个特定的内存地址。如果它的取值是零，结果指针就将自动分配。这是推荐的做法。

`prot` 参数用于设置内存段的访问权限。它是下列常数值的按位 `OR` 结果：

+ `PROT_READ`：允许读该内存段。
+ `PROT_WRITE`：允许写该内存段。
+ `PROT_EXEC`：允许执行该内存段。
+ `PROT_NONE`：该内存段不能被访问。

`flags` 参数控制程序对该内存段的改变所造成的影响，可以使用的选项如下表：

| flags 参数    | 描述                                     |
| ------------- | ---------------------------------------- |
| `MAP_PRIVATE` | 内存段是私有的，对它的修改只对本进程有效 |
| `MAP_SHARED`  | 把对该内存段的修改报存到磁盘文件中       |
| `MAP_FIXED`   | 该内存段必须位于 `addr` 指定的地址处     |

### 2. msync 函数

`msync` 函数的作用是：把再该内存段的某个部分或整段中的修改写回到被映射的文件中（或者从被映射文件里读出）。该函数原型如下：

```c
#include <sys/mman.h>

int msync(void *addr, size_t len, int flags);
```

内存段需要修改的部分由作为参数传递过来的起始地址 `addr` 和长度 `len` 确定。`flags` 参数控制这执行修改的具体方式，可以使用如下选项：

| 选项          | 描述             |
| ------------- | ---------------- |
| MS_ASYNC      | 采用异步写方式   |
| MS_SYNC       | 采用同步写方式   |
| MS_INVALIDATE | 从文件中读回数据 |

### 3. munmap 函数

`munmap` 函数的作用是释放内存段：

```c
#include <sys/mman.h>

int munmap(void *addr, size_t len);
```

### 4. 示例程序

```c
#include <unistd.h>
#include <stdio.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <stdlib.h>

typedef struct {
	int integer;
	char string[24];
} RECORD;

#define NRECORDS (100)

int main()
{
	RECORD record, *mapped;
	int i, f;
	FILE *fp;
	
	fp = fopen("test.py", "w+");
	for (i = 0; i < NRECORDS; i++)
	{
		record.integer = i;
		sprintf(record.string, "RECORD-%d", i);
		fwrite(&record, sizeof(record), 1, fp);
	}
	fclose(fp);
	
	fp = fopen("test.py", "r+");
	fseek(fp, 43 * sizeof(record), SEEK_SET);
	fread(&record, sizeof(record), 1, fp);
	
	printf("integer: %d, string: %s", record.integer, record.string);
	
	record.integer = 143;
	sprintf(record.string, "RECORD-%d", record.integer);
	
	fseek(fp, 43 * sizeof(record), SEEK_SET);
	fwrite(&record, sizeof(record), 1, fp);
	fclose(fp);
	
	f = open("test.py", O_RDWR);
	mapped = (RECORD *)mmap(0, NRECORDS * sizeof(record), 
		PROT_READ | PROT_WRITE, MAP_SHARED, f, 0);
		
	printf("integer: %d, string: %s", mapped[43].integer, mapped[43].string);
	
	mapped[43].integer = 243;
	sprintf(mapped[43].string, "RECORD-%d", mapped[43].integer);
	msync((void *)mapped, NRECORDS * sizeof(record), MS_ASYNC);
	munmap((void *)mapped, NRECORDS * sizeof(record));
	close(f);
	
	exit(0);
}
```

