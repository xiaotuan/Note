### 2.4 MongoDB shell脚本编程

正如您看到的，MongoDB shell命令、方法和数据结构都是基于交互式JavaScript的。为管理MongoDB，一种很不错的方法是创建脚本，这些脚本可运行多次，也可在指定的时间（如升级时）运行。

在脚本文件中，可包含任意数量使用JavaScript（如条件语句和循环）的MongoDB命令。MongoDB shell脚本编程主要是通过三种方式实现的。

+ 在命令行使用参数--eval <expression>，其中expression是要执行的JavaScript表达式。
+ 在MongoDB shell启动后，调用方法load(script_path)，其中script_path是要执行的JavaScript文件的路径。
+ 在命令行指定要执行的JavaScript文件。

接下来的几小节详细介绍这些方式。

