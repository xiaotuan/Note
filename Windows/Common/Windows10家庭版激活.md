（1）使用管理员打开Windows PowerShell窗口（可以通过按住Ctrl键，再右击任务栏左侧的Windows图标，在弹出的菜单中选择“Windows PowerShell (管理员)(A)”项。

（2）执行下面的命令（执行完后会弹出“已成功卸载了产品密钥”对话框）：

```shell
Slmgr.vbs /upk
```

（3）执行下面命令（执行完成后会弹出“产品密钥安装成功”对话框）：

```shell
Slmgr /ipk PVMJN-6DFY6-9CCP6-7BKTT-D3WVR
```

（4）执行下面的命令（确保没有出现错误信息）：

```shell
Slmgr /skms zh.us.to
```

> 注意：如果在下一步提示无法连接任何密钥管理服务器的错误，可以将上面这行命令替换成：
>
> ```shell
> Slmgr /skms kms.03k.org
> ```

（5）最后执行下面这个命令（确保没有出现错误信息）：

```shell
Slmgr /ato
```

（6）下面是网上找到的一些其他Win10家庭版的激活码：

**Win 10 Core OEM:NONSLP: **

PVMJN-6DFY6-9CCP6-7BKTT-D3WVR（我使用这个激活码激活成功了）

> 提示：或者使用下面命令进行激活：
>
> 1）以管理员权限打开 `CMD` 命令行工具。
>
> 2）在 `CMD` 窗口中输入如下命令，并等待系统弹框提示执行成功：
>
> ```shell
> slmgr/skms kms.03k.org
> ```
>
> 3）关闭系统弹框，继续在 `CMD` 窗口中输入如下命令，并等待系统弹框提示成功激活：
>
> ```shell
> slmgr/ato
> ```
>
> 4）重启电脑
