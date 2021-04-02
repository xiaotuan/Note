### 7.1.3　QFile和QTextStream结合读写文本文件

QTextStream与IO读写设备结合，为数据读写提供了一些方便的方法的类，QTextStream可以与QFile、QTemporaryFile、QBuffer、QTcpSocket和QUdpSocket等IO设备类结合使用。

在本例中，将QFile和QTextStream结合，读取文本文件的自定义函数openTextByStream()的代码如下：

```css
bool MainWindow::openTextByStream(const QString &aFileName)
{ //用 QTextStream打开文本文件
   QFile   aFile(aFileName);
   if (!aFile.exists()) //文件不存在
      return false;
   if (!aFile.open(QIODevice::ReadOnly | QIODevice::Text))
      return false;
   QTextStream  aStream(&aFile); //用文本流读取文件
   aStream.setAutoDetectUnicode(true); //自动检测Unicode,才能显示汉字
   ui->textEditStream->setPlainText(aStream.readAll());
   aFile.close();//关闭文件
   ui->tabWidget->setCurrentIndex(1);
   return  true;
}
```

在创建QTextStream实例时传递一个QFile对象，这样，QFile对象和QTextStream对象就结合在一起了，利用QTextStream可读写文件。如果文本文件里有汉字，需要设定为自动识别Unicode码，即调用setAutoDetectUnicode(true)函数。

在这段代码里，使用QTextStream::readAll()函数一次读出文件全部文本内容。但是QTextStream还提供了一些其他方便使用的接口函数，如使用QTextStream可以方便地实现逐行读取文本文件内容。对openTextByStream()函数的内容稍作修改，使其以逐行的方式读取文件内容，这种方式适用于需要逐行解析字符串的内容的应用，如5.4节的实例。

```css
bool MainWindow::openTextByStream(const QString &aFileName)
{ //用 QTextStream打开文本文件
   QFile   aFile(aFileName);
   if (!aFile.exists()) //文件不存在
      return false;
   if (!aFile.open(QIODevice::ReadOnly | QIODevice::Text))
      return false;
   QTextStream  aStream(&aFile); //用文本流读取文件
   aStream.setAutoDetectUnicode(true); //自动检测Unicode 
   ui->textEditStream->clear();
   while (!aStream.atEnd())
   {
      str=aStream.readLine();//读取文件的一行文本
      ui->textEditStream->appendPlainText(str); 
   }
   aFile.close();//关闭文件
   ui->tabWidget->setCurrentIndex(1);
   return  true;
}
```

QTextStream::readLine()函数通过自动识别换行符来读取一行字符串。

saveTextByStream()使用QTextStream保存文件的自定义函数，代码如下：

```css
bool MainWindow::saveTextByStream(const QString &aFileName)
{//用QTextStream保存文本文件
   QFile   aFile(aFileName);
   if (!aFile.open(QIODevice::WriteOnly | QIODevice::Text))
      return false;
   QTextStream aStream(&aFile); //用文本流读取文件
   aStream.setAutoDetectUnicode(true); //自动检测Unicode 
   QString str=ui->textEditStream->toPlainText();
   aStream<close();//关闭文件
   return  true;
}
```

因为在写入文件时，直接使用了流的写入操作，所以，使用QTextStream进行文件读写是比较方便的。

