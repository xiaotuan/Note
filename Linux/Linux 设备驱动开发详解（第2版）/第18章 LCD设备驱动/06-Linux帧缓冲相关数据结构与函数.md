### 18.2.3 Linux帧缓冲相关数据结构与函数

#### 1．fb_info结构体

帧缓冲设备最关键的一个数据结构体是fb_info结构体（为了便于记忆，我们把它简称为“FBI”），FBI中包括了关于帧缓冲设备属性和操作的完整描述，这个结构体的定义如代码清单18.1所示。

代码清单18.1 fb_info结构体

1 struct fb_info { 
 
 2 int node; 
 
 3 int flags; 
 
 4 struct mutex lock; /* 用于open/release/ioctl的锁 */ 
 
 5 struct fb_var_screeninfo var; /*可变参数 */ 
 
 6 struct fb_fix_screeninfo fix; /*固定参数 */ 
 
 7 struct fb_monspecs monspecs; /*显示器标准 */ 
 
 8 struct work_struct queue; /* 帧缓冲事件队列 */ 
 
 9 struct fb_pixmap pixmap; /* 图像硬件mapper */ 
 
 10 struct fb_pixmap sprite; /* 光标硬件mapper */ 
 
 11 struct fb_cmap cmap; /* 目前的颜色表*/ 
 
 12 struct list_head modelist; 
 
 13 struct fb_videomode *mode; /* 目前的video模式 */ 
 
 14 
 
 15 #ifdef CONFIG_FB_BACKLIGHT 
 
 16 /* 对应的背光设备 */ 
 
 17 struct backlight_device *bl_dev; 
 
 18 /* 背光调整 */ 
 
 19 struct mutex bl_mutex; 
 
 20 u8 bl_curve[FB_BACKLIGHT_LEVELS]; 
 
 21 #endif



22 #ifdef CONFIG_FB_DEFERRED_IO 
 
 23 struct delayed_work deferred_work; 
 
 24 struct fb_deferred_io *fbdefio; 
 
 25 #endif 
 
 26 struct fb_ops *fbops; /* fb_ops，帧缓冲操作 */ 
 
 27 struct device *device; /* 父设备 */ 
 
 28 struct device *dev; /* fb设备 */ 
 
 29 int class_flag; /* 私有sysfs标志 */ 
 
 30 #ifdef CONFIG_FB_TILEBLITTING 
 
 31 struct fb_tile_ops *tileops; /* 图块Blitting */ 
 
 32 #endif 
 
 33 char _ _iomem *screen_base; /* 虚拟基地址 */ 
 
 34 unsigned long screen_size; /* ioremapped的虚拟内存大小 */ 
 
 35 void *pseudo_palette; /* 伪16色颜色表 */ 
 
 36 #define FBINFO_STATE_RUNNING 0 
 
 37 #define FBINFO_STATE_SUSPENDED 1 
 
 38 u32 state; /* 硬件状态，如挂起 */ 
 
 39 void *fbcon_par; 
 
 40 void *par; 
 
 41 };

FBI中记录了帧缓冲设备的全部信息，包括设备的设置参数、状态以及操作函数指针。每一个帧缓冲设备都必须对应一个FBI。

#### 2．fb_ops结构体

FBI的成员变量fbops为指向底层操作的函数的指针，这些函数是需要驱动程序开发人员编写的，其定义如代码清单18.2所示。

代码清单18.2 fb_ops结构体

