

atime是Linux/UNIX系统下的一个文件属性，每当读取文件时，操作系统都会将读操作发生的时间回写到磁盘上。对于读写频繁的数据库文件来说，记录文件的访问时间一般没有任何用处，却会增加磁盘系统的负担，影响I/O的性能！因此，可以通过设置文件系统的mount属性，阻止操作系统写atime信息，以减轻磁盘I/O的负担。在Linux下的具体做法如下。

（1）修改文件系统配置文件/etc/fstab，指定noatime选项：

LABEL=/home /home ext3 noatime 1 2

（2）重新mount文件系统：

#mount -oremount /home

完成上述操作，以后读/home下文件就不会再写磁盘了。



