### 12.2.5　使用MSVC编译器输出中文的问题

在Qt Creator中使用MSVC编译器编译项目时，若处理不当容易出现中文字符串乱码问题。例如BatteryUser项目中，如果槽函数on_battery_powerLevelChanged()的代码改写为如下的形式，程序运行时，LabInfo显示的汉字就会出现乱码。

```css
void MainWindow::on_battery_powerLevelChanged(int arg1)
{ //电量值改变时，在标签中显示
   QString  str="当前电量："+QString::asprintf("%d %%",arg1);
   ui->LabInfo->setText(str);
}
```

这是因为Qt Creator保存的文件使用的是UTF-8编码（是任何平台、任何语言都可以使用的跨平台的字符集），MSVC编译器虽然可以正常编译带BOM的UTF-8编码的源文件，但是生成的可执行文件的编码是Windows本地字符集，比如GB2312。也就是在可执行文件中，字符串“当前电量：”是以GB2312编码的，而可执行程序执行到这条语句时，对这个字符串却是以UTF-8解码的，这样就会出现乱码。

解决这个问题有两种方法，一种方法是使用QStringLiteral()宏封装字符串，另一种方法是强制MSVC编译器生成的可执行文件使用UTF-8编码。

QStringLiteral(str)宏在编译时将一个字符串str生成字符串数据，并且存储在编译后文件的只读数据段中，程序运行时使用到此字符串时，只需读出此字符串数据即可。所以，BatteryUser项目中槽函数on_battery_powerLevelChanged()中使用的一行代码如下：

```css
QString  str=QStringLiteral("当前电量：")+QString::asprintf("%d %%",arg1);
```

程序中需要使用QStringLiteral()宏对每个中文字符串进行封装，并且不能再使用tr()函数用于翻译字符串。

强制MSVC编译器采用UTF-8编码生成可执行文件，需要在每个使用到中文字符串的头文件和源程序文件的前部加入如下的语句：

```css
#if _MSC_VER >= 1600    //MSVC2015>1899,   MSVC_VER=14.0
#pragma execution_character_set("utf-8")
#endif
```

MSVC2010以后的编译器可以使用此方案，这是强制编译后的执行文件采用UTF-8编码。这样，即使不再使用QStringLiteral()宏，程序运行时也不会再出现汉字乱码的问题了。而且，也可以采用tr()函数用于翻译字符串。

