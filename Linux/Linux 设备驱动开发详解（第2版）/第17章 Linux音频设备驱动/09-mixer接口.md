### 17.3.2 mixer接口

int register_sound_mixer(struct file_operations *fops, int dev);

上述函数用于注册一个混音器，第一个参数fops即是文件操作接口，第二个参数dev是设备编号，如果填入−1，则系统自动分配一个设备编号。mixer是一个典型的字符设备，因此编码的主要工作是实现file_operations中的open()、ioctl()等函数。

mixer接口file_operations中的最重要函数是ioctl()，它实现混音器的不同I/O控制命令，代码清单17.1所示为一个ioctl()的范例。

代码清单17.1 mixer()接口的ioctl()函数范例

1 static int mixdev_ioctl(struct inode *inode, struct file *file, unsigned int cmd,

unsigned long arg) 
 
 2 { 
 
 3 ... 
 
 4 switch (cmd) { 
 
 5 case SOUND_MIXER_READ_MIC: 
 
 6 ... 
 
 7 case SOUND_MIXER_WRITE_MIC: 
 
 8 ... 
 
 9 case SOUND_MIXER_WRITE_RECSRC: 
 
 10 ... 
 
 11 case SOUND_MIXER_WRITE_MUTE: 
 
 12 ... 
 
 13 }



14 /* 其他命令 */ 
 
 15 return mixer_ioctl(codec, cmd, arg); 
 
 16 }

