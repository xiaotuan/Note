下面是 emmc 设备开机打印的日志：

```txt
*** Warning - bad CRC or eMMC, using default 
Bootrom start
Boot Media: eMMC
Decrypt auxiliary code ...OK

lsadc voltage min: 000000FB, max: 00000106, aver: 00000102, index: 00000004

Enter boot auxiliary code

Auxiliary code - v1.00
DDR code - V1.1.2 20160205
Build: Jul 27 2018 - 00:49:01

Reg Version:  v1.5.3\
Reg Time:     2017/12/19 14:02:12
Reg Name:     hi3798mv3dmw_hi3798mv300_DDR3-1866_1GB_16bitx2_2layers.reg

Boot auxiliary code success
Bootrom success


System startup


Relocate Boot

Jump to C code


Fastboot 3.3.0 (jenkins@Jenkins-TSD02) (Mar 29 2020 - 14:15:45)

Fastboot:      Version 3.3.0
Build Date:    Mar 29 2020, 14:30:02
CPU:           Hi3798Mv300 
Boot Media:    eMMC
DDR Size:      1GB

Found flash memory controller hifmc100.
no found nand device.

MMC/SD controller initialization.
scan edges:2 p2f:4 f2p:6
mix set temp-phase 1
scan elemnts: startp:77 endp:72
Tuning SampleClock. mix set phase:[01/07] ele:[04/14] 
MMC/SD Card:
    MID:         0x45
    Read Block:  512 Bytes
    Write Block: 512 Bytes
    Chip Size:   7636800K Bytes (High Capacity)
    Name:        "DG4008"
    Chip Type:   MMC
    Version:     5.1
    Speed:       100000000Hz
    Mode:        HS400
    Voltage:     1.8V
    Bus Width:   8bit
    Boot Addr:   0 Bytes

*** Warning - bad CRC or eMMC, using default environment

Net:   up, down, gmac0

Boot Env on eMMC
    Env Offset:          0x00400000
    Env Size:            0x00010000
    Env Range:           0x00010000
Get ID_WORD lock flag : 0


SDK Version: HiSTBAndroidV600R003C01SPC031_v2020022809

emmc<5>
[sw_ptable_init,114] begin
partition addr : [0x0] 
partition addr : [0x200000, 0x100000]
[swflash_partition_read,217]part_addr:0x200000, part_size:0x100000, offset:0x0, bytes:0xb10
[sw_ptable_check,292]cksum [0xddba], ptable->checksum[0xddba] 
[sw_ptable_init,140] data at 0x0 is ok
[swflash_partition_read,217]part_addr:0x300000, part_size:0x100000, offset:0x0, bytes:0xb10
[sw_ptable_check,292]cksum [0xddba], ptable->checksum[0xddba] 
 0          fastboot    0x000000000     0x000200000
 0         partition    0x000200000     0x000200000
 0          recovery    0x000400000     0x001000000
 0         swdevinfo    0x001400000     0x000200000
 0         baseparam    0x001600000     0x000800000
 0           pqparam    0x001E00000     0x000800000
 0              logo    0x002600000     0x000800000
 0          fastplay    0x002E00000     0x002000000
 0              boot    0x004E00000     0x001000000
 0              misc    0x005E00000     0x000200000
 0       trustedcore    0x006000000     0x002800000
 0       securestore    0x008800000     0x000800000
 0              swdb    0x009000000     0x001000000
 0             cache    0x00A000000     0x02D000000
 0            system    0x037000000     0x040000000
 0          userdata    0x077000000     0x14E800000

ptable info:2M(fastboot),2M(partition),16M(recovery),2M(swdevinfo),8M(baseparam),8M(pqparam),8M(logo),32M(fastplay),16M(boot),2M(misc),40M(trustedcore),8M(securestore),16M(swdb),720M(cache),1024M(system),5352M(userdata)

[sw_ptable_dump->252] tmp_bootargs_env=blkdevparts=mmcblk0:2M(fastboot),2M(partition),16M(recovery),2M(swdevinfo),8M(baseparam),8M(pqparam),8M(logo),32M(fastplay),16M(boot),2M(misc),40M(trustedcore),8M(securestore),16M(swdb),720M(cache),1024M(system),5352M(userdata)
[sw_ptable_init,183] partition : ok
sw_devinfo_init begin [sw_devinfo_init,827]
[swflash_partition_read,217]part_addr:0x1400000, part_size:0x200000, offset:0x0, bytes:0x8461c
[swflash_partition_read,217]part_addr:0x1500000, part_size:0x200000, offset:0x0, bytes:0x8461c
version : [1]
[devinfo_check,169] ok! msg->checksum:0xd032, crc16:0xd032
devinfo_init begin [sw_devinfo_init,950]
[devinfo_ext_check,258] ok! msg->checksum:0x0, crc16:0x0
sw_devinfo_init OK
[check_mac_format,114] Devinfo MAC data is illegal
[swflash_partition_read,217]part_addr:0x4e00000, part_size:0x1000000, offset:0x0, bytes:0x2000
sw_boot_set_bootargs:Not hisilicon ADVCA image ...
sw_ir_detect begin 500 count 
sw_ir_detect ok  
[Android_Main,39] begin
[sw_set_gpio,128] OK
[swflash_partition_read,217]part_addr:0x5e00000, part_size:0x200000, offset:0x0, bytes:0x10000
boot normal!!!
[sw_boot_set_bootcmd->375]bootm now: mmc read 0 0x1FFFFC0 0x27000 0x8000;bootm 0x1FFFFC0 
[Android_Main,86] ok
Reserve Memory
    Start Addr:          0xFFFE000
    Bound Addr:          0x8DB4000
    Free  Addr:          0xF047000
    Alloc Block:  Addr         Size
                  0xFBFD000   0x400000
                  0xF8FC000   0x300000
                  0xF8F9000   0x2000
                  0xF878000   0x80000
                  0xF847000   0x30000
                  0xF816000   0x30000
                  0xF571000   0x2A4000
                  0xF1EB000   0x385000
                  0xF1E7000   0x3000
                  0xF051000   0x195000
                  0xF047000   0x9000

[abortboot,110] begin 
[abortboot,113] close loader keyed 

MMC read: dev # 0, block # 159744, count 32768 ... 32768 blocks read: OK

161071582 Bytes/s
Check Hisilicon_ADVCA ...
Not hisilicon ADVCA image ...

Found Initrd at 0x04E00000 (Size 706413 Bytes), align at 2048 Bytes

## Booting kernel from Legacy Image at 020007c0 ...
   Image Name:   Linux-3.18.24_hi3798mv2x
   Image Type:   ARM Linux Kernel Image (uncompressed)
   Data Size:    9319129 Bytes = 8.9 MiB
   Load Address: 02000000
   Entry Point:  02000000
   Loading Kernel Image from 0x33556480 to 0x33554432 ... OK
OK
There are some conflict between "booargs" and "bootargs_1G".
The param "mmz " in "bootargs_1G" will be ignored.

ATAGS [0x00000100 - 0x000004F4], 1012Bytes

Starting kernel ...

Uncompressing Linux... done, booting the kernel.
>>>  init /var/lib/jenkins/workspace/Himv300_shandong_gerrit/sduntiyrom/sdk/device/hisilicon/bigfish/sdk/source/kernel/linux-3.18.y/drivers/usb/usbir/usb-ir.c  usb_usbir_init
>>>  init /var/lib/jenkins/workspace/Himv300_shandong_gerrit/sduntiyrom/sdk/device/hisilicon/bigfish/sdk/source/kernel/linux-3.18.y/drivers/swgpios/swgpios.c  swgpios_init
swgpios Get GPIO function failed! 
```

