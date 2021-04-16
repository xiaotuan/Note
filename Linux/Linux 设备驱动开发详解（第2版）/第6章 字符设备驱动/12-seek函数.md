### 6.3.4 seek函数

seek()函数对文件定位的起始地址可以是文件开头（SEEK_SET，0）、当前位置（SEEK_CUR，1）和文件尾（SEEK_END，2），globalmem支持从文件开头和当前位置相对偏移。

在定位的时候，应该检查用户请求的合法性，若不合法，函数返回- EINVAL，合法时返回文件的当前位置，如代码清单6.14。

代码清单6.14 globalmem设备驱动seek()函数

1 static loff_t globalmem_llseek(struct file *filp, loff_t offset, int orig) 
 
 2 { 
 
 3 loff_t ret; 
 
 4 switch (orig) { 
 
 6 case 0: /*从文件开头开始偏移*/ 
 
 7 if (offset < 0) { 
 
 8 ret = - EINVAL; 
 
 9 break; 
 
 10 } 
 
 11 if ((unsigned int)offset > GLOBALMEM_SIZE) { 
 
 12 ret = - EINVAL; 
 
 13 break; 
 
 14 } 
 
 15 filp->f_pos = (unsigned int)offset; 
 
 16 ret = filp->f_pos; 
 
 17 break; 
 
 18 case 1: /*从当前位置开始偏移*/ 
 
 19 if ((filp->f_pos + offset) > GLOBALMEM_SIZE) { 
 
 20 ret = - EINVAL; 
 
 21 break; 
 
 22 } 
 
 23 if ((filp->f_pos + offset) < 0) { 
 
 24 ret = - EINVAL; 
 
 25 break; 
 
 26 } 
 
 27 filp->f_pos += offset; 
 
 28 ret = filp->f_pos; 
 
 29 break; 
 
 30 default: 
 
 31 ret = - EINVAL; 
 
 32 } 
 
 33 return ret; 
 
 34 }



