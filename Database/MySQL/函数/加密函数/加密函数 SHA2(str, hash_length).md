`SHA2(str, hash_length)` 使用 `hash_length` 作为长度，加密 `str`。`hash_length` 支持的值为 224, 256, 384, 512 和 0。其中， 0 等同于 256。

```sql
mysql> SELECT SHA2('tom123456', 0) A, SHA2('tom123456', 256) B\G
*************************** 1. row ***************************
A: 9242a986a9edbd14a60450e9284a372efeff7e9f6209f675fdc4457f55de5e27
B: 9242a986a9edbd14a60450e9284a372efeff7e9f6209f675fdc4457f55de5e27
1 row in set (0.00 sec)
```

