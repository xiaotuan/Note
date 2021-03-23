#### B.5.28　宽字符分类和映射工具： `wctype.h` （C99）

`wctype.h` 库提供了一些与 `ctype.h` 中的字符函数类似的宽字符函数，以及其他函数。 `wctype.h` 还定义了表B.5.51中列出的3种类型和宏。

<center class="my_markdown"><b class="my_markdown">表B.5.51　 `wctpe.h` 中定义的类型和宏</b></center>

| 类型/宏 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `wint_t` | 整数类型，用于存储扩展字符集中的任意值，还可以存储至少一个不是扩展字符成员的值 |
| `wctrans_t` | 标量类型，可以表示本地化指定的字符映射 |
| `wctype_t` | 标量类型，可以表示本地化指定的字符分类 |
| `WEOF` | `wint_t` 类型的常量表达式，不对应扩展字符集中的任何成员，相当于宽字符中的 `EOF` ，用于表示宽字符输入的文件结尾 |

在该库中，如果宽字符参数满足字符分类函数的条件时，函数返回真（非 `0` ）。一般而言，因为单字节字符对应宽字符，所以如果 `ctype.h` 中对应的函数返回真，宽字符函数也返回真。表B.5.52列出了这些函数。

<center class="my_markdown"><b class="my_markdown">表B.5.52　宽字节分类函数</b></center>

| 函数原型 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `int iswalnum(wint_t wc);` | 如果 `wc` 表示一个字母数字字符（字母或数字），函数返回真 |
| `int iswalpha(wint_t wc);` | 如果 `wc` 表示一个字母字符，函数返回真 |
| `int iswblank(wint_t wc);` | 如果 `wc` 表示一个空格，函数返回真 |
| `int iswcntrl(wint_t wc);` | 如果 `wc` 表示一个控制字符，函数返回真 |
| `int iswdigit(wint_t wc);` | 如果 `wc` 表示一个数字，函数返回真 |
| `int iswgraph(wint_t wc);` | 如果 `iswprint(wc)` 为真，且 `iswspace(wc)` 为假，函数返回真 |
| `int iswlower(wint_t wc);` | 如果 `wc` 表示一个小写字符，函数返回真 |
| `int iswprint(wint_t wc);` | 如果 `wc` 表示一个可打印字符，函数返回真 |
| `int iswpunct(wint_t wc);` | 如果 `wc` 表示一个标点字符，函数返回真 |
| `int iswspace(wint_t wc);` | 如果 `wc` 表示一个制表符、空格或换行符，函数返回真 |
| `int iswupper(wint_t wc);` | 如果 `wc` 表示一个大写字符，函数返回真 |
| `int iswxdigit(wint_t wc);` | 如果 `wc` 表示一个十六进制数字，函数返回真 |

该库还包含两个可扩展的分类函数，因为它们使用当前本地化的 `LC_CTYPE` 值进行分类。表B.5.53列出了这些函数。

<center class="my_markdown"><b class="my_markdown">表B.5.53　可扩展的宽字符分类函数</b></center>

| 原型 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `int iswctype(wint_t wc,wctype_t desc);` | 如果 `wc` 具有 `desc` 描述的属性，函数返回真 |
| `wctype_t wctype(const char`  * `property);` | `wctype()` 函数构建了一个 `wctpe_t` 类型的值，它描述了由字符串参数 `property` 指定的宽字符分类。如果根据当前本地化的 `LC_CTYPE` 类别， `property` 识别宽字符分类有效， `wctype()` 函数则返回非零值（可作为 `iswctype()` 函数的第 `2` 个参数）；否则，函数返回 `0` |

`wctype()` 函数的有效参数名即是宽字符分类函数名去掉 `isw` 前缀。例如， `wctype("alpha")` 表示的是 `iswalpha()` 函数判断的字符类别。因此，调用 `iswctype(wc, wctype("alpha"))` 相当于调用 `iswalpha(wc)` ，唯一的区别是前者使用 `LC_CTYPE` 类别进行分类。

该库还有4个与转换相关的函数。其中有两个函数分别与 `ctype.h` 库中 `toupper()` 和 `tolower()` 相对应。第3个函数是一个可扩展的版本，通过本地化的 `LC_CTYPE` 设置确定字符是大写还是小写。第4个函数为第3个函数提供合适的分类参数。表B.5.54列出了这些函数。

<center class="my_markdown"><b class="my_markdown">表B.5.54　宽字符转换函数</b></center>

| 原型 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `wint_t towlower(wint_t wc);` | 如果 `wc` 是大写字符，返回其小写形式；否则返回 `wc` |
| `wint_t towupper(wint_t wc);` | 如果 `wc` 是小写字符，返回其大写形式；否则返回 `wc` |
| `wint_t towctrans(wint_t wc, wctrans_t` | `desc);` | 如果 `desc` 等于 `wctrans("lower")` 的返回值，函数返回 `wc` 的小写形式（由 `LC_CTYPE` 设置确定）；如果 `dest` 等于 `wctrans("upper")` 的返回值，函数返回 `wc` 的大写形式（由 `LC_CTYPE` 设置确定） |
| `wctrans_t wctrans(const char` * `property);` | 如果参数是 `"lower"` 或 `"upper"` ，函数返回一个 `wctrans_t` 类型的值，可用作 `towctrans()` 的参数并反映 `LC_CTYPE` 设置，否则函数返回 `0` |

