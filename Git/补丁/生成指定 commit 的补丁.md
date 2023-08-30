生成某次提交（含）之前的几次提交的 `patch`：

```shell
git format-patch [commit sha1 id] -n
```

> 提示：`n` 指从 `sha1 id` 对应的 `commit` 开始算起 `n` 个提交。

例如：

```shell
$ git format-patch 0b2c00dcff8d62d08056065f1bef70e4bdf5ff06 -2
```

生成某个提交的 `patch`：

```shell
git format-patch [commit sha1 id] -1
```

例如：

```shell
$ git format-patch 0b2c00dcff8d62d08056065f1bef70e4bdf5ff06 -1
```

生成某两次提交之间的所有 `patch`：

```shell
git format-patch [commit sha1 id]..[commit sha1 id]
```

例如：

```shell
git format-patch  2a2fb4539925bfa4a141fe492d9828d030f7c8a8..89aebfcc73bdac8054be1a242598610d8ed5f3c8
```

