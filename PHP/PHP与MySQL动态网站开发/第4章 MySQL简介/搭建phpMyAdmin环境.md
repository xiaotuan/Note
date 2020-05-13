1. 下载 [phpMyAdmin](https://www.phpmyadmin.net/)
2. 下载 [WampServer](https://sourceforge.net/projects/wampserver/) 或者 [Xampp](https://www.apachefriends.org/index.html)，安装并启动该软件（我这里安装的是 WampServer）。
3. 将下载好的 phpMyAdmin 压缩包解压到 WampServer 安装目录下的www目录中。
4. 重新启动 WampServer。
5. 如果 MySQL 没有设置密码，可以在 MySQL 客户端中使用下面命令设置密码：

```console
$ mysql> set password for 用户名@localhost = password('新密码')
```

6. 在浏览器中输入如下网址：http://localhost
7. 在 phpMyAdmin 登录界面中使用 MySQL 用户名和密码进行登录即可开始使用 phpMyAdmin 了。