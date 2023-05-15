`getchar()` 和 `putchar()` 每次只处理一个字符。

**示例代码：echo.c**

```c
/* echo.c - 重复输入 */
#include <stdio.h>

int main(void)
{
	char ch;
	
	while ((ch = getchar()) != '#')
		putchar(ch);
	
	return 0;
}
```

运行效果如下：

```shell
$ gcc echo.c
$ ./a.out 
Hello, there. I would
Hello, there. I would
like a #3 bag of potatoes.
like a 
```

