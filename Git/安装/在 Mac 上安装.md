**1. 以二进制发布包的方式安装**

访问 git-osx-installer 的官方网站：<http://code.google.com/p/git-osx-installer/>，下载 Git 安装包。下载完成后，直接双击安装包即可开始安装。

**2. 使用 Homebrew 安装 Git**

首先是安装 Homebrew，执行下面的命令：

```shell
$ ruby -e "$(curl -fsSL https://gist.github.com/raw/323731/install_homebrew.rb)"
```

执行下面的命令，通过 Homebrew 安装 Git：

```shell
$ brew install git
```

可以通过下面命令查看 Git 的安装路径及内容：

```shell
$ brew list git
/usr/local/Cellar/git/1.7.4.1/bin/gitk
...
```

**3. 从源码安装**

要从源码安装 Git ，首先需要安装 Xcode 软件。

直接通过源码安装 Git 可能需要执行下面命令以解决编译问题：

```shell
$ brew install asciidoc
$ brew install docbook2x
$ brew install xmlto
```

当编译源码及文档的工具部署完成后，就可以通过源码编译 Git：

```shell
$ make prefix=/usr/local all doc info
$ sudo make prefix=/usr/local install install-doc install-html install-info
```

