要查看你使用的 MySQL 版本所支持的编码，可以运行下面的命令:

```sql
SHOW CHARACTER SET;
```

要查看 MySQL 可用的校对规则，运行一下查询，使用上次查询结果中适当的值来代替 charset。

```sql
SHOW COLLATION LIKE 'charset%';
```

校对规则名字的后缀 ci 表示不区分大小写，cs 后缀表示区分大小写，bin 后缀表示二元校对规则。

重要的是，数据库使用的字符集必须和你的 PHP 脚本一致。如果你的 PHP 脚本没有使用 UTF-8 编码，那就在数据库中使用与你的 PHP 脚本相匹配的编码。如果默认的校对规则不符合语言使用的大部分惯例，那就应该相应调整校对规则。

在 MySQL 中，服务器是一个整体，每个数据库、每个表，甚至每个字符串列都可以有一个定义的字符集合校对规则。要在创建数据库时设置这些值，使用以下命令：

```sql
CREATE DATABASE name CHARACTER SET charset COLLATE collation;
```

要在创建表时设置这些值，使用以下命令：

```sql
CREATE TABLE name {
column definitions
} CHARACTER SET charset COLLATE collation;
```

要为列创建字符集合校对规则，可以使用以下命令：

```sql
CREATE TABLE name {
something TEXT CHARACTER SET charset COLLATE collation
...)
};
```

在 MySQL 客户端，使用下面的代码设置编码：

```
$ mysql> CHARSET charset;
```

**提示**

+ MySQL 的校对规则同样可以在查询中指定以影响查询结果：

```sql
SELECT ... ORDER BY column COLLATE collation;
SELECT ... WHERE column LIKE 'value' COLLATE collation;
```

+ CONVERT() 函数可以转换文本的字符集。
+ 你可以使用 ALTER 命令改变数据库或表的默认字符集或校对规则。
+ 因为使用不同的字符集需要占用更多的空间表示字符串，所以可能需要为 UTF-8 字符增加列的大小。在修改列编码之前编辑列的大小以防止数据丢失。