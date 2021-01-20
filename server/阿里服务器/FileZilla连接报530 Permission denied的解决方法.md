> 摘自：[FTP连接阿里云服务器报530 Permission denied的解决办法](https://blog.csdn.net/aiyowei1106/article/details/99304058)

![img](https://img-blog.csdnimg.cn/20190812152625948.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2FpeW93ZWkxMTA2,size_16,color_FFFFFF,t_70)

使用 8uFTP 连接阿里云服务器，报了一个 “**530 Permission denied**”，当时就有点懵了，我是 root 登陆，怎么会报这个问题呢？？？

### **解决办法：**

（我的问题解决办法是第二步，如果修改配置以后还是无法解决问题，建议从第一步开始排除问题所在）

**第一步：首先检查系统是否开启了vsftp服务，如果没有开启，先开启该服务。**

**第二步：查看配置并做相应的修改**

+ `/etc/vsftpd`：这里面的配置文件中限定了 vsftpd 用户连接控制配置。
+ `/etc/vsftpd/ftpusers`：它指定了哪些用户账户不能访问FTP服务器，例如 root 等。（将访问的账户注释掉）
+ `/etc/vsftpd/user_list`：该文件里的用户账户在默认情况下也不能访问FTP服务器，仅当 `vsftpd .conf` 配置文件里启用 `userlist_enable=NO` 选项时才允许访问。（将访问的账户注释掉或者启用 `userlist_enable=NO` 选项）
+ `/etc/vsftpd/conf`：来自定义用户登录控制、用户权限控制、超时设置、服务器功能选项、服务器性能选项、服务器响应消息等FTP服务器的配置。（根据自己需求修改）

**第三步：配置修改完成后，执行service vsftpd restart重启vsftpd服务。**

***\*然！鹅！！！\****这个问题解决了，又出现了一个“***\*错误：  无法打开传输通道。原因：由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。\****”的错误信息。

![img](https://img-blog.csdnimg.cn/20190812155638523.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2FpeW93ZWkxMTA2,size_16,color_FFFFFF,t_70)

好吧，继续找解决办法！**找到以下几个问题所在，我的问题出在软件上，将找到的几个解决办法贴出来，遇到这个问题的可以做对应的排查：**

**1、服务器的防火墙没有开启21端口。**

（我的是阿里云的服务器，之前没有对服务器的防火墙做过什么修改，所以这一步不需要做修改。不知道有没有开启的同学可以查一下，指令自行百度撒）

**2、FTP软件设置问题，或者ftp的ip地址变更。**

如果是软件设置问题，那就到菜单栏 `文件` --> `站点管理器` -->（`选中你要连接的站点）点击高级` -->`（设置）活动模式`，再尝试看看能不能连接（这是我的问题所在，设置完成后再次连接可以获取到目录列表）

如果是IP地址变更导致的话，就自行做修改吧。

![img](https://img-blog.csdnimg.cn/20190812160005131.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2FpeW93ZWkxMTA2,size_16,color_FFFFFF,t_70)

**3、当前的网络防火墙设置问题。（如果上面的解决办法都不能解决，就检查下你本机的防火墙设置）**

**4、本地网络不稳定。（这个如果网络实在是很差的话，是可能会导致这个问题的）**

