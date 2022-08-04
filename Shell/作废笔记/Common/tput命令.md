### 什么是 `tput` ？

`tput` 命令将通过 `terminfo` 数据库对您的终端会话进行初始化和操作。通过使用 `tput`，您可以更改几项终端功能，如移动或更改光标、更改文本属性，以及清除终端屏幕的特定区域。



### 什么是 `terminfo` 数据库？

`UNIX` 系统上的 `terminfo` 数据库用于定义终端和打印机的属性及功能，包括各设备（例如，终端和打印机）的行数和列数以及要发送至该设备的文本的属性。`UNIX` 中的几个常用程序都依赖 `terminfo` 数据库提供这些属性以及许多其他内容，其中包括 `vi` 和 `emacs` 编辑器以及 `curses` 和 `man` 程序。



### 命令使用说明：

1. 文本属性

设置文本颜色

+ tput setab [0-7]：设置背景颜色，可使用 ANSI 转义符
+ tput setb [0-7]：设置背景颜色
+ tput setaf [0-7]：设置前景色，可使用 ANSI 转义符
+ tput setf [0-7]：设置前景色

其中颜色值为：

+ 0 ：黑色
+ 1 ：红色
+ 2 ：绿色
+ 3 ：黄色
+ 4 ：蓝色
+ 5 ：品红
+ 6 ：青色
+ 7 ：白色

设置文本样式：

+ tput bold：粗体
+ tput dim：半亮
+ tput smul：进入下划线模式
+ tput rmul：退出下划线模式
+ tput rev：反转模式
+ tput smso： Enter standout mode (bold on rxvt)
+ tput rmso：Exit standout mode
+ tput sgr0：Turn off all attributes



2. 光标属性

+ tput clear：清屏
+ tput sc：保存当前光标位置
+ tput cup 10 13：将光标移动到 row col
+ tput civis：光标不可见
+ tput cnorm：光标可见
+ tput rc：显示输出

