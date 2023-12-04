`find` 命令用于在目录结构中查找文件，其命令格式如下：

```shell
find [路径] [参数] [关键字]
```

路径是要查找的目录路径，如果不写的话表示在当前目录下查找，关键字是文件名的一部分，主要参数如下：

+ `-name <filename>`：按照文件名称查找，查找与 filename 匹配的文件，可使用通配符。
+ `-depth`：从指定目录下的最深层的子目录开始查找。
+ `-gid <群组识别码>`：查找符合指定的群组识别码的文件或目录。
+ `-group <群组名称>`：查找符合指定的群组名称的文件或目录。
+ `-size <文件大小>`：查找符合指定文件大小的文件。
+ `-type <文件类型>`：查找符合指定文件类型的文件。
+ `-user <拥有者名称>`：查找符合指定的拥有者名称的文件或目录。

例如：

```shell
xiaotuan@xiaotuan:~$ find /etc/ -name vim*
find: `/etc/ssl/private': 权限不够
find: `/etc/selinux/default/modules/active': 权限不够
/etc/alternatives/vimdiff
/etc/alternatives/vim
/etc/vim
/etc/vim/vimrc.tiny
/etc/vim/vimrc
find: `/etc/cups/ssl': 权限不够
find: `/etc/polkit-1/localauthority': 权限不够
```

