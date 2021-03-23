#### B.5.26　统一码工具： `uchar.h` （C11）

C99的 `wchar.h` 头文件提供两种途径支持大型字符集。C11专门针对统一码（Unicode）新增了适用于 `UTF-16` 和 `UTF-32` 编码的类型（见表B.5.44）。

<center class="my_markdown"><b class="my_markdown">表B.5.44　 `uchar.h` 中声明的类型</b></center>

| 类型 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `char16_t` | 使用 `16` 位字符的无符号整数类型（与 `stdint.h` 中的 `unit_least16_t` 相同） |
| `char32_t` | 使用 `32` 位字符的无符号整数类型（与 `stdint.h` 中的 `unit_least32_t` 相同） |
| `size_t` | `sizeof` 运算符 `(stddef.h)` 返回的整数类型 |
| `mbstate_t` | 非数组类型，可存储多字节字符序列和宽字符相互转换的转换状态信息 |

该头文件中还声明了一些多字节字符串与 `char16_t` 、 `char32_t` 格式相互转换的函数（见表B.5.45）。

<center class="my_markdown"><b class="my_markdown">表B.5.45　宽字符与多字节转换函数</b></center>

| 类型 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `size_t mbrto16(char16_t` *  `restrict` | `pwc, const char`  *  `restrict s, size_t` | `n, mbstate_t` *  `restrict ps);` | 与 `mbrtowc()` 函数相同（ `wchar.h` ），但该函数是把字符转换为 `char_16` 类型，而不是 `wchar_t` 类型 |
| `size_t mbrto32( char32_t`  *  `restrict` | `pwc, const char`  *  `restrict s, size_t` | `n, mbstate_t`  *  `restrict ps);` | 与 `mbrto16()` 函数相同，但该函数是把字符转换为 `char32_t` 类型 |
| `size_t c16rtomb(char`  *  `restrict s,` | `wchar_t wc, mbstate_t`  *  `restrict ps);` | 与 `wcrtobm()` 函数相同（ `wchar.h` ），但该函数转换的是 `char16_t` 类型字符，而不是 `wchar_t` 类型 |
| `size_t c32rtomb(char`  *  `restrict s,` | `wchar_t wc, mbstate_t`  *  `restrict ps);` | 与 `wcrtobm()` 函数相同（ `wchar.h` ），但该函数转换的是 `char32_t` 类型字符，而不是 `wchar_t` 类型 |

