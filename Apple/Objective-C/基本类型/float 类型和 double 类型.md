在 `Objective-C`程序中，`float` 类型变量可以存储带有小数的值。在 `Objective-C` 程序中，不但可以省略小数点之前的数字，而且也可以省略之后的数字，但是不能将它们全部省略。例如下面的值都是合法的浮点常量：

```
3.
125.8
-.0001
```

要显示浮点值，可以用 `NSLog` 转换字符串 `%f` 来实现：

```objc
float pi = 3.141592f;
NSLog(@"π = %f", pi);
```

大多数计算机使用 64 位来表示 `double` 值。除非另有说明，否则 `Objective-C` 编译器将全部浮点常量当作 `double` 值。要想清楚地表示 `float` 常量，需要再数字的尾部添加字符 `f` 或 `F`，例如：

```
12.4f
```

要想显示 `double` 的值，可以使用格式符号 `%f` 、`%e` 或 `%g` 来实现，它们与显示 `float` 值所用的格式符号是相同的。

```objc
#import <Foundation/Foundation.h>

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        double pi =3.141592;
        NSLog(@"%f, %e, %g", pi, pi, pi);
    }
    return 0;
}
```

运行结果如下：

```shell
3.141592, 3.141592e+00, 3.14159
```

### 1. 浮点型常量

在 `Objective-C` 中有两种形式的浮点型常量：小数形式和指数形式。

+   小数形式：由数字 0 ~9 和小数点组成。例如： 5.789、-267.823。注意，此处必须有小数点。在 `NSLog` 中，需要使用 `%f` 格式输出小数形式的实数。

+   指数形式：由十进制数，加阶码标志 `e` 或 `E` 以及阶码（只能为整数，可以带符号）组成。其一般形式为：`a E n`（`a` 为十进制数，`n` 为十进制整数），其值为 a*10<sup>n</sup>。在 `NSLog` 中，使用 `%e` 格式来输出指数形式的实数。

    ```
    2.1E5 （等于 2.1 * 10^5）
    3.7E-2 (等于 3.7 * 10^-2)
    ```

`Objective-C` 允许浮点数使用后缀，后缀为 `f` 或 `F`，表示该数为单精度浮点数，例如 365f 和 365F。

### 2. 浮点数变量

浮点数类型有单精度浮点类型（`float` 类型）、双精度浮点类型（`double` 类型）和长双精度浮点类型（`long double` 类型）。在大多数机器上，单精度数占 4 个字节（32 位）内存空间，其数值范围为 3.4E-38 ~ 3.4E+38，只能提供 7 位有效数字。双精度浮点占 8 个字节（64 位）内存空间，其数值范围为 1.7E-308~1.7E+308，可提供 16 位有效数字。

对于 `float` 和 `double` 类型来说，`%f` 为十进制数形式的格式转换符，表示使用浮点数小数形式打印出来；`%e` 表示用科学计数法的形式打印出来浮点数；`%g` 用最短的方式表示一个浮点数，并且使用科学计数法。

```objc
#import <Foundation/Foundation.h>

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        float floatingVar = 331.79;
        double doubleVar = 8.44e+11;
        NSLog(@"floatingVar = %f", floatingVar);
        NSLog(@"doubleVar = %e", doubleVar);
        NSLog(@"doubleVar = %g", doubleVar);
    }
    return 0;
}
```

运行结果如下：

```
floatingVar = 331.790009
doubleVar = 8.440000e+11
doubleVar = 8.44e+11
```

由于浮点型变量能提供的有效数字的位数总是有限的，比如，`float` 只能提供 7 位有效数字。这样会在实际计算中存在一些舍入误差。

```objc
#import <Foundation/Foundation.h>

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        float a = 123456.789e5;
        float b = a + 20;
        NSLog(@"%f", a);
        NSLog(@"%f", b);
    }
    return 0;
}
```

运行结果如下：

```
12345678848.000000
12345678848.000000
```

