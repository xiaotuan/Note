### 14.1.1　valarray类简介

valarray类是由头文件valarray支持的。顾名思义，这个类用于处理数值（或具有类似特性的类），它支持诸如将数组中所有元素的值相加以及在数组中找出最大和最小的值等操作。valarray被定义为一个模板类，以便能够处理不同的数据类型。本章后面将介绍如何定义模板类，但就现在而言，您只需知道如何使用模板类即可。

模板特性意味着声明对象时，必须指定具体的数据类型。因此，使用valarray类来声明一个对象时，需要在标识符valarray后面加上一对尖括号，并在其中包含所需的数据类型：

```css
valarray<int> q_values;   // an array of int
valarray<double> weights; // an array of double
```

第4章介绍vector和array类时，您见过这种语法，它非常简单。这些类也可用于存储数字，但它们提供的算术支持没有valarray多。

这是您需要学习的唯一新语法，它非常简单。

类特性意味着要使用valarray对象，需要了解这个类的构造函数和其他类方法。下面是几个使用其构造函数的例子：

```css
double gpa[5] = {3.1, 3.5, 3.8, 2.9, 3.3};
valarray<double> v1;    // an array of double, size 0
valarray<int> v2(8);    // an array of 8 int elements
valarray<int> v3(10,8); // an array of 8 int elements,
                        // each set to 10
valarray<double> v4(gpa, 4); // an array of 4 elements
                // initialized to the first 4 elements of gpa
```

从中可知，可以创建长度为零的空数组、指定长度的空数组、所有元素度被初始化为指定值的数组、用常规数组中的值进行初始化的数组。在C++11中，也可使用初始化列表：

```css
valarray<int> v5 = {20, 32, 17, 9}; // C++11
```

下面是这个类的一些方法。

+ operator ：让您能够访问各个元素。
+ size()：返回包含的元素数。
+ sum()：返回所有元素的总和。
+ max()：返回最大的元素。
+ min()：返回最小的元素。

还有很多其他的方法，其中的一些将在第16章介绍；但就这个例子而言，上述方法足够了。

