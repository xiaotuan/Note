#### B.5.18　整数类型： `stdint.h` 

`stdint.h` 头文件中使用 `typedef` 工具创建整数类型名，指定整数的属性。 `stdint.h` 头文件包含在 `inttypes.h` 中，后者提供输入 `/` 输出函数调用的宏。参考资料VI的“扩展的整数类型”中介绍了这些类型的用法。

#### 1．精确宽度类型

`stdint.h` 头文件中用一组 `typedef` 标识精确宽度的类型。表B.5.26列出了它们的类型名和大小。然而，注意，并不是所有的系统都支持其中的所有类型。

<center class="my_markdown"><b class="my_markdown">表B.5.26　确切宽度类型</b></center>

| **typedef** 名 | 属性 |
| :-----  | :-----  | :-----  | :-----  |
| `int8_t` | `8` 位，有符号 |
| `int16_t` | `16` 位，有符号 |
| `int32_t` | `32` 位，有符号 |
| `int64_t` | `64` 位，有符号 |
| `uint8_t` | `8` 位，无符号 |
| `uint16_t` | `16` 位，无符号 |
| `uint32_t` | `32` 位，无符号 |
| `uint64_t` | `64` 位，无符号 |

#### 2．最小宽度类型

最小宽度类型保证其类型的大小至少是某数量位。表B.5.27列出了最小宽度类型，系统中一定会有这些类型。

<center class="my_markdown"><b class="my_markdown">表B.5.27　最小宽度类型</b></center>

| **typedef** 名 | 属性 |
| :-----  | :-----  | :-----  | :-----  |
| `int_least8_t` | 至少 `8` 位，有符号 |
| `int_least16_t` | 至少 `16` 位，有符号 |
| `int_least32_t` | 至少 `32` 位，有符号 |
| `int_least64_t` | 至少 `64` 位，有符号 |
| `uint_least8_t` | 至少 `8` 位，无符号 |
| `uint_least16_t` | 至少 `16` 位，无符号 |
| `uint_least32_t` | 至少 `32` 位，无符号 |
| `uint_least64_t` | 至少 `64` 位，无符号 |

#### 3．最快最小宽度类型

在特定系统中，使用某些整数类型比其他整数类型更快。为此， `stdint.h` 也定义了最快最小宽度类型，如表B.5.28所列，系统中一定会有这些类型。

<center class="my_markdown"><b class="my_markdown">表B.5.28　最快最小宽度类型</b></center>

| **typedef** 名 | 属性 |
| :-----  | :-----  | :-----  | :-----  |
| `int_fast8_t` | 至少 `8` 位有符号 |
| `int_fast16_t` | 至少 `16` 位有符号 |
| `int_fast32_t` | 至少 `32` 位有符号 |
| `int_fast64_t` | 至少 `64` 位有符号 |
| `uint_fast8_t` | 至少 `8` 位无符号 |
| `uint_fast16_t` | 至少 `16` 位无符号 |
| `uint_fast32_t` | 至少 `32` 位无符号 |
| `uint_fast64_t` | 至少 `64` 位无符号 |

#### 4．最大宽度类型

`stdint.h` 头文件还定义了最大宽度类型。这种类型的变量可以存储系统中的任意整数值，还要考虑符号。表B.5.29列出了这些类型。

<center class="my_markdown"><b class="my_markdown">表B.5.29　最大宽度类型</b></center>

| **typedef** 名 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `intmax_t` | 最大宽度的有符号类型 |
| `uintmax_t` | 最大宽度的无符号类型 |

#### 5．可存储指针值的整数类型

`stdint.h` 头文件中还包括表B.5.30中所列的两种整数类型，它们可以精确地存储指针值。也就是说，如果把一个 `void`  *类型的值赋给这种类型的变量，然后再把该类型的值赋回给指针，不会丢失任何信息。系统可能不支持这类型。

<center class="my_markdown"><b class="my_markdown">表B.5.30　可存储指针值的整数类型</b></center>

