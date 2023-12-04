C99 新增了两个头文件 `stdint.h` 和 `inttypes.h`，以确保 C 语言的类型在各系统中的功能相同。

C 语言为现有类型创建了更多类型名。这些新的类型名定义在 `stdint.h` 头文件中。例如，`int32_t` 表示 32 位的有符号整数类型。在使用 32 位 `int` 的系统中，头文件会把 `int_32_t` 作为 `int` 的别名。

C99 和 C11 不仅提供可移植的类型名，还提供相应的输入和输出。例如，`inttypes.h` 头文件中定义了 `PRId32` 字符串宏，代表打印 32 位有符号值的合适转换说明（如 d 或 l）。例如：

```c
/* altnames.c -- 可移植整数类型名 */
#include <stdio.h>
#include <inttypes.h>	// 支持可移植类型

int main(void)
{
	int32_t me32;	// me32 是一个 32 为有符号整型变量
	me32 = 45933945;
	int_fast64_t dfk = 531321136543;
	printf("First, assume int32_t is int: ");
	printf("me32 = %d\n", me32);
	printf("Next, let's not make any assumptions.\n");
	printf("Instead, use a \"macro\" from inttypes.h: ");
	printf("me32 = %" PRId32 "\n", me32);
	printf("dfk = %" PRId64 "\n", dfk);
}
```

