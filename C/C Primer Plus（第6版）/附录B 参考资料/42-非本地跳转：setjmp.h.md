#### B.5.11　非本地跳转： `setjmp.h` 

`setjmp.h` 头文件可以让你不遵循通常的函数调用、函数返回顺序。 `setjmp()` 函数把当前执行环境的信息（例如，指向当前指令的指针）存储在 `jmp_buf` 类型（定义在 `setjmp.h` 头文件中的数组类型）的变量中，然后 `longjmp()` 函数把执行转至这个环境中。这些函数主要是用来处理错误条件，并不是通常程序流控制的一部分。表B.5.17列出了这些函数。

<center class="my_markdown"><b class="my_markdown">表B.5.17　 `setjmp.h` 中的函数</b></center>

| 原型 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `int setjmp(jmp_buf env);` | 把调用环境存储在数组 `env` 中，如果是直接调用，则返回 `0` ；如果是通过 `longjmp()` 调用，则返回非 `0` |
| `void longjmp(jmp_buf env,` | `int val);` | 恢复最近的 `setjmp()` 调用（设置 `env` 数组）存储的环境；完成后，程序继续像调用 `setjmp()` 那样执行该函数，返回 `val` （但是该函数不允许返回 `0` ，会将其转换成 `1` ） |

