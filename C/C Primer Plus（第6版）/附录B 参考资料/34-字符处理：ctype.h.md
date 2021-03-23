#### B.5.3　字符处理： `ctype.h` 

这些函数都接受 `int` 类型的参数，这些参数可以表示为 `unsigned char` 类型的值或 `EOF` 。使用其他值的效果是未定义的。在表B.5.4中，“真”表示“非 `0` 值”。对一些定义的解释取决于当前的本地设置，这些由 `locale.h` 中的函数来控制。该表显示了在解释本地化的“ `C` ”时要用到的一些函数。

<center class="my_markdown"><b class="my_markdown">表B.5.4　字符处理函数</b></center>

| 原型 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `int isalnum(int c);` | 如果 `c` 是字母或数字，则返回真 |
| `int isalpha(int c);` | 如果 `c` 是字母，则返回真 |
| `int isblank(int c);` | 如果 `c` 是空格或水平制表符，则返回真（ `C99` ） |
| `int iscntrl(int c);` | 如果 `c` 是控制字符（如 `Ctrl+B` ），则返回真 |
| `int isdigit(int c);` | 如果 `c` 是数字，则返回真 |
| `int isgraph(int c);` | 如果 `c` 是非空格打印字符，则返回真 |
| `int islower(int c);` | 如果 `c` 是小写字符，则返回真 |
| `int isprint(int c);` | 如果 `c` 是打印字符，则返回真 |
| `int ispunct(int c);` | 如果 `c` 是标点字符（除了空格、字母、数字以外的字符），则返回真 |
| `int isspace(int c);` | 如果 `c` 是空白字符（空格、换行符、换页符、回车符、垂直或水平制表符，或者其他实现定义的字符），则返回真 |
| `int isupper(int c);` | 如果 `c` 是大写字符，则返回真 |
| `int isxdigit(int c);` | 如果 `c` 是十六进制数字字符，则返回真 |
| `int tolower(int c);` | 如果 `c` 是大写字符，则返回其小写字符；否则返回 `c` |
| `int toupper(int c);` | 如果 `c` 是小写字符，则返回其大写字符；否则返回 `c` |

