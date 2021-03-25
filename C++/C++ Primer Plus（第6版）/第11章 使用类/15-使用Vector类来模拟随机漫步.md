### 11.5.4　使用Vector类来模拟随机漫步

程序清单11.15是一个小程序，它使用了修订后的Vector类。该程序模拟了著名的醉鬼走路问题（Drunkard Walk problem）。实际上，醉鬼被认为是一个有许多健康问题的人，而不是大家娱乐消遣的谈资，因此这个问题通常被称为随机漫步问题。其意思是，将一个人领到街灯柱下。这个人开始走动，但每一步的方向都是随机的（与前一步不同）。这个问题的一种表述是，这个人走到离灯柱50英尺处需要多少步。从矢量的角度看，这相当于不断将方向随机的矢量相加，直到长度超过50英尺。

程序清单11.15允许用户选择行走距离和步长。该程序用一个变量来表示位置（一个矢量），并报告到达指定距离处（用两种格式表示）所需的步数。可以看到，行走者前进得相当慢。虽然走了1000步，每步的距离为2英尺，但离起点可能只有50英尺。这个程序将行走者所走的净距离（这里为50英尺）除以步数，来指出这种行走方式的低效性。随机改变方向使得该平均值远远小于步长。为了随机选择方向，该程序使用了标准库函数rand()、srand()和time()（参见程序说明）。请务必将程序清单11.14和程序清单11.15一起进行编译。

程序清单11.15　randwalk.cpp

```css
// randwalk.cpp -- using the Vector class
// compile with the vect.cpp file
#include <iostream>
#include <cstdlib>    // rand(), srand() prototypes
#include <ctime>      // time() prototype
#include "vect.h"
int main()
{
    using namespace std;
    using VECTOR::Vector;
    srand(time(0));  // seed random-number generator
    double direction;
    Vector step;
    Vector result(0.0, 0.0);
    unsigned long steps = 0;
    double target;
    double dstep;
    cout << "Enter target distance (q to quit): ";
    while (cin >> target)
    {
        cout << "Enter step length: ";
        if (!(cin >> dstep))
            break;
        while (result.magval() < target)
        {
            direction = rand() % 360;
            step.reset(dstep, direction, Vector::POL);
            result = result + step;
            steps++;
        }
        cout << "After " << steps << " steps, the subject "
            "has the following location:\n";
        cout << result << endl;
        result.polar_mode();
        cout << " or\n" << result << endl;
        cout << "Average outward distance per step = "
            << result.magval()/steps << endl;
        steps = 0;
        result.reset(0.0, 0.0);
        cout << "Enter target distance (q to quit): ";
    }
    cout << "Bye!\n";
    cin.clear();
    while (cin.get() != '\n')
        continue;
    return 0;
}
```

该程序使用using声明导入了Vector，因此该程序可使用Vector::POL，而不必使用VECTOR:: Vector::POL。

下面是程序清单11.13～程序清单11.15组成的程序的运行情况：

```css
Enter target distance (q to quit): 50
Enter step length: 2
After 253 steps, the subject has the following location:
(x,y) = (46.1512, 20.4902)
or
(m,a) = (50.495, 23.9402)
Average outward distance per step = 0.199587
Enter target distance (q to quit): 50
Enter step length: 2
After 951 steps, the subject has the following location:
(x,y) = (-21.9577, 45.3019)
or
(m,a) = (50.3429, 115.8593)
Average outward distance per step = 0.0529362
Enter target distance (q to quit): 50
Enter step length: 1
After 1716 steps, the subject has the following location:
(x,y) = (40.0164, 31.1244)
or
(m,a) = (50.6956, 37.8755)
Average outward distance per step = 0.0295429
Enter target distance (q to quit): q
Bye!
```

这种处理的随机性使得每次运行结果都不同，即使初始条件相同。然而，平均而言，步长减半，步数将为原来的4倍。概率理论表明，平均而言，步数（N）、步长（s），净距离D之间的关系如下：

```css
N = (D/s)2
```

这只是平均情况，但每次试验结果可能相差很大。例如，进行1000次试验（走50英尺，步长为2英尺）时，平均步数为636（与理论值625非常接近），但实际步数位于91～3951。同样，进行1000次试验（走50英尺，步长为1英尺）时，平均步数为2557（与理论值2500非常接近），但实际步数位于345～10882。因此，如果发现自己在随机漫步时，请保持自信，迈大步走。虽然在蜿蜒前进的过程中仍旧无法控制前进的方向，但至少会走得远一点。

**程序说明**

首先需要指出的是，在程序清单11.15中使用VECTOR名称空间非常方便。下面的using声明使Vector类的名称可用：

```css
using VECTOR::Vector;
```

因为所有的Vector类方法的作用域都为整个类，所以导入类名后，无需提供其他using声明，就可以使用Vector的方法。

接下来谈谈随机数。标准ANSI C库（C++也有）中有一个rand()函数，它返回一个从0到某个值（取决于实现）之间的随机整数。该程序使用求模操作数来获得一个0～359的角度值。rand()函数将一种算法用于一个初始种子值来获得随机数，该随机值将用作下一次函数调用的种子）依此类推。这些数实际上是伪随机数，因为10次连续的调用通常将生成10个同样的随机数（具体值取决于实现）。然而，srand()函数允许覆盖默认的种子值，重新启动另一个随机数序列。该程序使用time（0）的返回值来设置种子。time（0）函数返回当前时间，通常为从某一个日期开始的秒数（更广义地，time()接受time_t变量的地址，将时间放到该变量中，并返回它。将0用作地址参数，可以省略time_t变量声明）。因此，下面的语句在每次运行程序时，都将设置不同的种子，使随机输出看上去更为随机：

```css
srand(time(0));
```

头文件cstdlib（以前为stdlib.h）包含了srand()和rand()的原型，而ctime（以前是time.h）包含了time()的原型。C++11使用头文件radom中的函数提供了更强大的随机数支持。

该程序使用result矢量记录行走者的前进情况。内循环每轮将step矢量设置为新的方向，并将它与当前的result矢量相加。当result的长度超过指定的距离后，该循环结束。

程序通过设置矢量的模式，用直角坐标和极坐标显示最终的位置。

下面这条语句将result设置为RECT模式，而不管result和step的初始模式是什么：

```css
result = result + step;
```

这样做的原因如下。首先，加法运算符函数创建并返回一个新矢量，该矢量存储了这两个参数的和。该函数使用默认构造函数以RECT模式创建矢量。因此，被赋给result的矢量的模式为RECT。默认情况下，赋值时将分别给每个成员变量赋值，因此将RECT赋给了result.mode。如果偏爱其他方式，例如，result保留原来的模式，可以通过为类定义赋值运算符来覆盖默认的赋值方式。第12章将介绍这样的示例。

顺便说一句，在将一系列位置存储到文件中很容易。首先包含头文件fstream，声明一个ofstream对象，将其同一个文件关联起来：

```css
#include <fstream>
...
ofstream fout;
fout.open("thewalk.txt");
```

然后，在计算结果的循环中加入类似于下面的代码：

```css
fout << result << endl;
```

这将调用友元函数operator<<(fout, result)，导致引用参数os指向fout，从而将输出写入到文件中。您还可以使用fout将其他信息写入到文件中，如当前由cout显示的总结信息。

