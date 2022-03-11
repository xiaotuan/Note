[toc]

### 1. MTK 平台

#### 1.1 MTK8766

##### 1.1.1 Android R

修改 `device/mediatek/system/mssi_t_32_ago_ww/mssi_system.prop` 文件中的 `service.adb.tcp.port` 的值为指定端口号即可：

```properties
service.adb.tcp.port=5555
```

> 提示
>
> 项目对应的这个文件夹可以通过 《[查看项目使用的是那个系统目标工程](./编译/查看项目使用的是那个系统目标工程.md)》文章获取。
