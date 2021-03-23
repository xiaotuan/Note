#### B.5.27　扩展的多字节字符和宽字符工具： `wchar.h` （C99）

每种实现都有一个基本字符集，要求C的 `char` 类型足够宽，以便能处理这个字符集。实现还要支持扩展的字符集，这些字符集中的字符可能需要多字节来表示。可以把多字节字符与单字节字符一起存储在普通的 `char` 类型数组，用特定的字节值指定多字节字符本身及其大小。如何解释多字节字符取决于移位状态（shift state）。在最初的移位状态中，单字节字符保留其通常的解释。特殊的多字节字符可以改变移位状态。除非显式改变特定的移位状态，否则移位状态一直保持有效。

`wchar_t` 类型提供另一种表示扩展字符的方法，该类型足够宽，可以表示扩展字符集中任何成员的编码。用这种宽字符类型来表示字符时，可以把单字符存储在 `wchar_t` 类型的变量中，把宽字符的字符串存储在 `wchar_t` 类型的数组中。字符的宽字符表示和多字节字符表示不必相同，因为后者可能使用前者并不使用的移位状态。

`wchar.h` 头文件提供了一些工具用于处理扩展字符的两种表示法。该头文件中定义的类型列在表B.5.46中（其中有些类型也定义在其他的头文件中）。

<center class="my_markdown"><b class="my_markdown">表B.5.46　 `wchar.h` 中定义的类型</b></center>

| 类型 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `wchar_t` | 整数类型，可表示本地化支持的最大扩展字符集 |
| `wint_t` | 整数类型，可存储扩展字符集的任意值和至少一个不是扩展字符集成员的值 |
| `size_t` | `sizeof` 运算符返回的整数类型 |
| `mbstate_t` | 非数组类型，可存储多字节字符序列和宽字符之间转换所需的转换状态信息 |
| `struct tm` | 结构类型，用于存储日历时间的组成部分 |

`wchar.h` 头文件中还定义了一些宏，如表B.5.47所列。

<center class="my_markdown"><b class="my_markdown">表B.5.47　 `wchar.h` 中定义的宏</b></center>

| 宏 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `NULL` | 空指针 |
| `WCHAR_MAX` | `wchar_t` 类型可存储的最大值 |
| `WCHAR_MIN` | `wchar_t` 类型可存储的最小值 |
| `WEOF` | `wint_t` 类型的常量表达式，不与扩展字符集的任何成员对；相当于 `EOF` 的宽字符表示，用于指定宽字符输入的文件结尾 |

该库提供的输入/输出函数类似于 `stdio.h` 中的标准输入/输出函数。在标准I/O函数返回 `EOF` 的情况中，对应的宽字符函数返回 `WEOF` 。表B.5.48中列出了这些函数。

<center class="my_markdown"><b class="my_markdown">表B.5.48　宽字符I/O函数</b></center>