| **typedef** 名 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `intptr_t` | 可存储指针值的有符号类型 |
| `uintptr_t` | 可存储指针值的无符号类型 |

#### 6．已定义的常量

`stdint.h` 头文件定义了一些常量，用于表示该头文件中所定义类型的限定值。常量都根据类型命名，即用 `_MIN` 或 `_MAX` 代替类型名中的 `_t` ，然后把所有字母大写即得到表示该类型最小值或最大值的常量名。例如， `int32_t` 类型的最小值是 `INT32_MIN` 、 `unit_fast16_t` 的最大值是 `UNIT_FAST16_MAX` 。表B.5.31总结了这些常量以及与之相关的 `intptr_t` 、 `unitptr_t` 、 `intmax_t` 和 `uintmax_t` 类型，其中的 `N` 表示位数。这些常量的值应等于或大于（除非指明了一定要等于）所列的值。

<center class="my_markdown"><b class="my_markdown">表B.5.31　整型常量</b></center>

| 常量标识符 | 最小值 |
| :-----  | :-----  | :-----  | :-----  |
| `INTN_MIN` | 等于 `-(2<sup class="my_markdown">N-1</sup>-1)` |
| `INTN_MAX` | 等于 `2<sup class="my_markdown">N-1</sup>-1` |
| `UINTN_MAX` | 等于 `2<sup class="my_markdown">N-1</sup>-1` |
| `INT_LEASTN_MIN` | `-(2<sup class="my_markdown">N-1</sup>-1)` |
| `INT_LEASTN_MAX` | `2<sup class="my_markdown">N-1</sup>-1` |
| `UINT_LEASTN_MAX` | `2<sup class="my_markdown">N</sup>-1` |
| `INT_FASTN_MIN` | `-(2<sup class="my_markdown">N-1</sup>-1)` |
| `INT_FASTN_MAX` | `2<sup class="my_markdown">N-1</sup>-1` |
| `UINT_FASN_MAX` | `2<sup class="my_markdown">N</sup>-1` |
| `INTPTR_MIN` | `-(2<sup class="my_markdown">15</sup>-1)` |
| `INTPTR_MAX` | `2<sup class="my_markdown">15</sup>-1` |
| `UINTPTR_MAX` | `2<sup class="my_markdown">16</sup>-1` |
| `INTMAX_MIN` | `-(2<sup class="my_markdown">15</sup>-1)` |
| `INTMAX_MAX` | `2<sup class="my_markdown">63</sup>-1` |
| `UINTMAX_MAX` | `2<sup class="my_markdown">64</sup>-1` |

该头文件还定义了一些别处定义的类型使用的常量，如表B.5.32所示。

<center class="my_markdown"><b class="my_markdown">表B.5.32　其他整型常量</b></center>

| 常量标识符 | 含义 |
| :-----  | :-----  | :-----  | :-----  |
| `PTRDIFF_MIN` | `ptrdiff_t` 类型的最小值 |
| `PTRDIFF_MAX` | `ptrdiff_t` 类型的最大值 |
| `SIG_ATOMIC_MIN` | `sig_atomic_t` 类型的最小值 |
| `SIG_ATOMIC_MAX` | `sig_atomic_t` 类型的最大值 |
| `WCHAR_MIN` | `wchar_t` 类型的最小值 |
| `WCHAR_MAX` | `wchar_t` 类型的最大值 |
| `WINT_MIN` | `wint_t` 类型的最小值 |
| `WINT_MAX` | `wint_t` 类型的最大值 |
| `SIZE_MAX` | `size_t` 类型的最大值 |

#### 7．扩展的整型常量

`stdin.h` 头文件定义了一些宏用于指定各种扩展整数类型。从本质上看，这种宏是底层类型（即在特定实现中表示扩展类型的基本类型）的强制转换。

把类型名后面的 `_t` 替换成 `_C` ，然后大写所有的字母就构成了一个宏名。例如，使用表达式 `UNIT_LEAST64_C(1000)` 后， `1000` 就是 `unit_least64_t` 类型的常量。

