#### B.5.20　通用工具： `stdlib.h` 

ANSI C标准库在 `stdlib.h` 头文件中定义了一些实用函数。该头文件定义了一些类型，如表B.5.34所示。

<center class="my_markdown"><b class="my_markdown">表B.5.34　 `stdlib.h` 中声明的类型</b></center>

| 类型 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `size_t` | `sizeof` 运算符返回的整数类型 |
| `wchar_t` | 用于表示宽字符的整数类型 |
| `div_t` | `div()` 返回的结构类型，该类型中的 `quot` 和 `rem` 成员都是 `int` 类型 |
| `ldiv_t` | `ldiv()` 返回的结构类型，该类型中的 `quot` 和 `rem` 成员都是 `long` 类型 |
| `lldiv_t` | `lldiv()` 返回的结构类型，该类型中的 `quot` 和 `rem` 成员都是 `long long` 类型（C99） |

`stdlib.h` 头文件定义的常量列于表B.5.35中。

<center class="my_markdown"><b class="my_markdown">表B.5.35　 `stdlib.h` 中定义的常量</b></center>

| 类型 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `NULL` | 空指针（相当于 `0` ） |
| `EXIT_FAILURE` | 可用作 `exit()` 的参数，表示执行程序失败 |
| `EXIT_SUCCESS` | 可用作 `exit()` 的参数，表示成功执行程序 |
| `RAND_MAX` | `rand()` 返回的最大值（一个整数） |
| `MB_CUR_MAX` | 当前本地化的扩展字符集中多字节字符的最大字节数 |

表B.5.36列出了 `stdlib.h` 中的函数原型。

<center class="my_markdown"><b class="my_markdown">表B.5.36　通用工具</b></center>

