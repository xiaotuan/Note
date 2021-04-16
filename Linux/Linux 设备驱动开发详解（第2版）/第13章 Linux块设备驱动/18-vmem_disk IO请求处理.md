### 13.7.4 vmem_disk I/O请求处理

在vmem_disk驱动中，通过模块参数request_mode的方式来支持3种不同的请求处理模式以加深读者对它们的理解，代码清单13.19列出了vmem_disk驱动的请求处理代码。

代码清单13.19 vmem.disk设备驱动的请求处理函数

1 /* 
 
 2 * 处理一个I/O request. 
 
 3 */ 
 
 4 static void vmem_disk_transfer(struct vmem_disk_dev *dev, unsigned long sector, 
 
 5 unsigned long nsect, char *buffer, int write) 
 
 6 { 
 
 7 unsigned long offset = sector*KERNEL_SECTOR_SIZE; 
 
 8 unsigned long nbytes = nsect*KERNEL_SECTOR_SIZE; 
 
 9 
 
 10 if ((offset + nbytes) > dev->size) { 
 
 11 printk (KERN_NOTICE "Beyond-end write (%ld %ld)\n", offset, nbytes); 
 
 12 return; 
 
 13 } 
 
 14 if (write) 
 
 15 memcpy(dev->data + offset, buffer, nbytes); 
 
 16 else 
 
 17 memcpy(buffer, dev->data + offset, nbytes); 
 
 18 } 
 
 19 
 
 20 /* 
 
 21 * request函数的简单形式 
 
 22 */ 
 
 23 static void vmem_disk_request(struct request_queue *q) 
 
 24 { 
 
 25 struct request *req; 
 
 26 
 
 27 while ((req = elv_next_request(q)) != NULL) { 
 
 28 struct vmem_disk_dev *dev = req->rq_disk->private_data; 
 
 29 if (! blk_fs_request(req)) { 
 
 30 printk (KERN_NOTICE "Skip non-fs request\n"); 
 
 31 end_request(req, 0); 
 
 32 continue; 
 
 33 }



34 
 
 35 vmem_disk_transfer(dev, req->sector, req->current_nr_sectors, 
 
 36 req->buffer, rq_data_dir(req)); 
 
 37 
 
 38 end_request(req, 1); 
 
 39 } 
 
 40 } 
 
 41 
 
 42 
 
 43 /* 
 
 44 * 传输一个单独的BIO 
 
 45 */ 
 
 46 static int vmem_disk_xfer_bio(struct vmem_disk_dev *dev, struct bio *bio) 
 
 47 { 
 
 48 int i; 
 
 49 struct bio_vec *bvec; 
 
 50 sector_t sector = bio->bi_sector; 
 
 51 
 
 52 /* Do each segment independently. */ 
 
 53 bio_for_each_segment(bvec, bio, i) { 
 
 54 char *buffer = __bio_kmap_atomic(bio, i, KM_USER0); 
 
 55 vmem_disk_transfer(dev, sector, bio_cur_sectors(bio), 
 
 56 buffer, bio_data_dir(bio) == WRITE); 
 
 57 sector += bio_cur_sectors(bio); 
 
 58 __bio_kunmap_atomic(bio, KM_USER0); 
 
 59 } 
 
 60 return 0; /* Always "succeed" */ 
 
 61 } 
 
 62 
 
 63 /* 
 
 64 * 传输一个完整的request 
 
 65 */ 
 
 66 static int vmem_disk_xfer_request(struct vmem_disk_dev *dev, struct request *req) 
 
 67 { 
 
 68 
 
 69 struct req_iterator iter; 
 
 70 int nsect = 0; 
 
 71 struct bio_vec *bvec; 
 
 72 
 
 73 rq_for_each_segment(bvec, req, iter) { 
 
 74 char *buffer = __bio_kmap_atomic(iter.bio, iter.i, KM_USER0); 
 
 75 sector_t sector = iter.bio->bi_sector; 
 
 76 vmem_disk_transfer(dev, sector, bio_cur_sectors(iter.bio), 
 
 77 buffer, bio_data_dir(iter.bio) == WRITE); 
 
 78 sector += bio_cur_sectors(iter.bio); 
 
 79 __bio_kunmap_atomic(iter.bio, KM_USER0); 
 
 80 nsect += iter.bio->bi_size/KERNEL_SECTOR_SIZE; 
 
 81 } 
 
 82 return nsect; 
 
 83 } 
 
 84 
 
 85 
 
 86 /* 
 
 87 * 更强大的request处理 
 
 88 */



89 static void vmem_disk_full_request(struct request_queue *q) 
 
 90 { 
 
 91 struct request *req; 
 
 92 int sectors_xferred; 
 
 93 struct vmem_disk_dev *dev = q->queuedata; 
 
 94 
 
 95 while ((req = elv_next_request(q)) != NULL) { 
 
 96 if (! blk_fs_request(req)) { 
 
 97 printk (KERN_NOTICE "Skip non-fs request\n"); 
 
 98 end_request(req, 0); 
 
 99 continue; 
 
 100 } 
 
 101 sectors_xferred = vmem_disk_xfer_request(dev, req); 
 
 102 end_request (req, 1); 
 
 103 } 
 
 104 } 
 
 105 
 
 106 /* 
 
 107 * "制造请求"方式 
 
 108 */ 
 
 109 static int vmem_disk_make_request(struct request_queue *q, struct bio *bio) 
 
 110 { 
 
 111 struct vmem_disk_dev *dev = q->queuedata; 
 
 112 int status; 
 
 113 
 
 114 status = vmem_disk_xfer_bio(dev, bio); 
 
 115 bio_endio(bio, status); 
 
 116 return 0; 
 
 117 }

上述代码中的1～40行、43～104行、106～117行分别对应了RM_SIMPLE、RM_FULL、RM_NOQUEUE这3种不同的请求处理方式。

vmem_disk的驱动位于VirtualBox虚拟机映像的/home/lihacker/develop/svn/ldd6410-read-only/ training/kernel/drivers/ vmem_disk下面，已经有编写好的Makefile，直接在其中运行make命令即可得到vmem_disk.ko模块。

