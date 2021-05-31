1. 幂运算：pow()

    ```java
    double y = Math.pow(x, a);
    ```

2. 整数求余：floorMod()

    该方法用于整数求余，当被除数为负数时，余数也为正整数。（遗憾的是当除数为负数时，`floorMod()` 方法会得到负数，不过这种情况在实际中很少出现）

    > 提示：`n % 2` 当 n 为负时，表达式的结果为 -1。

3. Math 类提供了一些常用的三角函数：

    ```txt
    Math.sin
    Math.cos
    Math.tan
    Math.atan
    Math.atan2
    ```

> 提示：不必在数学方法名和常量名前添加前缀“Math”，只要在源文件的顶部加上下面这行代码就可以了。
>
> ```java
> import static java.lang.Math.*;
> ```

> 注释：。如果得到一个完全可预测的结果比运行速度更重要的话，那么就应该使用StrictMath类。它使用“自由发布的Math库”（fdlibm）实现算法，以确保在所有平台上得到相同的结果。有关这些算法的源代码请参看www.netlib.org/fdlibm（当fdlibm为一个函数提供了多个定义时，StrictMath 类就会遵循IEEE754版本，它的名字将以“e”开头）。
>

