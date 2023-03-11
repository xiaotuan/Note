[toc]

### 1. 报错信息

```
[  147.964068] [libfs_mgr]Unmapped logical partition system
[  147.964164] [liblp]Partition system will resize from 1889034240 bytes to 1888980992 bytes
[  147.980069] [libfs_mgr]Unmapped logical partition vendor
[  147.980225] [liblp]Not enough free space to expand partition: vendor
[  147.980281] Failed to resize partition vendor to size 545923072.
[  147.980348] script aborted: assert failed: update_dynamic_partitions(package_extract_file("dynamic_partitions_op_list"))
[  148.022260] E:Error in /sideload/package.zip (status 1)
[  148.072235]
[  148.128519] W:failed to read uncrypt status: No such file or directory
[  148.156736] I:current maximum temperature: 40300
[  148.156966] I:/sideload/package.zip
```

升级界面显示：Error: assert failed: update_dynamic_partitions(package_extract_file("dynamic_partitions_op_list"))

### 2. 问题原因

项目因为 super 分区超了，改动过 super 分区大小；用作升级验证的基础版本不清楚其编译时是否已经同步改代码，而升级包确认已经更新至该修改。

### 3. 解决办法

将代码同步到最新修改后，重新 remake 工程，验证升级 OK。