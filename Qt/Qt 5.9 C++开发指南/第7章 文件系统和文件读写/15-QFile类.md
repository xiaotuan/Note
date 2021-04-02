### 7.3.4　QFile类

前两节使用QFile类进行文件的操作，应用了QFile::open()函数。除了打开文件提供读写操作外，QFile还有一些静态函数和成员函数用于文件操作。表7-5是QFile的一些静态函数（省略了函数参数中的const关键字）。

<center class="my_markdown"><b class="my_markdown">表7-5　QFile的一些静态函数</b></center>

| 函数原型 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| bool　copy(QString &fileName, QString &newName) | 复制文件 |
| bool　rename(QString &oldName, QString &newName) | 重命名文件 |
| bool　remove(QString &fileName) | 删除一个文件 |
| bool　exists(QString &fileName) | 判断文件是否存在 |
| bool　setPermissions(QString &fileName, Permissions permissions) | 设置文件的权限，权限类型是枚举类型QFileDevice::Permission |
| Permissions　permissions(QString &fileName) | 返回文件的权限 |

静态函数是无需创建QFile类对象实例就可以调用的函数，例如使用静态函数exists()判断一个文件是否存在的代码如下：

```css
void Dialog::on_pushButton_51_clicked()
{// QFile::exists()判断文件是否存在
   showBtnInfo(sender());
   QString sous=ui->editFile->text(); //源文件
   bool the=QFile::exists(sous);
   if(the)
      ui->plainTextEdit->appendPlainText(+"true \n");
   else
      ui->plainTextEdit->appendPlainText(+"false \n");
}
```

QFile还提供了对应的成员函数，见表7-6（省略了函数参数中的const关键字）。

<center class="my_markdown"><b class="my_markdown">表7-6　QFile的一些成员函数</b></center>

| 函数原型 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| void　setFileName(QString &name) | 设置文件名，文件已打开后不能再调用此函数 |
| bool　copy(QString &newName) | 当前文件复制为newName表示的文件 |
| bool　rename(QString &newName) | 将当前文件重命名为newName |
| bool　remove() | 删除当前文件 |
| bool　exists() | 判断当前文件是否存在 |
| bool　setPermissions(Permissions permissions) | 设置文件权限 |
| Permissions　permissions() | 返回文件的权限 |
| qint64　size() | 返回文件的大小，字节数 |

创建QFile对象时可以在构造函数里指定文件名，也可以用setFileName()指定文件，但是文件打开后不能再调用setFileName()函数。指定的文件作为QFile对象的当前文件，然后成员函数copy()、rename()等都是基于当前文件的操作。

