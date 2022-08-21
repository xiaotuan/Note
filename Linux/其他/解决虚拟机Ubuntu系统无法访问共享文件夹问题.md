之前已经搞定可以自动共享文件夹了,但是现在发现无法去访问，非 `root` 用户下，使用 `ls /media/sf_bak` 提示没有权限，当然如果切换到 `root`，是可以的。

【解决过程】

1. 把普通用户名加入到 `vboxsf` 之中。因为你的用户名不在 `vboxsf` 这个用户组。下面添加 `boarmy` 到 `vboxsf` 这个用户组。

	 ```shell
 boarmy@boarmy-Ubuntu:~$ sudo adduser boarmy vboxsf
    正在添加用户"boarmy"到"vboxsf"组...
    正在将用户“boarmy”加入到“vboxsf”组中
    完成。
    ```
   
2. 再去用命令行操作：

   ```shell
   boarmy@boarmy-Ubuntu:~$ ls /media/sf_bak
   ```

   但是还是无法访问共享文件夹。

3. 重启系统。

