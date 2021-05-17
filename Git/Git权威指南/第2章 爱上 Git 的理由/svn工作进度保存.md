如果在工作区的修改尚未完成时忽然有一个紧急的任务，需要从一个干净的工作区开始新的工作，或要切换到别的分支进行工作，那么如何保存当前尚未完成的工作进度呢？

可以执行下面的操作：

```shell
$ svn diff > /path/to/saved/patch.file
$ svn revert -R
$ svn switch <new_branch>
```

在新的分支中工作完毕后，再切换回当前分支，将补丁文件重新应用到工作分区。

```shell
$ svn switch <original_branch>
$ patch -p1 < /path/to/saved/patch.file
```

> 警告：SVN 的补丁文件不支持二进制文件。