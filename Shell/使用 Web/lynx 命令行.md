Web 页面由三种类型的数据组成：

+ HTTP 头部
+ cookie
+ HTML 内容

Lynx 程序支持三种不同的格式来查看 Web 页面实际的 HTML 内容：

+ 在终端会话中利用 `curses` 图形库显示文本图形；
+ 文本文件，文件内容是从 Web 页面中转储的原始数据；
+ 文本文件，文件内容是从 Web 页面中转储的原始 HTML 源码。

lynx 命令的基本格式如下：

```shell
lynx options URL
```

