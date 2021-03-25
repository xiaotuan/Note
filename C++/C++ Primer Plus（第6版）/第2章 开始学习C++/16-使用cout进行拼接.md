### 2.3.2　使用cout进行拼接

getinfo.cpp中的另一项新特性是将4条输出语句合并为一条。iostream文件定义了<<运算符，以便可以像下面这样合并（拼接）输出：

```css
cout << "Now you have " << carrots << " carrots." << endl;
```

这样能够将字符串输出和整数输出合并为一条语句。得到的输出与下述代码生成的相似：

```css
cout << "Now you have ";
cout << carrots;
cout << " carrots";
cout << endl;
```

根据有关cout的建议，也可以按照这样的方式重写拼接版本，即将一条语句放在4行上：

```css
cout << "Now you have "
     << carrots
     << " carrots."
     << endl;
```

这是由于C++的自由格式规则将标记间的换行符和空格看作是可相互替换的。当代码行很长，限制输出的显示风格时，最后一种技术很方便。

需要注意的另一点是：

```css
Now you have 14 carrots.
```

和

```css
Here are two more.
```

在同一行中。

这是因为前面指出过的，cout语句的输出紧跟在前一条cout语句的输出后面。即使两条cout语句之间有其他语句，情况也将如此。

