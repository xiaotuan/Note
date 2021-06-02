如果不小心误提交了一笔无用代码到远程仓库，可以使用下面方法将其从本地和远程仓库中删除：

```shell
$ git rm --cached winxp.img
$ git commit --amend
```

如果是历史版本，例如是在 \<commit-id> 所标识的提交中引入的文件，则需要使用变基操作。

```shell
$
```

