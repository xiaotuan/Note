

接下来开始安装部署MHA，具体搭建环境如表33-5所示。

表33-5 搭建环境信息



![figure_0626_0250.jpg](../images/figure_0626_0250.jpg)
其中master对外提供写服务，备选master提供读服务，slave也提供相关的读服务，一旦master宕机，将会把备选master提升为新的master，slave指向新的master。



