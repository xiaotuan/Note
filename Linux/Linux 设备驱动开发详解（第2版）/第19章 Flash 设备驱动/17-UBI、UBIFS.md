### 19.6.5 UBI/UBIFS

UBIFS是由Thomas Gleixner，Artem Bityutskiy等人于2006年发起，致力于开发性能卓越、扩展性高的Flash专用文件系统。UBI（unsorted block images）是一种类似于LVM的逻辑卷管理层，主要实现损益均衡，逻辑擦除块、卷管理和坏块管理等，而UBIFS则是基于UBI 的Flash日志文件系统。UBIFS并不直接工作于MTD之上而是工作于UBI卷之上，这是它与JFFS2、YAFFS2的一个显著区别。

为了使用UBIFS，我们需要在配置内核时使能如下选项：

Device Drivers --→ 
 
 Memory Technology Device(MTD) support --→ 
 
 UBI - Unsorted block images --→ 
 
 <*> Enable UBI 
 
 <*> MTD devices emulation driver(gluebi)(NEW) 
 
 File systems --→ 
 
 Miscellaneous filesystems --→ 
 
 <*> UBIFS file system support

下面给出一个使用制作、烧录和使用UBIFS的过程的例子。

（1）在PC上通过mtd-utils制作UBI映像：

mkfs.ubifs -r rootfs -m 2048 -e 129024 -c 4096 -o ubifs.img 
 
 ubinize -o ubi.img -m 2048 -s 512 -p 128KiB ubifs.conf

以上命令对应的Flash的page大小为2048字节，subpage大小为512字节，eraseblock大小为128KB。rootfs为要制作的根文件系统的目录。

（2）在目标机上烧录映像：

root:/> ubiformat /dev/mtd1 -s 512 -f ubi.img 
 
 ubiformat: mtd1 (NAND), size 130023424 bytes (124.0 MiB), 131072 eraseblocks of 131072 
 
 bytes (128.0 KiB), min. I/O size 2048 bytes 
 
 libscan: scanning eraseblock 991 -- 100 % complete 
 
 ubiformat: 992 eraseblocks are supposedly empty 
 
 ubiformat: flashing eraseblock 15 -- 100 % complete 
 
 ubiformat: formatting eraseblock 991 -- 100 % complete

（3）通过ubiattach关联MTD UBI：

root:/> ubiattach /dev/ubi_ctrl -m 1 
 
 UBI: attaching mtd1 to ubi0 
 
 UBI: physical eraseblock size: 131072 bytes (128 KiB) 
 
 UBI: logical eraseblock size: 129024 bytes 
 
 UBI: smallest flash I/O unit: 2048 
 
 UBI: sub-page size: 512 
 
 UBI: VID header offset: 512 (aligned 512) 
 
 UBI: data offset: 2048 
 
 UBI: volume 0 ("rootfs") re-sized from 17 to 979 LEBs 
 
 UBI: attached mtd1 to ubi0 
 
 UBI: MTD device name: "file system(nand)" 
 
 UBI: MTD device size: 124 MiB 
 
 UBI: number of good PEBs: 992 
 
 UBI: number of bad PEBs: 0 
 
 UBI: max. allowed volumes: 128 
 
 UBI: wear-leveling threshold: 4096 
 
 UBI: number of internal volumes: 1 
 
 UBI: number of user volumes: 1



UBI: available PEBs: 0 
 
 UBI: total number of reserved PEBs: 992 
 
 UBI: number of PEBs reserved for bad PEB handling: 9 
 
 UBI: max/mean erase counter: 0/0 
 
 UBI: image sequence number: 0 
 
 UBI: background thread "ubi_bgt0d" started, PID 179 
 
 UBI device number 0, total 992 LEBs (127991808 bytes, 122.1 MiB), available 0 LEBs (0 
 
 bytes), LEB size 129024 bytes (126.0 KiB)

（4）挂载UBIFS：

root:/> mount -t ubifs ubi0:rootfs /mnt 
 
 UBIFS: mounted UBI device 0, volume 0, name "rootfs" 
 
 UBIFS: file system size: 124895232 bytes (121968 KiB, 119 MiB, 968 LEBs) 
 
 UBIFS: journal size: 9033728 bytes (8822 KiB, 8 MiB, 71 LEBs) 
 
 UBIFS: media format: w4/r0 (latest is w4/r0) 
 
 UBIFS: default compressor: lzo 
 
 UBIFS: reserved for root: 0 bytes (0 KiB)

（5）现在我们可以通过mount和ubinfo命令查看下结果：

root:/> mount 
 
 rootfs on / type rootfs (rw) 
 
 proc on /proc type proc (rw,nosuid,nodev,noexec,relatime) 
 
 sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime) 
 
 ... 
 
 ubi0:rootfs on /mnt type ubifs (rw,relatime)

root:/mnt> ubinfo 
 
 UBI version: 1 
 
 Count of UBI devices: 1 
 
 UBI control device major/minor: 10:63 
 
 Present UBI devices: ubi0

UBIFS被认为是下一代的JFFS2，它也支持运行时压缩，但是挂载比JFFS2快。另外，被用于NAND时，其设计以及性能都优越于YAFFS2，特别是工作在大页MLC NAND Flash上面。因此，目前许多项目中都正在使用UBIFS替代YAFFS2。

