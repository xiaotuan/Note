### 18.8 LCD设备驱动的读写、mmap和ioctl函数

虽然帧缓冲设备的file_operations中的成员函数，即文件操作函数已经由内核在fbmem.c文件中实现，一般不再需要驱动工程师修改，但分析这些函数对于巩固字符设备驱动的知识以及加深对帧缓冲设备驱动的理解是大有裨益的。

代码清单18.12所示为LCD设备驱动的文件操作读写函数的源代码，从代码结构及习惯而言，与本书第2篇所讲解的字符设备驱动完全一致。

代码清单18.12 帧缓冲设备驱动的读写函数

1 static ssize_t 
 
 2 fb_read(struct file *file, char __user *buf, size_t count, loff_t *ppos) 
 
 3 { 
 
 4 unsigned long p = *ppos; 
 
 5 struct inode *inode = file->f_path.dentry->d_inode; 
 
 6 int fbidx = iminor(inode); 
 
 7 struct fb_info *info = registered_fb[fbidx]; 
 
 8 u32 *buffer, *dst; 
 
 9 u32 __iomem *src; 
 
 10 int c, i, cnt = 0, err = 0; 
 
 11 unsigned long total_size; 
 
 12 
 
 13 ... 
 
 14 
 
 15 buffer = kmalloc((count > PAGE_SIZE) ? PAGE_SIZE : count, 
 
 16 GFP_KERNEL); 
 
 17 if (!buffer) 
 
 18 return -ENOMEM; 
 
 19 
 
 20 src = (u32 __iomem *) (info->screen_base + p); 
 
 21 
 
 22 if (info->fbops->fb_sync) 
 
 23 info->fbops->fb_sync(info); 
 
 24



25 while (count) { 
 
 26 c = (count > PAGE_SIZE) ? PAGE_SIZE : count; 
 
 27 dst = buffer; 
 
 28 for (i = c >> 2; i--; ) 
 
 29 *dst++ = fb_readl(src++); 
 
 30 if (c & 3) { 
 
 31 u8 *dst8 = (u8 *) dst; 
 
 32 u8 __iomem *src8 = (u8 __iomem *) src; 
 
 33 
 
 34 for (i = c & 3; i--;) 
 
 35 *dst8++ = fb_readb(src8++); 
 
 36 
 
 37 src = (u32 __iomem *) src8; 
 
 38 } 
 
 39 
 
 40 if (copy_to_user(buf, buffer, c)) { 
 
 41 err = -EFAULT; 
 
 42 break; 
 
 43 } 
 
 44 *ppos += c; 
 
 45 buf += c; 
 
 46 cnt += c; 
 
 47 count -= c; 
 
 48 } 
 
 49 
 
 50 kfree(buffer); 
 
 51 
 
 52 return (err) ? err : cnt; 
 
 53 } 
 
 54 
 
 55 static ssize_t 
 
 56 fb_write(struct file *file, const char __user *buf, size_t count, loff_t *ppos) 
 
 57 { 
 
 58 unsigned long p = *ppos; 
 
 59 struct inode *inode = file->f_path.dentry->d_inode; 
 
 60 int fbidx = iminor(inode); 
 
 61 struct fb_info *info = registered_fb[fbidx]; 
 
 62 u32 *buffer, *src; 
 
 63 u32 __iomem *dst; 
 
 64 int c, i, cnt = 0, err = 0; 
 
 65 unsigned long total_size; 
 
 66 
 
 67 ... 
 
 68 
 
 69 buffer = kmalloc((count > PAGE_SIZE) ? PAGE_SIZE : count, 
 
 70 GFP_KERNEL); 
 
 71 if (!buffer) 
 
 72 return -ENOMEM; 
 
 73 
 
 74 dst = (u32 __iomem *) (info->screen_base + p); 
 
 75 
 
 76 if (info->fbops->fb_sync) 
 
 77 info->fbops->fb_sync(info); 
 
 78 
 
 79 while (count) {



80 c = (count > PAGE_SIZE) ? PAGE_SIZE : count; 
 
 81 src = buffer; 
 
 82 
 
 83 if (copy_from_user(src, buf, c)) { 
 
 84 err = -EFAULT; 
 
 85 break; 
 
 86 } 
 
 87 
 
 88 for (i = c >> 2; i--; ) 
 
 89 fb_writel(*src++, dst++); 
 
 90 
 
 91 if (c & 3) { 
 
 92 u8 *src8 = (u8 *) src; 
 
 93 u8 __iomem *dst8 = (u8 __iomem *) dst; 
 
 94 
 
 95 for (i = c & 3; i--; ) 
 
 96 fb_writeb(*src8++, dst8++); 
 
 97 
 
 98 dst = (u32 __iomem *) dst8; 
 
 99 } 
 
 100 
 
 101 *ppos += c; 
 
 102 buf += c; 
 
 103 cnt += c; 
 
 104 count -= c; 
 
 105 } 
 
 106 
 
 107 kfree(buffer); 
 
 108 
 
 109 return (cnt) ? cnt : err; 
 
 110 }

