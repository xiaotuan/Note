1. 删除 untracked files

```shell
$ git clean -f
```

2. 连 untracked 的目录也一起删除

```shell
$ git clean -fd
```

3. 连 gitignore 的 untrack 文件/目录也一起删除（慎用，一般这个是用来删除编译出来的 .o 之类的文件用的）

```shell
git clean -nxfd
```

4. 在用上述 `git clean` 前，强烈建议加上 `-n` 参数来先看看会删除那些文件，防止重要文件被误删

```shell
$ git clean -nxfd
$ git clean -nf
$ git clean -nfd
```

