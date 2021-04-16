### 1.5.4 主机端nfs和tftp服务安装

本书配套光盘的虚拟机映像中已经安装好了nfs和tftp，LDD6410可使用tftp或nfs文件系统与主机通过网口交互。如果用户想在其他环境下自行安装，对于Ubuntu或Debian用户而言，在主机端可通过如下方法安装tftp服务：

sudo apt­get install tftpd­hpa

开启tftp服务：

sudo /etc/init.d/tftpdhpa start 
 
 Starting HPA's tftpd: in.tftpd.

对于Ubuntu或Debian用户而言，在主机端可通过如下方法安装nfs服务：

apt-get install nfs-kernel-server 
 
 sudo mkdir /home/nfs 
 
 sudo chmod 777 /home/nfs

运行“sudo vim /etc/exports”或“sudo gedit /etc/exports”，修改该文件内容为：

/home/nfs *(sync,rw)

运行exportfs rv开启NFS服务：

/etc/init.d/nfs-kernel-server restart

