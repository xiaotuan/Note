## A.2　配置Docker使用TLS

前文提到，Docker支持两种TLS模式。

+ daemon模式。
+ 客户端模式。

daemon模式保证daemon只处理来自拥有有效证书的客户端发起的连接，客户端模式使得客户端只能连接到拥有有效证书的daemon。

下面会将node1上的daemon配置为daemon模式并进行验证，然后会将node2节点上的客户端进程配置为客户端模式并进行验证。

