

在MySQL 5.0以前的版本中执行 show processlist命令，有时会出现很多进程，类似于以下情况：

unauthenticated user | 192.168.5.71:57857 | NULL | Connect | NULL | login | NULL

这些进程会累计得越来越多，并且不会消失，应用无法正常响应，导致系统瘫痪。造成这种现象的原因是什么呢？

原来，MySQL在默认情况下对于远程连接过来的IP地址会进行域名的逆向解析，如果系统的hosts文件中没有与之对应的域名，MySQL就会将此连接认为是无效用户，所以在进程中出现“unauthenticated user”并导致进程阻塞。

解决的方法很简单，在启动时加上--skip-name-resolve选项，则MySQL就可以跳过域名解析过程，避免上述问题。在MySQL 5.0以后的版本中，默认都会跳过域名逆向解析。



