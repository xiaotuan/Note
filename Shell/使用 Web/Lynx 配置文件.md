lynx 命令会从配置文件中读取大量的参数设置。默认情况下，这个文件位于 `/usr/local/lib/lynx.cfg`，不过有许多 Linux 发行版将其改放到了 `/etc` 目录下（`/etc/lynx.cfg`）（Ubuntu 发行版将 lynx.cfg 放到了 `/etc/lynx-curl` 目录中）。

`lynx.cfg` 配置文件将相关的参数分组到不同的区域中，这样更容易找到参数。配置文件中条目的格式为：

```shell
PARAMETER:value			
```

其中 `PARAMETER` 是参数的全名（通常都是用大写字母，但也不总是如此），value 是跟参数关联的值。

用来定义代理服务器的配置参数有：

```shell
http_proxy:http://some.server.dom:port/
https_proxy:http://some.server.dom:port/
ftp_proxy:http://some.server.dom:port/
gopher_proxy:http://some.server.dom:port/
news_proxy:http://some.server.dom:port/
newspost_proxy:http://some.server.dom:port/
newsreply_proxy:http://some.server.dom:port/
snews_proxy:http://some.server.dom:port/
snewspost_proxy:http://some.server.dom:port/
snewsreply_proxy:http://some.server.dom:port/
nntp_proxy:http://some.server.dom:port/
wais_proxy:http://some.server.dom:port/
finger_proxy:http://some.server.dom:port/
cso_proxy:http://some.server.dom:port/
no_proxy:hose.domain.dom
```

你可以为任何 Lynx 支持的网络协议定义不同的代理服务器。NO_PROXY 参数是逗号分隔的网站列表。对于列表中的这些网站，不希望使用代理服务器直接访问。