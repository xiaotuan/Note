### Linux和FreeBSD

要在Linux或FreeBSD上安装Go，首先需要下载 `go<版本>.<操作系统>-<架构>.tar.gz` 文件。比如，当前64位架构的Linux安装包的名字就为 `go1.6.3.linux-amd64.tar.gz` 。

压缩包下载好了之后，将它解压到 `/usr/local` 目录中，并将目录 `/usr/local/go/bin` 添加到 `PATH` 环境变量当中。添加环境变量的工作可以通过将以下代码行添加到 `/etc/profile` 文件或 `$HOME/.profile` 文件中来完成：

```go
export PATH=$PATH:/usr/local/go/bin
```

