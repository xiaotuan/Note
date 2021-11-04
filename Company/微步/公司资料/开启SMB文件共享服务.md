[toc]

### 1. 安装 samba

```shell
$ sudo apt-get install samba
```

### 2. 创建要共享的文件夹

比如我们在 `/home/用户名` 目录下创建一个名为 `WorkSpace` 的文件：

```shell
$ mkdir WorkSpace
```

### 3. 给共享文件夹设置权限

```shell
$ chmod 777 -R WorkSpace/
```

### 4. 修改 samba 配置文件

`samba` 配置文件为：`/etc/samba/smb.conf`，在配置文件末尾添加如下内容：

```
[WorkSpace]
   comment = share folder
   browseable = yes
   path = /home/zhangwenlong/WorkSpace
   create mask = 0777
   directory mask = 0777
   valid users = zhangwenlong
   force user = zhangwenlong
   force group = zhangwenlong
   public = yes
   available = yes
   writable = yes
```

各个参数说明如下：
+ `[WorkSpace]` ：WorkSpace 在其他电脑上看到的文件夹名字，这个名字可以和实际的共享文件夹名字不一致。
+ `browseable = yes`：表示可以浏览
+ `path = /home/zhangwenlong/WorkSpace`：设置要共享的文件夹路径
+ `create mask = 0777`：在共享文件夹中创建文件时赋予的权限
+ `directory mask = 0777`：在共享文件夹中创建目录时赋予的权限
+ `valid users = zhangwenlong`：共享账号，这个账号必须在本机中已经存在，如果不存在则先创建改账号
+ `force user = zhangwenlong`：创建文件或文件夹时所属用户
+ `force group = zhangwenlong`：创建文件或文件夹时所属的用户组
+ `public = yes`：是否公开该共享文件夹
+ `available = yes`：这个共享是否生效
+ `writable = yes`：是否允许对共享文件夹进行写入操作

### 5. 将共享账号添加到 samba 中并设置登录密码

```shell
$ sudo smbpasswd -a zhangwenlong
```

### 6. 重启 samba 服务

```shell
sudo /etc/init.d/smbd restart
```

```shell
git diff 55f6ee88 820b9c9c 
```

