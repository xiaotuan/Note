### 3.5.4 goto

用不用goto一直是一个著名的争议话题，Linux内核源代码中对goto的应用非常广泛，但是一般只限于错误处理中，其结构如：

if(register_a()!=0) 
 
 goto err; 
 
 if(register_b()!=0) 
 
 goto err1; 
 
 if(register_c()!=0) 
 
 goto err2; 
 
 if(register_d()!=0) 
 
 goto err3;

... 
 
 err3: 
 
 unregister_c(); 
 
 err2: 
 
 unregister_b(); 
 
 err1: 
 
 unregister_a(); 
 
 err: 
 
 return ret;

这种goto用于错误处理的用法实在是简单而高效，只需保证在错误处理时注销、资源释放等与正常的注册、资源申请顺序相反。

