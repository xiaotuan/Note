exec 的典型用法是将当前 shell 替换为一个不同的程序。例如：

```shell
exec wall "Thanks for all the fish"
```

脚本中的这个命令会用 wall 命令替换当前的 shell。脚本程序中 exec  命令后面的代码都不会执行，因为执行这个脚本的 shell 已经不存在了。