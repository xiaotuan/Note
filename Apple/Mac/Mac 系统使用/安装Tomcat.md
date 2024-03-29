> 摘自：https://www.jianshu.com/p/69496fb3495e

一、安装Tomcat

1、首先到官网下载Tomcat：[https://tomcat.apache.org/download-90.cgi](https://links.jianshu.com/go?to=https%3A%2F%2Ftomcat.apache.org%2Fdownload-90.cgi)

在 `Core` 项中选择 `tar.gz(gpg, sha1, sha512)` 文件下载。

2、解压tomcat文件,最好把它文件名重命名为“Tomcat”，方便以后查找，最后把它放入/Library(资源库中)

(1).点击finder-->用户-->你电脑的名字-->资源库(有的也叫/Library)。

(2).有些苹果将library目录隐藏起来了，可以直接点左上角前往，前往文件夹，路径填 /资源库，就进入了资源库了。

二、用终端（Terminal）直接打开Tomcat了

1、进入Tomcat的bin目录下：终端输入cd /Library/Tomcat/bin ，输完回车

> cd /Library/Tomcat/bin 

  也可以打开Tomcat文件夹，把bin文件夹直接拖拉到终端，当然前提是先输入cd+空格

2、授权bin目录下的所有操作：终端输入sudo chmod 755 *.sh，输完回车

> sudo chmod 755 *.sh

3、这时要输入密码，输完回车

4、这时候就可以开启Tomcat了，终端输入sudo sh ./startup.sh，输完回车

> sudo sh ./startup.sh

![img](https:////upload-images.jianshu.io/upload_images/12618366-0b1782fc3bf554a4.png?imageMogr2/auto-orient/strip|imageView2/2/w/1132/format/webp)

成功后的终端是这样的

三、到浏览器输入网址 `http://127.0.0.1:8080`，若出现了下面的画面就证明成功了

四、关闭Tomcat，用终端输入sh ./shutdown.sh，回车即可关闭

*说明：*

*sudo为系统超级管理员权限.*

*chmod 改变一个或多个文件的存取模式*

*755代表用户对该文件拥有读、写、执行的权限，同组的其他人员拥有执行和读的权限，没有写的权限，其它用户的权限和同组人员一样.*

*777代表，user,group ,others ,都有读写和可执行权限.*

*chmod -R 777 folername,获取文件夹权限.*

