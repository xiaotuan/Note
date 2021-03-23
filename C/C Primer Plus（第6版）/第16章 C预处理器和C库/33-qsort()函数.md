#### 16.11.2　 `qsort()` 函数

对较大型的数组而言，“快速排序”方法是最有效的排序算法之一。该算法由C.A.R.Hoare于1962年开发。它把数组不断分成更小的数组，直到变成单元素数组。首先，把数组分成两部分，一部分的值都小于另一部分的值。这个过程一直持续到数组完全排序好为止。

快速排序算法在C实现中的名称是 `qsort()` 。 `qsort()` 函数排序数组的数据对象，其原型如下：

```c
void qsort(void *base, size_t nmemb, size_t size,
　　　　　　　int (*compar)(const void *, const void *));
```

第1个参数是指针，指向待排序数组的首元素。ANSI C允许把指向任何数据类型的指针强制转换成指向 `void` 的指针，因此， `qsort()` 的第1个实际参数可以引用任何类型的数组。

第2个参数是待排序项的数量。函数原型把该值转换为 `size_t` 类型。前面提到过， `size_t` 定义在标准头文件中，是 `sizeof` 运算符返回的整数类型。

由于 `qsort()` 把第1个参数转换为 `void` 指针，所以 `qsort()` 不知道数组中每个元素的大小。为此，函数原型用第3个参数补偿这一信息，显式指明待排序数组中每个元素的大小。例如，如果排序 `double` 类型的数组，那么第3个参数应该是 `sizeof(double)` 。

最后， `qsort()` 还需要一个指向函数的指针，这个被指针指向的比较函数用于确定排序的顺序。该函数应接受两个参数：分别指向待比较两项的指针。如果第1项的值大于第2项，比较函数则返回正数；如果两项相同，则返回 `0` ；如果第1项的值小于第2项，则返回负数。 `qsort()` 根据给定的其他信息计算出两个指针的值，然后把它们传递给比较函数。

`qsort()` 原型中的第4个参数确定了比较函数的形式：

```c
int (*compar)(const void *, const void *)
```

这表明 `qsort()` 最后一个参数是一个指向函数的指针，该函数返回 `int` 类型的值且接受两个指向 `const void` 的指针作为参数，这两个指针指向待比较项。

程序清单16.17和后面的讨论解释了如何定义一个比较函数，以及如何使用 `qsort()` 。该程序创建了一个内含随机浮点值的数组，并排序了这个数组。

程序清单16.17　 `qsorter.c` 程序

```c
/* qsorter.c -- 用 qsort()排序一组数字 */
#include <stdio.h>
#include <stdlib.h>
#define NUM 40
void fillarray(double ar [], int n);
void showarray(const double ar [], int n);
int mycomp(const void * p1, const void * p2);
int main(void)
{
　　 double vals[NUM];
　　 fillarray(vals, NUM);
　　 puts("Random list:");
　　 showarray(vals, NUM);
　　 qsort(vals, NUM, sizeof(double), mycomp);
　　 puts("\nSorted list:");
　　 showarray(vals, NUM);
　　 return 0;
}
void fillarray(double ar [], int n)
{
　　 int index;
　　 for (index = 0; index < n; index++)
　　　　　ar[index] = (double) rand() / ((double) rand() + 0.1);
}
void showarray(const double ar [], int n)
{
　　 int index;
　　 for (index = 0; index < n; index++)
　　 {
　　　　　printf("%9.4f ", ar[index]);
　　　　　if (index % 6 == 5)
　　　　　　　 putchar('\n');
　　 }
　　 if (index % 6 != 0)
　　　　　putchar('\n');
}
/* 按从小到大的顺序排序 */
int mycomp(const void * p1, const void * p2)
{
　　 /* 要使用指向double的指针来访问这两个值 */
　　 const double * a1 = (const double *) p1;
　　 const double * a2 = (const double *) p2;
　　 if (*a1 < *a2)
　　　　　return -1;
　　 else if (*a1 == *a2)
　　　　　return 0;
　　 else
　　　　　return 1;
}
```

下面是该程序的运行示例 `:`

```c
Random list:
0.0001 　 1.6475 　2.4332 　0.0693 　0.7268 　0.7383
24.0357 　0.1009 　87.1828　5.7361 　0.6079 　0.6330
1.6058  　0.1406 　0.5933 　1.1943 　5.5295 　2.2426
0.8364  　2.7127 　0.2514 　0.9593 　8.9635 　0.7139
0.6249  　1.6044 　0.8649 　2.1577 　0.5420 　15.0123
1.7931  　1.6183 　1.9973 　2.9333 　12.8512  1.3034
0.3032  　1.1406 　18.7880 　0.9887
Sorted list:
0.0001  　0.0693 　0.1009 　0.1406 　0.2514 　0.3032
0.5420  　0.5933 　0.6079 　0.6249 　0.6330 　0.7139
0.7268 　 0.7383 　0.8364 　0.8649 　0.9593　 0.9887
1.1406  　1.1943 　1.3034 　1.6044 　1.6058 　1.6183
1.6475  　1.7931 　1.9973 　2.1577 　2.2426 　2.4332
2.7127  　2.9333 　5.5295 　5.7361 　8.9635 　12.8512
15.0123 　18.7880　24.0357　87.1828
```

