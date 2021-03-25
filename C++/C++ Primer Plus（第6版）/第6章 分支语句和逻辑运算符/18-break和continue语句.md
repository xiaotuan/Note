### 6.6　break和continue语句

break和continue语句都使程序能够跳过部分代码。可以在switch语句或任何循环中使用break语句，使程序跳到switch或循环后面的语句处执行。continue语句用于循环中，让程序跳过循环体中余下的代码，并开始新一轮循环（参见图6.4）。

![42.png](../images/42.png)
<center class="my_markdown"><b class="my_markdown">图6.4　break和continue语句的结构</b></center>

程序清单6.12演示了这两条语句是如何工作的。该程序让用户输入一行文本。循环将回显每个字符，如果该字符为句点，则使用break结束循环。这表明，可以在某种条件为true时，使用break来结束循环。接下来，程序计算空格数，但不计算其他字符。当字符不为空格时，循环使用continue语句跳过计数部分。

程序清单6.12　jump.cpp

```css
// jump.cpp -- using continue and break
#include <iostream>
const int ArSize = 80;
int main()
{
    using namespace std;
    char line[ArSize];
    int spaces = 0;
    cout << "Enter a line of text:\n";
    cin.get(line, ArSize);
    cout << "Complete line:\n" << line << endl;
    cout << "Line through first period:\n";
    for (int i = 0; line[i] != '\0'; i++)
    {
        cout << line[i]; // display character
        if (line[i] == '.') // quit if it's a period
            break;
        if (line[i] != ' ') // skip rest of loop
            continue;
        spaces++;
    }
    cout << "\n" << spaces << " spaces\n";
    cout << "Done.\n";
    return 0;
}
```

下面是该程序的运行情况：

```css
Enter a line of text:
Let's do lunch today. You can pay!
Complete line:
Let's do lunch today. You can pay!
Line through first period:
Let's do lunch today.
3 spaces
Done.
```

**程序说明**

虽然continue语句导致该程序跳过循环体的剩余部分，但不会跳过循环的更新表达式。在for循环中，continue语句使程序直接跳到更新表达式处，然后跳到测试表达式处。然而，对于while循环来说，continue将使程序直接跳到测试表达式处，因此while循环体中位于continue之后的更新表达式都将被跳过。在某些情况下，这可能是一个问题。

该程序可以不使用continue语句，而使用下面的代码：

```css
if (line[i] == ' ')
    spaces++;
```

然而，当continue之后有多条语句时，continue语句可以提高程序的可读性。这样，就不必将所有这些语句放在if语句中。

和C语言一样，C++也有goto语句。下面的语句将跳到使用paris:作为标签的位置：

```css
goto paris;
```

也就是说，可以有下面这样的代码：

```css
char ch;
cin >> ch;
if (ch == 'P')
      goto paris;
cout << ...
...
paris: cout << "You've just arrived at Paris.\n";
```

在大多数情况下（有些人认为，在任何情况下），使用goto语句不好，而应使用结构化控制语句（如if else、switch、continue等）来控制程序的流程。

