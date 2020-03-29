# CoreData调试

**XCode调试命令**

如果希望看到`CoreData`执行`SQL`语句的调试信息需要在项目中将`CoreData`调试打开，可以通过以下方式打开：

1. 打开`Product`，选择`Edit Scheme`。
2. 选择`Arguments`，在下面的`Arguments Passed On Launch`中添加下面两个选项。
	（1） `-com.apple.CoreData.SQLDebug`。
	（2）`1`。

**终端调试命令**

如果是在模拟器上调试程序，可以通过`sqlite3/数据库路径/`命令来查看和操作数据库。
`.tables`查看当前数据库文件中所有的表名
`select * frome tableName`执行查询的`SQL`语句