下面我们来跟踪下各个日志对应的执行文件及方法：

```console
Fastboot:      Version 3.3.0
Build Date:    Mar 29 2020, 14:30:02
CPU:           Hi3798Mv300 
Boot Media:    eMMC
DDR Size:      1GB
```

上面的日志对应的执行文件及方法如下所示：

**sdk/sduntiyrom/sdk/device/hisilicon/bigfish/sdk/source/boot/fastboot/board/hi3798mv310/board.c**

```c
static void display_info(void)
{
	char *str;

	printf("Fastboot:      Version %d.%d.%d\n",
		VERSION, PATCHLEVEL, SUBLEVEL);
	printf("Build Date:    "__DATE__", "__TIME__"\n");
	printf("CPU:           %s ", strcmp(get_cpu_name(), "Hi3798Mv310") ? "Hi3798Mv300" : "Hi3798Mv310");
	if (CHIPSET_CATYPE_CA == get_ca_type())
		printf("(CA)");
	printf("\n");
	get_bootmedia(&str, NULL);
	printf("Boot Media:    %s\n", str);
	//printf("DDR Size:      %sB\n", ultohstr(get_ddr_size()));

	printf("\n");
}
```

> 注意：每个芯片都有自己的 board.c，因此需要根据自己设备的芯片型号 ，在 sdk/sduntiyrom/sdk/device/hisilicon/bigfish/sdk/source/boot/fastboot/board/ 目录中找到对应的芯片目录，在里面查看 board.c 文件。



