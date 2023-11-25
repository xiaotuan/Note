为了在 `git commit` 期间让 `Git` 打开你最爱的编辑器，要设置你的 `GIT_EDITOR` 环境变量：

```shell
# 在 tcsh 中
$ setenv GIT_EDITOR emacs

# 在 bash 中
$ export GIT_EDITOR=vim
```

编辑器的选择按照以下步骤的顺序确定：

+ `GIT_EDITOR` 环境变量；
+ `core.editor` 配置选项；
+ `VISUAL` 环境变量；
+ `EDITOR` 环境变量；
+ `vi` 命令。
