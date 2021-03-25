### 6.2.4　逻辑NOT运算符：!

!运算符将它后面的表达式的真值取反。也是说，如果expression为true，则!expression是false；如果expression为false，则!expression是true。更准确地说，如果expression为true或非零，则!expression为false。

通常，不使用这个运算符可以更清楚地表示关系：

```css
if (!(x > 5))             // if (x <= 5) is clearer
```

然而，!运算符对于返回true-false值或可以被解释为true-false值的函数来说很有用。例如，如果C-风格字符串s1和s2不同，则strcmp(s1, s2)将返回非零（true）值，否则返回0。这意味着如果这两个字符串相同，则!strcmp(s1, s2)为true。

程序清单6.7使用这种技术（将!运算符用于函数返回值）来筛选可赋给int变量的数字输入。如果用户定义的函数is_int()（稍后将详细介绍）的参数位于int类型的取值范围内，则它将返回true。然后，程序使用while(!is-int(num))测试来拒绝不在该取值范围内的值。

程序清单6.7　not.cpp

```css
// not.cpp -- using the not operator
#include <iostream>
#include <climits>
bool is_int(double);
int main()
{
    using namespace std;
    double num;
    cout << "Yo, dude! Enter an integer value: ";
    cin >> num;
    while (!is_int(num)) // continue while num is not int-able
    {
        cout << "Out of range -- please try again: ";
        cin >> num;
    }
    int val = int (num); // type cast
    cout << "You've entered the integer " << val << "\nBye\n";
    return 0;
}
bool is_int(double x)
{
    if (x <= INT_MAX && x >= INT_MIN) // use climits values
        return true;
    else
        return false;
}
```

下面是该程序在int占32位的系统上的运行情况：

```css
Yo, dude! Enter an integer value: 6234128679
Out of range -- please try again: -8000222333
Out of range -- please try again: 99999
You've entered the integer 99999
Bye
```

**程序说明**

如果给读取int值的程序输入一个过大的值，很多C++实现只是将这个值截短为合适的大小，并不会通知丢失了数据。程序清单6.7中的程序避免了这样的问题，它首先将可能的int值作为double值来读取。double类型的精度足以存储典型的int值，且取值范围更大。另一种选择是，使用long long来存储输入的值，因为其取值范围比int大。

布尔函数is_int()使用了climits文件（第3章讨论过）中定义的两个符号常量（INT_MAX和INT_MIN）来确定其参数是否位于适当的范围内。如果是，该函数将返回true，否则返回false。

main()程序使用while循环来拒绝无效输入，直到用户输入有效的值为止。可以在输入超出取值范围时显示int的界限，这样程序将更为友好。确认输入有效后，程序将其赋给一个int变量。

