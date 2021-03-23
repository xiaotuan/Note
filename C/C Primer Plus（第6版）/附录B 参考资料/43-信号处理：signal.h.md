#### B.5.12　信号处理： `signal.h` 

信号（signal）是在程序执行期间可以报告的一种情况，可以用正整数表示。 `raise()` 函数发送（或抛出）一个信号， `signal()` 函数设置特定信号的响应。

标准定义了一个整数类型： `sig_atomic_t` ，专门用于在处理信号时指定原子对象。也就是说，更新原子类型是不可分割的过程。

标准提供的宏列于表B.5.18中，它们表示可能的信号，可用作 `raise()` 和 `signal()` 的参数。当然，实现也可以添加更多的值。

<center class="my_markdown"><b class="my_markdown">表B.5.18　信号宏</b></center>

| 宏 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `SIGABRT` | 异常终止，例如 `abort()` 调用发出的信号 |
| `SIGFPE` | 错误的算术运算 |
| `SIGILL` | 检测到无效功能（例如，非法指令） |
| `SIGINT` | 接收到交互注意信号（如， `DOS` 中断） |
| `SIGSEGV` | 非法访问内存 |
| `SIGTERM` | 向程序发送终止请求 |

`signal()` 函数的第2个参数接受一个指向 `void` 函数的指针，该函数有一个 `int` 类型的参数，也返回相同类型的指针。为响应一个信号而被调用的函数称为信号处理器（signal handler）。标准定义了 `3` 个满足下面原型的宏：

`void (` * `funct)(int);`

表B.5.19列出了这3种宏。

<center class="my_markdown"><b class="my_markdown">表B.5.19　 `void (` * `f)(int)` 宏</b></center>

| 宏 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `SIG_DFL` | 当该宏与一个信号值一起作为 `signal()` 的参数时，表示默认处理信号 |
| `SIG_ERR` | 如果 `signal()` 不能返回它的第 `2` 个参数，就用该宏作为它的返回值 |
| `SIG_IGN` | 当该宏与一个信号值一起作为 `signal()` 的参数时，表示忽略信号 |

如果产生了信号 `sig` ，而且 `func` 指向一个函数（参见表B.5.20中 `signal()` 原型），那么大多数情况下先调用 `signal(sig, SIG_DFL)` 把信号重置为默认设置，然后调用 `(` * `func)(sig)` 。可以执行返回语句或调用 `abort()` 、 `exit()` 或 `longjmp()` 来结束 `func` 指向的信号处理函数。

<center class="my_markdown"><b class="my_markdown">表B.5.20　信号函数</b></center>

| 宏 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `void (` * `signal(int` | `sig, void (` * `func)` | `(int)))(int);` | 如果产生信号 `sig` ，则执行 `func` 指向的函数；如果能执行则返回 `func` ，否则返回 `SIG_ERR` |
| `int raise(int sig);` | 向执行程序发送信号 `sig` ；如果成功发送则返回 `0` ，否则返回非 `0` |

