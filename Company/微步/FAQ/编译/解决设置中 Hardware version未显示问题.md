[toc]

### 1. 问题描述

在 `Settings` -> `About tablet` -> `Model & hardware` -> `Hardware version` 中为显示硬件版本号。

### 2. 原因分析

`Hardware version` 显示的值是从 `ro.boot.hardware.revision` 属性中读取的，只要设置该属性即可。搜索 `ro.boot.hardware.revision` 发现只有 google GMS 会设置它的值，有时是直接赋值，有时是通过 `ro.version` 属性值赋值。

### 3. 解决办法

直接在 `build/tools/buildinfo.sh` 文件中给 `ro.boot.hardware.revision` 属性值赋值即可：

```shell
echo "ro.boot.hardware.revision=1.0"
```



