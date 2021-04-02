### 7.1.2　QFile读写文本文件

QFile类是直接与IO设备打交道，进行文件读写操作的类，使用QFile可以直接打开或保存文本文件。图7-1工具栏上的“QFile直接打开”按钮用QFile类的功能直接打开文本文件，按钮的槽函数及相关函数的代码如下：

```css
void MainWindow::on_actOpen_IODevice_triggered()
{//打开文件
   QString curPath=QDir::currentPath();
   QString dlgTitle="打开一个文件"; 
   QString filter="程序文件(*.h *.cpp);;文本文件(*.txt);;所有文件(*.*)";
   QString aFileName=QFileDialog::getOpenFileName(this,
                   dlgTitle,curPath,filter);
   if (aFileName.isEmpty())
      return;
   openTextByIODevice(aFileName);
}
bool MainWindow::openTextByIODevice(const QString &aFileName)
{//用IODevice方式打开文本文件
   QFile   aFile(aFileName);
   if (!aFile.exists()) //文件不存在
      return false;
   if (!aFile.open(QIODevice::ReadOnly | QIODevice::Text))
      return false;
   ui->textEditDevice->setPlainText(aFile.readAll());
   aFile.close();
   ui->tabWidget->setCurrentIndex(0);
   return  true;
}
```

自定义函数openTextByIODevice()实现文本文件打开的功能。定义QFile对象变量aFile时将文件名传递给它，检查文件存在后，通过open()函数打开文件。

QFile::open()函数打开文件时需要传递 QIODevice::OpenModeFlag 枚举类型的参数，决定文件以什么方式打开，QIODevice::OpenModeFlag类型的主要取值如下。

+ QIODevice::ReadOnly：以只读方式打开文件，用于载入文件。
+ QIODevice::WriteOnly：以只写方式打开文件，用于保存文件。
+ QIODevice::ReadWrite：以读写方式打开。
+ QIODevice::Append：以添加模式打开，新写入文件的数据添加到文件尾部。
+ QIODevice::Truncate：以截取方式打开文件，文件原有的内容全部被删除。
+ QIODevice::Text：以文本方式打开文件，读取时“\n”被自动翻译为换行符，写入时字符串结束符会自动翻译为系统平台的编码，如Windows平台下是“\r\n”。

这些取值可以组合，例如 QIODevice::ReadOnly | QIODevice::Text 表示以只读和文本方式打开文件。

将文件内容全部读出并设置为QPlaintextEdit组件的内容只需一条语句：

```css
ui->textEditDevice->setPlainText(aFile.readAll());
```

文件内容读取结束后，需要调用QFile::close()函数关闭文件。

图7-1工具栏上的“QFile另存”按钮用QFile类的功能将QPlaintextEdit组件中的文本保存为一个文本文件，实现代码如下：

```css
void MainWindow::on_actSave_IODevice_triggered()
{
   QString curPath=QDir::currentPath();
   QString dlgTitle="另存为一个文件"; 
   QString filter="h文件(*.h);;c++文件(*.cpp);;所有文件(*.*)";
   QString aFileName=QFileDialog::getSaveFileName(
               this,dlgTitle,curPath,filter);
   if (aFileName.isEmpty())
      return;
   saveTextByIODevice(aFileName);
}
bool MainWindow::saveTextByIODevice(const QString &aFileName)
{ //用IODevice方式保存文本文件
   QFile  aFile(aFileName);
   if (!aFile.open(QIODevice::WriteOnly | QIODevice::Text))
      return false;
   QString str=ui->textEditDevice->toPlainText();//整个内容作为字符串
   QByteArray  strBytes=str.toUtf8();//转换为字节数组
   aFile.write(strBytes,strBytes.length());  //写入文件
   aFile.close();
   ui->tabWidget->setCurrentIndex(0);
   return  true;
}
```

自定义函数saveTextByIODevice()实现文件保存功能，为了保存文件，用open()打开文件时，使用的模式是QIODevice::WriteOnly | QIODevice::Text。使用WriteOnly隐含着Truncate，即删除文件原有内容。

首先将QPlaintextEdit组件textEditDevice的文本导出为一个字符串，将QString类的toUtf8()函数转换为UTF8编码的字节数组strBytes，然后调用QFile::write()函数将字节数组内容写入文件。

