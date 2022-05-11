`fclose` 库函数关闭指定的文件流，使所有尚未写出的数据都写出。因为 stdio 库会对数据进行缓存，所以使用 `fclose` 是很重要的。

该函数原型如下所示：

```c
#include <stdio.h>

int fclose(FILE *stream);
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
	char *write_content = "这是通过 fwrite 写入的数据。\n";
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

