`ls` 命令用于查看目录文件列表，其基本使用方法是在终端中直接输入 `ls`，然后按回车键：

```shell
xiaotuan@xiaotuan:~$ ls
eclipse                                        phpMyAdmin  视频  音乐
eclipse-jee-2023-06-R-linux-gtk-x86_64.tar.gz  Qt5.9.0     图片  桌面
eclipse-workspace                              公共的      文档
examples.desktop  
```

常用参数：

+ `-a` ：显示目录所有文件及文件夹，包括隐藏文件，比如以 `.` 开头的：

  ```shell
  xiaotuan@xiaotuan:~$ ls -a
  ls: 无法访问'.gvfs': 权限不够
  .                  .gconf                     .Xauthority
  ..                 .gnupg                     .xinputrc
  .bash_history      .gvfs                      .xsession-errors
  .bash_logout       .ICEauthority              .xsession-errors.old
  .bashrc            .local                     公共的
  .cache             .mozilla                   模板
  .compiz            .mysql_history             视频
  .config            phpMyAdmin                 图片
  .dbus              .presage                   文档
  .dmrc              .profile                   下载
  eclipse            .python_history            音乐
  .eclipse           Qt5.9.0                    桌面
  eclipse-workspace  .sudo_as_admin_successful
  examples.desktop   .swt
  ```

+ `-l`：显示目录中文件及文件夹的详细信息

  ```shell
  xiaotuan@xiaotuan:~$ ls -l
  总用量 60
  drwxr-xr-x  8 xiaotuan xiaotuan 4096 6月   8 22:34 eclipse
  drwxrwxr-x  3 xiaotuan xiaotuan 4096 6月  29 08:43 eclipse-workspace
  -rw-r--r--  1 xiaotuan xiaotuan 8980 5月  11 17:39 examples.desktop
  drwxrwx--- 12 xiaotuan xiaotuan 4096 7月  24 20:02 phpMyAdmin
  drwxrwxr-x  8 xiaotuan xiaotuan 4096 5月  11 19:28 Qt5.9.0
  drwxr-xr-x  2 xiaotuan xiaotuan 4096 5月  11 17:45 公共的
  drwxr-xr-x  2 xiaotuan xiaotuan 4096 5月  11 17:45 模板
  drwxr-xr-x  2 xiaotuan xiaotuan 4096 5月  11 17:45 视频
  drwxr-xr-x  2 xiaotuan xiaotuan 4096 5月  11 17:45 图片
  drwxr-xr-x  2 xiaotuan xiaotuan 4096 5月  11 17:45 文档
  drwxr-xr-x  2 xiaotuan xiaotuan 4096 5月  11 18:17 下载
  drwxr-xr-x  2 xiaotuan xiaotuan 4096 5月  11 17:45 音乐
  drwxr-xr-x  2 xiaotuan xiaotuan 4096 10月 24 10:21 桌面
  ```

我们可以将多个参数组合起来使用，例如：

```shell
xiaotuan@xiaotuan:~$ ls -la
ls: 无法访问'.gvfs': 权限不够
总用量 164
drwxr-xr-x 26 xiaotuan xiaotuan 4096 10月 24 19:09 .
drwxr-xr-x  3 root     root     4096 5月  11 17:39 ..
-rw-------  1 xiaotuan xiaotuan 2129 7月  26 08:45 .bash_history
-rw-r--r--  1 xiaotuan xiaotuan  220 5月  11 17:39 .bash_logout
-rw-r--r--  1 xiaotuan xiaotuan 3771 5月  11 17:39 .bashrc
drwx------ 18 xiaotuan xiaotuan 4096 7月  25 17:58 .cache
drwx------  3 xiaotuan xiaotuan 4096 5月  11 17:46 .compiz
drwx------ 21 xiaotuan xiaotuan 4096 8月  18 10:04 .config
drwx------  3 xiaotuan xiaotuan 4096 5月  11 17:45 .dbus
-rw-r--r--  1 xiaotuan xiaotuan   41 5月  11 19:29 .dmrc
drwxr-xr-x  8 xiaotuan xiaotuan 4096 6月   8 22:34 eclipse
drwxrwxr-x  5 xiaotuan xiaotuan 4096 6月  29 08:44 .eclipse
drwxrwxr-x  3 xiaotuan xiaotuan 4096 6月  29 08:43 eclipse-workspace
-rw-r--r--  1 xiaotuan xiaotuan 8980 5月  11 17:39 examples.desktop
drwx------  2 xiaotuan xiaotuan 4096 5月  11 17:45 .gconf
drwx------  3 xiaotuan xiaotuan 4096 6月  28 17:04 .gnupg
d?????????  ? ?        ?           ?             ? .gvfs
-rw-------  1 xiaotuan xiaotuan 2938 6月  28 17:04 .ICEauthority
drwx------  3 xiaotuan xiaotuan 4096 5月  11 17:45 .local
drwx------  5 xiaotuan xiaotuan 4096 5月  11 18:05 .mozilla
-rw-------  1 xiaotuan xiaotuan 6436 7月  25 18:00 .mysql_history
drwxrwx--- 12 xiaotuan xiaotuan 4096 7月  24 20:02 phpMyAdmin
drwx------  2 xiaotuan xiaotuan 4096 5月  11 17:45 .presage
-rw-r--r--  1 xiaotuan xiaotuan  655 5月  11 17:39 .profile
-rw-------  1 xiaotuan xiaotuan    7 6月  27 09:45 .python_history
drwxrwxr-x  8 xiaotuan xiaotuan 4096 5月  11 19:28 Qt5.9.0
-rw-r--r--  1 xiaotuan xiaotuan    0 5月  11 18:05 .sudo_as_admin_successful
drwxrwxr-x  2 xiaotuan xiaotuan 4096 10月 24 19:03 .swt
-rw-------  1 xiaotuan xiaotuan   53 6月  28 17:04 .Xauthority
-rw-rw-r--  1 xiaotuan xiaotuan  132 6月  19 10:19 .xinputrc
-rw-------  1 xiaotuan xiaotuan  372 6月  28 17:09 .xsession-errors
-rw-------  1 xiaotuan xiaotuan  269 6月  28 15:28 .xsession-errors.old
drwxr-xr-x  2 xiaotuan xiaotuan 4096 5月  11 17:45 公共的
drwxr-xr-x  2 xiaotuan xiaotuan 4096 5月  11 17:45 模板
drwxr-xr-x  2 xiaotuan xiaotuan 4096 5月  11 17:45 视频
drwxr-xr-x  2 xiaotuan xiaotuan 4096 5月  11 17:45 图片
drwxr-xr-x  2 xiaotuan xiaotuan 4096 5月  11 17:45 文档
drwxr-xr-x  2 xiaotuan xiaotuan 4096 5月  11 18:17 下载
drwxr-xr-x  2 xiaotuan xiaotuan 4096 5月  11 17:45 音乐
drwxr-xr-x  2 xiaotuan xiaotuan 4096 10月 24 10:21 桌面
```

