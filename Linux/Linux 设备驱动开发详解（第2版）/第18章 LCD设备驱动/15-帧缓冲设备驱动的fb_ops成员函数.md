### 18.7 帧缓冲设备驱动的fb_ops成员函数

FBI中的fp_ops是使得帧缓冲设备工作所需函数的集合，它们最终与LCD控制器硬件打交道。

fb_check_var()用于调整可变参数，并修正为硬件所支持的值；fb_set_par()则根据屏幕参数设置具体读写LCD控制器的寄存器以使得LCD控制器进入相应的工作状态。

对于fb_ops中的fb_fillrect()、fb_copyarea()和fb_imageblit()成员函数，通常直接使用对应的通用的cfb_fillrect()、cfb_copyarea()和 cfb_imageblit()函数即可。cfb_fillrect()函数定义在drivers/video/cfbfillrect.c文件中，cfb_copyarea()定义在drivers/video/cfbcopyarea.c文件中，cfb_imageblit()定义在drivers/video/cfbimgblt.c文件中。

fb_ops中的fb_setcolreg()成员函数实现伪颜色表（针对FB_VISUAL_TRUECOLOR、FB_ VISUAL_DIRECTCOLOR模式）和颜色表的填充，其模板如代码清单18.11所示。

代码清单18.11 fb_setcolreg()函数模板

1 static int xxxfb_setcolreg(unsigned regno, unsigned red, unsigned green, 
 
 2 unsigned blue, unsigned transp, struct fb_info *info) 
 
 3 { 
 
 4 struct xxxfb_info *fbi = info->par; 
 
 5 unsigned int val; 
 
 6 
 
 7 switch (fbi->fb->fix.visual) { 
 
 8 case FB_VISUAL_TRUECOLOR: 
 
 9 /* 真彩色，设置伪颜色表 */ 
 
 10 if (regno < 16) { 
 
 11 u32 *pal = fbi->fb->pseudo_palette; 
 
 12 
 
 13 val = chan_to_field(red, &fbi->fb->var.red); 
 
 14 val |= chan_to_field(green, &fbi->fb->var.green); 
 
 15 val |= chan_to_field(blue, &fbi->fb->var.blue); 
 
 16 
 
 17 pal[regno] = val; 
 
 18 } 
 
 19 break; 
 
 20 
 
 21 case FB_VISUAL_PSEUDOCOLOR: 
 
 22 if (regno < 256) { 
 
 23 /* RGB565模式 */



24 val = ((red >> 0) &0xf800); 
 
 25 val |= ((green >> 5) &0x07e0); 
 
 26 val |= ((blue >> 11) &0x001f); 
 
 27 
 
 28 writel(val, XXX_TFTPAL(regno)); 
 
 29 schedule_palette_update(fbi, regno, val); 
 
 30 } 
 
 31 break; 
 
 32 ... 
 
 33 } 
 
 34 
 
 35 return 0; 
 
 36 }

上述代码第10行对regno < 16的判断意味着伪颜色表只有16个成员，实际上，它们对应16种控制台颜色，logo显示也会使用伪颜色表。

