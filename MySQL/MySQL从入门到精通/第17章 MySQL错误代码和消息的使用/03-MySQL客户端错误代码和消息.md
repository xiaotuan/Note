### 
  17.2 MySQL客户端错误代码和消息


<img class="my_markdown" class="h-pic" src="../images/Figure-0406-294.jpg" style="width:86px;  height: 86px; "/> 本节视频教学录像：4分钟

本节主要讲解MySQL客户端错误代码和消息的生成方式和查看方法。MySQL 5.6是根据MySQL安装目录下的include/errmsg.h文件来生成错误代码的。下面的代码是errmsg.h文件中的代码片段。

&#13;
    ……&#13;
    #define CR_UNKNOWN_ERROR      2000&#13;
    #define CR_SOCKET_CREATE_ERROR 2001&#13;
    #define CR_CONNECTION_ERROR 2002&#13;
    #define CR_CONN_HOST_ERROR 2003&#13;
    #define CR_IPSOCK_ERROR 2004&#13;
    ……&#13;

消息值与libmysql/errmsg.c文件中列出的错误消息对应。%d和%s分别代表数值和字符串，显示时，它们将被消息值取代，这一点和服务器端错误代码显示的方式一样。默认情况下服务器出错代码都是以2开头的,比如:错误消息“服务器握手过程中出错”的错误值为2012，错误代码为CR _SERVER_HANDSHAKE_ERR。

附录B中给出了常见的客户端错误代码、错误值和对应的错误信息。也给出了其他错误代码和错误信息。必须说明的是：由于MySQL的版本不断升级，可能出错代码和出错信息会随着版本的变化而变化。

