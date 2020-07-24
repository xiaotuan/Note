UTC_DATE() 函数会返回 UTC 日期、UTC_TIME() 函数会返回当前的 UTC 时间、UTC_TIMESTAMP() 函数会返回当前的日期和时间。

要将一个日期或时间从一个时区调整到另外一个，使用 CONVERT_TZ() 函数。

```sql
CONVERT_TZ(dt, from, to)
```

> 如果引用了无效的时区或 MySQL上没有安装时区，CONVERT_TZ() 函数会返回 NULL。

