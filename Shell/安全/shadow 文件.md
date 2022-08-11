`/etc/shadow` 文件为系统上的每个用户账户都保持了一条记录：

```
xiaotuan:$6$9mL9v3RarGDGYbJ0$PsAJVmRtCJ5jdVAhStikZ0ykhhZX4YNb6tpFwBl0Yi99kdT7pzPhjIf6E8E3KOxfp3csVf0GHs611WbutM6LY1:19045:0:99999:7:::
```

在 `/etc/shadow` 文件的每条记录中都有 9 个字段：

+ 与 `/etc/passwd` 文件中的登录名字段对应的登录名
+ 加密后的密码
+ 自上次修改密码后过去的天数密码（自 1970 年 1 月 1 日开始计算）
+ 多少天后才更改密码
+ 多少天后必须更改密码
+ 密码过期前提前多少天提醒用户更改密码
+ 密码过期后多少天禁用用户账户
+ 用户账户被禁用的日期（用自 1970 年 1 月 1 日到当天的天数表示）
+ 预留字段给将来使用