```console
Found flash memory controller hifmc100.
```

上面日志的打印位置和方法如下：

**sdk/sduntiyrom/sdk/device/hisilicon/bigfish/sdk/source/boot/fastboot/drivers/mtd/hifmc100/hifmc100_host.c**

```c
int hifmc100_host_init(void)
{
    ...
    hifmc100_set_system_clock(host, 0, ENABLE);

	regval = hifmc_read(host, HIFMC100_VERSION);
	if (regval != HIFMC100_VERSION_VALUE)
		return -ENODEV;

	printf("Found flash memory controller hifmc100.\n");
    ...
}
```

```console
no found nand device.
```

上面日志的打印位置和方法如下：

**sdk/sduntiyrom/sdk/device/hisilicon/bigfish/sdk/source/boot/fastboot/drivers/mtd/hifmc100/hifmc100_xnand.c**

```c
int hifmc100_xnand_init(struct nand_chip *chip, int if_mode)
{
	int ret;

	if (hifmc100_host_init())
		return -ENODEV;

	ret = hifmc100_xnand_probe(chip, if_mode);
	if (ret) {
		printf("no found nand device.\n");
		return -ENODEV;
	}

	return 0;
}
```



```console
MMC/SD controller initialization.
```

上面日志的打印位置和方法如下：

**sdk/sduntiyrom/sdk/device/hisilicon/bigfish/sdk/source/boot/fastboot/drivers/mmc/himciv300.c**

```c
int mmc_flash_init(void)
{
	unsigned int regval;
	struct mmc *mmc;
	int err = 0;
	unsigned int devs = (get_cpudevs() & DEV_EMMC_MASK);

	if (devs != DEV_EMMCV100
	    && devs != DEV_EMMCV200 && devs != DEV_EMMC_AUTO)
		return -1;

	puts("\nMMC/SD controller initialization.\n");
	if (mmc_initialize(NULL))
		return -1;
    ...
}
```



```console
scan edges:2 p2f:4 f2p:6
```

上面日志的打印位置和方法如下：

**sdk/sduntiyrom/sdk/device/hisilicon/bigfish/sdk/source/boot/fastboot/drivers/mmc/himciv300_hi3798mv310.c**

```c
int himciv300_tuning_mix_mode(struct mmc * mmc, u32 opcode)
{
    ...
    if ((edge_p2f == 0) && (edge_f2p == phase_num)) {
		printf("unfound correct edge! check your config is correct!!\n");
		return -1;
	}

	printf("scan edges:%d p2f:%d f2p:%d\n",edgeNum, edge_p2f, edge_f2p);
    ...
}

int himciv300_tuning_edge_mode(struct mmc * mmc, u32 opcode)
{
    ...
    if ((edge_p2f == 0) && (edge_f2p == phase_num)) {
		printf("unfound correct edge! check your config is correct!!\n");
		return -1;
	}
	printf("scan edges:%d p2f:%d f2p:%d\n",edgeNum, edge_p2f, edge_f2p);
	startp = edge_f2p * phase_dll_elements;
	endp = edge_p2f * phase_dll_elements;
	printf("found elemnts: startp:%d endp:%d\n", startp, endp);
	if (endp < startp)
		endp += totalphases;
    ...
}
```



