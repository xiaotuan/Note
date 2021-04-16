### 19.1.3 MTD用户空间编程

drivers/mtd/mtdchar.c文件实现了MTD字符设备接口，通过它，用户可以直接操作Flash设备。通过read()、write()系统调用可以读写Flash，通过一系列IOCTL命令可以获取Flash设备信息、擦除Flash、读写NAND的OOB、获取OOB layout及检查NAND坏块等。

代码清单19.5所示为MEMGETINFO、MEMERASE、MEMREADOOB、MEMWRITEOOB、MEMGETBADBLOCK IOCRL的例子。

代码清单19.5 /dev/mtdX IOCTL演示范例

1 mtd_oob_buf oob; 
 
 2 erase_info_user erase; 
 
 3 mtd_info_user meminfo; 
 
 4 
 
 5 /*得到MTD设备信息*/ 
 
 6 if (ioctl(fd, MEMGETINFO, &meminfo) != 0) 
 
 7 perror("ioctl(MEMGETINFO)"); 
 
 8 
 
 9 /*擦除块*/ 
 
 10 if (ioctl(ofd, MEMERASE, &erase) != 0) { 
 
 11 perror("ioctl(MEMERASE)"); 
 
 12 goto error; 
 
 13 } 
 
 14 
 
 15 /*读OOB */ 
 
 16 if (ioctl(fd, MEMREADOOB, &oob) != 0) 
 
 17 perror("ioctl(MEMREADOOB)"); 
 
 18 
 
 19 /*写OOB */ 
 
 20 if (ioctl(fd, MEMWRITEOOB, &oob) != 0) { 
 
 21 fprintf(stderr, "\n%s: %s: MTD writeoob failure: %s\n", exe_name, mtd_device, 
 
 22 strerror(errno)); 
 
 23 } 
 
 24 
 
 25 /*检查坏块*/ 
 
 26 if (blockstart != (ofs &(~meminfo.erasesize + 1))) { 
 
 27 blockstart = ofs &(~meminfo.erasesize + 1); 
 
 28 if ((badblock = ioctl(fd, MEMGETBADBLOCK, &blockstart)) < 0)



29 perror("ioctl(MEMGETBADBLOCK)"); 
 
 30 else if (badblock) {/*是坏块*/ 
 
 31 ... 
 
 32 } else/*是好块*/ 
 
 33 ... 
 
 34 }

代码清单19.6所示的过程如下：它读取记录在一个映像文件中的针对NAND的数据信息，并把它写到NAND Flash中。代码中涉及大量IOCTL的调用及NAND的擦除和写入过程（含坏块检查），mtd-utils中nand_write、flash_eraseall等工具也是借助类似方法实现的。

代码清单19.6 /dev/mtdX用户空间编程综合范例

1 int main(int argc, char **argv) 
 
 2 { 
 
 3 struct mtd_info_user meminfo; 
 
 4 struct mtd_oob_buf oob; 
 
 5 char oobbuf[MAX_OOB_SIZE]; 
 
 6 ... 
 
 7 
 
 8 memset(oobbuf, 0xff, sizeof(oobbuf)); 
 
 9 
 
 10 /* 打开/dev/mtdX */ 
 
 11 if ((fd = open(mtd_device, O_RDWR)) == - 1) { 
 
 12 perror("open Flash"); 
 
 13 exit(1); 
 
 14 } 
 
 15 
 
 16 /* 填充MTD设备容量结构体 */ 
 
 17 if (ioctl(fd, MEMGETINFO, &meminfo) != 0) { 
 
 18 perror("MEMGETINFO"); 
 
 19 close(fd); 
 
 20 exit(1); 
 
 21 } 
 
 22 
 
 23 oob.length = meminfo.oobsize; 
 
 24 oob.ptr = oobbuf; 
 
 25 
 
 26 /* 打开输入文件 */ 
 
 27 if ((ifd = open(img, O_RDONLY)) == - 1) { 
 
 28 perror("open input file"); 
 
 29 goto restoreoob; 
 
 30 } 
 
 31 
 
 32 
 
 33 imglen = lseek(ifd, 0, SEEK_END); /* 得到映像长度 */ 
 
 34 lseek(ifd, 0, SEEK_SET); 
 
 35 
 
 36 pagelen = meminfo.oobblock + meminfo.oobsize; /*一页的（数据+oob）长度*/ 
 
 37 ... 
 
 38 
 
 39 /* 从输入文件读数据然后写入MTD设备 */ 
 
 40 while (imglen && (mtdoffset < meminfo.size)) { 
 
 41 /* 在擦除块之前检查是否为坏块 */ 
 
 42 while (blockstart != (mtdoffset &(~meminfo.erasesize + 1))) {



43 blockstart = mtdoffset &(~meminfo.erasesize + 1); 
 
 44 offs = blockstart; 
 
 45 baderaseblock = 0; 
 
 46 if (!quiet) 
 
 47 fprintf(stdout, "Writing data to block %x\n", blockstart); 
 
 48 
 
 49 /* 检查坏块 */ 
 
 50 do { 
 
 51 if ((ret = ioctl(fd, MEMGETBADBLOCK, &offs)) < 0) { 
 
 52 perror("ioctl(MEMGETBADBLOCK)"); 
 
 53 goto closeall; 
 
 54 } 
 
 55 if (ret == 1) { 
 
 56 baderaseblock = 1; 
 
 57 if (!quiet) 
 
 58 fprintf(stderr, 
 
 59 "Bad block at %x, %u block(s) from %x will be skipped\n", 
 
 60 (int)offs, blockalign, blockstart); 
 
 61 } 
 
 62 if (baderaseblock) { 
 
 63 mtdoffset = blockstart + meminfo.erasesize; 
 
 64 } 
 
 65 offs += meminfo.erasesize / blockalign; 
 
 66 } while (offs < blockstart + meminfo.erasesize); 
 
 67 } 
 
 68 
 
 69 readlen = meminfo.oobblock; 
 
 70 
 
 71 /* 从输入文件中读page数据 */ 
 
 72 if ((cnt = read(ifd, writebuf, readlen)) != readlen) { 
 
 73 if (cnt == 0) /* EOF */ 
 
 74 break; 
 
 75 perror("File I/O error on input file"); 
 
 76 goto closeall; 
 
 77 } 
 
 78 
 
 79 /* 从输入文件读OOB数据 */ 
 
 80 if ((cnt = read(ifd, oobreadbuf, meminfo.oobsize)) != meminfo.oobsize) { 
 
 81 perror("File I/O error on input file"); 
 
 82 goto closeall; 
 
 83 } 
 
 84 
 
 85 /* 将OOB数据写入设备 */ 
 
 86 oob.start = mtdoffset; 
 
 87 if (ioctl(fd, MEMWRITEOOB, &oob) != 0) { 
 
 88 perror("ioctl(MEMWRITEOOB)"); 
 
 89 goto closeall; 
 
 90 } 
 
 91 
 
 92 /* 写page数据 */ 
 
 93 if (pwrite(fd, writebuf, meminfo.oobblock, mtdoffset) != meminfo.oobblock) { 
 
 94 perror("pwrite"); 
 
 95 goto closeall; 
 
 96 } 
 
 97 imglen -= readlen;



98 mtdoffset += meminfo.oobblock; 
 
 99 } 
 
 100 
 
 101 closeall: ... 
 
 102 return 0; 
 
 103 }

