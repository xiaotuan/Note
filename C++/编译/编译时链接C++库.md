可以使用如下命令在编译时链接 C++ 库：

```shell
$ g++ -std=c++0x 源码文件 -l库名称
```

例如：

```shell
$ g++ -std=c++0x spiffy.cpp -lg++
```

