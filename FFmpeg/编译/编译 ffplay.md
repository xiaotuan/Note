（1）安装 sdl

```shell
$ sudo apt-get install libsdl2-dev
```

如果执行上面命令后还是配置失败的话，再安装如下库：

```shell
$ sudo apt-get install libsdl2-2.0
```

（2）编译 FFmpeg

1. 启用 ffplay 功能

   ```shell
   $ ./configura --enable-sdl2
   ```

2. 编译 FFmpeg

   ```shell
   $ make
   ```

3. 安装 FFmpeg

   ```shell
   $ sudo make install
   ```

   