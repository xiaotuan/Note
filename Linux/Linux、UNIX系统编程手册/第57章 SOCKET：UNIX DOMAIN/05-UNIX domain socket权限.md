### 57.4　UNIX domain socket权限

socket文件的所有权和权限决定了哪些进程能够与这个socket进行通信。

+ 要连接一个UNIX domain流socket需要在该socket文件上拥有写权限。
+ 要通过一个UNIX domain数据报socket发送一个数据报需要在该socket文件上拥有写权限。

此外，需要在存放socket路径名的所有目录上都拥有执行（搜索）权限。

在默认情况下，创建socket（通过bind()）时会给所有者（用户）、组以及other用户赋予所有的权限。要改变这种行为可以在调用bind()之前先调用umask()来禁用不希望赋予的权限。

一些系统会忽略socket文件上的权限（SUSv3允许这种行为）。因此无法可移植地使用socket文件权限来控制对socket的访问，尽管可以可移植地使用宿主目录上的权限来达到这一目标。

