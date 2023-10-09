在终端中执行 `adb shell setenforce  0` 报如下错误：

```shell
Battlezone:/ # setenforce  0
setenforce: Couldn't set enforcing status to '0': Invalid argument
```

解决办法：

在 `Kernel Config` 中开启如下宏即可：

```
CONFIG_SECURITY_SELINUX_DEVELOP=y
```

> 提示：`Kernel Config` 即客制化文件中类似 `weibu/tb8788p1_64_bsp_k419/M100BS_CC_957_WIFI/config/tb8788p1_64_bsp_k419_defconfig` 的文件，或者在 `Kernel` 的 `/kernel-4.19/arch/arm64/configs/` 目录中的对应工程文件。