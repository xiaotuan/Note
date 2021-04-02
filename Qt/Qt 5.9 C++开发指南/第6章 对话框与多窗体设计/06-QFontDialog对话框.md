### 6.1.4　QFontDialog对话框

QFontDialog是选择字体对话框，选择字体使用静态函数QFontDialog::getFont()。下面是“选择字体”按钮的代码，它为文本框选择字体，字体设置的内容包括字体名称、大小、粗体、斜体等。

```css
void Dialog::on_btnFont_clicked()
{//选择字体
   QFont iniFont=ui->plainTextEdit->font();
   bool   ok=false;
   QFont font=QFontDialog::getFont(&ok,iniFont); 
   if (ok)
      ui->plainTextEdit->setFont(font);
}
```

getFont()返回一个字体变量，但是QFont没有类似于isValid()的函数来判断有效性，所以在调用getFont()函数时以引用方式传递一个逻辑变量ok，调用后通过判断ok是否为true来判断字体选择是否有效。

