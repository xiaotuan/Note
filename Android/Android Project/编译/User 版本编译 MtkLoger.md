1. 修改 `device/mediateksample/tb8788p1_64_bsp/ProjectConfig.mk` 文件中 MTK_LOG_CUSTOMER_SUPPORT 宏的值为 yes：

   ```makefile
   MTK_LOG_CUSTOMER_SUPPORT = yes
   ```

2. 修改 `device/mediatek/system/mssi_t_64/SystemConfig.mk` 文件中 MSSI_MTK_LOG_CUSTOMER_SUPPORT 宏的值为 yes：

   ```makefile
   MSSI_MTK_LOG_CUSTOMER_SUPPORT = yes
   ```

   > 提示
   >
   > 项目对应的这个文件夹可以通过 《[查看项目使用的是那个系统目标工程](./编译/查看项目使用的是那个系统目标工程.md)》文章获取。