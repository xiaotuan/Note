[toc]

### 1. 长虹现网开启方法

将一个名为 cboxPrivOperation.json 的文件放置到 U 盘的根目录下，然后将 U 盘插入盒子 USB 接口即可。cboxPrivOperation.json 文件的内容如下所示：

```json
{
    "operation":"open-adb",
    "mac_mode":"start-end",
    "mac":{
        "start":"00:00:00:00:00:00",
        "end":"FF:FF:FF:FF:FF:FF"
    }
}
```

### 2. 朝歌版本开启方法

+ 长虹、朝歌开发版本：根据《[新终端管理工具使用说明书](./新终端管理工具使用说明书.md)》连接。
+ 长虹、朝歌正式版本：在 U 盘根目录创建一个 cmdcconfig 没有后缀的空文件，将该 U 盘插入盒子即可。

### 3. 串口开启方法

在串口工具窗口中执行下面命令即可：

```shell
$ adbd&
```



