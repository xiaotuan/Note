[toc]

### 1. MTK 平台

#### 1.1 MTK8766

##### 1.1.1 Android R

可以通过查看 `device/mediateksample/m863u_bsp_64/ProjectConfig.mk` 文件中 `LINUX_KERNEL_VERSION` 的值来获取系统编译的 kernel 版本号：

```makefile
LINUX_KERNEL_VERSION = kernel-4.14
```

 