### F.5.5　find_first_not_of()系列

find_first_not_of()方法的原型如下：

```css
size_type find_first_not_of(const basic_string& str,
                           size_type pos = 0) const noexcept;
size_type find_first_not_of(const charT* s, size_type pos,
                            size_type n) const;
size_type find_first_not_of(const charT* s, size_type pos = 0) const;
size_type find_first_not_of(charT c, size_type pos = 0) const noexcept;
```

这些方法与对应find_first_of()方法的工作方式相似，但它们搜索第一个不位于子字符串中的字符。

下面的代码在字符串中查找第一个没有出现在“This”和“Thatch”中的字母：

```css
string longer("That is a funny hat.");
string shorter("This");
size_type loc1 = longer.find_first_not_of(shorter);  // sets loc1 to 2
size_type loc2 = longer.find_first_not_of("Thatch"); // sets loc2 to 4
```

在longer中，That中的a是第一个在This中没有出现的字符，而字符串longer中的第一个空格是第一个没有在Thatch中出现的字符。