```console
mix set temp-phase 1
```

上面日志的打印位置和方法如下：

**sdk/sduntiyrom/sdk/device/hisilicon/bigfish/sdk/source/boot/fastboot/drivers/mmc/himciv300_hi3798mv310.c**

```c
int himciv300_tuning_mix_mode(struct mmc * mmc, u32 opcode)
{
    ...
    printf("scan edges:%d p2f:%d f2p:%d\n",edgeNum, edge_p2f, edge_f2p);

	if (edge_f2p < edge_p2f)
		index = ((edge_f2p + edge_p2f) / 2) % phase_num;
	else
		index = ((edge_f2p + phase_num + edge_p2f) / 2) % phase_num;
	printf("mix set temp-phase %d\n", index);
	himciv300_set_sap_phase(host, index);
	err = himciv300_send_tuning(mmc,opcode);
    ...
}
```



```console
scan elemnts: startp:77 endp:72
```

上面日志的打印位置和方法如下：

**sdk/sduntiyrom/sdk/device/hisilicon/bigfish/sdk/source/boot/fastboot/drivers/mmc/himciv300_hi3798mv310.c**

```c
static int himciv300_tuning_edgedll_mode(struct mmc *mmc,
		 u32 opcode, int edge_p2f, int edge_f2p, u32 edgeNum)
{
    ...
tuning_out:

	if (found) {
		printf("scan elemnts: startp:%d endp:%d\n", startp, endp);

		if (endp <= startp)
			endp += totalphases;
     ...
}
    
int himciv300_tuning_dll_mode(struct mmc * mmc, u32 opcode)
{
    ...
tuning_out:

	if (found) {
		printf("scan elemnts: startp:%d endp:%d\n", startp, endp);
		if (endp < startp)
			endp += totalphases;
    ...
}
```

```console
Tuning SampleClock. mix set phase:[01/07] ele:[04/14] 
```

上面日志的打印位置和方法如下：

**sdk/sduntiyrom/sdk/device/hisilicon/bigfish/sdk/source/boot/fastboot/drivers/mmc/himciv300_hi3798mv310.c**

```c
int himciv300_tuning_dll_mode(struct mmc * mmc, u32 opcode)
{
    ...
    	himciv300_set_sap_phase(host, index);
		himciv300_set_dll_element(host,ele);
		#ifdef CONFIG_EMMC_PARAM_TAG
		emmc_samplephase = index;
		#endif
		printf("Tuning SampleClock. dll set phase:[%02d/%02d] ele:[%02d/%02d] \n",index,(phase_num-1),ele,phase_dll_elements);
    ...
}
```



```console
MMC/SD Card:
    MID:         0x45
    Read Block:  512 Bytes
    Write Block: 512 Bytes
    Chip Size:   7636800K Bytes (High Capacity)
    Name:        "DG4008"
    Chip Type:   MMC
    Version:     5.1
    Speed:       100000000Hz
    Mode:        HS400
    Voltage:     1.8V
    Bus Width:   8bit
    Boot Addr:   0 Bytes
```

上面日志的打印位置和方法如下：

**sdk/sduntiyrom/sdk/device/hisilicon/bigfish/sdk/source/boot/fastboot/drivers/mmc/himciv300.c**

