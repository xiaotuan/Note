#### 10.6.1　对形式参数使用const

在K&R C的年代，避免类似错误的唯一方法是提高警惕。ANSI C提供了一种预防手段。如果函数的意图不是修改数组中的数据内容，那么在函数原型和函数定义中声明形式参数时应使用关键字 `const` 。例如， `sum()` 函数的原型和定义如下：

```c
int sum(const int ar[], int n); /* 函数原型 */
int sum(const int ar[], int n) /* 函数定义 */
{
     int i;
     int total = 0;
     for( i = 0; i < n; i++)
          total += ar[i];
     return total;
}
```

以上代码中的 `const` 告诉编译器，该函数不能修改 `ar` 指向的数组中的内容。如果在函数中不小心使用类似 `ar[i]++` 的表达式，编译器会捕获这个错误，并生成一条错误信息。

这里一定要理解，这样使用 `const` 并不是要求原数组是常量，而是该函数在处理数组时将其视为常量，不可更改。这样使用 `const` 可以保护数组的数据不被修改，就像按值传递可以保护基本数据类型的原始值不被改变一样。一般而言，如果编写的函数需要修改数组，在声明数组形参时则不使用 `const` ；如果编写的函数不用修改数组，那么在声明数组形参时最好使用 `const` 。

程序清单10.14的程序中，一个函数显示数组的内容，另一个函数给数组每个元素都乘以一个给定值。因为第1个函数不用改变数组，所以在声明数组形参时使用了 `const` ；而第2个函数需要修改数组元素的值，所以不使用 `const` 。

程序清单10.14　 `arf.c` 程序

```c
/* arf.c -- 处理数组的函数 */
#include <stdio.h>
#define SIZE 5
void show_array(const double ar[], int n);
void mult_array(double ar[], int n, double mult);
int main(void)
{
     double dip[SIZE] = { 20.0, 17.66, 8.2, 15.3, 22.22 };
     printf("The original dip array:\n");
     show_array(dip, SIZE);
     mult_array(dip, SIZE, 2.5);
     printf("The dip array after calling mult_array():\n");
     show_array(dip, SIZE);
     return 0;
}
/* 显示数组的内容 */
void show_array(const double ar[], int n)
{
     int i;
     for (i = 0; i < n; i++)
          printf("%8.3f ", ar[i]);
     putchar('\n');
}
/* 把数组的每个元素都乘以相同的值 */
void mult_array(double ar[], int n, double mult)
{
     int i;
     for (i = 0; i < n; i++)
          ar[i] *= mult;
}
```

下面是该程序的输出：

```c
The original dip array:
  20.000     17.660      8.200       15.300      22.220
The dip array after calling mult_array():
  50.000     44.150      20.500      38.250      55.550
```

注意该程序中两个函数的返回类型都是 `void` 。虽然 `mult_array()` 函数更新了 `dip` 数组的值，但是并未使用 `return` 机制。

