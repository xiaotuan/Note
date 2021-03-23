#### B.5.10　数学库： `math.h` 

C99为 `math.h` 头文件定义了两种类型： `float_t` 和 `double_t` 。这两种类型分别与 `float` 和 `double` 类型至少等宽，是计算 `float` 和 `double` 时效率最高的类型。

该头文件还定义了一些宏，如表B.5.15所列。该表中除了 `HUGE_VAL` 外，都是 `C99` 新增的。在参考资料VIII：“C99数值计算增强”中会进一步详细介绍。

<center class="my_markdown"><b class="my_markdown">表B.5.15　 `math.h` 宏</b></center>

| 宏 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `HUGE_VAL` | 正双精度常量，不一定能用浮点数表示；在过去，函数的计算结果超过了可表示的最大值时，就用它作为函数的返回值 |
| `HUGE_VALF` | 与 `HUGE_VAL` 类似，适用于 `float` 类型 |
| `HUGE_VALL` | 与 `HUGE_VAL` 类似，适用于 `long double` 类型 |
| `INFINITY` | 如果允许的话，展开为一个表示无符号或正无穷大的常量 `float` 表达式；否则，展开为一个在编译时溢出的正浮点常量 |
| `NAN` | 当且仅当实现支持 `float` 类型的 `NaN` 时才被定义（ `NaN` 是 `Not-a-Number` 的缩写，表示“非数”，用于处理计算中的错误情况，如除以 `0.0` 或求负数的平方根） |
| `FP_INFINITE` | 分类数，表示一个无穷大的浮点值 |
| `FP_NAN` | 分类数，表示一个不是数的浮点值 |
| `FP_NORMAL` | 分类数，表示一个正常的浮点值 |
| `FP_SUBNORMAL` | 分类数，表示一个低于正常浮点值的值（精度被降低） |
| `FP_ZERO` | 分类数，表示 `0` 的浮点值 |
| `FP_FAST_FMA` | （可选）如果已定义，对于 `double` 类型的运算对象，该宏表明 `fma()` 函数与先乘法运算后加法运算的速度相当或更快 |
| `FP_FAST_FMAF` | （可选）如果已定义，对于 `double` 类型的运算对象，该宏表明 `fmaf()` 函数与先乘法运算后加法运算的速度相当或更快 |
| `FP_FAST_FMAL` | （可选）如果已定义，对于 `long double` 类型的运算对象，该宏表明 `fmal()` 函数与先乘法运算后加法运算的速度相当或更快 |
| `FP_ILOGB0` | 整型常量表达式，表示 `ilogn(0)` 的返回值 |
| `FP_ILOGBNAN` | 整型常量表达式，表示 `ilogn(NaN)` 的返回值 |
| `MATH_ERRNO` | 展开为整型常量 `1` |
| `MATH_ERREXCEPT` | 展开为整型常量 `2` |
| `math_errhandling` | 值为 `MATH_ERRNO` 、 `MATH_ERREXCEPT` 或这两个值的按位或 |

数学函数通常使用 `double` 类型的值。C99新增了这些函数的 `float` 和 `long double` 版本，其函数名为分别在原函数名后添加 `f` 后缀和 `l` 后缀。例如，C语言现在提供这些函数原型：

```c
double sin(double);
float sinf(float);
long double sinl(long double);
```

篇幅有限，表B.5.16仅列出了数学库中这些函数的 `double` 版本。该表引用了 `FLT_RADIX` ，该常量定义在 `float.h` 中，代表内部浮点表示法中幂的底数。最常用的值是 `2` 。

<center class="my_markdown"><b class="my_markdown">表B.5.16　ANSI C标准数学函数</b></center>

