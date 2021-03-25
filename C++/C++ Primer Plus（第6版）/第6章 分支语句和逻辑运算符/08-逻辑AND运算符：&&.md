### 6.2.2　逻辑AND运算符：&&

逻辑AND运算符（&&），也是将两个表达式组合成一个表达式。仅当原来的两个表达式都为true时，得到的表达式的值才为true。下面是一些例子：

```css
5 == 5 && 4 == 4 // true because both expressions are true
5 == 3 && 4 == 4 // false because first expression is false
5 > 3 && 5 > 10  // false because second expression is false
5 > 8 && 5 < 10  // false because first expression is false
5 < 8 && 5 > 2   // true because both expressions are true
5 > 8 && 5 < 2   // false because both expressions are false
```

由于&&的优先级低于关系运算符，因此不必在这些表达式中使用括号。和||运算符一样，&&运算符也是顺序点，因此将首先判定左侧，并且在右侧被判定之前产生所有的副作用。如果左侧为false，则整个逻辑表达式必定为false，在这种情况下，C++将不会再对右侧进行判定。表6.2总结了&&运算符的工作方式。

<center class="my_markdown"><b class="my_markdown">表6.2　&&运算符</b></center>

| expr1 && expr2的值 |
| :-----  | :-----  | :-----  |
| expr1 = = true | expr1 = = false |
| expr2 = = true | true | false |
| expr2 = = false | false | false |

程序清单6.5演示了如何用&&来处理一种常见的情况——由于两种不同的原因而结束while循环。在这个程序清单中，一个while循环将值读入到数组。一个测试（i<ArSize）在数组被填满时循环结束，另一个测试（temp>=0）让用户通过输入一个负值来提前结束循环。该程序使用&&运算符将两个测试组合成一个条件。该程序还使用了两条if语句、一条if else语句和一个for循环，因此它演示了本章和第5章的多个主题。

程序清单6.5　and.cpp

```css
// and.cpp -- using the logical AND operator
#include <iostream>
const int ArSize = 6;
int main()
{
    using namespace std;
    float naaq[ArSize];
    cout << "Enter the NAAQs (New Age Awareness Quotients) "
         << "of\nyour neighbors. Program terminates "
         << "when you make\n" << ArSize << " entries "
         << "or enter a negative value.\n";
    int i = 0;
    float temp;
    cout << "First value: ";
    cin >> temp;
    while (i < ArSize && temp >= 0)    // 2 quitting criteria
    {
        naaq[i] = temp;
        ++i;
        if (i < ArSize)              // room left in the array,
        {
            cout << "Next value: ";
            cin >> temp;             // so get next value
        }
    }
    if (i == 0)
        cout << "No data--bye\n";
    else
    {
        cout << "Enter your NAAQ: ";
        float you;
        cin >> you;
        int count = 0;
        for (int j = 0; j < i; j++)
            if (naaq[j] > you)
                ++count;
        cout << count;
        cout << " of your neighbors have greater awareness of\n"
             << "the New Age than you do.\n";
    }
    return 0;
}
```

注意，该程序将输入放在临时变量temp中。在核实输入有效后，程序才将这个值赋给数组。

下面是该程序的两次运行情况。一次在输入6个值后结束：

```css
Enter the NAAQs (New Age Awareness Quotients) of
your neighbors. Program terminates when you make
6 entries or enter a negative value.
First value: 28
Next value: 72
Next value: 15
Next value: 6
Next value: 130
Next value: 145
Enter your NAAQ: 50
3 of your neighbors have greater awareness of
the New Age than you do.
```

另一次在输入负值后结束：

```css
Enter the NAAQs (New Age Awareness Quotients) of
your neighbors. Program terminates when you make
6 entries or enter a negative value.
First value: 123
Next value: 119
Next value: 4
Next value: 89
Next value: -1
Enter your NAAQ: 123.031
0 of your neighbors have greater awareness of
the New Age than you do.
```

**程序说明**

来看看该程序的输入部分：

```css
cin >> temp;
while (i < ArSize && temp >= 0) // 2 quitting criteria
{
    naaq[i] = temp;
    ++i;
    if (i < ArSize)      // room left in the array,
    {
        cout << "Next value: ";
        cin >> temp;     // so get next value
    }
}
```

该程序首先将第一个输入值读入到临时变量（temp）中。然后，while测试条件查看数组中是否还有空间（i<ArSize）以及输入值是否为非负（temp >=0）。如果满足条件，则将temp的值复制到数组中，并将数组索引加1。此时，由于数组下标从0开始，因此i指示输入了多少个值。也是说，如果i从0开始，则第一轮循环将一个值赋给naaq[0]，然后将i设置为1。

当数组被填满或用户输入了负值时，循环将结束。注意，仅当i小于ArSize时，即数组中还有空间时，循环才将另外一个值读入到temp中。

获得数据后，如果没有输入任何数据（即第一次输入的是一个负数），程序将使用if else语句指出这一点，如果存在数据，就对数据进行处理。

