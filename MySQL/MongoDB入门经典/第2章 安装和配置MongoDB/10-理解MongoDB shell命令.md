### 2.3.2 理解MongoDB shell命令

MongoDB shell提供了多个命令，您可在shell提示符下执行它们。您需要熟悉这些命令，因为您将经常使用它们。表2.3列出了多个MongoDB shell命令及其用途。

<center class="my_markdown"><b class="my_markdown">表2.3 MongoDB shell命令</b></center>

| 命令 | 描述 |
| :-----  | :-----  | :-----  | :-----  |
| help <option> | 显示MongoDB shell命令的语法帮助。参数option让您能够指定需要哪方面的帮助，如db、collection或cursor |
| use <database> | 修改当前数据库句柄。数据库操作是在当前数据库句柄上进行的 |
| show <option> | 根据参数option显示一个列表。参数option的可能取值如下。 dbs：显示数据库列表 collections：显示当前数据库中的集合列表 users：显示当前数据库中的用户列表 profile：显示system.profile中时间超过1毫秒的条目 |
| log [name] | 显示内存中日志的最后一部分。如果没有指定日志名，则默认为global |
| exit | 退出MongoDB shell |