1 struct fb_ops { 
 
 2 struct module *owner; 
 
 3 /* 打开/释放 */ 
 
 4 int(*fb_open)(struct fb_info *info, int user); 
 
 5 int(*fb_release)(struct fb_info *info, int user); 
 
 6 
 
 7 /* 对于非线性布局的/常规内存映射无法工作的帧缓冲设备需要 */ 
 
 8 ssize_t(*fb_read)(struct file *file, char _ _user *buf, size_t count, 
 
 9 loff_t*ppos); 
 
 10 ssize_t(*fb_write)(struct file *file, const char _ _user *buf, size_t count, 
 
 11 loff_t *ppos); 
 
 12 
 
 13 /* 检测可变参数，并调整到支持的值*/ 
 
 14 int(*fb_check_var)(struct fb_var_screeninfo *var, struct fb_info *info); 
 
 15 
 
 16 /* 根据info->var设置video模式 */ 
 
 17 int(*fb_set_par)(struct fb_info *info); 
 
 18 
 
 19 /* 设置color寄存器 */ 
 
 20 int(*fb_setcolreg)(unsigned regno, unsigned red, unsigned green, unsigned 
 
 21 blue, unsigned transp, struct fb_info *info); 
 
 22 
 
 23 /* 批量设置color寄存器，设置颜色表 */ 
 
 24 int(*fb_setcmap)(struct fb_cmap *cmap, struct fb_info *info); 
 
 25



26 /*显示空白 */ 
 
 27 int(*fb_blank)(int blank, struct fb_info *info); 
 
 28 
 
 29 /* pan显示 */ 
 
 30 int(*fb_pan_display)(struct fb_var_screeninfo *var, struct fb_info *info); 
 
 31 
 
 32 /* 矩形填充 */ 
 
 33 void(*fb_fillrect)(struct fb_info *info, const struct fb_fillrect *rect); 
 
 34 /* 数据复制 */ 
 
 35 void(*fb_copyarea)(struct fb_info *info, const struct fb_copyarea *region); 
 
 36 /* 图形填充 */ 
 
 37 void(*fb_imageblit)(struct fb_info *info, const struct fb_image *image); 
 
 38 
 
 39 /* 绘制光标 */ 
 
 40 int(*fb_cursor)(struct fb_info *info, struct fb_cursor *cursor); 
 
 41 
 
 42 /* 旋转显示 */ 
 
 43 void(*fb_rotate)(struct fb_info *info, int angle); 
 
 44 
 
 45 /* 等待blit空闲 (可选) */ 
 
 46 int(*fb_sync)(struct fb_info *info); 
 
 47 
 
 48 /* fb特定的ioctl (可选) */ 
 
 49 int(*fb_ioctl)(struct fb_info *info, unsigned int cmd, unsigned long arg); 
 
 50 
 
 51 /* 处理32位的compat ioctl (可选) */ 
 
 52 int(*fb_compat_ioctl)(struct fb_info *info, unsigned cmd, unsigned long arg); 
 
 53 
 
 54 /* fb特定的mmap */ 
 
 55 int(*fb_mmap)(struct fb_info *info, struct vm_area_struct *vma); 
 
 56 
 
 57 /* 保存目前的硬件状态 */ 
 
 58 void(*fb_save_state)(struct fb_info *info); 
 
 59 
 
 60 /* 恢复被保存的硬件状态 */ 
 
 61 void(*fb_restore_state)(struct fb_info *info); 
 
 62 
 
 63 void (*fb_get_caps)(struct fb_info *info, struct fb_blit_caps *caps, 
 
 64 struct fb_var_screeninfo *var); 
 
 65 };

fb_ops的fb_check_var()成员函数用于检查可以修改的屏幕参数并调整到合适的值，而fb_set_par()则使得用户设置的屏幕参数在硬件上有效。

#### 3．fb_var_screeninfo和fb_fix_screeninfo结构体

FBI的fb_var_screeninfo和fb_fix_screeninfo成员也是结构体，fb_var_screeninfo记录用户可修改的显示控制器参数，包括屏幕分辨率和每个像素点的比特数。fb_var_screeninfo中的xres定义屏幕一行有多少个点，yres定义屏幕一列有多少个点，bits_per_pixel定义每个点用多少个字节表示。而fb_fix_screeninfo中记录用户不能修改的显示控制器的参数，如屏幕缓冲区的物理地址、长度。当对帧缓冲设备进行映射操作的时候，就是从fb_fix_screeninfo中取得缓冲区物理地址的。上述数据成员都需要在驱动程序中初始化和设置。

fb_var_screeninfo和fb_fix_screeninfo结构体的定义分别如代码清单18.3和代码清单18.4所示。



代码清单18.3 fb_var_screeninfo结构体

