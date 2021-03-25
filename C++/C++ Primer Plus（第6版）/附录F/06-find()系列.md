### F.5.1　find()系列

在C++11中，find()的原型如下：

```css
size_type find (const basic_string& str, size_type pos = 0) const noexcept;
size_type find (const charT* s, size_type pos = 0) const;
size_type find (const charT* s, size_type pos, size_type n) const;
size_type find (charT c, size_type pos = 0) const noexcept;
```

第一个返回str在调用对象中第一次出现时的起始位置。搜索从pos开始，如果没有找到子字符串，将返回npos。

下面的代码在一个字符串中查找字符串“hat”的位置：

```css
string longer("That is a funny hat.");
string shorter("hat");
size_type loc1 = longer.find(shorter);           // sets loc1 to 1
size_type loc2 = longer.find(shorter, loc1 + 1); // sets loc2 to 16
```

由于第二条搜索语句从位置2开始（That中的a），因此它找到的第一个hat位于字符串尾部。要测试是否失败，可使用string::npos值：

```css
if (loc1 == string::npos)
    cout << "Not found\n";
```

第二个方法完成同样的工作，但它使用字符数组而不是string对象作为子字符串：

```css
size_type loc3 = longer.find("is"); //sets loc3 to 5
```

第三个方法完成相同的工作，但它只使用字符串s的前n个字符。这与使用basic_string（const charT * s，size_type n）构造函数，然后将得到的对象用作第一种格式的find()的string参数的效果完全相同。例如，下面的代码搜索子字符串“fun”：

```css
size_type loc4 = longer.find("funds", 3); //sets loc4 to 10
```

第四个方法的功能与第一个相同，但它使用一个字符而不是string对象作为子字符串：

```css
size_type loc5 = longer.find('a'); //sets loc5 to 2
```

