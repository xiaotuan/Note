将 `const` 用于指针有一些很微妙的地方，我们来详细探讨一下。可用用两种不同的方式将 `const` 关键字用于指针。第一种方法是让指针指向一个常量对象，这样可以防止使用该指针来修改所指向的值；第二种方法是将指针本身声明为常量，这样可以防止改变指针指向的位置。

首先，声明一个指向常量的指针 `pt`：

```cpp
int age = 39;
const int * pt = &age;
```

该声明指出，`pt` 指向一个 `const int`，因此不能使用 `pt` 来修改这个值。换句话说，`*pt` 的值为 `const`，不能被修改：

```cpp
*pt += 1;	// INVALID because pt points to a const int
cin >> *pt;	// INVALID for the same reason
```

现在来看一个很微妙的问题。`pt` 的声明并不意味着它指向的值实际上就是一个常量，而只是意味着对 `pt` 而言，这个值是常量。例如，`pt` 指向 `age`，而 `age` 不是 `const`。可以直接通过 `age` 变量来修改 `age` 的值，但不能使用 `pt` 指针来修改它：

```cpp
*pt = 20;	// INVALID because pt points to a const int
age = 20;	// VALID because age is not declared to be const
```

以前我们将常规变量的地址赋给常规指针，而这里将常规变量的地址赋给指向 `const` 的指针。因此还有两种可能：将 `const` 变量的地址赋给指向 `const` 的指针、将 `const` 的地址赋给常规指针。这两种操作都可行吗？第一种可行，但第二种不可行：

```cpp
const float g_earth = 9.80;
const float * pe = &g_earth;	// VALID

const float g_moon = 1.63;
float * pm = &g_moon;	// INVALID
```

对于第一种情况来说，既不能使用 `g_earth` 来修改值 9.80，也不能使用 `pe` 来修改。C++ 进制第二种情况的原因很简单——如果将 `g_moon` 的地址赋给 `pm`，则可以使用 `pm` 来修改 `g_moon` 的值，这使得 `g_moon` 的 `const` 状态很荒谬，因此 C++ 禁止将 `const` 的地址赋给非 `const` 指针。如果读者非要这样做，可以使用强制类型转换来突破这种限制（使用 `const_cast` 运算符）。

如果将指针指向指针，则情况将更复杂。前面讲过，假设设计的是一级间接关系，则将非 `const` 指针赋给 `const` 指针是可以的：

```cpp
int age = 39;	// age++ is a valid operation
int * pd = &age;	// *pd = 41 is a valid operation
const int * pt = pd;	// *pt = 42 is an invalid operation
```

然而，进入两级间接关系时，与一级间接关系一样将 `const` 和非 `const` 混合的指针赋值方式将不再安全。如果允许这样做，则可以编写这样的代码：

```cpp
const int **pp2;
int *p1;
const int n = 13;
pp2 = &p1;	// not allowed, but suppose it were
*pp2 = &n;	// valid, both const, but sets p1 to point at n
*p1 = 10;	// valid, but changes const n
```

假设有一个由 `const` 数据组成的数组：

```cpp
const int months[12] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
```

则禁止将常量数组的地址赋给非常量指针将意味着不能将数组名作为参数传递给使用非常量形参的函数：

```cpp
int sum(int arr[], int n);	// should have been const int arr[]
...
int j = sum(months, 12);	// not allowed
```

第二种使用 `const` 的方式使得无法修改指针的值：

```cpp
int sloth = 3;
const int * ps = &sloth;	// a pointer to const int
int * const finger = &sloth;	// a const pointer to int
```

在最后一个声明中，关键字 `const` 的位置与以前不同。这种声明格式使得 `finger` 只能指向 `sloth`，但允许使用 `finger` 来修改 `sloth` 的值。中间的声明不允许使用 `ps` 来修改 `sloth` 的值，但允许将 `ps` 执行另一个位置。

如果愿意，还可以声明指向 `const` 对象的 `const` 指针：

```cpp
double trouble = 2.0E30;
const double * const stick = &trouble;
```

其中，`stick` 只能指向 `trouble`，而 `stick` 不能用来修改 `trouble` 的值。简而言之，`stick` 和 `*stick` 