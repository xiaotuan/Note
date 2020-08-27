[toc]

### 1. 创建初始版本库

如果你在 `~/public_html` 的个人网站还没有任何内容，那就新建一个目录，并将一些简单的内容放到 `index.html` 里。

```shell
$ mkdir ~/public_html
$ cd ~/public_html
$ echo 'My website is alive!' > index.html
```

执行 `git init`，将 `~/public_html` 或者任何目录转化为 `Git` 版本库。

```shell
$ git init
```

### 2. 将文件添加到版本库中

