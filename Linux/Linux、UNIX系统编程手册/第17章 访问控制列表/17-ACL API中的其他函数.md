### ACL API中的其他函数

接下来将介绍几个未见诸于图17-2的常用ACL函数。

acl_calc_mask(&acl)函数用来计算并设置内存ACL（其句柄由 acl 参数指定）中ACL_MASK型记录的权限。通常，只要是修改或创建ACL，就会用到该函数。其会对所有ACL_USER、ACL_GROUP以及ACL_GROUP_OBJ型记录的权限并集进行计算，作为ACL_MASK型记录的权限。若ACL_MASK型记录不存在，则该函数会创建一个，这也算是该函数的妙用之一。也就是说，在将ACL_USER和ACL_GROUP型记录添加到前面提及的“最小化”ACL时，调用该函数就能确保ACL_MASK型记录的创建。

若参数acl所指定的ACL有效，acl_valid(acl)函数将返回0，否则，返回-1。若以下所有条件成立(为真)，则可判定该ACL有效。

+ ACL_USER_OBJ、ACL_GROUP_OBJ以及ACL_OTHER类型的记录均只能有一条。
+ 若有任一ACL_USER 或 ACL_GROUP 类型的记录存在，则也必然存在一条ACL_MASK型记录。
+ 标记类型为ACL_MASK的ACE至多只有一条。
+ 每条标记类型为ACL_USER的记录都有一唯一的用户ID。
+ 每条标记类型为ACL_GROUP的记录都有一唯一的组ID。

> acl_check()和acl_error()函数（后者为Linux的扩展）与acl_valid()函数有异曲同工之妙，尽管可移植性不强，但在处理畸形ACL时却能对错误提供更为精确的描述。欲知详情，请参考手册页。

acl_delete_def_file(pathname)函数用来删除目录（由参数pathname指定）的默认型ACL。

acl_init(count)函数用来新建一个空的ACL结构，其空间足以容纳由参数count所指定的记录数。(参数count 向系统传递的是编程者的柔性诉求，而非硬性要求。)函数将返回这一新建ACL的句柄。

acl_dup(acl)函数用来为由acl参数所指定的ACL创建副本，并以该ACL副本的句柄作为返回值。

acl_free(handle)函数用来释放由其他ACL函数所分配的内存。例如，必须使用该函数来释放由acl_from_text()、acl_to_text()、acl_get_file()、acl_init()以及acl_dup()调用所分配的内存。

