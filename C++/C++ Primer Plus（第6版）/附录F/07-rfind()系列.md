### F.5.2　rfind()系列

rfind()方法的原型如下：

```css
size_type rfind(const basic_string& str,
                size_type pos = npos) const noexcept;
size_type rfind(const charT* s, size_type pos = npos) const;
size_type rfind(const charT* s, size_type pos, size_type n) const;
size_type rfind(charT c, size_type pos = npos) const noexcept;
```

这些方法与相应find()方法的工作方式相似，但它们搜索字符串最后一次出现的位置，该位置位于pos之前（包括pos）。如果没有找到，该方法将返回npos。

下面的代码从字符串末尾开始查找子字符串“hat”的位置：

```css
string longer("That is a funny hat.");
string shorter("hat");
size_type loc1 = longer.rfind(shorter);           // sets loc1 to 16
size_type loc2 = longer.rfind(shorter, loc1 - 1); // sets loc2 to 1
```

