`Git` 自带一个 `git config` 的工具来帮助设置控制 `Git` 外观和行为的配置变量。这些变量存储在三个不同的位置：

+ `/etc/gitconfig` 文件：包含系统上每一个用户及他们仓库的通用配置。如果在执行 `git config` 时带上 `--system` 选项，那么它就会读写该文件中的配置变量。
+ `~/.gitconfig` 或 `~/.config/git/config` 文件：只针对当前用户。你可以传递 `--global` 选项让 `Git` 读写此文件，这会对你系统上所有的仓库生效。
+ 当前使用仓库的 `Git` 目录中的 `config` 文件（即 `.git/config`）：针对该仓库。你可以传递 `--local` 选项让 `Git` 强制读写此文件，虽然默认情况下用的就是它。

每一个级别会覆盖上一级别的配置，所以，`.git/config` 的配置变量会覆盖 `/etc/gitconfig` 中配置变量。

在 `Windows` 系统中，`Git` 会查找 `$HOME` 目录下的 `.gitconfig`  文件。`Git` 同样也会寻找 `/etc/gitconfig` 文件，但只限于 MSys 的根目录下，即安装 `Git` 时所选的目标位置。

你可以通过以下命令查看所有配置以及它们所在的文件：

```shell
$ git config --list --show-origin
```

**用户信息**

安装完 `Git` 之后，要做的第一件事就是设置你的用户名和邮件地址。

```shell
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```

**文本编辑器**

如果你想使用不同的文本编辑器，例如 Emacs，可以这样做：

```shell
$ git config --global core.editor emacs
```

在 `Windows` 系统上，如果你想要使用别的文本编辑器，那么必须指定可执行文件的完整路径。例如设置 Notepad++，可以这样做：

```shell
$ git config --global core.editor "'C:/Program Files/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"
```

**检查配置信息**

可以使用 如下命令来列出所有 `Git` 当时能找到的配置。

```shell
$ git config --list
```

你也可以通过如下命令来检查 `Git` 的某一项配置：

```shell
$ git config user.name
John Doe
```

> 由于 `Git` 会从多个文件中读取同一配置变量的不同值，因此你可能会在其中看到意料之外的值而不知道为什么。此时，你可以查询 `Git` 中该变量的原始值，它会告诉你哪一个配置文件最后设置了该值：
>
> ```shell
> $ git config --show-origin rerere.autoUpdate
> file:/home/johndoe/.gitconfig false
> ```