```c
static void print_mmcinfo(struct mmc *mmc)
{
	HIMCI_DEBUG_FUN("Function Call");

	printf("MMC/SD Card:\n");
	printf("    MID:         0x%x\n", mmc->cid[0] >> 24);
	printf("    Read Block:  %d Bytes\n", mmc->read_bl_len);
	printf("    Write Block: %d Bytes\n", mmc->write_bl_len);
	printf("    Chip Size:   %s Bytes (%s)\n",
	       ultohstr(mmc->capacity),
	       mmc->high_capacity ? "High Capacity" : "Low Capacity");
	printf("    Name:        \"%c%c%c%c%c%c\"\n",
	       mmc->cid[0] & 0xff,
	       (mmc->cid[1] >> 24),
	       (mmc->cid[1] >> 16) & 0xff,
	       (mmc->cid[1] >> 8) & 0xff,
	       mmc->cid[1] & 0xff,
	       mmc->cid[2] >> 24);

	printf("    Chip Type:   %s\n"
	       "    Version:     %d.%d\n",
	       IS_SD(mmc) ? "SD" : "MMC",
	       (mmc->version >> 8) & 0xf, mmc->version & 0xff);

	printf("    Speed:       %sHz\n", ultohstr(mmc->tran_speed));
	printf("    Mode:        %s\n", ((mmc->timing == MMC_TIMING_MMC_HS400) ? "HS400":
		((mmc->timing == MMC_TIMING_MMC_HS200)?"HS200":
		(mmc->timing == MMC_TIMING_UHS_DDR50)?"DDR50":"HighSpeed")));
#if defined(CONFIG_ARCH_HIFONE) || defined(CONFIG_ARCH_HI3798CV2X) || defined(CONFIG_ARCH_HI3798MV2X) || defined(CONFIG_ARCH_HI3796MV2X) || defined(CONFIG_ARCH_HI3798MV310)
	printf("    Voltage:     %sV\n", (mmc->iovoltage == EMMC_IO_VOL_1_8V)?"1.8":"3.3");
#endif
	printf("    Bus Width:   %dbit\n", mmc->bus_width);
	printf("    Boot Addr:   %d Bytes\n", CONFIG_MMC_BOOT_ADDR);
}
```



```console
*** Warning - bad CRC or eMMC, using default environment
```

上面日志的打印位置和方法如下：

**sdk/sduntiyrom/sdk/device/hisilicon/bigfish/sdk/source/boot/fastboot/common/env_common.c**

```c
void env_relocate (void)
{
    ...
#endif /* CONFIG_ENV_BACKUP */
		if (rel) {
			printf("\n*** Warning - bad CRC or %s, "
			      "using default environment\n\n",
			      env_get_media(NULL));
			set_default_env();
		}
#else
        set_default_env();
#endif
    ...
}    
```



```console
Net:   up, down, gmac0
```

上面日志的打印位置和方法如下：

**sdk/sduntiyrom/sdk/device/hisilicon/bigfish/sdk/source/boot/fastboot/arch/arm/lib/board.c**

```c
void start_armboot (void)
{
    ...
#if defined(CONFIG_CMD_NET)
#if defined(CONFIG_NET_MULTI)
	puts ("Net:   ");
#endif
	eth_initialize(gd->bd);
#if defined(CONFIG_RESET_PHY_R)
	debug ("Reset Ethernet PHY\n");
	reset_phy();
#endif
#endif
    ...
}
```

```console
Boot Env on eMMC
    Env Offset:          0x00400000
    Env Size:            0x00010000
    Env Range:           0x00010000
```

上面日志的打印位置和方法如下：

**sdk/sduntiyrom/sdk/device/hisilicon/bigfish/sdk/source/boot/fastboot/arch/arm/lib/board.c**

