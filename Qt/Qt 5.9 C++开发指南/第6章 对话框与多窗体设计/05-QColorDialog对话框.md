### 6.1.3　QColorDialog对话框

QColorDialog是选择颜色对话框，选择颜色使用静态函数QColorDialog::getColor()。下面是“选择颜色”按钮的代码，它为文本框的字体选择颜色。

```css
void Dialog::on_btnColor_clicked()
{//选择颜色
   QPalette pal=ui->plainTextEdit->palette(); //获取现有 palette
   QColor  iniColor=pal.color(QPalette::Text); //现有的文字颜色
   QColor color=QColorDialog::getColor(iniColor,this,"选择颜色");
   if (color.isValid())
   {
      pal.setColor(QPalette::Text,color); 
      ui->plainTextEdit->setPalette(pal); 
   }
}
```

getColor()函数需要传递一个初始的颜色，这里是将palette提取的文本颜色作为初始颜色。getColor()函数返回一个颜色变量，若在颜色对话框里取消选择，则返回的颜色值无效，通过QColor::isValid()函数来判断返回是否有效。