1 struct fb_var_screeninfo { 
 
 2 /* 可见解析度 */ 
 
 3 u32 xres; 
 
 4 u32 yres; 
 
 5 /* 虚拟解析度 */ 
 
 6 u32 xres_virtual; 
 
 7 u32 yres_virtual; 
 
 8 /* 虚拟到可见之间的偏移 */ 
 
 9 u32 xoffset; 
 
 10 u32 yoffset; 
 
 11 
 
 12 u32 bits_per_pixel; /* 每像素位数，BPP */ 
 
 13 u32 grayscale; /非0时指灰度 */ 
 
 14 
 
 15 /* fb缓存的R\G\B位域 */ 
 
 16 struct fb_bitfield red; 
 
 17 struct fb_bitfield green; 
 
 18 struct fb_bitfield blue; 
 
 19 struct fb_bitfield transp; /* 透明度 */ 
 
 20 
 
 21 u32 nonstd; /* != 0 非标准像素格式 */ 
 
 22 
 
 23 u32 activate; 
 
 24 
 
 25 u32 height; /*高度 */ 
 
 26 u32 width; /*宽度 */ 
 
 27 
 
 28 u32 accel_flags; /* 看fb_info.flags */ 
 
 29 
 
 30 /* 定时: 除了pixclock本身外，其他的都以像素时钟为单位 */ 
 
 31 u32 pixclock; /* 像素时钟（皮秒） */ 
 
 32 u32 left_margin; /* 行切换：从同步到绘图之间的延迟 */ 
 
 33 u32 right_margin; /* 行切换：从绘图到同步之间的延迟 */ 
 
 34 u32 upper_margin; /* 帧切换：从同步到绘图之间的延迟 */ 
 
 35 u32 lower_margin; /* 帧切换：从绘图到同步之间的延迟 */ 
 
 36 u32 hsync_len; /* 水平同步的长度 */ 
 
 37 u32 vsync_len; /* 垂直同步的长度 */ 
 
 38 u32 sync; 
 
 39 u32 vmode; 
 
 40 u32 rotate; /* 顺时钟旋转的角度 */ 
 
 41 u32 reserved[5]; /* 保留 */ 
 
 42 };

代码清单18.4 fb_fix_screeninfo结构体

1 struct fb_fix_screeninfo { 
 
 2 char id[16]; /* 字符串形式的标识符 */ 
 
 3 unsigned long smem_start; /* fb缓冲内存的开始位置（物理地址） */ 
 
 4 u32 smem_len; /* fb缓冲的长度 */ 
 
 5 u32 type; /* FB_TYPE_* */ 
 
 6 u32 type_aux; /* Interleave */ 
 
 7 u32 visual; /* FB_VISUAL_* */ 
 
 8 u16 xpanstep; /* 如果没有硬件panning ，赋0 */



9 u16 ypanstep; 
 
 10 u16 ywrapstep;/ 
 
 11 u32 line_length; /* 1行的字节数 */ 
 
 12 unsigned long mmio_start; /* 内存映射I/O的开始位置 */ 
 
 13 u32 mmio_len; /* 内存映射I/O的长度 */ 
 
 14 u32 accel; 
 
 15 u16 reserved[3]; /* 保留*/ 
 
 16 };

代码清单18.4中第7行的visual记录屏幕使用的色彩模式，在Linux系统中，支持的色彩模式包括如下几种。

● Monochrome（FB_VISUAL_MONO01、FB_VISUAL_MONO10），每个像素是黑或白。

● Pseudo color（FB_VISUAL_PSEUDOCOLOR、FB_VISUAL_STATIC_PSEUDOCOLOR），即伪彩色，采用索引颜色显示。

● True color（FB_VISUAL_TRUECOLOR），真彩色，分成红、绿、蓝三基色。

● Direct color（FB_VISUAL_DIRECTCOLOR），每个像素颜色也是由红、绿、蓝组成，不过每个颜色值是个索引，需要查表。

● Grayscale displays，灰度显示，红、绿、蓝的值都一样。

#### 4．fb_bitfield结构体

代码清单18.3第16、17、18行分别记录R、G、B的位域，fb_bitfield结构体描述每一像素显示缓冲区的组织方式，包含位域偏移、位域长度和MSB（最高有效位）指示，如代码清单18.5所示。

代码清单18.5 fb_bitfield结构体

1 struct fb_bitfield { 
 
 2 _ _u32 offset; /* 位域偏移 */ 
 
 3 _ _u32 length; /* 位域长度 */ 
 
 4 _ _u32 msb_right; /*!=0: MSB在右边 */ 
 
 5 };

#### 5．fb_cmap结构体

