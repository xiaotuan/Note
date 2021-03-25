### 18.4.2　为何使用lambda

您可能会问，除那些表达式狂热爱好者，谁会使用lambda呢？下面从4个方面探讨这个问题：距离、简洁、效率和功能。

很多程序员认为，让定义位于使用的地方附近很有用。这样，就无需翻阅多页的源代码，以了解函数调用count_if()的第三个参数了。另外，如果需要修改代码，涉及的内容都将在附近；而剪切并粘贴代码以便在其他地方使用时，涉及的内容也在一起。从这种角度看，lambda是理想的选择，因为其定义和使用是在同一个地方进行的；而函数是最糟糕的选择，因为不能在函数内部定义其他函数，因此函数的定义可能离使用它的地方很远。函数符是不错的选择，因为可在函数内部定义类（包含函数符类），因此定义离使用地点可以很近。

从简洁的角度看，函数符代码比函数和lambda代码更繁琐。函数和lambda的简洁程度相当，一个显而易见的例外是，需要使用同一个lambda两次：

```css
count1 = std::count_if(n1.begin(), n1.end(),
         [](int x){return x % 3 == 0;});
count2 = std::count_if(n2.begin(), n2.end(),
         [](int x){return x % 3 == 0;});
```

但并非必须编写lambda两次，而可给lambda指定一个名称，并使用该名称两次：

```css
auto mod3 = [](int x){return x % 3 == 0;} // mod3 a name for the lambda
count1 = std::count_if(n1.begin(), n1.end(), mod3);
count2 = std::count_if(n2.begin(), n2.end(), mod3);
```

您甚至可以像使用常规函数那样使用有名称的lambda：

```css
bool result = mod3(z); // result is true if z % 3 == 0
```

然而，不同于常规函数，可在函数内部定义有名称的lambda。mod3的实际类型随实现而异，它取决于编译器使用什么类型来跟踪lambda。

这三种方法的相对效率取决于编译器内联那些东西。函数指针方法阻止了内联，因为编译器传统上不会内联其地址被获取的函数，因为函数地址的概念意味着非内联函数。而函数符和lambda通常不会阻止内联。

最后，lambda有一些额外的功能。具体地说，lambad可访问作用域内的任何动态变量；要捕获要使用的变量，可将其名称放在中括号内。如果只指定了变量名，如[z]，将按值访问变量；如果在名称前加上&，如[&count]，将按引用访问变量。[&]让您能够按引用访问所有动态变量，而[=]让您能够按值访问所有动态变量。还可混合使用这两种方式，例如，[ted, &ed]让您能够按值访问ted以及按引用访问ed，[&, ted]让您能够按值访问ted以及按引用访问其他所有动态变量，[=, &ed]让您能够按引用访问ed以及按值访问其他所有动态变量。在程序清单18.4中，可将下述代码：

```css
int count13;
...
count13 = std::count_if(numbers.begin(), numbers.end(),
          [](int x){return x % 13 == 0;});
```

替换为如下代码：

```css
int count13 = 0;
std::for_each(numbers.begin(), numbers.end(),
     [&count13](int x){count13 += x % 13 == 0;});
```

[&count13]让lambda能够在其代码中使用count13。由于count13是按引用捕获的，因此在lambda对count13所做的任何修改都将影响原始count13。如果x能被13整除，则表达式x % 13 == 0将为true，添加到count13中时，true将被转换为1。同样，false将被转换为0。因此，for_each()将lambda应用于numbers的每个元素后，count13将为能被13整除的元素数。

通过利用这种技术，可使用一个lambda表达式计算可被3整除的元素数和可被13整除的元素数：

```css
int count3 = 0;
int count13 = 0;
std::for_each(numbers.begin(), numbers.end(),
     [&](int x){count3 += x % 3 == 0; count13 += x % 13 == 0;});
```

在这里，[&]让您能够在lambad表达式中使用所有的自动变量，包括count3和count13。

程序清单18.5演示了如何使用这些技术。

程序清单18.5　lambda1.cpp

```css
// lambda1.cpp -- use captured variables
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <ctime>
const long Size = 390000L;
int main()
{
    using std::cout;
    std::vector<int> numbers(Size);
    std::srand(std::time(0));
    std::generate(numbers.begin(), numbers.end(), std::rand);
    cout << "Sample size = " << Size << '\n';
// using lambdas
    int count3 = std::count_if(numbers.begin(), numbers.end(),
          [](int x){return x % 3 == 0;});
    cout << "Count of numbers divisible by 3: " << count3 << '\n';
    int count13 = 0;
    std::for_each(numbers.begin(), numbers.end(),
         [&count13](int x){count13 += x % 13 == 0;});
    cout << "Count of numbers divisible by 13: " << count13 << '\n';
// using a single lambda
    count3 = count13 = 0;
    std::for_each(numbers.begin(), numbers.end(),
         [&](int x){count3 += x % 3 == 0; count13 += x % 13 == 0;});
    cout << "Count of numbers divisible by 3: " << count3 << '\n';
    cout << "Count of numbers divisible by 13: " << count13 << '\n';
    return 0;
}
```

下面是该程序的示例输出：

```css
Sample size = 390000
Count of numbers divisible by 3: 130274
Count of numbers divisible by 13: 30009
Count of numbers divisible by 3: 130274
Count of numbers divisible by 13: 30009
```

输出表明，该程序使用的两种方法（两个独立的lambda和单个lambda）的结果相同。

在C++中引入lambda的主要目的是，让您能够将类似于函数的表达式用作接受函数指针或函数符的函数的参数。因此，典型的lambda是测试表达式或比较表达式，可编写为一条返回语句。这使得lambda简洁而易于理解，且可自动推断返回类型。然而，有创意的C++程序员可能开发出其他用法。

