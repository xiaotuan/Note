使用代码创建 QPlainTextEdit 控件的代码如下所示：

```cpp
// 创建文本框，并设置初始字体
QPlainTextEdit *txtEdit = new QPlainTextEdit;
txtEdit->setPlainText("Hello world\n\nIt is my demo");
QFont font = txtEdit->font();   // 获取字体
font.setPointSize(20);  // 修改字体大小
txtEdit->setFont(font); // 设置字体
```

