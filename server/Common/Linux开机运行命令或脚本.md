[toc]

### 方法一：使用 rc.local

1. 首先需要为 `/etc/rc.d/rc.local` 添加执行权限：

   ```console
   $ sudo chomd +x /etc/rc.d/rc.local
   ```

2. 打开编辑 `/etc/rc.d/rc.local` 文件：

   ```console
   $ sudo vi /etc/rc.d/rc.local
   ```

3. 在文件后面加上要执行的命令：

   ```console
   sh /root/script.sh &
   或
   node /home/web.js &
   ```

> 提示：
>
> 要指定命令的完整路径可以使用下面命令查看：
>
> ```console
> $ which command
> ```
> 例如：
> ```console
> $ which node
> /usr/bin/node
> ```

### 方法二：使用 Crontab

我们创建一个 cron 任务，这个任务在系统启动后等待 90 秒，然后执行命令和脚本。
要创建 cron 任务，打开终端并执行：

```console
$ crontab -e
```

然后输入下行内容：

```console
@reboot(sleep 90; sh \location\script.sh)
```

