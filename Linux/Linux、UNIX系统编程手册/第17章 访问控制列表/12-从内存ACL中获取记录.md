### 从内存ACL中获取记录

acl_get_entry()函数会返回一句柄，指向内存ACL（由函数的acl参数指代）中的记录之一。句柄的返回位置由函数的最后一个参数指定。



![404.png](./images/404.png)
entry_id参数决定返回那条记录的句柄。若将其指定为ACL_FIRST_ENTRY，则会返回的句柄指向ACL中的首条ACE。若将该参数指定为ACL_NEXT_ENTRY，则所返回的句柄将指向上次所获取记录之后的ACE。因此，在首次调用acl_get_entry()时，把type参数指定为ACL_FIRST_ENTRY，在随后的调用中，再将其指定为ACL_NEXT_ENTRY，如此这般，就可以遍历ACL的所有记录。

若成功获取到一条ACE，acl_get_entry()函数将返回1；如无记录可取，则返回0；失败，则返回−1。

