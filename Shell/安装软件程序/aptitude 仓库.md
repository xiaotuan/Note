`aptitude` 默认的软件仓库位置是在安装 Linux 发行版时设置的。具体位置存储在文件 `/etc/apt/sources.list` 中。

可以使用下面的结构来指定仓库源：

```
deb (or deb-src) address distribution_name package_type_list
```

deb 或 deb-src 的值表明了软件包的类型。deb 值说明这是一个已编译程序源，而 deb-src 值则 deb-src 值则说明这是一个源代码的源。

address 条目是软件仓库的 Web 地址。distribution_name 条目是这个特定软件仓库的发行版版本的名称。

最后，package_type_list 条目可能并不止一个词，它还表明仓库里面有什么类型的包。你可以看到诸如 main、restricted、universe 和 patner 这样的值。