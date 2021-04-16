### 12.7 Linux设备驱动的固件加载

一个外设的运行可能依赖于固件，如一些CSR公司的WiFi模块，在启动前需要加载固件。传统的设备驱动将固件的二进制码作为一个数组直接编译进目标代码，而在Linux 2.6中，有一套成熟的固件加载流程。

首先，申请固件的驱动程序发起如下请求：

int request_firmware(const struct firmware **fw, const char *name, struct device *device);

第1个参数用于保存申请到的固件，第2个参数是固件名，第3个参数是申请固件的设备结构体。

在发起此调用后，内核的udevd会配合将固件通过对应的sysfs结点写入内核（在设置好udev规则的情况下）。之后内核将收到的firmware写入外设，最后通过如下API释放请求：

void release_firmware(const struct firmware *fw);

下面看一个典型的例子drivers/media/video/cx25840/cx25840-firmware.c的cx25840_loadfw()函数，如代码清单12.24所示。

代码清单12.24 Linux设备驱动申请firmware的例子

1 int cx25840_loadfw(struct i2c_client *client) 
 
 2 { 
 
 3 struct cx25840_state *state = i2c_get_clientdata(client); 
 
 4 const struct firmware *fw = NULL; 
 
 5 u8 buffer[FWSEND]; 
 
 6 const u8 *ptr; 
 
 7 int size, retval; 
 
 8 
 
 9 if (state->is_cx23885) 
 
 10 firmware = FWFILE_CX23885; 
 
 11 /* 申请firmware */ 
 
 12 if (request_firmware(&fw, firmware, FWDEV(client)) != 0) { 
 
 13 v4l_err(client, "unable to open firmware %s\n", firmware); 
 
 14 return -EINVAL; 
 
 15 } 
 
 16 /* 开始加载firmware到设备 */ 
 
 17 start_fw_load(client); 
 
 18



19 buffer[0] = 0x08; 
 
 20 buffer[1] = 0x02; 
 
 21 
 
 22 size = fw->size; 
 
 23 ptr = fw->data; 
 
 24 while (size > 0) { 
 
 25 int len = min(FWSEND - 2, size); 
 
 26 
 
 27 memcpy(buffer + 2, ptr, len); 
 
 28 
 
 29 retval = fw_write(client, buffer, len + 2); 
 
 30 
 
 31 if (retval < 0) { 
 
 32 release_firmware(fw); 
 
 33 return retval; 
 
 34 } 
 
 35 
 
 36 size -= len; 
 
 37 ptr += len; 
 
 38 } 
 
 39 
 
 40 end_fw_load(client); 
 
 41 
 
 42 size = fw->size; 
 
 43 /* 释放firmware */ 
 
 44 elease_firmware(fw); 
 
 45 
 
 46 return check_fw_load(client, size); 
 
 47 }

