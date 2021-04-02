### 7.3.5　QFileInfo类

QFileInfo类的接口函数提供文件的各种信息。QFileInfo对象创建时可以指定一个文件名作为当前文件，也可以用setFile()函数指定一个文件作为当前文件。

QFileInfo常见接口函数和功能见表7-7。除了一个静态函数exists()之外，其他都是公共接口函数，接口函数的操作都是针对当前文件（省略了函数参数中的const关键字）。

<center class="my_markdown"><b class="my_markdown">表7-7　QFileInfo的一些函数</b></center>

| 函数原型 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| void　setFile(QString &file) | 设置一个文件名，作为QFileInfo操作的文件 |
| QString　absoluteFilePath() | 返回带有文件名的绝对文件路径 |
| QString　absolutePath() | 返回绝对路径，不带文件名 |
| QString　fileName() | 返回去除路径的文件名 |
| QString　filePath() | 返回包含路径的文件名 |
| QString　path() | 返回不含文件名的路径 |
| qint64　size() | 返回文件大小，以字节为单位 |
| QString　baseName() | 返回文件基名，第一个“.”之前的文件名 |
| QString　completeBaseName() | 返回文件基名，最后一个“.”之前的文件名 |
| QString　suffix() | 最后一个“.”之后的后缀 |
| QString　completeSuffix() | 第一个“.”之后的后缀 |
| bool　isDir() | 判断当前对象是否是一个目录或目录的快捷方式 |
| bool　isFile() | 判断当前对象是否是一个文件或文件的快捷方式 |
| bool　isExecutable() | 判断当前文件是否是可执行文件 |
| QDateTime　created() | 返回文件创建时间 |
| QDateTime　lastModified() | 返回文件最后一次被修改的时间 |
| QDateTime　lastRead() | 返回文件最后一次被读取的时间 |
| bool　exists() | 判断文件是否存在 |
| bool exists(QString &file) | 静态函数，判断file表示的文件是否存在 |

QFileInfo提供的这些函数可以提取文件的信息，包括目录名、文件基名（不带后缀）、文件后缀等，利用这些函数可以实现灵活的文件操作。例如，下面的代码是利用QFile::rename()函数和QFileInfo的一些功能实现文件重命名功能的代码，其中就用到了提取路径、提取文件基名的功能。

```css
void Dialog::on_pushButton_50_clicked()
{//QFile::rename()
   showBtnInfo(sender());
   QString sous=ui->editFile->text(); //源文件
   QFileInfo   fileInfo(sous);//源文件信息
   QString newFile=fileInfo.path()+"/"+fileInfo.baseName()+".XYZ"; 
   QFile::rename(sous,newFile); //重命名文件,更改后缀名
   ui->plainTextEdit->appendPlainText("源文件："+sous);
   ui->plainTextEdit->appendPlainText("重命名为："+newFile+"\n");
}
```

表7-7中的函数的使用方法和执行效果不再详细列举和说明，运行实例samp7_3观察执行结果，可参考Qt帮助文件或samp7_3的源程序看函数使用方法。

