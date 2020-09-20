**在 Linux 上安装**

以 `Fedora` 为例，如果你在使用它（或与之紧密相关的基于 RPM 的发行版，如 `RHEL` 或 `CentOS`，你可以使用 `dnf`：

```shell
$ sudo dnf install git-all
```

如果你在基于 `Debian` 的发行版上，如 `Ubuntu`，请使用 `apt`：

```shell
$ sudo apt install git-all
```

**在 macOS 上安装**

在 `Terminal` 里尝试首次运行 `git` 命令即可：

```shell
$ git --version
```

如果你想安装最新的版本，可以使用二进制安装程序。官方维护的 macOS Git 安装程序可以在 `Git` 官方网站下载，网址为：<https://git-scm.com/download/mac>。

**在 Windows 上安装**

在 `Windows` 上安装 `Git` 也有几种安装方法。官方版本可以在 `Git` 官方网站下载。打开 <https://git-scm.com/download/win> ，下载会自动开始。更多信息请访问 <http://msysgit.github.io/>。

要进行自动安装，你可以使用 [Git Chocolatey 包](https://chocolatey.org/packages/git) 。

**从源代码安装**

如果你想从源代码安装 `Git`，需要安装 `Git` 依赖的库：autotools、curl、zlib、openssl、expat 和 libiconv。如果你的系统上有 `dnf` 或者 `apt`，可以使用对应的命令来安装依赖以便编译并安装 `Git` 的二进制版：

```shell
$ sudo dnf install dh-autoreconf curl-devel expat-devel gettext-devel \
openssl-devel perl-devel zlib-devel
$ sudo apt-get install dh-autoreconf libcurl4-gnutls-dev libexpat1-dev \
gettext libz-dev libssl-dev
```

为了添加文档的多种格式（doc、html、info），需要以下附加的依赖：

```shell
$ sudo dnf install asciidoc xmlto docbook2X
$ sudo apt-get install asciidoc xmlto docbook2x 
```

> 使用 `RHEL` 和 `RHEL` 衍生版，如 `CentOS` 和 `Scientific Linux` 的用户需要 [开启 EPEL 库](https://fedoraproject.org) 以便下载 `docbook2X` 包。

如果你使用基于 `Debian` 的发行版，你也需要 `install-info` 包：

```shell
$ sudo apt-get install install-info
```

如果你使用基于 RPM 的发行版（Fedora/RHEL/RHEL衍生版），你还需要 getopt 包：

```shell
$ sudo dnf install getopt
```

此外，如果你使用 Fedora/RHEL/RHEL 衍生版，那么你需要执行以下命令：

```shell
$ sudo ln -s /usr/bin/db2x_docbook2texi /usr/bin/docbook2x-texi
```

你可以从 kernel.org 网站获取，网址为：<https://www.kernel.org/pub/software/scm/git>，或从GitHub 网站上的镜像来获得，网址为 <https://github.com/git/git/release>。

接着，编译并安装：

```shell
$ tar -zxf git-2.8.0.tar.gz
$ cd git-2.8.0
$ make configure
$ ./configure --prefix=/usr
$ make all doc info
$ sudo make install install-doc install-html install-info
```

完成后，你可以使用 `Git` 来获取 `Git` 的更新：

```shell
$ git clone git://git.kernel.org/pub/scm/git/git.git
```

