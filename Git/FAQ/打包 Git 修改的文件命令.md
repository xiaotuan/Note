可以通过如下命令打包 Git 修改的文件：

```shell
$ git diff --cached --name-only | xargs zip update.zip
```

如果需要在打包前过滤指定文件可以使用如下命令：

```shell
$ git diff --cached --name-only | grep webapp | xargs zip update.zip
```

