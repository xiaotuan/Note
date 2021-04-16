### 19.4 NOR Flash驱动实例：S3C6410外围的NOR Flash驱动

针对S3C2410、S3C6410等平台而言，外接NOR Flash的情况下，由于该NOR Flash直接映射在CPU的内存空间上，因此可以直接使用通用的drivers/mtd/maps/physmap.c驱动，在内核配置的时候应该使能MTD_PHYSMAP。为了使用NOR Flash，我们只需要在BSP的板文件中添加相应的信息，如NOR Flash所在的物理地址和大小、分区信息、总线宽度等，这些信息以platform资源和数据的形式呈现，如代码清单19.13。

代码清单19.13 S3C6410外围NOR Flash的platform数据

1 static struct resource ldd6410_nor_resource = { 
 
 2 .start = LDD6410_NOR_BASE, 
 
 3 .end = LDD6410_NOR_BASE + 0x200000 - 1, 
 
 4 .flags = IORESOURCE_MEM, 
 
 5 }; 
 
 6 
 
 7 static struct mtd_partition ldd6410_mtd_partitions[] = { 
 
 8 { 
 
 9 .name = "System", 
 
 10 .size = 0x40000, 
 
 11 .offset = 0, 
 
 12 .mask_flags = MTD_WRITEABLE, /* force read-only */ 
 
 13 }, { 
 
 14 .name = "Data", 
 
 15 .size = 0x1C0000, 
 
 16 .offset = MTDPART_OFS_APPEND, 
 
 17 }, 
 
 18 }; 
 
 19 
 
 20 static struct physmap_flash_data ldd6410_flash_data = { 
 
 21 .width = 2, 
 
 22 .parts = ldd6410_mtd_partitions,



23 .nr_parts = ARRAY_SIZE(ldd6410_mtd_partitions), 
 
 24 }; 
 
 25 
 
 26 static struct platform_device ldd6410_device_nor = { 
 
 27 .name = "physmap-flash", 
 
 28 .id = 0, 
 
 29 .dev = { 
 
 30 .platform_data = &ldd6410_flash_data, 
 
 31 }, 
 
 32 .num_resources = 1, 
 
 33 .resource = &ldd6410_nor_resource, 
 
 34 };

上述代码第27行指定platform设备的名称为“physmap-flash”，这和对应platform驱动drivers/ mtd/maps/physmap.c中定义的名称是一致的。

