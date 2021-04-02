### 4.5.3　QPlainTextEdit的使用

#### 1．QPlainTextEdit的功能

QPlainTextEdit是用于编辑多行文本的编辑器，可以编辑普通文本。另外，还有一个QTextEdit组件，是一个所见即所得的可以编辑带格式文本的组件，以HTML格式标记符定义文本格式。

从前面的代码已经看出，使用QPlainTextEdit::appendPlainText(const QString &text)函数就可以向PlainTextEdit组件添加一行字符串。

QPlainTextEdit提供cut()、copy()、paste()、undo()、redo()、clear()、selectAll()等标准编辑功能的槽函数，QPlainTextEdit还提供一个标准的右键快捷菜单。

#### 2．逐行读取文字内容

如果要将QPlainTextEdit组件里显示的所有文字读取出来，有一个简单的函数toPlainText()可以将全部文字内容输出为一个字符串，其定义如下：

```css
QString QPlainTextEdit::toPlainText() const
```

但是如果要逐行读取QPlainTextEdit组件里的字符串，则稍微麻烦一点。

下面是图4-6窗口中“文本框内容添加到ComboBox”按钮的响应代码，它将plainTextEdit里的每一行作为一个项添加到comboBox里。

```css
void Widget::on_btnToComboBox_clicked()
{ //plainTextEdit 的内容逐行添加为 comboBox 的项
   QTextDocument* doc=ui->plainTextEdit->document();//文本对象
   int cnt=doc->blockCount();//回车符是一个block
   QIcon   icon(":/images/icons/aim.ico");
   ui->comboBox->clear();
   for (int i=0; i<cnt;i++) 
   {
       QTextBlock  textLine=doc->findBlockByNumber(i);// 文本中的一段
       QString str=textLine.text();
       ui->comboBox->addItem(icon,str); 
   }
}
```

QPlainTextEdit的文字内容以QTextDocument类型存储，函数document()返回这个文档对象的指针。

QTextDocument是内存中的文本对象，以文本块的方式存储，一个文本块就是一个段落，每个段落以回车符结束。QTextDocument提供一些函数实现对文本内容的存取。

+ int blockCount()，获得文本块个数。
+ QTextBlock findBlockByNumber(int blockNumber)，读取某一个文本块，序号从0开始，至blockCount()-1结束。

一个document有多个TextBlock，从document中读取出的一个文本块类型为QTextBlock，通过QTextBlock::text()函数可以获取其纯文本文字。

#### 3．使用QPlainTextEdit自带的快捷菜单

QPlainTextEdit是一个多行文字编辑框，有自带的右键快捷菜单，可实现常见的编辑功能。在UI设计器里，选择为plainTextEdit的customContextMenuRequested()信号生成槽函数，编写如下的代码，就可以创建并显示QPlainTextEdit的标准快捷菜单：

```css
void Widget::on_plainTextEdit_customContextMenuRequested(const QPoint &pos)
{ //创建并显示标准弹出式菜单
   QMenu* menu=ui->plainTextEdit->createStandardContextMenu(); 
   menu->exec(pos); 
}
```

