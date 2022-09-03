[toc]

### 1. 使用 yum 命令列出已安装软件包

要找出系统上已安装的包，可在 shell 提示符下输入如下命令：

```shell
yum list installed
```

`yum` 擅长找出某个特定软件包的详细信息。它能给出关于包的非常详尽的描述，另外你还可以通过一条简单的命令查看包是否已安装。

```
# yum list xterm
Loaded plugins: langpacks, presto, refresh- packagekit
Adding en_ US to language list
Available Packages
xterm. i686 253- 1. el6
#
# yum list installed xterm
Loaded plugins: refresh- packagekit
Error: No matching Packages to list
#
```

### 2. 使用 zypper 和 urpm 列出已安装软件包

<center><b>使用 zypper 和 urpm 列出已安装软件</b></center>

| 版本     | 前端工具 | 命令                                  |
| -------- | -------- | ------------------------------------- |
| Mandriva | urpm     | rpm -qa > installed_software          |
| openSUSE | zypper   | zypper search -I > installed_software |

<center><b>用 zypper 和 urpm 查看各种包详细信息</b></center>

| 信息类型 | 前端工具 | 命令                               |
| -------- | -------- | ---------------------------------- |
| 包信息   | urpm     | urpmq -i package_name              |
| 是否安装 | urpm     | rpm -q package_name                |
| 包信息   | zypper   | zypper search -s package_name      |
| 是否安装 | zypper   | 同样的命令，注意在 Status 列查找 i |

