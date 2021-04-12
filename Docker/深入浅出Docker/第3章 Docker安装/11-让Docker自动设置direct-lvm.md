### 3.6.2　让Docker自动设置direct-lvm

下面的步骤会将Docker配置存储驱动为 `Device Mapper` ，并使用 `direct-lvm` 模式。

（1）将下面的存储驱动配置添加到 `/etc/docker/daemon.json` 当中。

```rust
{
"storage-driver": "devicemapper",
"storage-opts": [
  "dm.directlvm_device=/dev/xdf",
  "dm.thinp_percent=95",
  "dm.thinp_metapercent=1",
  "dm.thinp_autoextend_threshold=80",
  "dm.thinp_autoextend_percent=20",
  "dm.directlvm_device_force=false"
]
}
```

Device Mapper和LVM是很复杂的知识点，并不在本书的讨论范围之内。下面简单介绍一下各配置项的含义。

+ `dm.directlvm_device` ：设置了块设备的位置。为了存储的最佳性能以及可用性，块设备应当位于高性能存储设备（如本地SSD）或者外部RAID存储阵列之上。
+ `dm.thinp_percent=95` ：设置了镜像和容器允许使用的最大存储空间占比，默认是95%。
+ `dm.thinp_metapercent` ：设置了元数据存储（MetaData Storage）允许使用的存储空间大小。默认是1%。
+ `dm.thinp_autoextend_threshold` ：设置了LVM自动扩展精简池的阈值，默认是80%。
+ `dm.thinp_autoextend_percent` ：表示当触发精简池（thin pool）自动扩容机制的时候，扩容的大小应当占现有空间的比例。
+ `dm.directlvm_device_force` ：允许用户决定是否将块设备格式化为新的文件系统。

（2）重启Docker。

（3）确认Docker已成功运行，并且块设备配置已被成功加载。

```rust
$ docker version
Client:
Version:      18.01.0-ce
<Snip>
Server:
Version:      18.01.0-ce
<Snip>
$ docker system info
<Snipped output only showing relevant data>
Storage Driver: devicemapper
Pool Name: docker-thinpool
Pool Blocksize: 524.3 kB
Base Device Size: 25 GB
Backing Filesystem: xfs
Data file:       << Would show a loop file if in loopback mode
Metadata file:   << Would show a loop file if in loopback mode
Data Space Used: 1.9 GB
Data Space Total: 23.75 GB
Data Space Available: 21.5 GB
Metadata Space Used: 180.5 kB
Metadata Space Total: 250 MB
Metadata Space Available: 250 MB
```

即使Docker在 `direct-lvm` 模式下只能设置单一块设备，其性能也会显著优于 `loopback` 模式。

