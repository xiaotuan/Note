### 17.3.4　其他istream方法

除前面讨论过的外，其他istream方法包括read()、peek()、gcount()和putback()。read()函数读取指定数目的字节，并将它们存储在指定的位置中。例如，下面的语句从标准输入中读取144个字符，并将它们存储在gross数组中：

```css
char gross[144];
cin.read(gross, 144);
```

与getline()和get()不同的是，read()不会在输入后加上空值字符，因此不能将输入转换为字符串。read()方法不是专为键盘输入设计的，它最常与ostream write()函数结合使用，来完成文件输入和输出。该方法的返回类型为istream &，因此可以像下面这样将它拼接起来：

```css
char gross[144];
char score[20];
cin.read(gross, 144).read(score, 20);
```

peek()函数返回输入中的下一个字符，但不抽取输入流中的字符。也就是说，它使得能够查看下一个字符。假设要读取输入，直到遇到换行符或句点，则可以用peek()查看输入流中的下一个字符，以此来判断是否继续读取：

```css
char great_input[80];
char ch;
int i = 0;
while ((ch = cin.peek()) != '.' && ch != '\n')
    cin.get(great_input[i++]);
great_input [i] = '\0';
```

cin.peek()查看下一个输入字符，并将它赋给ch。然后，while循环的测试条件检查ch是否是句点或换行符。如果是，循环将该字符读入到数组中，并更新数组索引。当循环终止时，句点和换行符将留在输入流中，并作为接下来的输入操作读取的第一个字符。然后，代码将一个空值字符放在数组的最后，使之成为一个字符串。

gcount()方法返回最后一个非格式化抽取方法读取的字符数。这意味着字符是由get()、getline()、ignore()或read()方法读取的，不是由抽取运算符（>>）读取的，抽取运算符对输入进行格式化，使之与特定的数据类型匹配。例如，假设使用cin.get（myarray，80）将一行读入myarray数组中，并想知道读取了多少个字符，则可以使用strlen()函数来计算数组中的字符数，这种方法比使用cin.gcount()计算从输入流中读取了多少字符的速度要快。

putback()函数将一个字符插入到输入字符串中，被插入的字符将是下一条输入语句读取的第一个字符。putback()方法接受一个char参数——要插入的字符，其返回类型为istream &，这使得可以将该函数调用与其他istream方法拼接起来。使用peek()的效果相当于先使用get()读取一个字符，然后使用putback()将该字符放回到输入流中。然而，putback()允许将字符放到不是刚才读取的位置。

程序清单17.14采用两种方式来读取并显示输入中#字符（不包括）之前的内容。第一种方法读取#字符，然后使用putback()将它插回到输入中。第二种方法在读取之前使用peek()查看下一个字符。

程序清单17.14　peeker.cpp

```css
// peeker.cpp -- some istream methods
#include <iostream>
int main()
{
    using std::cout;
    using std::cin;
    using std::endl;
// read and echo input up to a # character
    char ch;
    while(cin.get(ch)) // terminates on EOF
    {
        if (ch != '#')
            cout << ch;
        else
        {
            cin.putback(ch); // reinsert character
            break;
    }
}
if (!cin.eof())
{
    cin.get(ch);
    cout << endl << ch << " is next input character.\n";
}
else
{
    cout << "End of file reached.\n";
    std::exit(0);
}
while(cin.peek() != '#') // look ahead
{
    cin.get(ch);
    cout << ch;
}
if (!cin.eof())
    {
        cin.get(ch);
        cout << endl << ch << " is next input character.\n";
    }
    else
        cout << "End of file reached.\n";
    return 0;
}
```

下面是程序清单17.14中程序的运行情况：

```css
I used a #3 pencil when I should have used a #2.
I used a
# is next input character.
3 pencil when I should have used a
# is next input character.
```

**程序说明**

来详细讨论程序清单17.14中的一些代码。第一种方法是用while循环来读取输入：

```css
while(cin.get(ch))    // terminates on EOF
{
    if (ch != '#')
        cout << ch;
    else
    {
        cin.putback(ch);    // reinsert character
        break;
    }
}
```

达到文件尾时，表达式（cin.get（ch））将返回false，因此从键盘模拟文件尾将终止循环。如果#字符首先出现，则程序将该字符放回到输入流中，并使用break语句来终止循环。

第二种方法看上去更简单：

```css
while(cin.peek() != '#') // look ahead
{
    cin.get(ch);
    cout << ch;
}
```

程序查看下一个字符。如果它不是#，则读取并显示它，然后再查看下一个字符。这一过程将一直继续下去，直到出现分界字符。

现在来看一个例子（参见程序清单17.15），它使用peek()来确定是否读取了整行。如果一行中只有部分内容被加入到输入数组中，程序将删除余下的内容。

程序清单17.15　truncate.cpp

```css
// truncate.cpp -- using get() to truncate input line, if necessary
#include <iostream>
const int SLEN = 10;
inline void eatline() { while (std::cin.get() != '\n') continue; }
int main()
{
    using std::cin;
    using std::cout;
    using std::endl;
    char name[SLEN];
    char title[SLEN];
    cout << "Enter your name: ";
    cin.get(name,SLEN);
    if (cin.peek() != '\n')
        cout << "Sorry, we only have enough room for "
                << name << endl;
    eatline();
    cout << "Dear " << name << ", enter your title: \n";
    cin.get(title,SLEN);
    if (cin.peek() != '\n')
        cout << "We were forced to truncate your title.\n";
    eatline();
    cout << " Name: " << name
         << "\nTitle: " << title << endl;
    return 0;
}
```

下面是程序清单17.15中程序的运行情况：

```css
Enter your name: Ella Fishsniffer
Sorry, we only have enough room for Ella Fish
Dear Ella Fish, enter your title:
Executive Adjunct
We were forced to truncate your title.
 Name: Ella Fish
Title: Executive
```

注意，下面的代码确定第一条输入语句是否读取了整行：

```css
while (cin.get() != '\n') continue;
```

如果get()读取了整行，它将保留换行符，而上述代码将读取并丢弃换行符。如果get()只读取一部分，则上述代码将读取并丢弃该行中余下的内容。如果不删除余下的内容，则下一条输入语句将从第一个输入行中余下部分的开始位置读取。对于这个例子，这将导致程序把字符串sniffer读取到title数组中。

