### 7.3.7　QTemporaryDir和QTemporaryFile

QTemporaryDir是用于创建、删除临时目录的类，其主要函数见表7-10。

<center class="my_markdown"><b class="my_markdown">表7-10　QTemporaryDir的一些成员函数</b></center>

| 函数原型 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| void　setAutoRemove(bool b) | 设置为是否自动删除 |
| QString　path() | 返回创建的临时目录名称 |
| bool　remove() | 删除此临时目录及其下面所有文件 |

在系统临时目录，即QDir::tempPath目录下创建一个临时目录，临时目录名称以QCoreApplication:: applicationName()为前缀，后加6个字符。临时目录可以设置为使用完后自动删除，即临时目录变量删除时，临时目录也删除。

QTemporaryFile是用于创建临时文件的类，临时文件保存在系统临时目录下。临时文件以QCoreApplication::applicationName()作为文件名，以“XXXXXX”6个随机数字作为文件后缀。将QTemporaryFile::setAutoRemove()函数设置为是否自动删除临时文件，QTemporaryFile::open()函数用于打开临时文件，只有打开临时文件，才实际创建了此文件。