```c
static void show_boot_env(void)
{
	int env_media;

	printf("\nBoot Env on %s\n", env_get_media(&env_media));
	printf("    Env Offset:          0x%08X\n", CONFIG_ENV_ADDR);
#ifdef CONFIG_ENV_BACKUP
	printf("    Backup Env Offset:   0x%08X\n", CONFIG_ENV_BACKUP_ADDR);
#endif /* CONFIG_ENV_BACKUP */
	printf("    Env Size:            0x%08X\n", CONFIG_ENV_SIZE);
	printf("    Env Range:           0x%08X\n", CONFIG_ENV_RANGE);

	/* check if env addr is alignment block size */
#if defined(CONFIG_GENERIC_SF)
	if ((env_media == BOOT_MEDIA_SPIFLASH) &&
	    ((get_spiflash_info()->erasesize - 1) & CONFIG_ENV_OFFSET))
		printf("*** Warning - Env offset is NOT aligned to SPI Flash "
		       "block size, environment value is read only.\n\n");
#endif /* CONFIG_GENERIC_SF */

#if defined(CONFIG_GENERIC_NAND)
	if (((env_media == BOOT_MEDIA_NAND) || (env_media == BOOT_MEDIA_SPI_NAND)) &&
	    ((get_nand_info()->erasesize - 1) & CONFIG_ENV_OFFSET))
		printf("*** Warning - Env offset is NOT aligned to NAND Flash "
		       "block size, environment value is read only.\n\n");
#endif /* CONFIG_GENERIC_SF */
}
```

```console
MMC read: dev # 0, block # 159744, count 32768 ... 32768 blocks read: OK

161071582 Bytes/s
```

上面日志的打印位置和方法如下：

**sdk/sduntiyrom/sdk/device/hisilicon/bigfish/sdk/source/boot/fastboot/common/cmd_mmc.c**

```c
int do_mmcops(cmd_tbl_t *cmdtp, int flag, int argc, char *argv[])
{
    ...
    		printf("\nMMC read: dev # %d, block # %d, count %d ... ",
				dev, blk, cnt);

			mmc_init(mmc);

			start_ticks = get_ticks();
			n = mmc->block_dev.block_read(dev, blk, cnt, addr);
			end_ticks = get_ticks();

			/* flush cache after read */
			flush_cache((ulong)addr, cnt * 512); /* FIXME */

			size = mmc->read_bl_len * cnt;

			printf("%d blocks read: %s\n",
				n, (n==cnt) ? "OK" : "ERROR");
			printf("\n%llu Bytes/s\n", (size * CONFIG_SYS_HZ)/(end_ticks - start_ticks));
    ...
}
```



```console
Reserve Memory
    Start Addr:          0xFFFE000
    Bound Addr:          0x8DB4000
    Free  Addr:          0xF047000
    Alloc Block:  Addr         Size
                  0xFBFD000   0x400000
                  0xF8FC000   0x300000
                  0xF8F9000   0x2000
                  0xF878000   0x80000
                  0xF847000   0x30000
                  0xF816000   0x30000
                  0xF571000   0x2A4000
                  0xF1EB000   0x385000
                  0xF1E7000   0x3000
                  0xF051000   0x195000
                  0xF047000   0x9000
```

上面日志的打印位置和方法如下：

**sdk/sduntiyrom/sdk/device/hisilicon/bigfish/sdk/source/boot/fastboot/lib/reserve_mem.c**

```c
void show_reserve_mem(void)
{
	struct list_head *tmp = NULL;
	reserve_mem_head *head = NULL;

	printf("Reserve Memory\n");
	printf("    Start Addr:          0x%lX\n", reserve_mem_start);
	printf("    Bound Addr:          0x%lX\n", reserve_mem_bound);
	printf("    Free  Addr:          0x%lX\n", reserve_mem_free);
	printf("    Alloc Block:  Addr         Size\n");
	list_for_each(tmp, &reserve_mem) {
		head = list_entry(tmp, reserve_mem_head, list);
		printf("                  0x%lX   0x%lX\n", head->addr, head->size);
	}

	printf("\n");
}
```



```console
[abortboot,110] begin 
[abortboot,113] close loader keyed 
```

上面日志的打印位置和方法如下：

**sdk/sduntiyrom/sdk/device/hisilicon/bigfish/sdk/source/boot/fastboot/common/main.c**

```c
static __inline__ int abortboot(int bootdelay)
{
	int abort = 0;

	printf("[%s,%d] begin \n", __FUNCTION__, __LINE__);
    if(loader_keyed != 1)
    {
        printf("[%s,%d] close loader keyed \n", __FUNCTION__, __LINE__);
        return abort;
    }
    ...
}
```



