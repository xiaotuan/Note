[toc]

### 1. 使用下面命令查看节点信息

```shell
ls -Za -n
```

例如：

```shell
tb8168p1_64_bsp:/dev $ ls -Za -n
crw-------  1 0    0   u:object_r:ttyS_device:s0                3,   1 2021-07-31 10:21 ttyS1
```

### 2. 确认节点类型

通过上面输出的信息 `u:object_r:ttyp_device:s0`，可以看出它是设备类型。

### 3. 添加权限

#### 3.1 在 `device/mediatek/sepolicy/basic/non_plat/device.te` 文件中创建一个设备类型

```
type ttyS1_device, dev_type, mlstrustedobject;
```

> 注意：如果该节点是文件类型，则需要在 `device/mediatek/sepolicy/basic/non_plat/file.te` 中创建一个文件类型。例如：
>
> ```
> type sysfs_setirstate, fs_type, sysfs_type;
> ```

#### 3.2 在 `device/mediatek/sepolicy/basic/non_plat/file_contexts` 文件中将设备类型或文件类型与真实的节点映射起来

```
/dev/ttyS1 u:object_r:ttyS1_device:s0
```

```
/sys/devices/platform/soc/10010000.keypad/setirstate u:object_r:sysfs_setirstate:s0
```

#### 3.3 为使用的地方赋予权限

如果操作该节点的是 `private app` 则在 `priv_app.te` 文件中添加权限：

```
allow priv_app ttyS1_device:chr_file rw_file_perms;
allow priv_app sysfs_setirstate:file rw_file_perms;
```

如果操作节点的是第三方 app，则在 `untrusted_app_all.te` 文件中添加权限：

```
allow untrusted_app_all ttyS1_device:chr_file rw_file_perms;
allow untrusted_app_all sysfs_setirstate:file rw_file_perms;
```

其他的依次类推。

