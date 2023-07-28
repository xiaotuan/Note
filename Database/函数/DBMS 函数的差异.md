<center><b>DBMS 函数的差异</b></center>

| 函数                 | 语法                                                         |
| -------------------- | ------------------------------------------------------------ |
| 提取字符串的组成部分 | `DB2`、`Oracle`、`PostgreSQL` 和 `SQLite` 使用 `SUBSTR()`；`MariaDB`、`MySQL` 和 `SQL Server` 使用 `SUBSTRING()` |
| 数据类型转换         | `Oracle` 使用多个函数，每种类型的转换有一个函数；`DB2` 和 `PostgreSQL` 使用 `CAST()`；`MariaDB`、`MySQL` 和 `SQL Server` 使用 `CONVERT()` |
| 取当前日期           | `DB2` 和 `PostgreSQL` 使用 `CURRENT_DATE`；`MariaDB` 和 `MySQL` 使用 `CURDATE()`；`Oracle` 使用 `SYSDATE`；`SQL Server` 使用 `GETDATE()`；`SQLite` 使用 `DATE()` |

