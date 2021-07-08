[toc]

[Trojan 服务客户端设置教程索引](https://order.yizhihongxing.network/index.php?rp=/knowledgebase/13/)

- 本教程提供的配置文件中对应的本地 Socks5 端口监听端口为 1080，**使用 Trojan-Qt5 软件需要将 1080 端口修改为 51837**。
- 本教程支持 **Chrome** 、 **Firefox** 以及 **新版 Microsoft Edge** 浏览器
- 新版 Microsoft Edge 浏览器下载地址：https://www.microsoft.com/zh-cn/edge

### 首先要安装 Proxy SwitchyOmega 扩展

可以从各自浏览器商店进行安装，只有 Chrome 的商店需要在代理环境下进行访问。

- Firefox 请访问: [Firefox 应用商店](https://addons.mozilla.org/en-US/firefox/addon/switchyomega/)
- Edge、Chrome 请访问： [Chrome 应用商店](https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif?hl=zh-CN)
  Chrome 需要先开启代理客户端系统代理再进行安装，如果系统代理无法生效请查看： [无扩展、无系统代理情况下以代理模式启动 Chrome](https://order.yizhihongxing.network/index.php?rp=/knowledgebase/20/如何在无系统代理情况下启动-Google-Chrome-.html)

注：**EDGE 商店中的 SwitchyOmega 扩展为非官方上传者添加了恶意脚本后上传的，不要从 EDGE 商店中安装**

### 导入配置文件

打开扩展的选项页面，选择 `导入/导出`。

根据所使用的客户端选择恢复链接，复制粘贴到在线恢复的输入框内(右键，选择复制链接地址)，点击恢复。

- [OmegaOptions-1080.bak](https://dl.trojan-cdn.com/browser/OmegaOptions-1080.bak) (本地 Socks5 端口为 1080 的客户端：**TrojanX**)
- [OmegaOptions-51837.bak](https://dl.trojan-cdn.com/browser/OmegaOptions-51837.bak) (本地 Socks5 端口为 51837 的客户端：**Trojan-QT5 1.1.0 及以上版本**)
- [OmegaOptions-7890.bak](https://dl.trojan-cdn.com/browser/OmegaOptions-7890.bak) (本地 Socks5 端口为 7890 的客户端：**ClashX、Clash for Windows v0.10.3 及以上版本**)

导入成功后左侧情景模式会变为 `代理模式` 与 `自动切换` 两个模式，使用方法请看后面的使用介绍。