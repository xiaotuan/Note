### 3.4.3　foreach关键字

如果只是想遍历容器中所有的项，可以使用foreach关键字。foreach是<QtGlobal>头文件中定义的一个宏。使用foreach的句法是：

```css
foreach (variable, container) 
```

使用foreach的代码比使用迭代器更简洁。例如，使用foreach遍历一个QLinkedList<QString>的示例代码如下：

```css
QLinkedList<QString> list;
...
QString str;
foreach (str, list)
   qDebug() << str;
```

用于迭代的变量也可以在foreach语句里定义，foreach语句也可以使用花括号，可以使用break退出迭代，示例代码如下：

```css
QLinkedList<QString> list;
...
foreach (const QString &str, list) {
   if (str.isEmpty())
      break;
   qDebug() << str;
}
```

对于QMap和QHash，foreach会自动访问“键——值”对里的值，所以无需调用values()。如果需要访问键则可以调用keys()，示例代码如下：

```css
QMap<QString, int> map;
...
foreach (const QString &str, map.keys())
   qDebug() << str << ':' << map.value(str);
```

对于多值映射，可以使用两重foreach语句，示例代码如下：

```css
QMultiMap<QString, int> map;
...
foreach (const QString &str, map.uniqueKeys()) {
   foreach (int i, map.values(str))
      qDebug() << str << ':' << i;
}
```

> **注意**
> foreach关键字遍历一个容器变量是创建了容器的一个副本，所以不能修改原来容器变量的数据项。

