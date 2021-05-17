（1） 创建现场版本。

```shell
$ git init
```

（2）添加文件并提交。

```shell
$ git add -A
$ git commit -m "initialized"
```

（3）添加里程碑："v1"。

```shell
$ git tag v1
```

（4）提交代码。

```shell
git commit -a
```

（5）提取补丁。

```shell
$ git format-patc
```

（6）通过邮件将补丁文件发出。

```shell
$ git send-email *.patch
```

