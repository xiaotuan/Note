当采用命令行方式启动一个程序时，可以利用 Shell 的重定向语法将任意文件关联到 `System.in` 和 `System.out` 中：

```shell
$ java MyProg < myfile.txt > output.txt
```

