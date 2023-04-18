（1）安装 libfdk-aac

```shell
$ sudo apt install libfdk-aac-dev
```

（2）安装 libx264

```shell
$ sudo apt install libx264-dev
```

（3）配置 FFmpeg 功能

```shell
$ ./configure --enable-libx264 --enable-libfdk-aac --enable-gpl --enable-nonfree
```

（4）编译 FFmpeg

```shell
$ make
```

（5）安装 FFmpeg

```shell
$ sudo make install
```

