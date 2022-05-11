`fflush` 库函数的作用是吧文件流里的所有未写出数据立刻写出。使用这个函数还可以确保在程序继续执行之前重要的数据都已经被写到磁盘上。有时在调试程序时，你还可以用它来确认程序是否正在写数据而不是被挂起了。注意，调用 `fclose` 函数隐含执行了一次 flush 操作，所以你不必在调用 `fclose` 之前调用 `fflush`。

该函数原型如下所示：

```c
#include <stdio.h>

int fflush(FILE *stream);
```

例如：

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

int main(void)
{
	const int buffer_size = 1024;
	char buffer[buffer_size];
	char *write_content = "这fflush库函数的作用是把文件流里的所有未写出数据立刻写出。 例如， 你可以用这个函数来确保在试图读入一个用户响应之前， 先向终端送出一个交互提示符。 使用这个函数还可以确保在程序继续执行之前重要的数据都已经被写到磁盘上。 有时在调试程序时， 你还可以用它来确认程序是正在写数据而不是被挂起了。 注意， 调用fclose函数隐含执行了一次flush操作， 所以你不必在调用fclose之前调用fflush。";
	FILE *fd;
	int count;
	int start;
	int seek_result;
	
	fd = fopen("/home/xiaotuan/test.py", "a+");
	if (!fd)
	{
		printf("无法打开文件 \"/home/xiaotuan/test.py\"\n");
		exit(-1);
	}
	
	count = fwrite(write_content, sizeof(char), strlen(write_content), fd);
	if (count == strlen(write_content))
	{
		printf("写入数据成功！\n");
	} else {
		printf("写入数据失败！\n");
		exit(-2);
	}
	
	fflush(fd);
	
	printf("下面是修改后的内容：\n");
	seek_result = fseek(fd, 0, SEEK_SET);
	if (seek_result) {
		printf("移动读取位置失败。错误代码: %d", errno);
		exit(-3);
	}
	count = fread(buffer, sizeof(char), buffer_size, fd);
	while (count > 0)
	{
		for (int i = 0; i < count; i++)
		{
			putc(buffer[i], stdout);
		}
		count = fread(buffer, sizeof(char), buffer_size, fd);
	}
    
    fclose(fd);
    
	return 0;
}
```

