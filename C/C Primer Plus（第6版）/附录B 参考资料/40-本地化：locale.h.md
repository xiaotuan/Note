#### B.5.9　本地化： `locale.h` 

本地化是一组设置，用于控制一些特定的设置项，如表示小数点的符号。本地值存储在 `struct lconv` 类型的结构中，定义在 `locale.h` 头文件中。可以用一个字符串来指定本地化，该字符串指定了一组结构成员的特殊值。默认的本地化由字符串 `"C"` 指定。表B.5.12列出了本地化函数，后面做了简要说明。

<center class="my_markdown"><b class="my_markdown">表B.5.12　本地化函数</b></center>

| 原型 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `char`  *  `setlocale(int category,` | `const char`  *  `locale);` | 该函数把某些值设置为本地和 `locale` 指定的值。 `category` 的值决定要设置哪些本地值（参见B.5.13）。如果成功设置本地化，该函数将返回一个在新本地化中与指定类别相关联的指针；如果不能完成本地化请求，则返回空指针 |
| `struct lconv`  * `localeconv(void);` | 返回一个指向 `struct lconv` 类型结构的指针，该结构中存储着当前的本地值 |

`setlocale()` 函数的 `locale` 形参所需的值可能是默认值 `"C"` ，也可能是 `""` ，表示实现定义的本地环境。实现可以定义更多的本地化设置。 `category` 形参的值可能由表B.5.13中所列的宏表示。

<center class="my_markdown"><b class="my_markdown">表B.5.13　 `category` 宏</b></center>

| 原型 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `NULL` | 本地化设置不变，返回指向当前本地化的指针 |
| `LC_ALL` | 改变所有的本地值 |
| `LC_COLLATE` | 改变 `strcoll()` 和 `strxfrm()` 所用的排列顺序的本地值 |
| `LC_CTYPE` | 改变字符处理函数和多字节函数的本地值 |
| `LC_MONETARY` | 改变货币格式信息的本地值 |
| `LC_NUMERIC` | 改变十进制小数点符号和格式化 `I/O` 使用的非货币格式本地值 |
| `LC_TIME` | 改变 `strftime()` 所用的时间格式本地值 |

表B.5.14列出了 `struct lconv` 结构所需的成员。

<center class="my_markdown"><b class="my_markdown">表B.5.14　 `struct lcconv` 所需的成员</b></center>

| 成员变量 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `char`  * `decimal_point` | 非货币值的小数点字符 |
| `char`  * `thousands_sep` | 非货币值中小数点前面的千位分隔符 |
| `char`  * `grouping` | 一个字符串，表示非货币量中每组数字的大小 |
| `char`  * `int_curr_symbol` | 国际货币符号 |
| `char`  * `currency_symbol` | 本地货币符号 |
| `char`  * `mon_decimal_point` | 货币值的小数点符号 |
| `char`  * `mon_thousands_sep` | 货币值的千位分隔符 |
| `char`  * `mon_grouping` | 一个字符串，表示货币量中每组数字的大小 |
| `char`  * `positive_sign` | 指明非负格式化货币值的字符串 |
| `char`  * `negative_sign` | 指明负格式化货币值的字符串 |
| `char int_frac_digits` | 国际格式化货币值中，小数点后面的数字个数 |
| `char frac_digits` | 本地格式化货币值中，小数点后面的数字个数 |
| `char p_cs_precedes` | 如果该值为 `1` ，则 `currency_symbol` 在非负格式化货币值的前面； | 如果该值为 `0` ，则 `currency_symbol` 在非负格式化货币值的后面 |
| `char p_sep_by_space` | 如果该值为 `1` ，则用空格把 `currency_symbol` 和非负格式化货币值隔开； | 如果该值为 `0` ，则不用空格分隔 `currency_symbol` 和非负格式化货币值 |
| `char n_cs_precedes` | 如果该值为 `1` ，则 `currency_symbol` 在负格式化货币值的前面； | 如果该值为 `0` ，则 `currency_symbol` 在负格式化货币值的后面 |
| `char n_sep_by_space` | 如果该值为 `1` ，则用空格把 `currency_symbol` 和负格式化货币值隔开； | 如果该值为 `0` ，则不用空格分隔 `currency_symbol` 和负格式化货币值 |
| `char p_sign_posn` | 其值表示 `positive_sign` 字符串的位置： | `0` 表示用圆括号把数值和货币符号括起来 | `1` 表示字符串在数值和货币符号前面 | `2` 表示字符串在数值和货币符号后面 | `3` 表示直接把字符串放在货币前面 | `4` 表示字符串紧跟在货币符号后面 |
| `char n_sign_posn` | 其值表示 `negative_sign` 字符串的位置，含义与 `p_sign_posn` 相同 |
| `char int_p_cs_precedes` | 如果该值为 `1` ，则 `int_currency_symbol` 在非负格式化货币值的前面； | 如果该值为 `0` ，则 `int_currency_symbol` 在非负格式化货币值的后面 |
| `char int_p_sep_by_space` | 如果该值为 `1` ，则用空格把 `int_currency_symbol` 和非负格式化货币值隔开；如果该值为 `0` ，则不用空格分隔 `int_currency_symbol` 和非负格式化货币值 |
| `char int_n_cs_precedes` | 如果该值为 `1` ，则 `int_currency_symbol` 在负格式化货币值的前面； | 如果该值为 `0` ，则 `int_currency_symbol` 在负格式化货币值的后面 |
| `char int_n_sep_by_space` | 如果该值为 `1` ，则用空格把 `int_currency_symbol` 和负格式化货币值隔开；如果该值为 `0` ，则不用空格分隔 `int_currency_symbol` 和负格式化货币值 |
| `char int_p_sign_posn` | 其值表示 `positive_sign` 相对于非负国际格式化货币值的位置 |
| `char int_n_sign_posn` | 其值表示 `negative_sign` 相对于负国际格式化货币值的位置 |

