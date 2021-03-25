### F.7.6　其他修改方法：copy()和swap()

copy()方法将string对象或其中的一部分复制到指定的字符串数组中：

```css
size_type copy(charT* s, size_type n, size_type pos = 0) const;
```

其中，s指向目标数组，n是要复制的字符数，pos指出从string对象的什么位置开始复制。复制将一直进行下去，直到复制了n个字符或到达string对象的最后一个字符。函数返回复制的字符数，该方法不追加空值字符，同时由程序员负责检查数组的长度是否足够存储复制的内容。

> **警告：**
> copy()方法不追加空值字符，也不检查目标数组的长度是否足够。

swap()方法使用一个时间恒定的算法来交换两个string对象的内容：

```css
void swap(basic_string& str);
```

