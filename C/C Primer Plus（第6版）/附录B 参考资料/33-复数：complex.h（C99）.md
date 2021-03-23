#### B.5.2　复数： `complex.h` （C99）

C99标准支持复数计算，C11进一步支持了这个功能。实现除提供 `_Complex` 类型外还可以选择是否提供 `_Imaginary` 类型。在C11中，可以选择是否提供这两种类型。C99规定，实现必须提供 `_Complex` 类型，但是 `_Imaginary` 类型为可选，可以提供或不提供。附录B的参考资料VIII中进一步讨论了 `C` 如何支持复数。 `complex.h` 头文件中定义了表B.5.2所列的宏。

<center class="my_markdown"><b class="my_markdown">表B.5.2　 `complex.h` 宏</b></center>

| 宏 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `complex` | 展开为类型关键字 `_Complex` |
| `_Complex_I` | 展开为 `const float _Complex` 类型的表达式，其值的平方是 `-1` |
| `imaginary` | 如果支持虚数类型，展开为类型关键字 `_Imaginary` |
| `_Imaginary_I` | 如果支持虚数类型，展开为 `const float _Imaginary` 类型的表达式，其值的平方是 `-1` |
| `I` | 展开为 `_Complex_I` 或 `_Imaginary_I` |

对于实现复数方面，C和C++不同。C通过 `complex.h` 头文件支持，而C++通过 `complex` 头文件支持。而且，C++使用类来定义复数类型。

可以使用 `STDC CX_LIMITED_RANGE` 编译指令来表明是使用普通的数学公式（设置为 `on` 时），还是要特别注意极值（设置为 `off` 时）：

```c
#include <complex.h>
#pragma STDC CX_LIMITED_RANGE on
```

库函数分为3种： `double` 、 `float` 、 `long double` 。表B.5.3列出了 `double` 版本的函数。 `float` 和 `long double` 版本只需要在函数名后面分别加上 `f` 和 `l` 。即 `csinf()` 就是 `csin()` 的 `float` 版本，而 `csinl()` 是 `csin()` 的 `long double` 版本。另外要注意，角度的单位是弧度。

<center class="my_markdown"><b class="my_markdown">表B.5.3　复数函数</b></center>

| 原型 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `double complex cacos(double complex z);` | 返回 `z` 的复数反余弦 |
| `double complex casin(double complex z);` | 返回 `z` 的复数反正弦 |
| `double complex catan(double complex z);` | 返回 `z` 的复数反正切 |
| `double complex ccos(double complex z);` | 返回 `z` 的复数余弦 |
| `double complex csin(double complex z);` | 返回 `z` 的复数正弦 |
| `double complex ctan(double complex z);` | 返回 `z` 的复数正切 |
| `double complex cacosh(double complex z);` | 返回 `z` 的复数反双曲余弦 |
| `double complex casinh(double complex z);` | 返回 `z` 的复数反双曲正弦 |
| `double complex catanh(double complex z);` | 返回 `z` 的复数反双曲正切 |
| `double complex ccosh(double complex z);` | 返回 `z` 的复数双曲余弦 |
| `double complex csinh(double complex z);` | 返回 `z` 的复数双曲正弦 |
| `double complex ctanh(double complex z);` | 返回 `z` 的复数双曲正切 |
| `double complex cexp(double complex z);` | 返回 `e` 的 `z` 次幂复数值 |
| `double complex clog(double complex z);` | 返回 `z` 的自然对数（以 `e` 为底）的复数值 |
| `double cabs(double complex z);` | 返回 `z` 的绝对值（或大小） |
| `double complex cpows(double complex z,` | `double complex y);` | 返回 `z` 的 `y` 次幂 |
| `double complex csqrt(double complex z);` | 返回 `z` 的复数平方根 |
| `double carg(double complex z);` | 以弧度为单位返回 `z` 的相位角（或幅角） |
| `double cimag(double complex z);` | 以实数形式返回 `z` 的虚部 |
| `double complex conj(double complex z);` | 返回 `z` 的共轭复数 |
| `double complex cproj(double complex z);` | 返回 `z` 在黎曼球面上的投影 |
| `double complex CMPLX(double x,double y);` | 返回实部为 `x` 、虚部为 `y` 的复数（ `C11` ） |
| `double creal(double complex z);` | 以实数形式返回 `z` 的实部 |