```console
Check Hisilicon_ADVCA ...
Not hisilicon ADVCA image ...
```

上面日志的打印位置和方法如下：

**sdk/sduntiyrom/sdk/device/hisilicon/bigfish/sdk/source/boot/fastboot/common/cmd_bootm.c**

```c
int do_bootm (cmd_tbl_t *cmdtp, int flag, int argc, char *argv[])
{
    ...
#ifdef CONFIG_SUPPORT_CA
		printf("Check Hisilicon_ADVCA ...\n");
		if (memcmp((char *)buf, HI_ADVCA_MAGIC, HI_ADVCA_MAGIC_SIZE)) {
			printf("Not hisilicon ADVCA image ...\n");
		} else {
			printf("Boot hisilicon ADVCA image ...\n");
			buf += HI_ADVCA_HEADER_SIZE;
		}
#endif
    ...
}

static void *boot_get_kernel (cmd_tbl_t *cmdtp, int flag, int argc, char *argv[],
		bootm_headers_t *images, ulong *os_data, ulong *os_len)
{
    ...
    /* 64M */
	printf("Check Hisilicon_ADVCA ...\n");
	if (memcmp((char *)img_addr, HI_ADVCA_MAGIC, HI_ADVCA_MAGIC_SIZE)) {
		printf("Not hisilicon ADVCA image ...\n");
	} else {
		printf("Boot hisilicon ADVCA image ...\n");
		img_addr += HI_ADVCA_HEADER_SIZE;
	}
    ...
}
```

**sdk/sduntiyrom/sdk/device/hisilicon/bigfish/sdk/source/boot/fastboot/common/cmd_bootss.c**

```c
int dev_read_page(struct mmc *mymmc, unsigned long page_i, int page_nr, void *dst)
{

	int dev = simple_strtoul("0", NULL, 10);
	u32 qbdata_flag = simple_strtoul(&part_ofs,NULL,16);
	u32 mypart_ofs = ((u64)part_ofs)/512;
	void *addr = dst;
	u32 cnt = page_nr*8;
	u32 n;
	u32 blk = mypart_ofs + 8*page_i;

	mymmc = find_mmc_device(mymmc);

	if (!mymmc)
		return 1;

	ss_dbg("\nMMC read: dev # %d, block # %d, count %d ... ",
		dev, blk, cnt);

	mmc_init(mymmc);

	n = mymmc->block_dev.block_read(dev, blk, cnt, addr);

	/* flush cache after read */
	flush_cache((ulong)addr, cnt * 512); /* FIXME */

	printf("%d blocks read: %s\n",
		n, (n == cnt) ? "OK" : "ERROR");

	if (n == cnt)
		return 1;
	else
		return 0;

}
```



```console
Found Initrd at 0x04E00000 (Size 706413 Bytes), align at 2048 Bytes
```

上面日志的打印位置和方法如下：

**sdk/sduntiyrom/sdk/device/hisilicon/bigfish/sdk/source/boot/fastboot/lib/bootimg.c**

```c
void show_bootimg_header(void *buf)
{
	struct boot_img_hdr *hdr = buf;

	if (!hdr)
		return;

	printf("\nFound Initrd at 0x%08X (Size %d Bytes), align at %d Bytes\n", \
		hdr->ramdisk_addr, hdr->ramdisk_size, hdr->page_size);
	printf("\n");
}
```



```console
## Booting kernel from Legacy Image at 020007c0 ...
```

上面日志的打印位置和方法如下：

**sdk/sduntiyrom/sdk/device/hisilicon/bigfish/sdk/source/boot/fastboot/common/cmd_bootm.c**

```c
static void *boot_get_kernel (cmd_tbl_t *cmdtp, int flag, int argc, char *argv[],
		bootm_headers_t *images, ulong *os_data, ulong *os_len)
{
    ...
    switch (genimg_get_format ((void *)img_addr)) {
	case IMAGE_FORMAT_LEGACY:
		printf ("## Booting kernel from Legacy Image at %08lx ...\n",
				img_addr);
		hdr = image_get_kernel (img_addr, images->verify);
		if (!hdr)
			return NULL;
		show_boot_progress (5);
     ...
}
```