| 函数原型 |
| :-----  | :-----  | :-----  |
| `int fwprintf(FILE`  *  `restrict stream, const wchar_t`  *  `restrict format, ...);` |
| `int fwscanf(FILE`  *  `restrict stream, const wchar_t`  *  `restrict format, ...);` |
| `int swprintf(wchar_t`  *  `restrict s, size_t n, const wchar_t`  *  `restrict format, ...);` |
| `int swscanf(const wchar_t`  *  `restrict s, const wchar_t`  *  `restrict format,...);` |
| `int vfwprintf(FILE`  *  `restrict stream, const wchar_t`  *  `restrict format,va_list arg);` |
| `int vfwscanf(FILE`  *  `restrict stream, const wchar_t`  *  `restrict format,va_list arg);` |
| `int vswprintf(wchar_t`  *  `restrict s, size_t n, const wchar_t`  *  `restrict format, va_list arg);` |
| `int vswscanf(const wchar_t`  *  `restrict s, const wchar_t`  *  `restrict format,va_list arg);` |
| `int vwprintf(const wchar_t`  *  `restrict format, va_list arg);` |
| `int vwscanf(const wchar_t`  *  `restrict format, va_list arg);` |
| `int wprintf(const wchar_t`  *  `restrict format, ...);` |
| `int wscanf(const wchar_t`  *  `restrict format, ...);` |
| `wint_t fgetwc(FILE`  * `stream);` |
| `wchar_t`  * `fgetws(wchar_t`  *  `restrict s, int n, FILE`  *  `restrict stream);` |
| `wint_t fputwc(wchar_t c, FILE`  * `stream);` |
| `int fputws(const wchar_t`  *  `restrict s, FILE`  *  `restrict stream);` |
| `int fwide(FILE`  * `stream, int mode);` |
| `wint_t getwc(FILE`  * `stream);` |
| `wint_t getwchar(void);` |
| `wint_t putwc(wchar_t c, FILE`  * `stream);` |
| `wint_t putwchar(wchar_t c);` |
| `wint t ungetwc(wint_t c, FILE`  * `stream);` |

有一个宽字符I/O函数没有对应的标准I/O函数：

```c
int fwide(FILE *stream, int mode)[4];

```

如果 `mode` 为正，函数先尝试把形参表示的流指定为宽字符定向（wide-charaacter oriented）；如果 `mode` 为负，函数先尝试把流指定为字节定向（byte oriented）；如果 `mode` 为 `0` ，函数则不改变流的定向。该函数只有在流最初无定向时才改变其定向。在以上所有的情况中，如果流是宽字符定向，函数返回正值；如果流是字节定向，函数返回负值；如果流没有定向，函数则返回 `0` 。

`wchar.h` 头文件参照 `string.h` ，也提供了一些转换和控制字符串的函数。一般而言，用 `wcs` 代替 `sting.h` 中的 `str` 标识符，这样 `wcstod()` 就是 `strtod()` 函数的宽字符版本。表B.5.49列出了这些函数。

<center class="my_markdown"><b class="my_markdown">表B.5.49　宽字符字符串工具</b></center>

| 函数原型 |
| :-----  | :-----  | :-----  |
| `double wcstod(const wchar_t`  *  `restrict nptr, wchar_t`  **  `restrict endptr);` |
| `float wcstof(const wchar_t`  *  `restrict nptr, wchar_t`  **  `restrict endptr);` |
| `long double wcstold(const wchar_t`  *  `restrict nptr, wchar_t`  **  `restrict endptr);` |
| `long int wcstol(const wchar_t`  *  `restrict nptr, wchar_t`  **  `restrict endptr,int base);` |
| `long long int wcstoll(const wchar_t`  *  `restrict nptr, wchar_t`  **  `restrict endptr, int base);` |
| `unsigned long int wcstoul(const wchar_t`  *  `restrict nptr, wchar_t`  **  `restrict endptr, int base);` |
| `unsigned long long int wcstoull( const wchar_t`  *  `restrict nptr, wchar_t`  ** `restrict endptr, int base);` |
| `wchar_t`  * `wcscpy(wchar_t`  *  `restrict s1, const wchar_t`  *  `restrict s2);` |
| `wchar_t`  * `wcsncpy(wchar_t`  *  `restrict s1, const wchar_t`  *  `restrict s2, size_tn);` |
| `wchar_t`  * `wcscat(wchar_t`  *  `restrict s1, const wchar_t`  *  `restrict s2);` |
| `wchar_t`  * `wcsncat(wchar_t`  *  `restrict s1, const wchar_t`  *  `restrict s2, size_tn);` |
| `int wcscmp(const wchar_t`  * `s1, const wchar_t`  * `s2);` |
| `int wcscoll(const wchar_t`  * `s1, const wchar_t`  * `s2);` |
| `int wcsncmp(const wchar_t`  * `s1, const wchar_t`  * `s2, size_t n);` |
| `size_t wcsxfrm(wchar_t`  *  `restrict s1, const wchar_t`  *  `restrict s2, size_tn);` |
| `wchar_t`  * `wcschr(const wchar_t`  * `s, wchar_t c);` |
| `size_t wcscspn(const wchar_t`  * `s1, const wchar_t`  * `s2);` |
| `size_t wcslen(const wchar_t`  * `s);` |
| `wchar_t`  * `wcspbrk(const wchar_t`  * `s1, const wchar_t`  * `s2);` |
| `wchar_t`  * `wcsrchr(const wchar_t`  * `s, wchar_t c);` |
| `size_t wcsspn(const wchar_t`  * `s1, const wchar_t`  * `s2);` |
| `wchar_t`  * `wcsstr(const wchar_t`  * `s1, const wchar_t`  * `s2);` |
| `wchar_t`  * `wcstok(wchar_t`  *  `restrict s1, const wchar_t`  *  `restrict s2, wchar_t` **  `restrict ptr);` |
| `wchar_t`  * `wmemchr(const wchar_t`  * `s, wchar_t c, size_t n);` |
| `int wmemcmp(wchar_t`  *  `restrict s1, const wchar_t`  *  `restrict s2, size_t n);` |
| `wchar_t`  * `wmemcpy(wchar_t`  *  `restrict s1,const wchar_t`  *  `restrict s2, size_t n);` |
| `wchar_t`  * `wmemmove(wchar_t`  * `s1, const wchar_t`  * `s2, size_t n);` |
| `wchar_t`  * `wmemset(wchar_t`  * `s, wchar_t c, size_t n);` |

