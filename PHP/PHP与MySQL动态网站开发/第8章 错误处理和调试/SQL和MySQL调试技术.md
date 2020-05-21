**调试脚本**

大多数常见的 SQL 错误是由以下问题引起的：

+ 引号或圆括号的使用不对称；
+ 列值中有未转义的撇号；
+ 列名、表名或函数拼写错误；
+ 在联结中有歧义地引用某一列；
+ 以错误的顺序放置查询子句（WHERE、GROUP BY、ORDER BY、LIMIT）。

**调试SQL问题**

1. 在 PHP 脚本中打印出任何使用的查询。
2. 在 MySQL 客户端或其他工具中运行查询。
3. 以其最基本的形式重写查询，然后向其中添加回各个元素，直到你发现那个子句正在引发问题。

**调试访问问题**

+ 在改变特权之后重新加载 MySQL，使得所做的更改生效。
+ 复查所用的密码。Access denied for user: 'user@localhost' (Using password: YES)
+ Can't connect to ... （错误编号2002）这条出错消息指示 MySQL 要么运行，要么未运行在客户试验的 socket 或 TCP/IP 端口上。


MySQL 保存它自己的错误日志，这在解决 MySQL 问题时非常有用。MySQL 的错误日志将位于数据目录中，其名称为 hostname.err。