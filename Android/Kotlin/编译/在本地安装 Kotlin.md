<https://kotlinlang.org/docs/command-line.html#install-the-compiler> 上的页面讨论了安装命令行编译器的选项。其中一项是下载一个适用于你的操作系统的包含安装器的 `ZIP` 文件。该页面包含指向 `Kotlin` 当前版本的 `Github` 库（<https://github.com/JetBrains/kotlin/releases/tag/v1.9.0>）的链接。`ZIP` 文件可以用于 `Linux`、`macOS`、`Windows`，以及源代码发行版。只需解压缩发行版并将其 `bin` 子目录添加到你的路径即可。

包管理器可以自动执行安装程序，其中一些包管理器还允许你维护指定编译器的多个版本。

**SDKMAN!、Scoop，以及其他包管理器**

`SDKMAN!`（<https://sdkman.io>）是最受欢迎的安装器之一。从使用 `curl` 安装 `SDKMAN!` 开始安装 `Kotlin`：

```shell
> curl -s https://get.sdkman.io | bash
```

安装完成后，你可以使用 `sdk` 命令来安装包含 `Kotlin` 在内的任何产品：

```shell
> sdk install kotlin
```

最新的版本将会被默认安装到 `~/.sdkman/candidates/kotlin` 目录，以及一个指向所选版本的名为 `current` 的链接。

你可以使用 `list` 命令找出可用的版本：

```shell
> sdk list kotlin
```

`install` 命令会默认选择最新版本，但是 `use` 命令则可以让你在必要时选择任何版本进行安装：

```shell
> sdk use kotlin 1.3.50
```

其他支持 `kotlin` 的包管理器包括 `Homebrew`（<http://brew.sh>）、`MacPorts`（<https://www.macports.org>）以及 `Snapcraft`（<https://snapcraft.io>）。

在 `Windows` 上，你可以使用 `Scoop`（<https://scoop.sh>）。`Scoop` 需要 `PowerShell 5`（或更新版本）与 `.NET Framework 4.5`（或更新版本）。简单的安装说明可以在 `Scoop` 网站上找到。

打开一个 `PowerShell` 终端（5.1 版本及以上），并运行下面命令：

```shell
> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser # Optional: Needed to run a remote script the first time
> irm get.scoop.sh | iex
```

`Scoop` 安装成功之后，主 `bucket` 会允许你安装当前版本的 `Kotlin`：

```shell
> scoop install kotlin
```

无论你如何安装 `Kotlin`，都可以使用简单的命令 `kotlin-version` 来验证它是否正确工作以及是否在你的路径中：

```shell
> kotlin -version
Kotlin version 1.9.0-release-358 (JRE 1.8.0_321-b07)
```



