### 18.5.1　包装器function及模板的低效性

请看下面的代码行：

```css
answer = ef(q);
```

ef是什么呢？它可以是函数名、函数指针、函数对象或有名称的lambda表达式。所有这些都是可调用的类型（callable type）。鉴于可调用的类型如此丰富，这可能导致模板的效率极低。为明白这一点，来看一个简单的案例。

首先，在头文件中定义一些模板，如程序清单18.6所示。

程序清单18.6　somedefs.h

```css
// somedefs.h
#include <iostream>
template <typename T, typename F>
T use_f(T v, F f)
{
    static int count = 0;
    count++;
    std::cout << " use_f count = " << count
              << ", &count = " << &count << std::endl;
    return f(v);
}
class Fp
{
private:
    double z_;
public:
    Fp(double z = 1.0) : z_(z) {}
    double operator()(double p) { return z_*p; }
};
class Fq
{
private:
    double z_;
public:
    Fq(double z = 1.0) : z_(z) {}
    double operator()(double q) { return z_+ q; }
};
```

模板use_f使用参数f表示调用类型：

```css
return f(v);
```

接下来，程序清单18.7所示的程序调用模板函数use_f()6次。

程序清单18.7　callable.cpp

```css
// callable.cpp -- callable types and templates
#include "somedefs.h"
#include <iostream>
double dub(double x) {return 2.0*x;}
double square(double x) {return x*x;}
int main()
{
    using std::cout;
    using std::endl;
    double y = 1.21;
    cout << "Function pointer dub:\n";
    cout << " " << use_f(y, dub) << endl;
    cout << "Function pointer square:\n";
    cout << " " << use_f(y, square) << endl;
    cout << "Function object Fp:\n";
    cout << " " << use_f(y, Fp(5.0)) << endl;
    cout << "Function object Fq:\n";
    cout << " " << use_f(y, Fq(5.0)) << endl;
    cout << "Lambda expression 1:\n";
    cout << " " << use_f(y, [](double u) {return u*u;}) << endl;
    cout << "Lambda expression 2:\n";
    cout << " " << use_f(y, [](double u) {return u+u/2.0;}) << endl;
    return 0;
}
```

在每次调用中，模板参数T都被设置为类型double。模板参数F呢？每次调用时，F都接受一个double值并返回一个double值，因此在6次use_of() 调用中，好像F的类型都相同，因此只会实例化模板一次。但正如下面的输出表明的，这种想法太天真了：

```css
Function pointer dub:
  use_f count = 1, &count = 0x402028
  2.42
Function pointer square:
  use_f count = 2, &count = 0x402028
  1.1
Function object Fp:
  use_f count = 1, &count = 0x402020
  6.05
Function object Fq:
  use_f count = 1, &count = 0x402024
  6.21
Lambda expression 1:
  use_f count = 1, &count = 0x405020
  1.4641
Lambda expression 2:
  use_f count = 1, &count = 0x40501c
  1.815
```

模板函数use_f()有一个静态成员count，可根据它的地址确定模板实例化了多少次。有5个不同的地址，这表明模板use_f()有5个不同的实例化。

为了解其中的原因，请考虑编译器如何判断模板参数F的类型。首先，来看下面的调用：

```css
use_f(y, dub);
```

其中的dub是一个函数的名称，该函数接受一个double参数并返回一个double值。函数名是指针，因此参数F的类型为double(*) (double)：一个指向这样的函数的指针，即它接受一个double参数并返回一个double值。

下一个调用如下：

```css
use_f(y, square);
```

第二个参数的类型也是double(*) (double)，因此该调用使用的use_f()实例化与第一个调用相同。

在接下来的两个use_f()调用中，第二个参数为对象，F的类型分别为Fp和Fq，因为将为这些F值实例化use_f()模板两次。最后，最后两个调用将F的类型设置为编译器为lambda表达式使用的类型。

