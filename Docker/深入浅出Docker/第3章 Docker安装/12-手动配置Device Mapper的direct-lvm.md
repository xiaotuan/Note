### 3.6.3　手动配置Device Mapper的direct-lvm

完整介绍如何进行Device Mapper direct-lvm的手动配置已经超越了本书的范畴，并且不同操作系统版本之下配置方式也不尽相同。但是，下面列出的内容是读者需要了解并在配置的时候仔细斟酌的。

+ **块设备（Block Device）：** 在使用direct-lvm模式的时候，读者需要有可用的块设备。这些块设备应该位于高性能的存储设备之上，比如本地SSD或者外部高性能LUN存储。如果Docker环境部署在企业私有云（On-Premise）之上，那么外部LUN存储可以使用FC、iSCSI，或者其他支持块设备协议的存储阵列。如果Docker环境部署在公有云之上，那么可以采用公有云厂商提供的任何高性能的块设备（通常基于SSD）。
+ **LVM配置：** Docker的Device Mapper存储驱动底层利用LVM（Logical Volume Manager）来实现，因此需要配置LVM所需的物理设备、卷组、逻辑卷和精简池。读者应当使用专用的物理卷并将其配置在相同的卷组当中。这个卷组不应当被Docker之外的工作负载所使用。此外还需要配置额外两个逻辑卷，分别用于存储数据和源数据信息。另外，要创建LVM配置文件、指定LVM自动扩容的触发阈值，以及自动扩容的大小，并且为自动扩容配置相应的监控，保证自动扩容会被触发。
+ **Docker配置：** 修改Docker配置文件之前要先保存原始文件（ `etc/docker/daemon.json` ），然后再进行修改。读者环境中的dm.thinpooldev配置项对应值可能跟下面的示例内容有所不同，需要修改为合适的配置。

```rust
{
  "storage-driver": "devicemapper",
  "storage-opts": [
  "dm.thinpooldev=/dev/mapper/docker-thinpool",
  "dm.use_deferred_removal=true",
  "dm.use_deferred_deletion=true"
  ]
}
```

修改并保存配置后，读者可以重启Docker daemon。

如果想获取更多细节信息，可以参考Docker文档，或者咨询Docker技术账户管理员。