fb_cmap结构体记录设备无关的颜色表信息，用户空间可以通过ioctl()的FBIOGETCMAP 和FBIOPUTCMAP命令读取或设定颜色表。

代码清单18.6 fb_cmap结构体

1 struct fb_cmap { 
 
 2 u32 start; /* 第1个元素入口 */ 
 
 3 u32 len; /* 元素数量 */ 
 
 4 /* R、G、B、透明度*/ 
 
 5 u16 *red; 
 
 6 u16 *green; 
 
 7 u16 *blue; 
 
 8 u16 *transp; 
 
 9 };

代码清单18.7所示为用户空间获取颜色表的例程，若BPP为8位，则颜色表长度为256；若BPP为4位，则颜色表长度为16；否则，颜色表长度为0，这是因为，对于BPP大于等于16的情况，使用颜色表是不划算的。



代码清单18.7 用户空间获取颜色表例程

1 /* 读入颜色表 */ 
 
 2 if ((vinfo.bits_per_pixel == 8) || (vinfo.bits_per_pixel == 4)) { 
 
 3 screencols = (vinfo.bits_per_pixel == 8) ? 256 : 16;/* 颜色表大小 */ 
 
 4 int loopc; 
 
 5 startcmap = new fb_cmap; 
 
 6 startcmap->start = 0; 
 
 7 startcmap->len = screencols; 
 
 8 /* 分配颜色表的内存 */ 
 
 9 startcmap->red = (unsigned short int*)malloc(sizeof(unsigned short int) 
 
 10 *screencols); 
 
 11 startcmap->green = (unsigned short int*)malloc(sizeof(unsigned short int) 
 
 12 *screencols); 
 
 13 startcmap->blue = (unsigned short int*)malloc(sizeof(unsigned short int) 
 
 14 *screencols); 
 
 15 startcmap->transp = (unsigned short int*)malloc(sizeof(unsigned short int) 
 
 16 *screencols); 
 
 17 /* 获取颜色表 */ 
 
 18 ioctl(fd, FBIOGETCMAP, startcmap); 
 
 19 for (loopc = 0; loopc < screencols; loopc++) { 
 
 20 screenclut[loopc] = qRgb(startcmap->red[loopc] >> 8, startcmap 
 
 21 ->green[loopc] >> 8, startcmap->blue[loopc] >> 8); 
 
 22 } 
 
 23 }

对于一个256色（BPP=8）的800×600分辨率的图像而言，若红、绿、蓝分别用一个字节描述，则需要800×600×3=1 440 000Byte的空间，而若使用颜色表，则只需要800×600×1+256×3= 480768Byte的空间。

#### 6．文件操作结构体

作为一种字符设备，帧缓冲设备的文件操作结构体定义于/linux/drivers/vedio/fbmem.c文件中，如代码清单18.8所示。

代码清单18.8 帧缓冲设备文件操作结构体

1 static struct file_operations fb_fops = { 
 
 2 .owner = THIS_MODULE, 
 
 3 .read = fb_read, 
 
 4 .write = fb_write, 
 
 5 .ioctl = fb_ioctl, 
 
 6 #ifdef CONFIG_COMPAT 
 
 7 .compat_ioctl = fb_compat_ioctl, 
 
 8 #endif 
 
 9 .mmap = fb_mmap, 
 
 10 .open = fb_open, 
 
 11 .release = fb_release, 
 
 12 #ifdef HAVE_ARCH_FB_UNMAPPED_AREA 
 
 13 .get_unmapped_area = get_fb_unmapped_area, 
 
 14 #endif 
 
 15 #ifdef CONFIG_FB_DEFERRED_IO 
 
 16 .fsync = fb_deferred_io_fsync, 
 
 17 #endif 
 
 18 };

帧缓冲设备驱动的文件操作接口函数已经在fbmem.c中被统一实现，一般不需要由驱动工程师再编写。

#### 7．注册与注销帧缓冲设备

Linux内核提供了register_framebuffer()和unregister_framebuffer()函数分别注册和注销帧缓冲设备，这两个函数都接受FBI指针为参数，原型为：

int register_framebuffer(struct fb_info *fb_info); 
 
 int unregister_framebuffer(struct fb_info *fb_info);

对于register_framebuffer()函数而言，如果注册的帧缓冲设备数超过了FB_MAX（目前定义为32），则函数返回-ENXIO，注册成功则返回0。

