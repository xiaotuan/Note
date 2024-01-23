如果使用的是 `Windows` 操作系统，那么 `@electron/get` 会首先把下载到的 `Electron` 可执行文件及其二进制资源压缩包放置到如下目录中：

```
C:\Users\ADMINI~1\AppData\Local\Temp
```

文件下载完成后，`@electron/get` 会把它复制到缓冲目录中以备下次使用。在 `Windows` 环境下，默认的缓存目录为：

```
C:\Users\[your os username]\AppData\Local\electron\Cache
```

开发者可以通过为系统设置名为 `electron_config_cache` 的环境变量来自定义缓存目录。

知道了缓存目录的位置之后，开发者就可以先手动把 `Electron` 可执行文件及其二进制资源压缩包和哈希文件放置到响应的缓存目录中。这样再通过 `npm install` 命令安装 `Electron` 依赖包时，就会先从你的缓存目录里获取相应的文件，而不是去网络上下载了。

需要注意的是，缓冲目录子目录的命令方式是有要求的，如下所示：

```
// 二进制包文件的路径
[你的缓存目录]/httpsgithub.comelectronelectronreleasesdownloadv11.1.0electron-v11.1.0-win32-x64.zip/electron-v9.2.0-win32-x64.zip
// 哈希值文件的路径
[你的缓存目录]/httpsgithub.comelectronelectronreleasesdownloadv11.1.0SHASUMS256.txt/SHASUMS256.txt
```