file_operations中的mmap()函数非常关键，它将显示缓冲区映射到用户空间，从而使得用户空间可以直接操作显示缓冲区而省去一次用户空间到内核空间的内存复制过程，提高效率，其源代码如代码清单18.13所示。

代码清单18.13 帧缓冲设备驱动的mmap函数

1 static int 
 
 2 fb_mmap(struct file *file, struct vm_area_struct * vma) 
 
 3 __acquires(&info->lock) 
 
 4 __releases(&info->lock) 
 
 5 { 
 
 6 int fbidx = iminor(file->f_path.dentry->d_inode); 
 
 7 struct fb_info *info = registered_fb[fbidx]; 
 
 8 struct fb_ops *fb = info->fbops; 
 
 9 unsigned long off; 
 
 10 unsigned long start; 
 
 11 u32 len; 
 
 12 
 
 13 if (vma->vm_pgoff > (～0UL >> PAGE_SHIFT)) 
 
 14 return -EINVAL; 
 
 15 off = vma->vm_pgoff << PAGE_SHIFT; 
 
 16 if (!fb) 
 
 17 return -ENODEV;



18 if (fb->fb_mmap) { 
 
 19 int res; 
 
 20 mutex_lock(&info->lock); 
 
 21 res = fb->fb_mmap(info, vma); 
 
 22 mutex_unlock(&info->lock); 
 
 23 return res; 
 
 24 } 
 
 25 
 
 26 mutex_lock(&info->lock); 
 
 27 
 
 28 /* 帧缓冲区内存 */ 
 
 29 start = info->fix.smem_start; 
 
 30 len = PAGE_ALIGN((start & ～PAGE_MASK) + info->fix.smem_len); 
 
 31 if (off >= len) { 
 
 32 /* 内存映射的IO */ 
 
 33 off -= len; 
 
 34 if (info->var.accel_flags) { 
 
 35 mutex_unlock(&info->lock); 
 
 36 return -EINVAL; 
 
 37 } 
 
 38 start = info->fix.mmio_start; 
 
 39 len = PAGE_ALIGN((start & ～PAGE_MASK) + info->fix.mmio_len); 
 
 40 } 
 
 41 mutex_unlock(&info->lock); 
 
 42 start &= PAGE_MASK; 
 
 43 if ((vma->vm_end - vma->vm_start + off) > len) 
 
 44 return -EINVAL; 
 
 45 off += start; 
 
 46 vma->vm_pgoff = off >> PAGE_SHIFT; 
 
 47 /* 这是一个I/O映射 – 告诉 maydump跳过此VMA */ 
 
 48 vma->vm_flags |= VM_IO | VM_RESERVED; 
 
 49 fb_pgprotect(file, vma, off); 
 
 50 if (io_remap_pfn_range(vma, vma->vm_start, off >> PAGE_SHIFT, 
 
 51 vma->vm_end - vma->vm_start, vma->vm_page_prot)) 
 
 52 return -EAGAIN; 
 
 53 return 0; 
 
 54 }