该头文件还参照 `time.h` 头文件中的 `strtime()` 函数，声明了一个时间函数：

```c
size_t wcsftime(wchar_t * restrict s, size_t maxsize,const wchar_t * restrict format,
const struct tm * restrict timeptr);
```

除此之外，该头文件还声明了一些用于宽字符字符串和多字节字符相互转换的函数，如表B.5.50所列。

<center class="my_markdown"><b class="my_markdown">表B.5.50　宽字节和多字节字符转换函数</b></center>

| 函数原型 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `wint_t btowc(int c);` | 如果在初始移位状态中 `c` （ `unsigned char` ）是有效的单字节字符，那么该函数返回宽字节表示；否则，返回 `WEOF` |
| `int wctob(wint_t c);` | 如果 `c` 是一个扩展字符集的成员，它在初始移位状态中的多字节字符表示的是单字节，该函数就返回一个转换为 `int` 类型的 `unsigned char` 的单字节表示；否则，函数返回 `EOF` |
| `int mbsinit(const mbstate_t`  * `ps);` | 如果 `ps` 是空指针或指向一个指定为初始转换状态的数据对象，函数就返回非零值；否则，函数返回 `0` |
| `size_t mbrlen(const char` | *  `restrict s, size_t n,` | `mbstate_t`  *  `restrict ps);` | `mbrlen()` 函数相当于调用 `mbrtowc(NULL, s, n, ps != NULL ? ps : &internal)` ，其中 `internal` 是 `mbrlen()` 函数的 `mbstate_t` 对象，除非 `ps` 指定的表达式只计算一次 |
| `size_t mbrtowc(wchar_t`  * | `restrict pwc, const char` | *  `restrict s, size_t n,` | `mbstate_t`  *  `restrict ps);` | 如果 `s` 是空指针，调用该函数相当于把 `pwc` 设置为空指针、把 `n` 设置为 `1` 。如果 `s` 不是空指针，该函数最多检查 `n` 字节以确定下一个完整的多字节字符所需的字节数（包括所有的移位序列）。如果该函数确定了下一个多字节字符的结束处且合法，它就确定了对应宽字符的值。然后，如果 `pwc` 不为空，则把值存储在 `pwc` 指向的对象中。如果对应的宽字符是空的宽字符，描述的最终状态就是初始转换状态。如果检测到空的宽字符，函数返回 `0` ；如果检测到另一个有效宽字符，函数返回完整字符所需的字节数。如果 `n` 字节不足以表示一个有效的宽字符，但是能表示其中的一部分，函数返回 `-2` 。如果出现编码错误，函数返回 `-1` ，并把 `EILSEQ` 存储在 `errno` 中，且不存储任何值 |
| `size_t wcrtomb(char`  * | `restrict s, wchar_t wc,` | `mbstate_t`  *  `restrict ps);` | 如果 `s` 是空指针，那么调用该函数相当于把 `wc` 设置为空的宽字符，并为第 `1` 个参数使用内部缓冲区。如果 `s` 不是空指针， `wcrtomb()` 函数则确定表示 `wc` 指定宽字符对应的多字节字符表示所需的字节数（包括所有移位序列），并把多字节字符表示存储在一个数组中（ `s` 指向该数组的第 `1` 个元素），最多存储 `MB_CUR_MAX` 字节。如果 `wc` 是空的宽字符，就在初始移位状态所需的移位序列后存储一个空字节。描述的结果状态就是初始转换状态。如果 `wc` 是有效的宽字符，该函数返回存储多字节字符所需的字节数（包括指定移位状态的字节）。如果 `wc` 无效，函数则把 `EILSEQ` 存储在 `errno` 中，并返回 `-1` |
| `size_t mbsrtowcs(wchar_t`  * | `restrict dst, const char`  ** | `restrict src, size_t len,` | `mbstate_t`  *  `restrict ps);` | `mbstrtows()` 函数把 `src` 间接指向的数组中的多字节字符序列转换成对应的宽字符序列，从 `ps` 指向的对象所描述的转换状态开始，一直转换到结尾的空字符（包括该字符并存储）或转换了 `len` 个宽字符。如果 `dst` 不是空指针，则待转换的字符将存储在 `dst` 指向的数组中。出现这两种情况时停止转换：如果字节序列无法构成一个有效的多字节字符，或者（如果 `dst` 不是空指针） `len` 个宽字符已存储在 `dst` 指向的数组中。每转换一次都相当于调用一次 `mbrtowc()` 函数。如果 `dst` 不是空指针，就把空指针（如果因到达结尾的空字符而停止转换）或最后一个待转换多字节字符的地址赋给 `src` 指向的指针对象。如果由于到达结尾的空字符而停止转换，且 `dst` 不是空指针，那么描述的结果状态就是初始转状态。如果执行成功，函数返回成功转换的多字节字符数（不包括空字符）；否则函数返回 `-1` |
| `size_t wcsrtombs(char`  * | `restrict dst,const wchar_t` | **  `restrict src,size_t` | `len,mbstate_t`  *  `restrict` | `ps);` | `wcsrtombs()` 函数把 `src` 间接指向的数组中的宽字符序列转换成对应的多字节字符序列（从 `ps` 指向的对象描述的转换状态开始）。如果 `dst` 不是空指针，待转换的字符将被存储在 `dst` 指向的数组中。一直转换到结尾的空字符（包括该字符并存储）或换了 `len` 个多字节字符。出现这两种情况时停止转换：如果宽字符没有对应的有效多字节字符，或者（如果 `dst` 不是空指针）下一个多字节字超过了存储在 `dst` 指向的数组中的总字节数 `len` 的限制。每转换一次都相当于调用一次 `wcrtomb()` 函数。如果 `dst` 不是空指针，就把空指针（如果因到达结尾的空字符而停止转换）或最后一个待转换多字节字符的地址赋给 `src` 指向的指针对象。如果由于到达结尾的空字符而停止转换，描述的结果状态就是初始转状态。如果执行成功，函数返回成功转换的多字节字符数（不包括空字符）；否则函数返回 `-1` |

