<center><b>printf() 的修饰符</b></center>

| 修饰符 | 含义                                                         |
| ------ | ------------------------------------------------------------ |
| 标记   | 下面 printf() 中的标记表描述了 5 中标记（`-`、`+`、空格、`#` 和 `0`），可以不使用标记或使用多个标记<br />示例：`%-10d` |
| 数字   | 最小字段宽度<br />如果该字段不能容纳待打印的数字或字符串，系统会使用更宽的字段<br />示例：`%4d` |
| .数字  | 精度<br />对于 `%e`、`%E` 和 `%f` 转换，表示小数点右边数字的位数<br />对于 `%g` 和 `%G` 转换，表示有效数字最大位数<br />对于 `%s` 转换，表示待打印字符的最大数量<br />对于整型转换，表示待带有数字的最小位数<br />如有必要，使用前导 0 来达到这个位数<br />只使用 `.` 表示气候跟随一个 0，所以 `%.f` 和 `%.0f` 相同<br />示例：`%5.2f` 打印一个浮点数，字段宽度为 5 字符，其中小数点后有两位数字 |
| h      | 和整型转换说明一起使用，表示 short int 或 unsigned short int 类型的值<br />示例：`%hu`、`%hx`、`%6.4hd` |
| hh     | 和整型转换说明一起使用，表示 signed char 或 unsigned char 类型的值<br />示例：`%hhu`、`%hhx`、`%6.4hhd` |
| j      | 和整型转换说明一起使用，表示 intmax_t 或 uintmax_t 类型的值。这些类型定义在 stdint.h 中<br />示例：`%jd`、`%8jx` |
| `l`    | 和整型转换说明一起使用，表示 long int 或 unsigned long int 类型的值<br />示例：`%ld`、`%8lu` |
| `ll`   | 和整型转换说明一起使用，表示 long long int 或 unsigned long long int 类型的值（C99）<br />示例：`%lld`、`%8llu` |
| L      | 和浮点转换说明一起使用，表示 long double 类型的值<br />示例：`%Lf`、`%10.4Le` |
| t      | 和整型转换说明一起使用，表示 ptrdiff_t 类型的值。ptrdiff_t 是两个指针差值的类型（C99）<br />示例：`%td`、`%12ti` |
| z      | 和整型转换说明一起使用，表示 size_t 类型的值。size_t 是 sizeof 返回的类型（C99）<br />示例：`%zd`、`%12zd` |

C 提供了可移植性更好的类型。首先，`stddef.h` 头文件（在包含 `stdio.h` 头文件时已包含其中）把 `size_t` 定义成系统使用 `sizeof` 返回的类型，这被称为底层类型。其次，`printf()` 使用 `z` 修饰符表示打印相应的类型。同样，C 还定义了 `ptrdiff_t` 类型和 `t` 修饰符来表示系统使用的两个底层有符号整数类型。

> 注意：对于浮点类型，有用于 double 和 long double 类型的转换说明，却没有 float 类型的。这是因为在 K&R C 中，表达式或参数中的 float 类型值会被自动转换成 double 类型。

<center><b>printf() 中的标记</b></center>

| 标记 | 含义                                                         |
| ---- | ------------------------------------------------------------ |
| `-`  | 待打印项左对齐。即，从字段的左侧开始打印该项<br />示例：`%-20s` |
| `+`  | 有符号值若为正，则在值前面显示加号；若为负，则在值前面显示减号<br />示例：`%+6.2f` |
| 空格 | 有符号值若为正，则在值前面显示前导空格（不显示任何符号）；若为负，则在值前面显示减号<br />`+` 标记覆盖一个空格<br />示例：`% 6.2f` |
| `#`  | 把结果转换成另一种形式。如果是 `%o`格式，则以 0 开始；如果是 `%x` 或 `%X` 格式，则以 0x 或 0X 开始；对于所有的浮点格式，`#` 保证了即使后面没有任何数字，也打印一个小数点字符。对于 `%g` 和 `%G` 格式，`#` 防止结果后面的 0 被删除<br />示例：`%#o`、`%#8.0f`、`%+#10.3e`<br /> |
| 0    | 对于数值格式，用前导 0 代替空格填充字段宽度。对于整数格式，如果出现 `-` 标记或指定精度，则忽略该标记 |



