执行脚本时提示如下错误：

```shell
$ ./memory_check.sh
: No such file or directorydata
./memory_check.sh[56]: syntax error: unexpected 'done'
```

这是 Windows 和 Linux 的回车换行是不一样的字符导致的，可以在终端中执行下面命令解决该问题：

```shell
$ sed -i 's/\r$//' memory_check.sh
```

