[toc]

### 1. Homebrew

[Homebrew 官网](https://link.jianshu.com/?t=https%3A%2F%2Fbrew.sh%2F) 提供了安装命令：

```shell
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### 2. Homebrew-cask

`Homebrew-cask` 相当于 `Homebrew` 的扩展，区别在于，`brew` 命令首先获取程序源代码然后编译安装（包括依赖库），并自动做好必要的配置（如环境变量等）；而 `brew cask` 命令是下载已编译好的应用包并放在统一的目录中。安装好 `Homebrew` 后，可使用 `brew tap caskroom/cask` 命令直接安装 `Homebrew-cask`。