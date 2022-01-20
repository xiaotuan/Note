[toc]

> 提示：
>
> **Android R（11）** 中 `hardward.c` 文件路径为：`hardware/libhardware/hardware.c`

### 1. hw_get_module() 函数

此函数的功能是根据模块 ID 寻找硬件模块动态链接库的地址，然后调用 `load()` 函数打开动态链接库，并从中获取硬件模块结构体地址。执行后首先得到根据固定的符号 HAL_MODULE_INFO_SYM 寻找到的 `hw_module_t` 结构体，然后再 `hw_module_t` 中的 `hw_module_methods_t` 结构体成员函数提供的 `open` 结构打开相应的模块，并进行初始化。因为用户在调用 `open()` 时通常都会传入一个指向 `hw_device_t` 结构体的指针。这样函数 `open()` 就将对模块的操作函数结构保存到 `hw_device_t` 结构体里面，用户通过它可以和模块进行交互。

### 2. load() 函数

`load()` 函数通过 `dlopen()` 函数加载库文件，然后通过 `dlsym()` 函数找到 `hal_module_info` 的首地址。


