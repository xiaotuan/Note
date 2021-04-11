### 创建和删除ACE

acl_create_entry()函数用来在某一现有ACL中新建一条记录。该函数会将一个指代新建ACE的句柄返回到由其第二个参数所指定的内存位置。



![409.png](../images/409.png)
然后，即可利用先前介绍过的函数来设置该记录。

acl_delete_entry()函数用来从ACL中删除一条ACE。



![410.png](../images/410.png)
