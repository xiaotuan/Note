#### 
  1.2.3 在Linux系统环境下的安装


1.下载MySQL-5.6.23-1.el7.x86_64.rpm-bundle.tar

下载页面地址：http://dev.mysql.com/downloads/mysql/，此处选择“Red Hat Enterprise Linux 7 / Oracle Linux 6 (x86, 32-bit), RPM Bundle”下载，下载至/root/mysql/目录下，下载文件名为“MySQL-5.6.23-1.el7.x86_64.rpm-bundle.tar”。

2.解压tar包

&#13;
    cd /mysql/Downloads/&#13;
    tar -xvf MySQL-5.6.23-1.el7.x86_64.rpm-bundle.tar&#13;

3.以RPM方式安装MySQL

在RHEL系统中，必须先安装“MySQL-shared-compat-5.6.23-1.el7.x86_64.rpm”兼容包，然后才能安装Server和Client，否则安装时会出错。

&#13;
    yum install MySQL-shared-compat-5.6.23-1.el7.x86_64.rpm   #RHEL兼容包&#13;
    yum install MySQL-server-5.6.23-1.el7.x86_64.rpm       #MySQL服务端程序&#13;
    yum install MySQL-client-5.6.23-1.el7.x86_64.rpm       #MySQL客户端程序&#13;
    yum install MySQL-devel-5.6.23-1.el7.x86_64.rpm        #MySQL的库和头文件&#13;
    yum install MySQL-shared-5.6.23-1.el7.x86_64.rpm       #MySQL的共享库&#13;

4.配置MySQL登录密码

&#13;
    cat/root/.mysql_secret #获取MySQL安装时生成的随机密码&#13;
    service mysql start   #启动MySQL服务&#13;
    mysql-uroot-p     #进入MySQL，使用之前获取的随机密码&#13;
    SET PASSWORD FOR'root'@'localhost'=PASSWORD('123456'); #在MySQL命令行中设置root账户的密码为123456&#13;
    quit         #退出MySQL命令行&#13;
    service mysql restart  #重新启动MySQL服务&#13;

