### 7.3.3　QCoreApplication类

QCoreApplication是为无GUI应用提供事件循环的类，是所有应用程序类的基类，其子类QGuiApplication为有GUI界面的应用程序提供流控制和主要的设定，QGuiApplication的子类QApplication为基于QWidget的应用程序提供支持，包括界面的初始化等。

创建的Qt Widget Application都是基于QApplication的，在main()函数里可以看到QApplication的应用。

QCoreApplication提供了一些有用的静态函数，可以获取应用程序的名称、启动路径等信息，几个函数的名称和功能见表7-4（省略了函数参数中的const关键字）。

<center class="my_markdown"><b class="my_markdown">表7-4　QCoreApplication的有用函数</b></center>

| 函数原型 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| QString　applicationDirPath() | 返回应用程序启动路径 |
| QString　applicationFilePath() | 返回应用程序的带有目录的完整文件名 |
| QString　applicationName() | 返回应用程序名称，无路径无后缀 |
| QStringList　libraryPaths() | 返回动态加载库文件时，应用程序搜索的目录列表 |
| void　setOrganizationName(QString &orgName) | 为应用程序设置一个机构名 |
| QString　organizationName() | 返回应用程序的机构名 |
| void　exit() | 退出应用程序 |

