LIKE 和 NOT LIKE 用于检测相似性，它们通常与两个通配符一起使用。下划线（\_）通配符用于匹配单个字符；百分号（%）通配符用于匹配 0 个或多个字符。

```sql
SELECT * FROM users
WHERE last_name LIKE 'Smith%';
```

如果想排除字符串中存在某些值，那么可以结合使用 NOT LIKE 和通配符。

**提示**

+ 带有 LIKE 条件语句的查询一般比较慢，因为它们不能利用索引，所以仅当绝对需要时才应该使用这种格式。

+ 在查询中，可以在字符串的前面和/或后面使用通配符。

```sql
SELECT * FROM users
WHERE last_name LIKE '_smith%';
```

+ 尽管 LIKE 和 NOT LIKE 通常用于字符串，但是它们也可以用于数字列。
+ 为了在 LIKE 或 NOT LIKE 查询中使用原意的下划线或百分号，需要对它们进行转义。
+ 下划线可以预期自身组合使用。例如，`Like '__'`将找出两个字母的任意组合。