### 5.1　for循环

很多情况下都需要程序执行重复的任务，如将数组中的元素累加起来或将歌颂生产的赞歌打印20份，C++中的for循环可以轻松地完成这种任务。我们来看看程序清单5.1中，以了解for循环所做的工作，然后讨论它是如何工作的。

程序清单5.1　forloop.cpp

```css
// forloop.cpp -- introducing the for loop
#include <iostream>
int main()
{
    using namespace std;
    int i; // create a counter
//   initialize; test ; update
    for (i = 0; i < 5; i++)
        cout << "C++ knows loops.\n";
    cout << "C++ knows when to stop.\n";
    return 0;
}
```

下面是该程序的输出：

```css
C++ knows loops.
C++ knows loops.
C++ knows loops.
C++ knows loops.
C++ knows loops.
C++ knows when to stop.
```

该循环首先将整数变量i设置为0：

```css
i = 0
```

这是循环的初始化（loop initialization）部分。然后，循环测试（loop test）部分检查i是否小于5：

```css
i < 5
```

如果确实小于5，则程序将执行接下来的语句——循环体（loop body）：

```css
cout << "C++ knows loops.\n";
```

然后，程序使用循环更新（loop update）部分将i加1：

```css
i++
```

这里使用了++运算符——递增运算符（increment operator），它将操作数的值加1。递增运算符并不仅限于用于for循环。例如，在程序中，可以使用i++;来替换语句i = i + 1;。将i加1后，便结束了循环的第一个周期。

接下来，循环开始了新的周期，将新的i值与5进行比较。由于新值（1）也小于5，因此循环打印另一行，然后再次将i加1，从而结束这一周期。这样又进入了新的一轮测试、执行语句和更新i的值。这一过程将一直进行下去，直到循环将i更新为5为止。这样，接下来的测试失败，程序将接着执行循环后的语句。

