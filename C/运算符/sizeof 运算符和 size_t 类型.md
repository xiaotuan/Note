`sizeof` 运算符以字节为单位返回运算对象的大小（在 `C` 中， · 字节定义为 `char` 类型占用的空间大小。）

`C` 语言规定， `sizeof` 返回 `size_t` 类型的值。

`C99` 做了进一步调整，新增了 `%zd` 转换说明用于 `printf()` 显示 `size_t` 类型的值。如果系统不支持 `%zd`，可使用 `%u` 或 `%lu` 代替 `%zd`。

```c
#include <stdio.h>

int main(void)
{
  int n = 0;
  size_t intsize;
  intsize = sizeof(int);
  printf("n = %d, n has %zd bytes; all ints have %zd bytes.\n", n, sizeof n, intsize);
  return 0;
}
```

