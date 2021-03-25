### 18.8.3　使用Boost

虽然在C++11中，可访问Boost开发的众多库，但还有很多其他的Boost库。例如，Conversion库中的lexical_cast让您能够在数值和字符串类型之间进行简单地转换，其语法类似于dynamic_cast：将模板参数指定为目标类型。程序清单18.11是一个简单示例。

程序清单18.11　lexcast.cpp

```css
// lexcast.cpp -- simple cast from float to string
#include <iostream>
#include <string>
#include "boost/lexical_cast.hpp"
int main()
{
    using namespace std;
    cout << "Enter your weight: ";
    float weight;
    cin >> weight;
    string gain = "A 10% increase raises ";
    string wt = boost::lexical_cast<string>(weight);
    gain = gain + wt + " to "; // string operator+()
    weight = 1.1 * weight;
    gain = gain + boost::lexical_cast<string>(weight) + ".";
    cout << gain << endl;
    return 0;
}
```

下面是两次运行该程序的情况：

```css
Enter your weight: 150
A 10% increase raises 150 to 165.
Enter your weight: 156
A 10% increase raises 156 to 171.600006.
```

第二次运行的结果凸显了lexical_cast的局限性：它未能很好地控制浮点数的格式。为控制浮点数的格式，需要使用更精致的内核格式化工具，这在第17章讨论过。

还可以使用lexical_cast将字符串转换为数值。

显然，Boost提供的功能比这里介绍的要多得多。例如，Any库让您能够在STL容器中存储一系列不同类型的值和对象，方法是将Any模板用作各种值的包装器。Math库在标准math库的基础上增加了数学函数。Filesystem库让您编写的代码可在使用不同文件系统的平台之间移植。有关这个库以及如何将其加入到各种平台的更详细信息，请参阅Boost网站（www.boost.org）。另外，有些C++编译器（如Cygwin编译器）还自带了Boost库。

