`killall` 命令支持通过进程名而不是 PID 来结束进程。`killall` 命令也支持通配符，这在系统因负载过大而变得很慢时很有用。例如：

```shell
$ killall http*
```

上例中的命令结束了所有以 `http` 开头的进程，比如 Apache Web 服务器的 httpd 服务。

> 警告：以 `root` 用户身份登录系统时，使用 `killall` 命令要特别小心，因为很容易就会误用通配符而结束了重要的系统进程。