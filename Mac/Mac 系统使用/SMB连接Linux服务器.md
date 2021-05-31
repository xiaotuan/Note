目的
为了mac能够挂载远程服务器的家目录

安装samba

```shell
$ sudo apt-get install samba
```

添加用户
我在远程服务器上的用户名是jagger, 所以

```shell
$ sudo smbpasswd -a jagger
```

这个时候要你设置密码，输入就好

配置
编辑/etc/samba/smb.conf文件，在最后加上如下内容：

```txt
[jagger]
   comment = kagger's Home
   path = /home/jagger
   browseable = yes
   read only = no
   guest ok = no
   create mask = 0600
```

保存退出

重启服务

```shell
$ sudo /etc/init.d/samba restart
```

看到如下输出

```shell
[ ok ] Restarting nmbd (via systemctl): nmbd.service.
[ ok ] Restarting smbd (via systemctl): smbd.service.
```

在mac上挂载smb远程目录
在finder下同时按下command+r+k，输入smb://ip，然后输入用户名密码即可.

此时就可以在finder上看到远程家目录挂载到本机上，挂载点是

```
/Volumes/jagger/
```
