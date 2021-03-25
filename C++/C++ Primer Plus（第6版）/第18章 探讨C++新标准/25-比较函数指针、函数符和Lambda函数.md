### 18.4.1　比较函数指针、函数符和Lambda函数

来看一个示例，它使用三种方法给STL算法传递信息：函数指针、函数符和lambda。出于方便的考虑，将这三种形式通称为函数对象，以免不断地重复“函数指针、函数符或lambda”。假设您要生成一个随机整数列表，并判断其中多少个整数可被3整除，多个少整数可被13整除。

生成这样的列表很简单。一种方案是，使用vector<int>存储数字，并使用STL算法generate() 在其中填充随机数：

```css
#include <vector>
#include <algorithm>
#include <cmath>
...
std::vector<int> numbers(1000);
std::generate(vector.begin(), vector.end(), std::rand);
```

函数generate()接受一个区间（由前两个参数指定），并将每个元素设置为第三个参数返回的值，而第三个参数是一个不接受任何参数的函数对象。在上述示例中，该函数对象是一个指向标准函数rand()的指针。

通过使用算法count_if()，很容易计算出有多少个元素可被3整除。与函数generate()一样，前两个参数应指定区间，而第三个参数应是一个返回true或false的函数对象。函数count_if()计算这样的元素数，即它使得指定的函数对象返回true。为判断元素能否被3整除，可使用下面的函数定义：

```css
bool f3(int x) {return x % 3 == 0;}
```

同样，为判断元素能否被13整除，可使用下面的函数定义：

```css
bool f13(int x) {return x % 13 == 0;}
```

定义上述函数后，便可计算复合条件的元素数了，如下所示：

```css
int count3 = std::count_if(numbers.begin(), numbers.end(), f3);
cout << "Count of numbers divisible by 3: " << count3 << '\n';
int count13 = std::count_if(numbers.begin(), numbers.end(), f13);
cout << "Count of numbers divisible by 13: " << count13 << "\n\n";
```

下面复习一下如何使用函数符来完成这个任务。第16章介绍过，函数符是一个类对象，并非只能像函数名那样使用它，这要归功于类方法operator() ()。就这个示例而言，函数符的优点之一是，可使用同一个函数符来完成这两项计数任务。下面是一种可能的定义：

```css
class f_mod
{
private:
    int dv;
public:
    f_mod(int d = 1) : dv(d) {}
    bool operator()(int x) {return x % dv == 0;}
};
```

这为何可行呢？因为可使用构造函数创建存储特定整数值的f_mod对象：

```css
f_mod obj(3); // f_mod.dv set to 3
```

而这个对象可使用方法operator()来返回一个bool值：

```css
bool is_div_by_3 = obj(7); // same as obj.operator()(7)
```

构造函数本身可用作诸如count_if()等函数的参数：

```css
count3 = std::count_if(numbers.begin(), numbers.end(), f_mod(3));
```

参数f_mod(3)创建一个对象，它存储了值3；而count_if()使用该对象来调用operator() ()，并将参数x设置为numbers的一个元素。要计算有多少个数字可被13（而不是3）整除，只需将第三个参数设置为f_mod(3)。

最后，来看看使用lambda的情况。名称lambda来自lambda calculus（λ演算）—— 一种定义和应用函数的数学系统。这个系统让您能够使用匿名函数——即无需给函数命名。在C++11中，对于接受函数指针或函数符的函数，可使用匿名函数定义（lambda）作为其参数。与前述函数f3()对应的lambda如下：

```css
[](int x) {return x % 3 == 0;}
```

这与f3()的函数定义很像：

```css
bool f3(int x) {return x % 3 == 0;}
```

差别有两个：使用[]替代了函数名（这就是匿名的由来）；没有声明返回类型。返回类型相当于使用decltyp根据返回值推断得到的，这里为bool。如果lambda不包含返回语句，推断出的返回类型将为void。就这个示例而言，您将以如下方式使用该lambda：

```css
count3 = std::count_if(numbers.begin(), numbers.end(),
         [](int x){return x % 3 == 0;});
```

也就是说，使用使用整个lambda表达式替换函数指针或函数符构造函数。

仅当lambda表达式完全由一条返回语句组成时，自动类型推断才管用；否则，需要使用新增的返回类型后置语法：

```css
[](double x)->double{int y = x; return x – y;} // return type is double
```

程序清单18.4演示了前面讨论的各个要点。

程序清单18.4　lambda0.cpp

```css
// lambda0.cpp -- using lambda expressions
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <ctime>
const long Size1 = 39L;
const long Size2 = 100*Size1;
const long Size3 = 100*Size2;
bool f3(int x) {return x % 3 == 0;}
bool f13(int x) {return x % 13 == 0;}
int main()
{
    using std::cout;
    std::vector<int> numbers(Size1);
    std::srand(std::time(0));
    std::generate(numbers.begin(), numbers.end(), std::rand);
// using function pointers
    cout << "Sample size = " << Size1 << '\n';
    int count3 = std::count_if(numbers.begin(), numbers.end(), f3);
    cout << "Count of numbers divisible by 3: " << count3 << '\n';
    int count13 = std::count_if(numbers.begin(), numbers.end(), f13);
    cout << "Count of numbers divisible by 13: " << count13 << "\n\n";
// increase number of numbers
    numbers.resize(Size2);
    std::generate(numbers.begin(), numbers.end(), std::rand);
    cout << "Sample size = " << Size2 << '\n';
// using a functor
    class f_mod
    {
    private:
        int dv;
    public:
        f_mod(int d = 1) : dv(d) {}
        bool operator()(int x) {return x % dv == 0;}
    };
    count3 = std::count_if(numbers.begin(), numbers.end(), f_mod(3));
    cout << "Count of numbers divisible by 3: " << count3 << '\n';
    count13 = std::count_if(numbers.begin(), numbers.end(), f_mod(13));
    cout << "Count of numbers divisible by 13: " << count13 << "\n\n";
// increase number of numbers again
    numbers.resize(Size3);
    std::generate(numbers.begin(), numbers.end(), std::rand);
    cout << "Sample size = " << Size3 << '\n';
// using lambdas
    count3 = std::count_if(numbers.begin(), numbers.end(),
             [](int x){return x % 3 == 0;});
    cout << "Count of numbers divisible by 3: " << count3 << '\n';
    count13 = std::count_if(numbers.begin(), numbers.end(),
              [](int x){return x % 13 == 0;});
    cout << "Count of numbers divisible by 13: " << count13 << '\n';
    return 0;
}
```

下面是该程序的输出示例：

```css
Sample size = 39
Count of numbers divisible by 3: 15
Count of numbers divisible by 13: 6
Sample size = 3900
Count of numbers divisible by 3: 1305
Count of numbers divisible by 13: 302
Sample size = 390000
Count of numbers divisible by 3: 130241
   Count of numbers divisible by 13: 29860
```

输出表明，样本很小时，得到的统计数据并不可靠。

