### 5.1 PHP与Redis

Redis官方推荐的PHP客户端是Predis1和phpredis2。前者是完全使用PHP代码实现的原生客户端，而后者则是使用C语言编写的PHP扩展。在功能上两者区别并不大，就性能而言后者会更胜一筹。考虑到很多主机并未提供安装PHP扩展的权限，本节会以Predis为示例介绍如何在PHP中使用Redis。

1
<a class="my_markdown" href="['https://github.com/nrk/predis']">https://github.com/nrk/predis</a>

2
<a class="my_markdown" href="['https://github.com/nicolasff/phpredis']">https://github.com/nicolasff/phpredis</a>

虽然Predis的性能逊于phpredis，但是除非执行大量Redis命令，否则很难区分二者的性能。而且实际应用中执行Redis命令的开销更多在网络传输上，单纯注重客户端的性能意义不大。读者在开发时可以根据自己的项目需要来权衡使用哪个客户端。

Predis对PHP版本的最低要求为5.3。

