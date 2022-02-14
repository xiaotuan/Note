在终端中运行一下命令创建 SD 卡映象文件路径：

```shell
$ mksdcard 256M c:\Android\sdcard\sdcard.img
```

使用创建的 SD 卡映象启动虚拟机：

```shell
emulator -avd AVDName -sdcard "PATH_TO_YOUR_SD_CARD_IMAGE_FILE"
```

