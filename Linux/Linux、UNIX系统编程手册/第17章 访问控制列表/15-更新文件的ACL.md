### 更新文件的ACL

acl_set_file()函数的作用与acl_get_file()相反，将使用驻留于内存的ACL内容（由acl参数所指代）来更新磁盘上的ACL。



![411.png](../images/411.png)
如欲更新访问型ACL，需将该函数的tpye参数指定为ACL_TYPE_ACCESS；如欲更新目录的默认型ACL，则需将type指定为ACL_TYPE_DEFAULT。

