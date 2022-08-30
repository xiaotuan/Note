[toc]

### 1. 搜索软件包

首先，使用 `aptitude` 命令加 `search` 选项确定准备安装的软件包名称。

```shell
aptitude search package_name
```

`search` 选项的妙处在于你无需在 package_name 周围加通配符。通配符会隐式添加。下面是用 `aptitude` 来查找 wine 软件包的例子：

```shell
$ aptitude search wine
p   gnome-wine-icon-theme           - red variation of the GNOME-Colors icon the
p   libkwineffects7                 - KDE window manager effects library        
p   libkwineffects7:i386            - KDE window manager effects library        
p   libwine-development             - Windows API implementation - library      
p   libwine-development:i386        - Windows API implementation - library      
p   libwine-development-dev         - Windows API implementation - development f
p   libwine-development-dev:i386    - Windows API implementation - development f
p   q4wine                          - Qt GUI for wine (WINE)                    
p   q4wine:i386
[...]
```

> 注意：在每个包名字之前都有一个 p 或 i。如果看到一个 i，说明这个包现在已经安装到了你的系统上了。如果看到一个 p 或 v， 说明这个包可用，但还没安装。你可能还会看到一个 i 或 u，这是因为 `aptitude` 自动解析了必要的包依赖关系，并安装了需要的额外的库和软件包。

### 2. 安装软件包

使用 `aptitude` 安装软件包命令如下：

```shell
aptitude install package_name
```

例如：

```shell
$ sudo aptitude install wine
[sudo] xiatuan 的密码： 
下列“新”软件包将被安装。         
  binfmt-support{a} cabextract{a} fonts-horai-umefont{a} 
  fonts-unfonts-core{a} fonts-wqy-microhei{a} gcc-5-base:i386{a} 
  gcc-6-base:i386{a} gnome-exe-thumbnailer{a} icoutils{a} 
[...]
```

