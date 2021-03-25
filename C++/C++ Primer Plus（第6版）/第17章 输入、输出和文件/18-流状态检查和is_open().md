### 17.4.2　流状态检查和is_open()

C++文件流类从ios_base类那里继承了一个流状态成员。正如前面指出的，该成员存储了指出流状态的信息：一切顺利、已到达文件尾、I/O操作失败等。如果一切顺利，则流状态为零（没有消息就是好消息）。其他状态都是通过将特定位设置为1来记录的。文件流类还继承了ios_base类中报告流状态的方法，表17.4对这些方法进行了总结。可以通过检查流状态来判断最后一个流操作是否成功。对于文件流，这包括检查试图打开文件时是否成功。例如，试图打开一个不存在的文件进行输入时，将设置failbit位，因此可以这样进行检查：

```css
fin.open(argv[file]);
if (fin.fail()) // open attempt failed
{
    ...
}
```

由于ifstream对象和istream对象一样，被放在需要bool类型的地方时，将被转换为bool值，因此您也可以这样做：

```css
fin.open(argv[file]);
if (!fin) // open attempt failed
{
    ...
}
```

然而，较新的C++实现提供了一种更好的检查文件是否被打开的方法——is_open()方法：

```css
if (!fin.is_open()) // open attempt failed
{
    ...
}
```

这种方式之所以更好，是因为它能够检测出其他方式不能检测出的微妙问题，接下来的“警告”将讨论这一点。

> **警告：**
> 以前，检查文件是否成功打开的常见方式如下：

```css
if(fin.fail()) ...  // failed to open
if(!fin.good()) ... // failed to open
if (!fin) ...       // failed to open
```

> fin对象被用于测试条件中时，如果fin.good()为false，将被转换为false；否则将被转换为true。因此上面三种方式等价。然而，这些测试无法检测到这样一种情形：试图以不合适的文件模式（参见本章后面的“文件模式”一节）打开文件时失败。方法is_open()能够检测到这种错误以及good()能够检测到的错误。然而，老式C++实现没有is_open()。