| 原型 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| `int classify(real-floating x);` | C99宏，返回适合 `x` 的浮点分类值 |
| `int isfinite(real-floating x);` | C99宏，当且仅当 `x` 为有穷时返回一个非 `0` 值 |
| `int isfin(real-floating x);` | C99宏，当且仅当 `x` 为无穷时返回一个非 `0` 值 |
| `int isnan(real-floating x);` | C99宏，当且仅当 `x` 为 `NaN` 时返回一个非 `0` 值 |
| `int isnormal(real-floating x);` | C99宏，当且仅当 `x` 为正常数时返回一个非 `0` 值 |
| `int signbit(real-floating x);` | C99宏，当且仅当 `x` 的符号为负时返回一个非 `0` 值 |
| `double acos(double x);` | 返回余弦为 `x` 的角度（ `0` ～π弧度） |
| `double asin(double x);` | 返回正弦为 `x` 的角度（ `-` π `/2` ～π `/2` 弧度） |
| `double atan(double x);` | 返回正切为 `x` 的角度（ `-` π `/2` ～π `/2` 弧度） |
| `double atan2(double y, double x);` | 返回正切为 `y/x` 的角度（ `-` π～π弧度） |
| `double cos(double x);` | 返回 `x` （弧度）的余弦值 |
| `double sin(double x);` | 返回 `x` （弧度）的正弦值 |
| `double tan(double x);` | 返回 `x` （弧度）的正切值 |
| `double cosh(double x);` | 返回 `x` 的双曲余弦值 |
| `double sinh(double x);` | 返回 `x` 的双曲正弦值 |
| `double tanh(double x);` | 返回 `x` 的双曲切值 |
| `double exp(double x);` | 返回 `e` 的 `x` 次幂（ `e<sup class="my_markdown">x</sup>` ） |
| `double exp2(double x);` | 返回 `2` 的 `x` 次幂（ `2<sup class="my_markdown">x</sup>` ） |
| `double expm1(double x);` | 返回 `e<sup class="my_markdown">x</sup> - 1` （C99） |
| `double frexp(double v, int`  * `pt_e);` | 把 `v` 的值分成两部分，一个是返回的规范化小数；一个是 `2` 的幂，存储在 `pt_e` 指向的位置上 |
| `int ilogb(double x);` | 以 `signed int` 类型返回 `x` 的指数（C99） |
| `double ldexp(double x, int p);` | 返回 `x` 乘以 `2` 的 `p` 次幂（即 `x`  *  `2<sup class="my_markdown">p</sup>` ） |
| `double log(double x);` | 返回 `x` 的自然对数 |
| `double log10(double x);` | 返回以 `10` 为底 `x` 的对数 |
| `double log1p(double x);` | 返回 `log(1 + x)` （C99） |
| `double log2(double x);` | 返回以 `2` 为底 `x` 的对数（C99） |
| `double logb(double x);` | 返回 `FLT_RADIX` （系统内部浮点表示法中幂的底数）为底 `x` 的有符号对数（C99） |
| `double modf(double x, double`  * `p);` | 把 `x` 分成整数部分和小数部分，两部分的符号相同，返回小数部分，并把整数部分存储在 `p` 所指向的位置上 |
| `double scalbn(double x, int n);` | 返回 `x`  ×  `FLT_RADIX<sup class="my_markdown">n</sup>` （C99） |
| `double scalbln(double x, long n);` | 返回 `x`  ×  `FLT_RADIX<sup class="my_markdown">n</sup>` （C99） |
| `double cbrt(double x);` | 返回 `x` 的立方根（C99） |
| `double hypot(double x, double y);` | 返回 `x` 平方与 `y` 平方之和的平方根（C99） |
| `double pow(double x, double y);` | 返回 `x` 的 `y` 次幂 |
| `double sqrt(double x);` | 返回 `x` 的平方根 |
| `double erf(double x);` | 返回 `x` 的误差函数（C99） |
| `double lgamma(double x);` | 返回 `x` 的伽马函数绝对值的自然对数（C99） |
| `double tgamma(double x);` | 返回 `x` 的伽马函数（C99） |
| `double ceil(double x);` | 返回不小于 `x` 的最小整数值 |
| `double fabs(double x);` | 返回 `x` 的绝对值 |
| `double floor(double x);` | 返回不大于 `x` 的最大值 |
| `double nearbyint(double x);` | 以浮点格式把 `x` 四舍五入为最接近的整数；使用浮点环境指定的舍入规则（C99） |
| `double rint(double x);` | 与 `nearbyint()` 类似，但是该函数会抛出“不精确”异常 |
| `long int lrint(double x);` | 以 `long int` 格式把 `x` 舍入为最接近的整数；使用浮点环境指定的舍入规则（C99） |
| `long long int llrint(double x);` | 以 `long long int` 格式把 `x` 舍入为最接近的整数；使用浮点环境指定的舍入规则（C99） |
| `double round(double x);` | 以浮点格式把 `x` 舍入为最接近的整数，总是四舍五入 |
| `long int lround(double x);` | 与 `round()` 类似，但是该函数返回值的类型是 `long int` |
| `long long int llround(double x);` | 与 `round()` 类似，但是该函数返回值的类型是 `long long int` |
| `double trunc(double x);` | 以浮点格式把 `x` 舍入为最接近的整数，其结果的绝对值不大于 `x` 的绝对值（C99） |
| `int fmod(double x, double y);` | 返回 `x/y` 的小数部分，如果 `y` 不是 `0` ，则其计算结果的符号与 `x` 相同，而且该结果的绝对值要小于 `y` 的绝对值 |
| `double remainder(double x, double y);` | 返回 `x` 除以 `y` 的余数， `IEC 60559` 定义为 `x - n` * `y` ， `n` 取与 `x/y` 最接近的整数；如果 `(n - x/y)` 的绝对值是 `1/2` ， `n` 取偶数 |
| `double remquo(double x, double y,` | `int`  * `quo);` | 返回与 `remainder()` 相同的值；把 `x/y` 的整数大小求模 `2<sup class="my_markdown">k</sup>` 的值存储在 `quo` 所指向的位置中，符号与 `x/y` 的符号相同，其中 `k` 为整数，至少是 `3` ，具体值因实现而异（C99） |
| `double copysign(double x, double y);` | 返回 `x` 的大小和 `y` 的符号（C99） |
| `double nan(const char`  * `tagp);` | 返回以 `double` 类型表示的 `quiet NaN` <sup class="my_markdown">[2]</sup>； | `nan("n-char-seq")` 与 `strtod("NAN(n-char-seq)"` ,  `(char`  ** `)NULL)` 等价； `nan("")` 与 `strtod("NAN()"` ,  `(char` ** `)NULL)` 等价。如果不支持 `quiet NaN` ，则返回 `0` |
| `double nextafter(double x, double y);` | 返回 `x` 在 `y` 方向上可表示的最接近的 `double` 类型值；如果 `x` 等于 `y` ，则返回 `x` （C99） |
| `double nexttoward(double x, long` | `double y);` | 与 `nextafter()` 类似，但该函数的第2个参数是 `long double` 类型；如果 `x` 等于 `y` ，则返回转换为 `double` 类型的 `y` （C99） |
| `double fdim(double x, double y);` | 如果 `x` 大于 `y` ，则返回 `x - y` 的值；如果 `x` 小于或等于 `y` ，则返回 `0` （C99） |
| `double fmax(double x, double y);` | 返回参数的最大值，如果一个参数是 `NaN` 、另一个参数是数值，则返回数值（C99） |
| `double fmin(double x, double y);` | 返回参数的最小值，如果一个参数是 `NaN` 、另一个参数是数值，则返回数值（C99） |
| `double fma(double x, double y,` | `double z);` | 返回三元运算 `(x` * `y)+z` 的大小，只在最后舍入一次（C99） |
| `int isgreater(real-floating x,` | `real-floating y);` | C99宏，返回 `(x)>(y)` 的值，如果有参数是 `NaN` ，不会抛出“无效”浮点异常 |
| `int isgreaterequal(real-floating` | `x,real-floating y);` | C99宏，返回 `(x)>=(y)` 的值，如果有参数是 `NaN` ，不会抛出无效浮点异常 |
| `int isless(real-floating x,` | `real-floating y);` | C99宏，返回 `(x)<(y)` 的值，如果有参数是 `NaN` ，不会抛出无效浮点异常 |
| `int islessequal(real-floating x,` | `real-floating y);` | C99宏，返回 `(x)<=(y)` 的值，如果有参数是 `NaN` ，不会抛出无效浮点异常 |
| `int islessgreater(real-floating x,` | `real-floating y);` | C99宏，返回 `(x)<(y)|| (x)>(y)` 的值，如果有参数是 `NaN` ，不会抛出无效浮点异常 |
| `int isunordered(real-floating x,` | `real-floating y);` | 如果参数不按顺序排列（至少有一个参数是 `NaN` ），函数返回 `1` ；否则，返回 `0` |

