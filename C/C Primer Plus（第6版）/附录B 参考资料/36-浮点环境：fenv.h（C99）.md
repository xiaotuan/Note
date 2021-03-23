#### B.5.5　浮点环境： `fenv.h` （C99）

C99标准通过 `fenv.h` 头文件提供访问和控制浮点环境。

浮点环境（floating-point environment）由一组状态标志（status flag）和控制模式（control mode）组成。在浮点计算中发生异常情况时（如，被零除），可以“抛出一个异常”。这意味着该异常情况设置了一个浮点环境标志。控制模式值可以进行一些控制，例如控制舍入的方向。 `fenv.h` 头文件定义了一组宏表示多种异常情况和控制模式，并提供了与环境交互的函数原型。头文件还提供了一个编译指令来启用或禁用访问浮点环境的功能。

下面的指令开启访问浮点环境：

```c
#pragma STDC FENV_ACCESS on
```

下面的指令关闭访问浮点环境：

```c
#pragma STDC FENV_ACCESS off
```

应该把该编译指示放在所有外部声明之前或者复合块的开始处。在遇到下一个编译指示之前、或到达文件末尾（外部指令）、或到达复合语句的末尾（块指令），当前编译指示一直有效。

头文件定义了两种类型，如表B.5.6所示。

<center class="my_markdown"><b class="my_markdown">表B.5.6　 `fenv.h` 类型</b></center>

| 类型 | 表示 |
| :-----  | :-----  | :-----  | :-----  |
| `fenv_t` | 整个浮点环境 |
| `fexcept_t` | 浮点状态标志集合 |

头文件定义了一些宏，表示一些可能发生的浮点异常情况控制状态。其他实现可能定义更多的宏，但是必须以 `FE_` 开头，后面跟大写字母。表B.5.7列出了一些标准异常宏。

<center class="my_markdown"><b class="my_markdown">表B.5.7　 `fenv.h` 中的标准异常宏</b></center>

| 宏 | 含义 |
| :-----  | :-----  | :-----  | :-----  |
| `FE_DIVBYZERO` | 抛出被零除异常 |
| `FE_INEXACT` | 抛出不精确值异常 |
| `FE_INVALID` | 抛出无效值异常 |
| `FE_OVERFLOW` | 抛出上溢异常 |
| `FE_UNDERFLOW` | 抛出下溢异常 |
| `FE_ALL_EXCEPT` | 实现支持的所有浮点异常的按位或 |
| `FE_DOWNWARD` | 向下舍入 |
| `FE_TONEAREST` | 向最近的舍入 |
| `FE_TOWARDZERO` | 趋 `0` 舍入 |
| `FE_UPWARD` | 向上舍入 |
| `FE_DFL_ENV` | 表示默认环境，类型是 `const fenv_t`  * |

表B.5.8中列出了 `fenv.h` 头文件中的标准函数原型。注意，常用的参数值和返回值与表B.5.7中的宏相对应。例如， `FE_UPWARD` 是 `fesetround()` 的一个合适参数。

<center class="my_markdown"><b class="my_markdown">表B.5.8　 `fenv.h` 中的标准函数原型</b></center>

| 原型 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `void feclearexcept(int excepts);` | 清理 `excepts` 表示的异常 |
| `void fegetexceptflag(fexcept_t`  * `flagp, int excepts);` | 把 `excepts` 指明的浮点状态标志存储在 `flagp` 指向的对象中 |
| `void feraiseexcept(int excepts);` | 抛出 `excepts` 指定的异常 |
| `void fesetexceptflag(const fexcept_t`  * `flagp, intexcepts);` | 把 `excepts` 指明的浮点状态标志设置为 `flagp` 的值；在此之前， `fegetexceptflag()` 调用应该设置 `flagp` 的值 |
| `int fetestexcept(int excepts);` | 测试 `excepts` 指定的状态标志；该函数返回指定状态标志的按位或 |
| `int fegetround(void);` | 返回当前的舍入方向 |
| `int fesetround(int round);` | 把舍入方向设置为 `round` 的值；当且仅当设置成功时，函数返回 `0` |
| `void fegetenv(fenv_t`  * `envp);` | 把当前环境存储至 `envp` 指向的位置中 |
| `int feholdexcept(fenv_t`  * `envp);` | 把当前浮点环境存储至 `envp` 指向的位置中，清除浮点状态标志，然后如果可能的话就设置非停模式（nonstop mode），在这种模式中即使发生异常也继续执行。当且仅当执行成功时，函数返回 `0` |
| `void fesetenv(const fenv_t`  * `envp);` | 建立 `envp` 表示的浮点环境； `envp` 应指向一个之前通过调用 `fegetenv()` 、 `feholdexcept()` 或浮点环境宏设置的数据对象 |
| `void feupdateenv` | `(const fenv_t`  * `envp);` | 函数在自动存储区中存储当前抛出的异常，建立 `envp` 指向的对象表示的浮点环境，然后抛出已存储的浮点异常； `envp` 应指向一个之前通过调用 `fegetenv()` 、 `feholdexcept()` 或浮点环境宏设置的数据对象 |

