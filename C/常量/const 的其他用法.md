虽然用 `#define` 指令可以创建类似功能的符号常量，但是 `const` 的用法更加灵活。可以创建 `const` 数组、`const` 指针和指向 `const` 的指针。

```c
#define MONTHS 12
...
const int days[MONTHS] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
```

如果程序稍后尝试改变数组元素的值，编译器将生成一个编译期错误消息：

```c
days[9] = 44;	/* 编译错误 */
```

指向 `const` 的指针不能用于改变值。考虑下面的代码：

```c
double rates[5] = { 88.99, 100.12, 59.45, 183.11, 340.5 };
const double *pd = rates;	// pd 指向数组的首元素
```

`pd` 指向的 `double` 类型的值声明为 `const`，这表明不能使用 `pd` 来更改它所指向的值：

```c
*pd = 29.89;	// 不允许
pd[2] = 222.22;	// 不允许
rates[0] = 99.99;	// 允许，因为 rates 未被 const 限定
```

可以让 `pd` 指向别处：

```c
pd++;	// 让 pd 指向 rates[1] —— 没问题
```

指向 `const` 的指针通常用于函数形参中，表明该函数不会使用指针改变数据。

```c
void show_array(const double *ar, int n);
```

关于指针赋值和  `const` 需要注意一些规则。首先，把 `const` 数据或非 `const` 数据的地址初始化为指向 `const` 的指针或为其赋值时合法的：

```c
double rates[5] = { 88.99, 100.12, 59.45, 183.11, 340.5 };
const double locked[4] = { 0.08, 0.075, 0.0725, 0.07 };
const double *pc = rates;	// 有效
pc = locked;	// 有效
pc = &rates[3];	// 有效
```

然而，只能把非 `const` 数据的地址赋给普通指针：

```c
double rates[5] = { 88.99, 100.12, 59.45, 183.11, 340.5 };
const double locked[4] = { 0.08, 0.075, 0.0725, 0.07 };
double *pnc = rates;	// 有效
pnc = locked;	// 无效
pnc = &rates[3];	// 有效
```

C 标准规定，使用非 `const` 标识符修改 `const` 数据导致的结果是未定义的。

`const` 还有其他的用法。例如，可以声明并初始化一个不能指向别处的指针，关键是 `const` 的位置：

```c
double rates[5] = { 88.99, 100.12, 59.45, 183.11, 340.5 };
double * const pc = rates;	// pc 指向数组的开始
pc = &rates[2];	// 不允许，因为该指针不能指向别处
*pc = 92.99;	// 没有问题——更改 rates[0] 的值
```

最后，在创建指针时还可以使用 `const` 两次，该指针既不能更改它所指向的地址，也不能修改指向地址上的值：

```c
double rates[5] = { 88.99, 100.12, 59.45, 183.11, 340.5 };
const double * const pc = rates;
pc = &rates[2];	// 不允许
*pc = 92.99;	// 不允许
```

