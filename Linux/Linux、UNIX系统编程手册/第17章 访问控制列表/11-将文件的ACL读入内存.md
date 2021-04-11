### 将文件的ACL读入内存

acl_get_file()函数可用来获取（由pathname所标识）文件的ACL副本。



![403.png](../images/403.png)
取决于参数type的值（ACL_TYPE_ACCESS或ACL_TYPE_DEFAULT），可调用该函数来获取访问型ACL或默认型ACL。acl_get_file()函数将返回一（类型为acl_t的)句柄，供其他ACL函数使用。

