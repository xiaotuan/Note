#### B.5.23　通用类型数学： `tgmath.h` （C99）

`math.h` 和 `complex.h` 库中有许多类型不同但功能相似的函数。例如,下面6个都是计算正弦的函数：

```c
double sin(double);
float sinf(float);
long double sinl(long double);
double complex csin(double complex);
float csinf(float complex);
long double csinl(long double complex);
```

`tgmath.h` 头文件定义了展开为通用调用的宏，即根据指定的参数类型调用合适的函数。下面的代码演示了使用 `sin()` 宏时，展开为正弦函数的不同形式：

```c
#include <tgmath.h>
...
double dx, dy;
float fx, fy;
long double complex clx, cly;
dy = sin(dx);                    // 展开为dy = sin(dx) （函数）
fy = sin(fx);                    // 展开为fy = sinf(fx)
cly = sin(clx);                  // 展开为cly = csinl(clyx)
```

`tgmath.h` 头文件为 `3` 类函数定义了通用宏。第1类由 `math.h` 和 `complex.h` 中定义的 `6` 个函数的变式组成，用 `l` 和 `f` 后缀和 `c` 前缀，如前面的 `sin()` 函数所示。在这种情况下，通用宏名与该函数 `double` 类型版本的函数名相同。

第2类由 `math.h` 头文件中定义的 `3` 个函数变式组成，使用 `l` 和 `f` 后缀，没有对应的复数函数（如， `erf()` ）。在这种情况下，宏名与没有后缀的函数名相同，如 `erf()` 。使用带复数参数的这种宏的效果是未定义的。

第3类由 `complex.h` 头文件中定义的 `3` 个函数变式组成，使用 `l` 和 `f` 后缀，没有对应的实数函数，如 `cimag()` 。使用带实数参数的这种宏的效果是未定义的。

表B.5.38列出了一些通用宏函数。

<center class="my_markdown"><b class="my_markdown">表B.5.38　通用数学函数</b></center>

| `acos` | `asin` | `atanb` | `acosh` | `asinh` | `atanh` |
| :-----  | :-----  | :-----  | :-----  | :-----  | :-----  | :-----  | :-----  |
| `cos` | `sin` | `tan` | `cosh` | `sinh` | `tanh` |
| `exp` | `log` | `pow` | `sqrt` | `fabs` | `atan2` |
| `cbrt` | `ceil` | `copysign` | `erf` | `erfc` | `exp2` |
| `expm1` | `fdim` | `floor` | `fma` | `fmax` | `fmin` |
| `fmod` | `frexp` | `hypot` | `ilogb` | `ldexp` | `lgamma` |
| `llrint` | `llround` | `log10` | `log1p` | `log2` | `logb` |
| `lrint` | `lround` | `nearbyint` | `nextafter` | `nexttoward` | `remainder` |
| `remquo` | `rint` | `round` | `scalbn` | `scalbln` | `tgamma` |
| `trunc` | `carg` | `cimag` | `conj` | `cproj` | `creal` |

在C11以前，编写实现必须依赖扩展标准才能实现通用宏。但是使用C11新增的 `_Generic` 表达式可以直接实现。

