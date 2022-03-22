编译 C++ 源码的命令如下：

```shell
$ g++ use_auto.cpp
```

上面的命令使用默认版本标准来编译，也可以使用 C++98 或 C++11 来编译，例如：

```shell
$ g++ -std=c++98 use_auto.cpp
$ g++ -std=c++11 use_auto.cpp
$ g++ -std=c++0x use_auto.cpp
```

