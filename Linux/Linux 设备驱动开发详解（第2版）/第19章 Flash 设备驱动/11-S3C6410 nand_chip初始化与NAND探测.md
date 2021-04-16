### 19.5.2 S3C6410 nand_chip初始化与NAND探测

S3C6410的NAND驱动以platform驱动的形式存在，在执行probe()时，初始化nand_chip实例并运行nand_scan()扫描NAND设备，最后调用add_mtd_partitions()添加板文件platform中定义的分区表。nand_chip是NAND Flash驱动的核心数据结构，这个结构体中的成员直接对应着NAND Flash的底层操作，针对具体的NAND控制器情况，本驱动中初始化了IO_ADDR_R、IO_ADDR_W、cmd_ctrl()、dev_ready()、scan_bbt()以及ECC相关的信息。代码清单19.14所示为S3C6410外围NAND Flash驱动的nand_chip初始化与注册过程。

代码清单19.14 S3C6410 nand_chip初始化与注册

1 static int s3c_nand_probe(struct platform_device *pdev, enum s3c_cpu_type cpu_type) 
 
 2 { 
 
 3 ... 
 
 4 for (i = 0; i < plat_info→chip_nr; i++) { 
 
 5 nand→IO_ADDR_R = (char *)(s3c_nand.regs + S3C_NFDATA); 
 
 6 nand→IO_ADDR_W = (char *)(s3c_nand.regs + S3C_NFDATA); 
 
 7 nand→cmd_ctrl = s3c_nand_hwcontrol; 
 
 8 nand→dev_ready = s3c_nand_device_ready; 
 
 9 nand→scan_bbt = s3c_nand_scan_bbt; 
 
 10 nand→options = 0; 
 
 11 
 
 12 #if defined(CONFIG_MTD_NAND_S3C_CACHEDPROG) 
 
 13 nand→options |= NAND_CACHEPRG; 
 
 14 #endif 
 
 15 
 
 16 #if defined(CONFIG_MTD_NAND_S3C_HWECC) 
 
 17 nand→ecc.mode = NAND_ECC_HW; 
 
 18 nand→ecc.hwctl = s3c_nand_enable_hwecc; 
 
 19 nand→ecc.calculate = s3c_nand_calculate_ecc; 
 
 20 nand→ecc.correct = s3c_nand_correct_data; 
 
 21 
 
 22 s3c_nand_hwcontrol(0, NAND_CMD_READID, NAND_NCE|NAND_CLE| NAND_CTRL_CHANGE); 
 
 23 s3c_nand_hwcontrol(0, 0x00, NAND_CTRL_CHANGE | NAND_NCE | NAND_ALE); 
 
 24 s3c_nand_hwcontrol(0, 0x00, NAND_NCE | NAND_ALE); 
 
 25 s3c_nand_hwcontrol(0, NAND_CMD_NONE, NAND_NCE | NAND_CTRL_CHANGE); 
 
 26 s3c_nand_device_ready(0); 
 
 27 
 
 28 tmp = readb(nand→IO_ADDR_R); /* 制造商ID */ 
 
 29 tmp = readb(nand→IO_ADDR_R); /* 设备ID */ 
 
 30 devID = tmp; 
 
 31 
 
 32 for (j = 0; nand_flash_ids[j].name != NULL; j++) { 
 
 33 if (tmp == nand_flash_ids[j].id) { 
 
 34 type = &nand_flash_ids[j]; 
 
 35 break; 
 
 36 } 
 
 37 } 
 
 38 
 
 39 ... 
 
 40 nand→cellinfo = readb(nand→IO_ADDR_R); /* 第3个字节 */ 
 
 41 tmp = readb(nand→IO_ADDR_R); /* 第4个字节 */ 
 
 42 
 
 43 if (!type→pagesize) {



44 if (((nand→cellinfo >> 2) & 0x3) == 0) { 
 
 45 nand_type = S3C_NAND_TYPE_SLC; 
 
 46 nand→ecc.size = 512; 
 
 47 nand→ecc.bytes = 4; 
 
 48 if (devID == 0xd5) { 
 
 49 /* Page size is 4Kbytes */ 
 
 50 nand→ecc.read_page = s3c_nand_read_page_8bit; 
 
 51 ... 
 
 52 } else { 
 
 53 if ((1024 << (tmp & 3)) == 4096) /* For 4KB Page 8_bit ECC */ 
 
 54 { 
 
 55 /* Page size is 4Kbytes */ 
 
 56 nand→ecc.read_page = s3c_nand_read_page_8bit; 
 
 57 ... 
 
 58 } else { 
 
 59 ... 
 
 60 } 
 
 61 } 
 
 62 } else { 
 
 63 nand_type = S3C_NAND_TYPE_MLC; 
 
 64 nand→options |= NAND_NO_SUBPAGE_WRITE; /* NOP = 1 if MLC */ 
 
 65 if (devID == 0xd5) { 
 
 66 /* Page size is 4Kbytes */ 
 
 67 nand→ecc.read_page = s3c_nand_read_page_8bit; 
 
 68 nand→ecc.write_page = s3c_nand_write_page_8bit; 
 
 69 ... 
 
 70 } else { 
 
 71 if ((1024 << (tmp & 3)) == 4096) { 
 
 72 /* Page size is 4Kbytes */ 
 
 73 nand→ecc.read_page = s3c_nand_read_page_8bit; 
 
 74 nand→ecc.write_page = s3c_nand_write_page_8bit; 
 
 75 nand→ecc.read_oob = s3c_nand_read_oob_8bit; 
 
 76 ... 
 
 77 } else { 
 
 78 nand→ecc.read_page = s3c_nand_read_page_4bit; 
 
 79 ... 
 
 80 } 
 
 81 } 
 
 82 } 
 
 83 ... 
 
 84 
 
 85 printk("S3C NAND Driver is using hardware ECC.\n"); 
 
 86 #else 
 
 87 nand→ecc.mode = NAND_ECC_SOFT; 
 
 88 printk("S3C NAND Driver is using software ECC.\n"); 
 
 89 #endif 
 
 
 90 
 if (nand_scan(s3c_mtd, 1)) { 
 
 91 ret = -ENXIO; 
 
 92 goto exit_error; 
 
 93 } 
 
 94 
 
 95 /* 注册分区信息 */ 
 
 
 96 
 add_mtd_partitions(s3c_mtd, partition_info, plat_info→mtd_part_nr); 
 
 97 } 
 
 98



99 pr_debug("initialized ok\n"); 
 
 100 return 0; 
 
 101 ... 
 
 102 }

drivers/mtd/nand/s3c_nand.c是一个platform驱动，我们在LDD6410的BSP中只需要添加相关的针对NAND的platform设备和分区信息即可。

