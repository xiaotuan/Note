### 6.1.3　if else if else结构

与实际生活中发生的情况类似，计算机程序也可能提供两个以上的选择。可以将C++的if else语句进行扩展来满足这种需求。正如读者知道的，else之后应是一条语句，也可以是语句块。由于if else语句本身是一条语句，所以可以放在else的后面：

```css
if (ch == 'A')
    a_grade++;       // alternative # 1
else
    if (ch == 'B')   // alternative # 2
        b_grade++;   // subalternative # 2a
else
    soso++;          // subalternative # 2b
```

如果ch不是'A'，则程序将执行else。执行到那里，另一个if else又提供了两种选择。C++的自由格式允许将这些元素排列成便于阅读的格式：

```css
if (ch == 'A')
    a_grade++;       // alternative # 1
else if (ch == 'B')
    b_grade++;       // alternative # 2
else
    soso++;          // alternative # 3
```

这看上去像是一个新的控制结构——if else if else结构。但实际上，它只是一个if else被包含在另一个if else中。修订后的格式更为清晰，使程序员通过浏览代码便能确定不同的选择。整个构造仍被视为一条语句。

程序清单6.3使用这种格式创建了一个小型测验程序。

程序清单6.3　ifelseif.cpp

```css
// ifelseif.cpp -- using if else if else
#include <iostream>
const int Fave = 27;
int main()
{
    using namespace std;
    int n;
    cout << "Enter a number in the range 1-100 to find ";
    cout << "my favorite number: ";
    do
    {
        cin >> n;
        if (n < Fave)
            cout << "Too low -- guess again: ";
        else if (n > Fave)
            cout << "Too high -- guess again: ";
        else
            cout << Fave << " is right!\n";
    } while (n != Fave);
    return 0;
}
```

下面是该程序的输出：

```css
Enter a number in the range 1-100 to find my favorite number: 50
Too high -- guess again: 25
Too low -- guess again: 37
Too high -- guess again: 31
Too high -- guess again: 28
Too high -- guess again: 27
27 is right! 
```

条件运算符和错误防范

许多程序员将更直观的表达式variable = =value反转为value = =variable，以此来捕获将相等运算符误写为赋值运算符的错误。例如，下述条件有效，可以正常工作：

```css
if (3 == myNumber)
```

但如果错误地使用下面的条件，编译器将生成错误消息，因为它以为程序员试图将一个值赋给一个字面值（3总是等于3，而不能将另一个值赋给它）：

```css
if (3 = myNumber)
```

假设犯了类似的错误，但使用的是前一种表示方法：

```css
if (myNumber = 3)
```

编译器将只是把3赋给myNumber，而if中的语句块将包含非常常见的、而又非常难以发现的错误（然而，很多编译器会发出警告，因此注意警告是明智的）。一般来说，编写让编译器能够发现错误的代码，比找出导致难以理解的错误的原因要容易得多。

