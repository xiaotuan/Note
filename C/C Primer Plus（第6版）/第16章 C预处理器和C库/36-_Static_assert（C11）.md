#### 16.12.2　 `_Static_assert` （C11）

`assert()` 表达式是在运行时进行检查。C11新增了一个特性： `_Static_assert` 声明，可以在编译时检查 `assert()` 表达式。因此， `assert()` 会导致正在运行的程序中止，而 `_Static_assert()` 会导致程序无法通过编译。 `_Static_assert()` 接受两个参数。第1个参数是整型常量表达式，第2个参数是一个字符串。如果第1个表达式求值为 `0` （或 `_False` ），编译器会显示字符串，而且不编译该程序。看看程序清单16.19的小程序，然后查看 `assert()` 和 `_Static_assert()` 的区别。

程序清单16.19　 `statasrt.c` 程序

```c
//　statasrt.c
#include <stdio.h>
#include <limits.h>
_Static_assert(CHAR_BIT == 16, "16-bit char falsely assumed");
int main(void)
{
　　 puts("char is 16 bits.");
　　 return 0;
}
```

下面是在命令行编译的示例：

```c
$ clang statasrt.c
statasrt.c:4:1: error: static_assert failed "16-bit char falsely assumed"
_Static_assert(CHAR_BIT == 16, "16-bit char falsely assumed");
^　　　　　　　　 ～～～～～～～～～～～～～～
1 error generated.
$
```

根据语法， `_Static_assert()` 被视为声明。因此，它可以出现在函数中，或者在这种情况下出现在函数的外部。

`_Static_assert` 要求它的第1个参数是整型常量表达式，这保证了能在编译期求值（ `sizeof` 表达式被视为整型常量）。不能用程序清单16.18中的 `assert` 代替 `_Static_assert` ，因为 `assert` 中作为测试表达式的 `z > 0` 不是常量表达式，要到程序运行时才求值。当然，可以在程序清单16.19的 `main()` 函数中使用 `assert(CHAR_BIT == 16)` ，但这会在编译和运行程序后才生成一条错误信息，很没效率。

