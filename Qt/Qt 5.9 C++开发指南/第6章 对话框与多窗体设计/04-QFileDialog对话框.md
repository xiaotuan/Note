### 6.1.2　QFileDialog对话框

#### 1．选择打开一个文件

若要打开一个文件，可调用静态函数QFileDialog::getOpenFileName()，“打开一个文件”按钮的响应代码如下：

```css
void Dialog::on_btnOpen_clicked()
{ //选择单个文件
   QString curPath=QDir::currentPath();//获取应用程序当前目录
   QString dlgTitle="选择一个文件"; 
   QString filter="文本文件(*.txt);;图片文件(*.jpg *.gif);;所有文件(*.*)";
   QString aFileName=QFileDialog::getOpenFileName(this, 
                       dlgTitle, curPath, filter);
   if (!aFileName.isEmpty())
      ui->plainTextEdit->appendPlainText(aFileName);
}
```

QFileDialog::getOpenFileName()函数需要传递3个字符串型参数，分别如下。

+ 对话框标题，这里设置为"选择一个文件"。
+ 初始化目录，打开对话框时的初始目录，这里用QDir::currentPath() 获取应用程序当前目录。
+ 文件过滤器，设置选择不同后缀的文件，可以设置多组文件，如：

```css
QString filter="文本文件(*.txt);;图片文件(*.jpg *.gif *.png);;所有文件(*.*)";
```

每组文件之间用两个分号隔开，同一组内不同后缀之间用空格隔开。

QFileDialog ::getOpenFileName()函数返回的是选择文件的带路径的完整文件名，如果在对话框里取消选择，则返回字符串为空。

#### 2．选择打开多个文件

若要选择打开多个文件，可使用静态函数QFileDialog::getOpenFileNames()，“打开多个文件”按钮的响应代码如下：

```css
void Dialog::on_btnOpenMulti_clicked()
{ //选择多个文件
   QString curPath=QDir::currentPath();
   QString dlgTitle="选择多个文件"; 
   QString filter="文本文件(*.txt);;图片文件(*.jpg *.gif);;所有文件(*.*)"; 
   QStringList fileList=QFileDialog::getOpenFileNames(this,
                   dlgTitle,curPath,filter);
   for (int i=0; i<fileList.count();i++)
      ui->plainTextEdit->appendPlainText(fileList.at(i));
}
```

getOpenFileNames()函数的传递参数与getOpenFileName()一样，只是返回值是一个字符串列表，列表的每一行是选择的一个文件。

#### 3．选择已有目录

选择已有目录可调用静态函数QFileDialog::getExistingDirectory()，同样，若需要传递对话框标题和初始路径，还应传递一个选项，一般用QFileDialog::ShowDirsOnly，表示对话框中只显示目录。

```css
void Dialog::on_btnSelDir_clicked()
{ //选择文件夹
   QString curPath=QCoreApplication::applicationDirPath();
   QString dlgTitle="选择一个目录"; 
   QString selectedDir=QFileDialog::getExistingDirectory(this,
                dlgTitle,curPath, QFileDialog::ShowDirsOnly);
   if (!selectedDir.isEmpty())
      ui->plainTextEdit->appendPlainText(selectedDir);
}
```

静态函数QCoreApplication::applicationDirPath()返回应用程序可执行文件所在的目录，getExistingDirectory()函数的返回值是选择的目录名称字符串。

#### 4．选择保存文件名

选择一个保存文件，使用静态函数QFileDialog::getSaveFileName()，传递的参数与getOpenFile　Name()函数相同。只是在调用getSaveFileName()函数时，若选择的是一个已经存在的文件，会提示是否覆盖原有的文件。如果提示覆盖，会返回为选择的文件，但是并不会对文件进行实质操作，对文件的删除操作需要在选择文件之后自己编码实现。如下面的代码，即使选择覆盖文件，由于代码里没有实质地覆盖原来的文件，也不会对选择的文件造成任何影响。

```css
void Dialog::on_btnSave_clicked()
{//保存文件
   QString curPath=QCoreApplication::applicationDirPath();
   QString dlgTitle="保存文件";
   QString filter="h文件(*.h);;C++文件(.cpp);;所有文件(*.*)";
   QString aFileName=QFileDialog::getSaveFileName(this,
                  dlgTitle,curPath,filter);
   if (!aFileName.isEmpty())
      ui->plainTextEdit->appendPlainText(aFileName);
}
```

