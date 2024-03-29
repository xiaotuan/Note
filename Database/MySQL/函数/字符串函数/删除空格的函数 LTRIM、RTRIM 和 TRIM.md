`LTRIM(s)` 返回字符串 `s`，字符串左侧空格字符被删除。

```sql
mysql> SELECT '(  book  )', CONCAT('(', LTRIM('  book  '), ')');
+------------+-------------------------------------+
| (  book  ) | CONCAT('(', LTRIM('  book  '), ')') |
+------------+-------------------------------------+
| (  book  ) | (book  )                            |
+------------+-------------------------------------+
1 row in set (0.00 sec)
```

`LTRIM` 只删除字符串左边的空格，而右边的空格不会被删除：

```sql
mysql> SELECT '(  book  )', CONCAT('(', RTRIM('  book  '), ')');
+------------+-------------------------------------+
| (  book  ) | CONCAT('(', RTRIM('  book  '), ')') |
+------------+-------------------------------------+
| (  book  ) | (  book)                            |
+------------+-------------------------------------+
1 row in set (0.00 sec)
```

`TRIM(s)` 删除字符串 `s` 两侧的空格：

```sql
mysql> SELECT '(  book  )', CONCAT('(', TRIM('  book  '), ')');
+------------+------------------------------------+
| (  book  ) | CONCAT('(', TRIM('  book  '), ')') |
+------------+------------------------------------+
| (  book  ) | (book)                             |
+------------+------------------------------------+
1 row in set (0.00 sec)
```

