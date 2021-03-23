#### 16.10.3　 `tgmath.h` 库（C99）

C99标准提供的 `tgmath.h` 头文件中定义了泛型类型宏，其效果与程序清单16.15类似。如果在 `math.h` 中为一个函数定义了3种类型（ `float` 、 `double` 和 `long double` ）的版本，那么 `tgmath.h` 文件就创建一个泛型类型宏，与原来 `double` 版本的函数名同名。例如，根据提供的参数类型，定义 `sqrt()` 宏展开为 `sqrtf()` 、 `sqrt()` 或 `sqrtl()` 函数。换言之， `sqrt()` 宏的行为和程序清单16.15中的 `SQRT()` 宏类似。

如果编译器支持复数运算，就会支持 `complex.h` 头文件，其中声明了与复数运算相关的函数。例如，声明有 `csqrtf()` 、 `csqrt()` 和 `csqrtl()` ，这些函数分别返回 `float complex` 、 `double complex` 和 `long double complex` 类型的复数平方根。如果提供这些支持，那么 `tgmath.h` 中的 `sqrt()` 宏也能展开为相应的复数平方根函数。

如果包含了 `tgmath.h` ，要调用 `sqrt()` 函数而不是 `sqrt()` 宏，可以用圆括号把被调用的函数名括起来：

```c
#include <tgmath.h>
...
　　 float x = 44.0;
　　 double y;
　　 y = sqrt(x);　　// 调用宏，所以是 sqrtf(x)
　　 y = (sqrt)(x);　// 调用函数 sqrt()
```

这样做没问题，因为类函数宏的名称必须用圆括号括起来。圆括号只会影响操作顺序，不会影响括起来的表达式，所以这样做得到的仍然是函数调用的结果。实际上，在讨论函数指针时提到过，由于C语言奇怪而矛盾的函数指针规则，还可以使用 `(` * `sqrt)()` 的形式来调用 `sqrt()` 函数。

不借助C标准以外的机制，C11新增的 `_Generic` 表达式是实现 `tgmath.h` 最简单的方式。

