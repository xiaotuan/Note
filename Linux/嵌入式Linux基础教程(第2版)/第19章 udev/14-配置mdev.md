### 19.8.2　配置mdev

可以使用一个名为/etc/mdev.conf的配置文件来定制busybox mdev的行为。它一般用于设置mdev所创建的设备节点的访问权限。默认情况下，mdev在创建设备节点时会将文件拥有者的uid:gid设置为root:root，并将访问权限设置为0660。/etc/mdev.conf中的条目很简单，它们采用如下形式：



![635.png](../images/635.png)
`device` 是一个描述设备名称的简单正则表达式（regex），类似于udev的设备名称规范。其余字段就无须解释了，但要注意 `uid` 和 `gid` 是数字形式的，而不是ASCII字符串形式的用户名/组名。

下面列举几个例子。下面这条mdev规则将默认的访问权限改为777，默认的user:group则保持不变，还是root:root。当然，也可以使用类似规则修改默认的user和group：



![636.png](../images/636.png)
还可以使用/etc/mdev.conf重命名（并重定位）设备节点。以下这条规则将所有鼠标设备移动到dev目录的input子目录中。



![637.png](../images/637.png)
可以从busybox源码树的文档中了解更多有关busybox mdev的知识。

