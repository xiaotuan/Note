#### **背景信息**

在Linux及托管网站上默认的字符编码均是**“UTF-8”**，而Windows系统默认编码不是采用**“UTF-8”**。如果不设置Git字符编码为**“UTF-8”**，Git客户端在Windows下中文内容可能会出现乱码。设置字符编码后，可以解决中文显示的问题。

#### **操作步骤**

1. 设置Git编码为**“UTF-8”**。

```console
$ git config --global core.quotepath false          # 显示status编码 
$ git config --global gui.encoding utf-8            # 图形界面编码 
$ git config --global i18n.commit.encoding utf-8    # 提交信息编码 
$ git config --global i18n.logoutputencoding utf-8  # 输出log编码 
$ export LESSCHARSET=utf-8                          # 最后一条命令是因为git log默认使用less分页，所以需要bash对less命令进行utf-8
```

以上命令等效于：

+ 在“etc\gitconfig”中添加：

```console
[core]    
    quotepath = false 
[gui]    
    encoding = utf-8 
[i18n]    
    commitencoding = utf-8 
    logoutputencoding = utf-8
```

+ 在“etc\profile”中添加：

```console
export LESSCHARSET=utf-8
````

> 说明：
> + gui.encoding = utf-8
> 解决在$ git gui和gitk中的中文乱码。如果发现代码中的注释显示乱码，可以设置项目根目录中“git/config”文件添加：[gui] encoding = utf-8
> + i18n.commitencoding = utf-8
> 设置commit log提交时使用“utf-8”编码，可避免服务器上乱码，同时与Unix上的编码提交保持一致。
> + i18n.logoutputencoding = gbk
> 保证在$ git log时编码设置为“utf-8”。
> + export LESSCHARSET=utf-8
> 保证$ git log可以正常显示中文（配合i18n.logoutputencoding设置)。

2. 设置ls命令可以显示中文名称。

修改“etc\git-completion.bash”文件：alias ls="ls --show-control-chars --color"