fb_ioctl()函数最终实现对用户I/O控制命令的执行，这些命令包括FBIOGET_VSCREENINFO（获得可变的屏幕参数）、FBIOPUT_VSCREENINFO（设置可变的屏幕参数）、FBIOGET _FSCREENINFO（获得固定的屏幕参数设置，注意，固定的屏幕参数不能由用户设置）、FBIOPUTCMAP（设置颜色表）、FBIOGETCMAP（获得颜色表）等。代码清单18.14所示为帧缓冲设备ioctl()函数的源代码。

代码清单18.14 帧缓冲设备驱动的ioctl函数

1 long do_fb_ioctl(struct fb_info *info, unsigned int cmd, 
 
 2 unsigned long arg) 
 
 3 { 
 
 4 struct fb_ops *fb; 
 
 5 struct fb_var_screeninfo var; 
 
 6 struct fb_fix_screeninfo fix; 
 
 7 struct fb_con2fbmap con2fb; 
 
 8 struct fb_cmap_user cmap;



9 struct fb_event event; 
 
 10 void __user *argp = (void __user *)arg; 
 
 11 long ret = 0; 
 
 12 
 
 13 fb = info->fbops; 
 
 14 if (!fb) 
 
 15 return -ENODEV; 
 
 16 
 
 17 switch (cmd) { 
 
 18 case FBIOGET_VSCREENINFO: 
 
 19 ret = copy_to_user(argp, &info->var, 
 
 20 sizeof(var)) ? -EFAULT : 0; 
 
 21 break; 
 
 22 case FBIOPUT_VSCREENINFO: 
 
 23 if (copy_from_user(&var, argp, sizeof(var))) { 
 
 24 ret = -EFAULT; 
 
 25 break; 
 
 26 } 
 
 27 acquire_console_sem(); 
 
 28 info->flags |= FBINFO_MISC_USEREVENT; 
 
 29 ret = fb_set_var(info, &var); 
 
 30 info->flags &= ～FBINFO_MISC_USEREVENT; 
 
 31 release_console_sem(); 
 
 32 if (ret == 0 && copy_to_user(argp, &var, sizeof(var))) 
 
 33 ret = -EFAULT; 
 
 34 break; 
 
 35 case FBIOGET_FSCREENINFO: 
 
 36 ret = copy_to_user(argp, &info->fix, 
 
 37 sizeof(fix)) ? -EFAULT : 0; 
 
 38 break; 
 
 39 case FBIOPUTCMAP: 
 
 40 if (copy_from_user(&cmap, argp, sizeof(cmap))) 
 
 41 ret = -EFAULT; 
 
 42 else 
 
 43 ret = fb_set_user_cmap(&cmap, info); 
 
 44 break; 
 
 45 case FBIOGETCMAP: 
 
 46 if (copy_from_user(&cmap, argp, sizeof(cmap))) 
 
 47 ret = -EFAULT; 
 
 48 else 
 
 49 ret = fb_cmap_to_user(&info->cmap, &cmap); 
 
 50 break; 
 
 51 ... 
 
 52 default: 
 
 53 if (fb->fb_ioctl == NULL) 
 
 54 ret = -ENOTTY; 
 
 55 else 
 
 56 ret = fb->fb_ioctl(info, cmd, arg); 
 
 57 } 
 
 58 return ret; 
 
 59 } 
 
 60 
 
 61 static long fb_ioctl(struct file *file, unsigned int cmd, unsigned long arg) 
 
 62 __acquires(&info->lock) 
 
 63 __releases(&info->lock)



64 { 
 
 65 struct inode *inode = file->f_path.dentry->d_inode; 
 
 66 int fbidx = iminor(inode); 
 
 67 struct fb_info *info; 
 
 68 long ret; 
 
 69 
 
 70 info = registered_fb[fbidx]; 
 
 71 mutex_lock(&info->lock); 
 
 72 ret = do_fb_ioctl(info, cmd, arg); 
 
 73 mutex_unlock(&info->lock); 
 
 74 return ret; 
 
 75 }

