### 18.1.8　模板和STL方面的修改

为改善模板和标准模板库的可用性，C++11做了多个改进；有些是库本身，有些与易用性相关。本章前面提到了模板别名和适用于STL的智能指针。

#### 1．基于范围的for循环

对于内置数组以及包含方法begin() 和end() 的类（如std::string）和STL容器，基于范围的for循环（第5章和第16章讨论过）可简化为它们编写循环的工作。这种循环对数组或容器中的每个元素执行指定的操作：

```css
double prices[5] = {4.99, 10.99, 6.87, 7.99, 8.49};
for (double x : prices)
    std::cout << x << std::endl;
```

其中，x将依次为prices中每个元素的值。x的类型应与数组元素的类型匹配。一种更容易、更安全的方式是，使用auto来声明x，这样编译器将根据prices声明中的信息来推断x的类型：

```css
double prices[5] = {4.99, 10.99, 6.87, 7.99, 8.49};
for (auto x : prices)
    std::cout << x << std::endl;
```

如果要在循环中修改数组或容器的每个元素，可使用引用类型：

```css
std::vector<int> vi(6);
for (auto & x: vi) // use a reference if loop alters contents
    x = std::rand();
```

#### 2．新的STL容器

C++11新增了STL容器forward_list、unordered_map、unordered_multimap、unordered_set和unordered_multiset（参见第16章）。容器forward_list是一种单向链表，只能沿一个方向遍历；与双向链接的list容器相比，它更简单，在占用存储空间方面更经济。其他四种容器都是使用哈希表实现的。

C++11还新增了模板array（这在第4章和第16章讨论过）。要实例化这种模板，可指定元素类型和固定的元素数：

```css
std::array<int,360> ar; // array of 360 ints
```

这个模板类没有满足所有的常规模板需求。例如，由于长度固定，您不能使用任何修改容器大小的方法，如put_back()。但array确实有方法begin()和end()，这让您能够对array对象使用众多基于范围的STL算法。

#### 3．新的STL方法

C++11新增了STL方法cbegin()和cend()。与begin()和end()一样，这些新方法也返回一个迭代器，指向容器的第一个元素和最后一个元素的后面，因此可用于指定包含全部元素的区间。另外，这些新方法将元素视为const。与此类似，crbegin()和crend()是rbegin()和rend()的const版本。

更重要的是，除传统的复制构造函数和常规赋值运算符外，STL容器现在还有移动构造函数和移动赋值运算符。移动语义将在本章后面介绍。

#### 4．valarray升级

模板valarray独立于STL开发的，其最初的设计导致无法将基于范围的STL算法用于valarray对象。C++11添加了两个函数（begin()和end()），它们都接受valarray作为参数，并返回迭代器，这些迭代器分别指向valarray对象的第一个元素和最后一个元素后面。这让您能够将基于范围的STL算法用于valarray（参见第16章）。

#### 5．摒弃export

C++98新增了关键字export，旨在提供一种途径，让程序员能够将模板定义放在接口文件和实现文件中，其中前者包含原型和模板声明，而后者包含模板函数和方法的定义。实践证明这不现实，因此C++11终止了这种用法，但仍保留了关键字export，供以后使用。

#### 6．尖括号

为避免与运算符>>混淆，C++要求在声明嵌套模板时使用空格将尖括号分开：

```css
std::vector<std::list<int> > vl; // >> not ok
```

C++11不再这样要求：

```css
std::vector<std::list<int>> vl; // >> ok in C++11
```

