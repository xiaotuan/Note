PATH 环境变量定义了用于进行命令和程序查找的目录。

PATH 中各个目录之间是用冒号分隔的。你只需引用原来的 PATH 值，然后再给这个字符串添加新目录就行了。例如：

```shell
$ echo $PATH
home/xiaotuan/jdk-11.0.14/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
$ PATH=$PATH:/home/christine/Scripts
$ echo $PATH
home/xiaotuan/jdk-11.0.14/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/christine/Scripts
```

对 PATH 变量的修改只能持续到退出或重启系统。