### 4.3.3　string类的其他操作

在C++新增string类之前，程序员也需要完成诸如给字符串赋值等工作。对于C-风格字符串，程序员使用C语言库中的函数来完成这些任务。头文件cstring（以前为string.h）提供了这些函数。例如，可以使用函数strcpy()将字符串复制到字符数组中，使用函数strcat()将字符串附加到字符数组末尾：

```css
strcpy(charr1, charr2);  // copy charr2 to charr1
strcat(charr1, charr2);  // append contents of charr2 to char1
```

程序清单4.9对用于string对象的技术和用于字符数组的技术进行了比较。

程序清单4.9　strtype3.cpp

```css
// strtype3.cpp -- more string class features
#include <iostream>
#include <string>         // make string class available
#include <cstring>        // C-style string library
int main()
{
    using namespace std;
    char charr1[20];
    char charr2[20] = "jaguar";
    string str1;
    string str2 = "panther";
    // assignment for string objects and character arrays
    str1 = str2;              // copy str2 to str1
    strcpy(charr1, charr2);   // copy charr2 to charr1
    // appending for string objects and character arrays
    str1 += " paste";          // add paste to end of str1
    strcat(charr1, " juice");  // add juice to end of charr1
    // finding the length of a string object and a C-style string
    int len1 = str1.size();     // obtain length of str1
    int len2 = strlen(charr1);  // obtain length of charr1
    cout << "The string " << str1 << " contains "
         << len1 << " characters.\n";
    cout << "The string " << charr1 << " contains "
         << len2 << " characters.\n";
    return 0;
}
```

下面是该程序的输出：

```css
The string panther paste contains 13 characters.
The string jaguar juice contains 12 characters.
```

处理string对象的语法通常比使用C字符串函数简单，尤其是执行较为复杂的操作时。例如，对于下述操作：

```css
str3 = str1 + str2;
```

使用C-风格字符串时，需要使用的函数如下：

```css
strcpy(charr3, charr1);
strcat(charr3, charr2);
```

另外，使用字符数组时，总是存在目标数组过小，无法存储指定信息的危险，如下面的示例所示：

```css
char site[10] = "house";
strcat(site, " of pancakes"); // memory problem
```

函数strcat()试图将全部12个字符复制到数组site中，这将覆盖相邻的内存。这可能导致程序终止，或者程序继续运行，但数据被损坏。string类具有自动调整大小的功能，从而能够避免这种问题发生。C函数库确实提供了与strcat()和strcpy()类似的函数——strncat()和strncpy()，它们接受指出目标数组最大允许长度的第三个参数，因此更为安全，但使用它们进一步增加了编写程序的复杂度。

下面是两种确定字符串中字符数的方法：

```css
int len1 = str1.size(); // obtain length of str1
int len2 = strlen(charr1); // obtain length of charr1
```

函数strlen()是一个常规函数，它接受一个C-风格字符串作为参数，并返回该字符串包含的字符数。函数size()的功能基本上与此相同，但句法不同：str1不是被用作函数参数，而是位于函数名之前，它们之间用句点连接。与第3章介绍的put()方法相同，这种句法表明，str1是一个对象，而size()是一个类方法。方法是一个函数，只能通过其所属类的对象进行调用。在这里，str1是一个string对象，而size()是string类的一个方法。总之，C函数使用参数来指出要使用哪个字符串，而C++ string类对象使用对象名和句点运算符来指出要使用哪个字符串。