```console
Image Name:   Linux-3.18.24_hi3798mv2x
   Image Type:   ARM Linux Kernel Image (uncompressed)
   Data Size:    9319129 Bytes = 8.9 MiB
   Load Address: 02000000
   Entry Point:  02000000
```

上面日志的打印位置和方法如下：

**sdk/sduntiyrom/sdk/device/hisilicon/bigfish/sdk/source/boot/fastboot/common/image.c**

```c
void image_print_contents (const void *ptr)
{
    ...
    printf ("%sImage Type:   ", p);
	image_print_type (hdr);
	printf ("%sData Size:    ", p);
	genimg_print_size (image_get_data_size (hdr));
	printf ("%sLoad Address: %08x\n", p, image_get_load (hdr));
	printf ("%sEntry Point:  %08x\n", p, image_get_ep (hdr));
 	...
}
```



```console
There are some conflict between "booargs" and "bootargs_1G".
The param "mmz " in "bootargs_1G" will be ignored.
```

上面日志的打印位置和方法如下：

**sdk/sduntiyrom/sdk/device/hisilicon/bigfish/sdk/source/boot/fastboot/arch/arm/lib/params.c**

```c
char *merge_args(const char *args, const char *args_merge, char *args_name,
		 char *args_merge_name)
{
    ...
    for (ix = 0; ix < nr_pv_merge; ix++) {
		char *param, *val;

		/* for echo param in 'args_merge' */
		param = pv_merge[ix].param;
		val = pv_merge[ix].val;

		/* search param in 'args' */
		ret = find_param_val(pv, nr_pv, param, val);
		if (ret == 1) { /* equate */
			continue;
		} else if (ret == 0) { /* conflict */
			if (isprint == 0) {
				isprint = 1;
				printf("There are some conflict between \"%s\" and \"%s\".\n",
				       args_name, args_merge_name);
				printf("The param \"");
			}

			printf("%s ", param);

			continue;
		} else { /* no found */
			int num;
			char *space = (pcmdline == cmdline) ? "" : " ";

			num = snprintf(pcmdline, count, "%s%s", space, param);
			count -= num;
			pcmdline += num;

			if (val) {
				num = snprintf(pcmdline, count, "=%s", val);
				count -= num;
				pcmdline += num;
			}
		}
	}

	if (isprint == 1)
		printf("\" in \"%s\" will be ignored.\n\n", args_merge_name);
    ...
}
```



```console
ATAGS [0x00000100 - 0x000004F4], 1012Bytes
```

上面日志的打印位置和方法如下：

**sdk/sduntiyrom/sdk/device/hisilicon/bigfish/sdk/source/boot/fastboot/arch/arm/lib/bootm.c**

```c
static void setup_end_tag (bd_t *bd)
{

	params->hdr.tag = ATAG_NONE;
	params->hdr.size = 0;

	if (((ulong)params - bd->bi_boot_params) >= CONFIG_BOOT_PARAMS_MAX_SIZE) {
		printf("ERROR: NOT enough TAG area!\n");
		hang();
	}

	printf("ATAGS [0x%08lX - 0x%08lX], %luBytes\n", bd->bi_boot_params, (ulong)params, ((ulong)params - bd->bi_boot_params));
}
```



```console
Starting kernel ...
```

上面日志的打印位置和方法如下：

**sdk/sduntiyrom/sdk/device/hisilicon/bigfish/sdk/source/boot/fastboot/arch/arm/lib/bootm.c**

```c
int do_bootm_linux(int flag, int argc, char *argv[], bootm_headers_t *images)
{
    ...
#ifndef CONFIG_ARM64_SUPPORT
	/* we assume that the kernel is in place */
	printf ("\nStarting kernel ...\n\n");
#endif
    ...
}
```