| 原型 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `double atof(const char`  *  `nptr);` | 返回把字符串 `nptr` 开始部分的数字（和符号）字符转换为 `double` 类型的值，跳过开始的空白，遇到第1个非数字字符时结束转换；如果未发现数字则返回 `0` |
| `int atoi(const char` *  `nptr);` | 返回把字符串 `nptr` 开始部分的数字（和符号）字符转换为 `int` 类型的值，跳过开始的空白，遇到第1个非数字字符时结束转换；如果未发现数字则返回 `0` |
| `int atol(const char` *  `nptr);` | 返回把字符串 `nptr` 开始部分的数字（和符号）字符转换为 `long` 类型的值，跳过开始的空白，遇到第1个非数字字符时结束转换；如果未发现数字则返回 `0` |
| `double strtod(const char` *  `restrict npt,char`  **  `restrictept);` | 返回把字符串 `npt` 开始部分的数字（和符号）字符转换为 `double` 类型的值，跳过开始的空白，遇到第1个非数字字符时结束转换；如果未发现数字则返回 `0` ；如果转换成功，则把数字后第 `1` 个字符的地址赋给 `ept` 指向的位置；如果转换失败，则把 `npt` 赋给 `ept` 指向的位置 |
| `float strtof(const char`  *  `restrictnpt,char`  **  `restrict ept);` | 与 `strtod()` 类似，但是该函数把 `npt` 指向的字符串转换为 `float` 类型的值（C99） |
| `long double strtols(const char`  * | `restrictnpt, char`  ** `restrict ept);` | 与 `strtod()` 类似，但是该函数把 `npt` 指向的字符串转换成 `long double` 类型的值（C99） |
| `long strtol(const char`  *  `restrict npt` | `char`  **  `restrict ept, int base);` | 返回把字符串 `npt` 开始部分的数字（和符号）字符转换成 `long` 类型的值，跳过开始的空白，遇到第1个非数字字符时结束转换；如果未发现数字则返回 `0` ；如果转换成功，则把数字后第 `1` 个字符的地址赋给 `ept` 指向的位置；如果转换失败，则把 `npt` 赋给 `ept` 指向的位置；假定字符串中的数字以 `base` 指定的数为基数 |
| `long long strtoll(const char`  * `restrict npt, char` **  `restrict ept,int base);` | 与 `strtol()` 类似，但是该函数把 `npt` 指向的字符串转换为 `long long` 类型的值（C99） |
| `unsigned long strtoul(const char`  * | `restrict npt, char` **  `restrict ept,` | `int base);` | 返回把字符串 `npt` 开始部分的数字（和符号）字符转换为 `unsigned long` 类型的值，跳过开始的空白，遇到第1个非数字字符时结束转换；如果未发现数字则返回 `0` ；如果转换成功，则把数字后第 `1` 个字符的地址赋给 `ept` 指向的位置；如果转换失败，则把 `npt` 赋给 `ept` 指向的位置；假定字符串中的数字以 `base` 指定的数为基数 |
| `unsigned long long strtoull(const char` *  `restrict npt,char`  **  `restrict` | `ept, int base);` | 与 `strtoul()` 类似，但是该函数把 `npt` 指向的字符串转换为 `unsigned long long` 类型的值（C99） |
| `int rand(void);` | 返回 `0` ～ `RAND_MAX` 范围内的一个伪随机整数 |
| `void srand(unsigned int seed);` | 把随机数生成器种子设置为 `seed` ，如果在调用 `rand()` 之前调用 `srand()` ，则种子为 `1` |
| `void`  * `aligned_alloc(size_t algn,` | `size_t size);` | 为对齐对象 `algn` 分配 `size` 字节的空间，应支持 `algn` 对齐值， `size` 应该是 `algn` 的倍数（ `C11` ） |
| `void`  * `calloc(size_t nmem, size_t size);` | 为内含 `nmem` 个成员的数组分配空间，每个元素占 `size` 字节大；空间中的所有位都初始化为 `0` ；如果操作成功，该函数返回数组的地址，否则返回 `NULL` |
| `void free(void` * `ptr);` | 释放 `ptr` 指向的空间， `ptr` 应该是之前调用 `calloc()` 、 `malloc()` 或 `realloc()` 返回的值，或者 `ptr` 也可以是空指针，出现这种情况时什么也不做。如果 `ptr` 是其他值，其行为是未定义的 |
| `void`  * `malloc(size_t size);` | 分配 `size` 字节的未初始化内存块；如果成功分配，该函数返回数组的地址，否则返回 `NULL` |
| `void`  * `realloc(void` * `ptr, size_t size);` | 把 `ptr` 指向的内存块大小改为 `size` 字节， `size` 字节内的内存块内容不变。该函数返回块的位置，它可能被移动。如果不能重新分配空间，函数返回 `NULL` ，原始块不变；如果 `ptr` 为 `NULL` ，其行为与调用带 `size` 参数的 `malloc()` 相同；如果 `size` 是 `0` ，且 `ptr` 不是 `NULL` ，其行为与调用带 `ptr` 参数的 `free()` 相同 |
| `void abort(void);` | 除非捕获信号 `SIGABRT` ，且相应的信号处理器没有返回，否则该函数将导致程序异常结束。是否关闭 `I/O` 流和临时文件，因实现而异。该函数执行 `raise(SIGABRT)` |
| `int atexit(void(` * `func)(void));` | 注册 `func` 指向的函数，使其在程序正常结束时被调用。实现应支持注册至少 `32` 个函数，并根据它们注册顺序的逆序调用。如果注册成功，函数返回 `0` ；否则返回非 `0` |
| `int at_quick_exit(void (` * `func)(void));` | 注册 `func` 指向的函数，如果调用 `quick_exit()` 则调用被注册的函数。实现应支持注册至少 `32` 个函数，并根据它们注册顺序的逆序调用。如果注册成功，函数返回 `0` ；否则返回非 `0` （C11） |
| `void exit(int status);` | 该函数将正常结束程序。首先调用由 `atexit()` 注册的函数，然后刷新所有打开的输出流、关闭所有的I/O流、关闭 `tmpfile()` 创建的所有文件，并把控制权返回主机环境中；如果 `status` 是 `0` 或 `EXIT_SUCCESS` ，则返回一个实现定义的值，表明未成功结束程序 |
| `void _Exit(int status);` | 与 `exit()` 类似，但是该函数不调用 `atexit()` 注册的函数和 `signal()` 注册的信号处理器，其处理打开流的方式依实现而异 |
| `char`  * `getenv(const char`  *  `name);` | 返回一个指向字符串的指针，该字符串表示 `name` 指向的环境变量的值。如果无法匹配指定的 `name` ，则返回 `NULL` |
| `_Noreturn void quick_exit(int` | `status);` | 该函数将正常结束程序。不调用 `atexit()` 注册的函数和 `signal()` 注册的信号处理器。根据 `at_quick_exit()` 注册函数的顺序，逆序调用这些函数。如果程序多次调用 `quick_exit()` 或者同时调用 `quick_exit()` 和 `exit()` ，其行为是未定义的。通过调用 `_Exit(status)` 将控制权返回主机环境（C11） |
| `int system(const char`  * `str);` | 把 `str` 指向的字符串传递给命令处理器（如DOS或UNIX）执行的主机环境。如果 `str` 是 `NULL` 指针，且命令处理器可用，则该函数返回非 `0` ，否则返回；如果 `str` 不是 `NULL` ，返回值依实现而异 |
| `void`  * `bsearch(const void`  * `key, const` | `void`  * `base, size_tnmem, size_t size,` | `int (` * `comp)(const void`  * `, const void` | * `));` | 查找 `base` 指向的一个数组（有 `nmem` 个元素，每个元素的大小为 `size` ）中是否有元素匹配 `key` 指向的对象。通过 `comp` 指向的函数比较各项，如果 `key` 指向的对象小于数组元素，那么比较函数将返回小于 `0` 的值；如果两者相等，则返回 `0` ；如果 `key` 指向的对象大于数组元素，则返回大于 `0` 的值。该函数返回指向匹配元素的指针或 `NULL` （如果无匹配元素）。如果有多个元素匹配，未定义返回哪一个元素 |
| `void qsort(void` * `base, size_t nmem,` | `size_t size, int(` * `comp) (const void` | * `, const void`  * `));` | 根据 `comp` 指向的函数所提供的顺排列 `base` 指向的数组。该数组有 `nmem` 个元素，每个元素的大小是 `size` 。如果第 `1` 个参数指向的对象小于数组元素，那么比较函数将返回小于 `0` 的值；如果两者相等，则返回 `0` ；如果第 `1` 个参数指向的对象大于数组元素，则返回大于 `0` 的值 |
| `int abs(int n);` | 返回 `n` 的绝对值。如果 `n` 是负数但没有与之对应的正数，那么返回值是未定义的（当 `n` 是以二进制补码表示的 `INT_MIN` 时，会出现这种情况） |
| `div_t div(int numer, int denom);` | 计算 `number` 除以 `denom` 的商和余，把商和余数分别存储在 `div_t` 结构的 `quot` 成员和 `rem` 成员中。对于无法整除的除法，商要趋零截断（即直接截去小数部分） |
| `long labs(int n);` | 返回 `n` 的绝对值，如果 `n` 是负数但没有与之对应的正数，那么返回值是未定义的（当 `n` 是以二进制补码表示的 `LONG_MIN` 时，会出现这种情况） |
| `ldiv_t ldiv(long numer, long denom);` | 计算 `number` 除以 `denom` 的商和余，把商和余数分别存储在 `ldiv_t` 结构的 `quot` 成员和 `rem` 成员中。对于无法整除的除法，商要趋零截断（即直接截去小数部分） |
| `long long llabs(int n);` | 返回 `n` 的绝对值，如果 `n` 是负数但没有与之对应的正数，那么返回值是未定义的（当 `n` 是以二进制补码表示的 `LONG_LONG_MIN` 时，会出现这种情况） |
| `lldiv_t lldiv(long numer, long denom);` | 计算 `number` 除以 `denom` 的商和余，把商和余数分别存储在 `lldiv_t` 结构的 `quot` 成员和 `rem` 成员中。对于无法整除的除法，商要趋零截断（即直接截去小数部分）（C99） |
| `int mblen(const char`  * `s, size_t n);` | 返回组成 `s` 指向的多字节字符的字节数（最大为 `n` ）。如果 `s` 指向空字符，该函数则返回 `0` ；如果 `s` 未指向多字节字符，则返回 `-1` ；如果 `s` 是 `NULL` ，且多字节根据状态进行编码，该函数则返回非 `0` ，否则返回 `0` |
| `int mbtowc(wchar_t` * `pw, const char`  * `s,` | `size_t n);` | 如果 `s` 不是 `NULL` ，该函数确定了组成 `s` 指向的多字节字符的字节数（最大为 `n` ），并确定字符的 `wchar_t` 类型编码。如果 `pw` 不是 `NULL` ，则把类型编码赋给 `pw` 指向的位置。返回值与 `mblen(s, n)` 相同 |
| `int wctomb(char`  * `s,wchar_t wc);` | 把 `wc` 中的字符代码转换成相应的多字节字符表示，并将其存储在 `s` 指向的数组中，除非 `s` 是 `NULL` 。如果 `s` 不是 `NULL` ，且如果 `wc` 无法转换成相应的有效多字节字符，该函数返回 `-1` ；如果 `wc` 有效，该函数返回组成多字节的字节数；如果 `s` 是 `NULL` ，且如果多字节字符根据状态进行编码，该函数则返回非 `0` ，否则返回 `0` |
| `size_t mbstowcs(wchar_t`  * `restrict pwcs,const char`  * `srestrict ,size_t n);` | 把 `s` 指向的多字节字符数组转换成存储在 `pwcs` 开始位置的宽字符编码数组中，转换 `pwcs` 数组中的 `n` 个字符或转换到 `s` 数组的空字节停止。如果遇到无效的多字节字符，该函数返回 `(size_t)(-1);` ，否则返回已填充的数组元素个数（如果有空字符，不包含空字符） |
| `size_t wcstombs(char`  *  `restricts, const wchart_t` *  `restrict pwcs,size_t n);` | 把存储在 `pwcs` 指向数组中的宽字符编码序列转换成一个多字节字符序列，并把它拷贝到 `s` 指向的位置上，存储 `n` 个字节或遇到空字符时停止转换。如果遇到无效的宽字符编码，该函数返回 `(size_t)(-1)` ，否则返回已填充数组的字节数（如果有空字符，不包含空字符） |

