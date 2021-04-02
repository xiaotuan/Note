### 7.3.6　QDir类

QDir是进行目录操作的类，在创建QDir对象时传递一个目录字符串作为当前目录，然后QDir函数就可以针对当前目录或目录下的文件进行操作。表7-8是QDir的一些静态函数（省略了函数参数中的const关键字）。

<center class="my_markdown"><b class="my_markdown">表7-8　QDir的一些静态函数</b></center>

| 函数原型 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| QString　tempPath() | 返回临时文件目录名称 |
| QString　rootPath() | 返回根目录名称 |
| QString　homePath() | 返回主目录名称 |
| QString　currentPath() | 返回当前目录名称 |
| bool　setCurrent(QString &path) | 设置path表示的目录为当前目录 |
| QFileInfoList　drives() | 返回系统的根目录列表，在Windows系统上返回的是盘符列表 |

在使用QFileDialog选择打开一个文件或目录时需要传递一个初始目录，这个时候就可以使用QDir:: currentPath()获取应用程序当前目录作为初始目录，前面一些实例程序的代码中已经用到过这个功能。

表7-9是QDir的一些公共接口函数（省略了函数参数中的const关键字）。

<center class="my_markdown"><b class="my_markdown">表7-9　QDir的一些成员函数</b></center>

| 函数原型 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| QString　absoluteFilePath(QString &fileName) | 返回当前目录下的一个文件的含绝对路径文件名 |
| QString　absolutePath() | 返回当前目录的绝对路径 |
| QString　canonicalPath() | 返回当前目录的标准路径 |
| QString　filePath(QString &fileName) | 返回目录下一个文件的目录名 |
| QString　dirName() | 返回最后一级目录的名称 |
| bool　exists() | 判断当前目录是否存在 |
| QStringList　entryList(Filters filters = NoFilter, SortFlags sort = NoSort) | 返回目录下的所有文件名、子目录名等 |
| bool　mkdir(QString &dirName) | 在当前目录下建一个名称为dirName的子目录 |
| bool　rmdir(QString &dirName) | 删除指定的目录dirName |
| bool　remove(QString &fileName) | 删除当前目录下的文件fileName |
| bool　rename(QString &oldName, QString &newName) | 将文件或目录oldName更名为newName |
| void　setPath(QString &path) | 设置QDir对象的当前目录 |
| bool　removeRecursively() | 删除当前目录及其下面的所有文件 |

获取目录下的目录或文件列表的函数entryList()需要传递QDir::Filter枚举类型的参数以获取不同的结果，QDir::Filter枚举类型的常用取值如下。

+ QDir::AllDirs：列出所有目录名。
+ QDir::Files：列出所有文件。
+ QDir::Drives：列出所有盘符（Unix系统下无效）。
+ QDir::NoDotAndDotDot：不列出特殊的符号，如“.”和“..”。
+ QDir::AllEntries：列出目录下所有项目。

列出所有子目录的程序如下：

```css
void Dialog::on_pushButton_11_clicked()
{//列出子目录
   showBtnInfo(sender());
   QDir   dir(ui->editDir->text());
   QStringList strList=dir.entryList(QDir::Dirs | QDir::NoDotAndDotDot);
   ui->plainTextEdit->appendPlainText("所选目录下的所有目录:");
   for(int i=0;i<strList.count();i++)
      ui->plainTextEdit->appendPlainText(strList.at(i));
   ui->plainTextEdit->appendPlainText("\n");
}
```

列出一个目录下所有文件的程序如下：

```css
void Dialog::on_pushButton_17_clicked()
{//列出所有文件
   showBtnInfo(sender());
   QDir   dir(ui->editDir->text());
   QStringList strList=dir.entryList(QDir::Files);
   ui->plainTextEdit->appendPlainText("所选目录下的所有文件：");
   for(int i=0;i<strList.count();i++)
      ui->plainTextEdit->appendPlainText(strList.at(i));
   ui->plainTextEdit->appendPlainText("\n");
}
```

