首先，FULLTEXT 搜索需要 FULLTEXT 索引。这种类型的索引，只能在 MyISAM 表中创建.

查看数据库中表的信息：

```sql
SHOW TABLE STATUS\G
```

> 命令以 \G 结尾而不是分号，是告诉 MySQL 客户端以垂直的列表返回结果而不是一个表格。

更改数据库存储引擎：

```sql
ALTER TABLE messages ENGINE = MyISAM;
```

添加 FULLTEXT 索引：

```sql
ALTER TABLE messages ADD FULLTEXT (body, subject);
```

**提示**

+ 在表中插入 FULLTEXT 索引可能会非常慢，因为这需要的索引非常复杂。
+ FULLTEXT 搜索可以成功地用于简单的搜索引擎。但是 FULLTEXT 索引一次只能用于一个表，所以内容跨多个表存储的复杂网站一般使用更加正式的搜索引擎。

一旦在列上建立了一个 FULLTEXT 索引，就可以在 WHERE 条件语句中使用 MATCH ... AGAINST 表达式开始针对它的查询。

```sql
SELECT * FROM tablename WHERE MATCH (columns) AGAINST (terms);
```

执行该操作时，会应用以下一些规则：

+ 把字符串分解为它们独立的关键字；
+ 长度不足4个字符的关键字将被忽略；
+ 将会忽略称为停止词（stopword）的非常普遍的单词；
+ 如果 50% 以上的记录与关键字匹配，则不会返回记录。

```sql
SELECT subject, body FROM messages
WHERE MATCH (body, subject)
AGAINST('database');
```

只要 messages 表中至少有一条记录在其正文或主题中具有单词 database，并且这样的记录数在 50% 以下，它就会返回一些结果。注意：MATCH 中引用的列必须与对齐建立 FULLTEXT 索引的那些列相同。在这个示例中，可以使用 body, subject 或 subject, body， 但是不能只使用 body 或者只使用 subject。

**提示**

+ 记住，如果 FULLTEXT 查找没有返回任何记录，那么这意味着没有产生匹配，或者匹配了超过一半的记录。
+ 最短的关键字长度（默认为4个字符）是一种配置设置，在 MySQL中可以更改它。
+ FULLTEXT 查找默认情况下不区分大小写。

** 执行布尔型FULLTEXT查找**

可以使用其布尔模式可以完成更复杂的 FULLTEXT 查找。为了执行该操作，可以在 AGAINST 子句中添加短语 IN BOOLEAN MODE：

```sql
SELECT * FROM _tablename_ WHERE 
MATCH (columns) AGAINST('terms' IN BOOLEAN MODE);
```

** 表7-3 布尔模式运算符**

| 运算符 | 含义 |
| :- | :- |
| + | 必须存在于每个匹配中 |
| - | 绝对不会存在于任何匹配中 |
| ~ | 如果存在，则降低一个等级 |
| * | 通配符,可以匹配一个单词的变体 |
| < | 降低单词的重要性 |
| > | 提高单词的重要性 |
| " " | 必须匹配精确的短语 |
| () | 创建子表达式 |

```sql
SELECT * FROM tablename WHERE
MATCH (columns) AGAINST('+database -mysql' IN BOOLEAN MODE);
```

```sql
SELECT * FROM tablename WHERE MATCH (columns) AGAINST ('>"Web develop" + html ~JavaScript' IN BOOLEAN MODE)
```

使用布尔模式时，就 FULLTEXT 查找的工作方式来说，有几个不同之处：

+ 如果关键字前面没有任何运算符，则这个单词是可选的；但是，如果它存在，匹配的等级会更高；
+ 即使 50% 以上的记录与查找匹配，也会返回结果。
+ 不会自动按相关性对结果进行排序。

**提示**

+ MySQL 5.1.7 添加了另一种 FULLTEXT 查找模式：自然语言。如果没有指定其他模式，这就是默认的模式。
+ WITH QUERY EXPANSION 将增加返回结果的数量。这种查询执行两次查找并返回一个结果集。它依据在初次查找的最相关的结果中发现的项目进行第二次查找。虽然 WITH QUERY EXPAANSION 查找可以发现未返回的几个，但它也可以返回与原始查找项目完全不相关的结果。


