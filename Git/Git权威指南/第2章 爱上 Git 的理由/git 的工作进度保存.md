`Git` 提供了一个可以保存和恢复工作进度的命令 `git stash`。在切换到新的工作分支之前执行 `git stash` 保存工作进度，工作区就变得非常干净，然后就可以切换到新的分支中了。

```shell
$ git stash
$ git checkout <new_branch>
```

新的工作分支修改完毕后，再切换回当前分支，调用 `git stash pop` 命令即可恢复之前保存的工作进度。

```shell
$ git checkout <original_branch>
$ git stash pop
```

