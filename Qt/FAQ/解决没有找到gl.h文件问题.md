opencv第一次编译时，报错 `GL/gl.h: No such file or directory`，原因是系统里面缺少 OpenGL 库，执行下面命令安装库即可：

```shell
$ sudo apt-get install mesa-common-dev
$ sudo apt-get install libgl1-mesa-dev libglu1-mesa-dev
```

