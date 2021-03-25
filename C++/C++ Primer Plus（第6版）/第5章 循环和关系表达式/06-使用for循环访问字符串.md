### 5.1.4　使用for循环访问字符串

for循环提供了一种依次访问字符串中每个字符的方式。例如，程序清单5.6让用户能够输入一个字符串，然后按相反的方向逐个字符地显示该字符串。在这个例子中，可以使用string对象，也可以使用char数组，因为它们都让您能够使用数组表示法来访问字符串中的字符。程序清单5.6使用的是string对象。string类的size()获得字符串中的字符数；循环在其初始化表达式中使用这个值，将i设置为字符串中最后一个字符的索引（不考虑空值字符）。为了反向计数，程序使用递减运算符（− −），在每轮循环后将数组下标减1。另外，程序清单5.6使用关系运算符大于或等于（>=）来测试循环是否到达第一个元素。稍后我们将对所有的关系运算符做一总结。

程序清单5.6　forstr1.cpp

```css
// forstr1.cpp -- using for with a string
#include <iostream>
#include <string>
int main()
{
    using namespace std;
    cout << "Enter a word: ";
    string word;
    cin >> word;
    // display letters in reverse order
    for (int i = word.size() - 1; i >= 0; i--)
        cout << word[i];
    cout << "\nBye.\n";
    return 0;
}
```

> **注意：**
> 如果所用的实现没有添加新的头文件，则必须使用string.h，而不是cstring。

下面是该程序的运行情况：

```css
Enter a word: animal
lamina
Bye.
```

程序成功地按相反的方向打印了animal；与回文rotator、redder或stats相比，animal能更清晰地说明这个程序的作用。

