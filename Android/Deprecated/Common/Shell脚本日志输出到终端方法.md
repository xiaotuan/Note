可以将日志写入 `/dev/console` 文件中：

```shell
#CONSOLEDEV=/dev/console
echo "please chmod u+r /system/etc/ppp" > $CONSOLEDEV
```

