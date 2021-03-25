### 2.4.5　在多函数程序中使用using编译指令

在程序清单2.5中，两个函数中都包含下面一条using编译指令：

```css
using namespace std;
```

这是因为每个函数都使用了cout，因此需要能够访问位于名称空间std中的cout定义。

在程序清单2.5中，可以采用另一种方法让两个函数都能够访问名称空间std，即将编译指令放在函数的外面，且位于两个函数的前面：

```css
// ourfunc1.cpp -- repositioning the using directive
#include <iostream>
using namespace std; // affects all function definitions in this file
void simon(int);
int main()
{
    simon(3);
    cout << "Pick an integer: ";
    int count;
    cin >> count;
    simon(count);
    cout << "Done!" << endl;
    return 0;
}
void simon(int n)
{
    cout << "Simon says touch your toes " << n << " times." << endl;
}
```

当前通行的理念是，只让需要访问名称空间std的函数访问它是更好的选择。例如，在程序清单2.6中，只有main()函数使用cout，因此没有必要让函数stonetolb()能够访问名称空间std。因此编译指令using被放在函数main()中，使得只有该函数能够访问名称空间std。

总之，让程序能够访问名称空间std的方法有多种，下面是其中的4种。

+ 将using namespace std；放在函数定义之前，让文件中所有的函数都能够使用名称空间std中所有的元素。
+ 将using namespace std；放在特定的函数定义中，让该函数能够使用名称空间std中的所有元素。
+ 在特定的函数中使用类似using std::cout;这样的编译指令，而不是using namespace std;，让该函数能够使用指定的元素，如cout。
+ 完全不使用编译指令using，而在需要使用名称空间std中的元素时，使用前缀std::，如下所示：

```css
std::cout << "I’m using cout and endl from the std namespace" << std::endl;
```



**命名约定**

C++程序员给函数、类和变量命名时，可以有很多种选择。程序员对风格的观点五花八门，这些看法有时就像公共论坛上的圣战。就函数名称而言，程序员有以下选择：

```css
Myfunction()
myfunction()
myFunction()
my_function()
my_funct()
```

选择取决于开发团体、使用的技术或库以及程序员个人的品位和喜好。因此凡是符合第3章将介绍的C++规则的风格都是正确的，都可以根据个人的判断而使用。

撇开语言是否允许不谈，个人的命名风格也是值得注意的——它有助于保持一致性和精确性。精确、让人一目了然的个人命名约定是良好的软件工程的标志，它在整个编程生涯中都会起到很好的作用。



