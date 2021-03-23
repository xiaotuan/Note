#### B.5.7　整数类型的格式转换： `inttypes.h` 

该头文件定义了一些宏可用作转换说明来扩展整数类型。参考资料VI“扩展的整数类型”将进一步讨论。该头文件还声明了这个类型： `imaxdiv_t` 。这是一个结构类型，表示 `idivmax()` 函数的返回值。

该头文件中还包含 `stdint.h` ，并声明了一些使用最大长度整数类型的函数，这种整数类型在 `stdint.h` 中声明为 `intmax` 。表B.5.10列出了这些函数。

<center class="my_markdown"><b class="my_markdown">表B.5.10　使用最大长度整数的函数</b></center>

| 原型 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `intmax_t imaxabs(intmax_t j);` | 返回 `j` 的绝对值 |
| `imaxdiv_t imaxdiv(intmax_t numer,` | `intmax_t denom);` | 单独计算 `numer/denom` 的商和余数，并把两个计算结果存储在返回的结构中 |
| `intmax_t strtoimax(const char`  * | `restrict nptr, char`  **  `restrict endptr,` | `int base);` | 相当于 `strtol()` 函数，但是该函数把字符串转换成 `intmax_t` 类型并返回该值 |
| `uintmax_t strtoumax(const char`  * | `restrict nptr, char`  **  `restrict endptr,` | `int base);` | 相当于 `strtoul()` 函数，但是该函数但是该函数把字符串转换成 `intmax_t` 类型并返回该值 |
| `intmax_t wcstoimax(const wchar_t`  * | `restrict nptr, wchar_t`  **  `restrict` | `endptr, int base);` | `strtoimax()` 函数的 `wchar_t` 类型的版本 |
| `uintmax_t wcstoumax(const wchar_t`  * | `restrict nptr, wchar_t`  **  `restrict` | `endptr, int base);` | `strtoumax()` 函数的 `wchar_t` 类型的版本 |

