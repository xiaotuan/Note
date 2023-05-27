[toc]

### 1. MTK 平台

#### 1.1 MTK 8766

##### 1.1.1 Android R

修改 `device/mediateksample/tb8768p1_bsp/BoardConfig.mk` 文件，添加或修改如下宏的值：

```makefile
BOARD_MTK_SYSTEM_SIZE_KB := 2342036
```

##### 1.1.2 Android T

修改 `sys/device/mediatek/system/common/BoardConfig.mk` 文件，修改如下代码：

```makefile
BOARD_SUPER_PARTITION_SIZE : 6442450944
```

