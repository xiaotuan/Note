`TRIM(s1 FROM s)` 删除字符串 `s` 中两端所有的子字符串 `s1`。`s1` 为可选项，在未指定情况下，删除空格。

```sql
mysql> SELECT TRIM('xy' FROM 'xyxboxyokxxyxy');
+----------------------------------+
| TRIM('xy' FROM 'xyxboxyokxxyxy') |
+----------------------------------+
| xboxyokx                         |
+----------------------------------+
1 row in set (0.00 sec)
```

