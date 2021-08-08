[toc]

### 1. 修改 `device/sprd/sharkl3/s9863a1h10_go_32b/s9863a1h10_go_32b.xml` 文件

在文件中搜索 `super` 字符串，可以找到如下代码：

```xml
<Partition id="dtbo_a" size="8"/>
<Partition id="dtbo_b" size="8"/>
<Partition id="super" size="3130"/>
<Partition id="cache" size="20"/>
<Partition id="socko_a" size="75"/>
```

将 `super` 值修改成自己需要的值即可，它的单位是 `MB`，例如将其修改为 4GB：

```xml
<Partition id="super" size="4096"/>
```

### 2. 修改 `device/sprd/sharkl3/s9863a1h10_go_32b/module/partition/md.mk` 文件

> 注意：这个文件中的单位是 `byte` 。

将 `BOARD_SUPER_PARTITION_SIZE` 的值修改为 4GB，将 `BOARD_GROUP_UNISOC_SIZE` 的值修改为 `BOARD_SUPER_PARTITION_SIZE` 的值再减去 `4MB`，即 4096MB - 4 MB= 4092MB，最终修改内容如下所示：

```makefile
BOARD_SUPER_PARTITION_SIZE := 4294967296
# BOARD_GROUP_UNISOC_SIZE = BOARD_SUPER_PARTITION_SIZE - RESERVED_SIZE(4MB for metadata)
BOARD_GROUP_UNISOC_SIZE := 4290772992
$(call md-set, BOARD_CACHEIMAGE_PARTITION_SIZE, 20971520)
```