接下来分析两点： `qsort()` 的用法和 `mycomp()` 的定义。

#### 1． `qsort()` 的用法

`qsort()` 函数排序数组的数据对象。该函数的ANSI原型如下：

```c
void qsort (void *base, size_t nmemb, size_t size,
　　　　　　　 int (*compar)(const void *, const void *));
```

第1个参数值指向待排序数组首元素的指针。在该程序中，实际参数是 `double` 类型的数组名 `vals` ，因此指针指向该数组的首元素。根据该函数的原型，参数 `vals` 会被强制转换成指向 `void` 的指针。由于ANSI C允许把指向任何数据类型的指针强制转换成指向 `void` 的指针，所以 `qsort()` 的第1个实际参数可以引用任何类型的数组。

第2个参数是待排序项的数量。在程序清单16.17中是 `NUM` ，即数组元素的数量。函数原型把该值转换为 `size_t` 类型。

第3个参数是数组中每个元素占用的空间大小，本例中为 `sizeof(double)` 。

最后一个参数是 `mycomp` ，这里函数名即是函数的地址，该函数用于比较元素。

#### 2． `mycomp()` 的定义

前面提到过， `qsort()` 的原型中规定了比较函数的形式：

```c
int (*compar)(const void *, const void *)
```

这表明 `qsort()` 最后一个参数是一个指向函数的指针，该函数返回 `int` 类型的值且接受两个指向 `const void` 的指针作为参数。程序中 `mycomp()` 使用的就是这个原型：

```c
int mycomp(const void * p1, const void * p2);
```

记住，函数名作为参数时即是指向该函数的指针。因此， `mycomp` 与 `compar` 原型相匹配。

`qsort()` 函数把两个待比较元素的地址传递给比较函数。在该程序中，把待比较的两个 `double` 类型值的地址赋给 `p1` 和 `p2` 。注意， `qsort()` 的第1个参数引用整个数组，比较函数中的两个参数引用数组中的两个元素。这里存在一个问题。为了比较指针所指向的值，必须解引用指针。因为值是 `double` 类型，所以要把指针解引用为 `double` 类型的值。然而， `qsort()` 要求指针指向 `void` 。要解决这个问题，必须在比较函数的内部声明两个类型正确的指针，并初始化它们分别指向作为参数传入的值：

```c
/* 按从小到大的顺序排序值 */
int mycomp(const void * p1, const void * p2)
{
　　 /* 使用指向double类型的指针访问值 */
　　 const double * a1 = (const double *) p1;
　　 const double * a2 = (const double *) p2;
　　 if (*a1 < *a2)
　　　　　return -1;
　　 else if (*a1 == *a2)
　　　　　return 0;
　　 else
　　　　　return 1;
}
```

简而言之，为了让该方法具有通用性， `qsort()` 和比较函数使用了指向 `void` 的指针。因此，必须把数组中每个元素的大小明确告诉 `qsort()` ，并且在比较函数的定义中，必须把该函数的指针参数转换为对具体应用而言类型正确的指针。

> **注意C和C++中的void***
> C和C++对待指向 `void` 的指针有所不同。在这两种语言中，都可以把任何类型的指针赋给 `void` 类型的指针。例如，程序清单16.17中， `qsort()` 的函数调用中把 `double` *指针赋给 `void` *指针。但是，C++要求在把 `void` *指针赋给任何类型的指针时必须进行强制类型转换。而C没有这样的要求。例如，程序清单16.17中的 `mycomp()` 函数，就使用了这样的强制类型转换：

```c
const double * a1 = (const double *) p1;
```

> 这种强制类型转换，在C中是可选的，但在C++中是必须的。因为两种语言都使用强制类型转换，所以遵循C++的要求也无不妥。将来如果要把该程序转成C++，就不必更改这部分的代码。

下面再来看一个比较函数的例子。假设有下面的声明：

```c
struct names {
　　 char first[40];
　　 char last[40];
};
struct names staff[100];
```

如何调用 `qsort()` ？模仿程序清单16.17中 `qsort()` 的函数调用，应该是这样：

```c
qsort(staff, 100, sizeof(struct names), comp);
```

这里 `comp` 是比较函数的函数名。那么，应如何编写这个函数？假设要先按姓排序，如果同姓再按名排序，可以这样编写该函数：

```c
#include <string.h>
int comp(const void * p1, const void * p2) /* 该函数的形式必须是这样 */
{
　　 /* 得到正确类型的指针 */
　　 const struct names *ps1 = (const struct names *) p1;
　　 const struct names *ps2 = (const struct names *) p2;
　　 int res;
　　 res = strcmp(ps1->last, ps2->last); /* 比较姓 */
　　 if (res != 0)
　　　　　return res;
　　 else /* 如果同姓，则比较名 */
　　　　　return strcmp(ps1->first, ps2->first);
}
```

该函数使用 `strcmp()` 函数进行比较。 `strcmp()` 的返回值与比较函数的要求相匹配。注意，通过指针访问结构成员时必须使用 `->` 运算符。

