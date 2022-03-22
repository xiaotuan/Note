[toc]

### 1. 报错信息

```
14:58:11: Could not determine which "make" command to run. Check the "make" step in the build configuration.
Error while building/deploying project chartthemes (kit: Desktop Qt 5.9.1 GCC 64bit)
When executing step "qmake"
```

### 2. 错误分析

未安装 Qt 支持环境。

### 3. 解决办法

安装 g++：

```shell
sudo apt install g++
sudo apt install gcc
sudo apt install cmake
```

