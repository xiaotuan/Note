#### B.5.14　可变参数： `stdarg.h` 

`stdarg.h` 头文件提供一种方法定义参数数量可变的函数。这种函数的原型有一个形参列表，列表中至少有一个形参后面跟有省略号：

```c
void f1(int n, ...);                   /* 有效 */
int f2(int n, float x, int k, ...);    /* 有效 */
double f3(...);                        /* 无效 */
```

在下面的表中， `parmN` 是省略号前面的最后一个形参的标识符。在上面的例子中，第1种情况的 `parmN` 为 `n` ，第 `2` 种情况的 `parmN` 为 `k` 。

头文件中声明了 `va_lis` 类型表示存储形参列表中省略号部分的形参数据对象。表B.5.22中列出了3个带可变参数列表的函数中用到的宏。在使用这些宏之前要声明一个 `va_list` 类型的对象。

<center class="my_markdown"><b class="my_markdown">表B.5.22　可变参数列表宏</b></center>

| 宏 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `void va_start(va_list ap, parmN);` | 该宏在 `va_arg()` 和 `va_end()` 使用 `ap` 之前初始化 `ap` ，`parN`是形参列表中最后一个形参名的标识符 |
| `void va_copy(va_list dest, va_list src);` | 该宏把 `dest` 初始化为 `src` 当前状态的备份（C99） |
| `type va_arg(va_list ap, type );` | 该宏展开为一个表达式，其值和类型都与 `ap` 表示的形参列表的下一项相同， `type` 是该项的类型。每次调用该宏都前进到 `ap` 中的下一项 |
| `void va_end(va_list ap);` | 该宏关闭以上过程，可能导致 `ap` 在再次调用 `va_start()` 之前不可用 |
| `void va_copy(va_list dest, va_list src);` | 该宏把 `dest` 初始化为 `srt` 当前状态的备份（C99） |

