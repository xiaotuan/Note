> 该操作只针对未上传远程服务器的 git commit 撤销操作。

```shell
$ git reset --soft HEAD^
```

**关于 HEAD 的理解**

`HEAD^` 的意思是上一个版本，也可以写成 `HEAD~1`。如果你金项链2次 `commit`，想都撤回，可以使用 `HEAD~2`。

**可用参数**

+ --mixed：不删除工作空间改动代码，撤销 `commit`，并且撤销 `git add . ` 操作这个为默认参数，`git reset --mixed HEAD^` 和 `git reset HEAD^` 效果是一样的；
+ --soft：不删除工作空间改动代码，撤销 `commit`，不撤销 `git add .`；
+ --hard：删除工作空间改动代码，撤销 `commit`，撤销 `git add . `，注意完成这个操作后，就恢复到了上一次的 commit 状态。

> 如果 `commit` 注释写错了，只是想修改一下注释，只需要执行下面命令即可：
>
> ```shell
> $ git commit --amend
> ```
>
> 此时会进入默认 `vim` 编辑器，修改注释完毕后保存就好了。