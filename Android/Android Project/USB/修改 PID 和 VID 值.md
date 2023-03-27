[toc]

### 1. MTK

#### 1.1 MT8766

##### 1.1.1 Android S

1. 修改 `device/mediatek/mt6771/init.mt6771.usb.rc` 文件如下代码：

   1. 修改 VID 的值（ `vendor.usb.vid` 的值）：

      ```diff
      @@ -2,7 +2,7 @@ on early-init
           write /sys/module/musb_hdrc/parameters/kernel_init_done 1
       
       on post-fs
      -    setprop vendor.usb.vid "0x0E8D"
      +    setprop vendor.usb.vid "0x0502"
           mkdir /dev/usb-ffs 0770 shell shell
           mkdir /dev/usb-ffs/adb 0770 shell shell
           mkdir /config/usb_gadget/g1 0770 shell shell
      ```

   2. 修改 mtp 的 PID 值：

      ```diff
      @@ -168,7 +168,7 @@ property:vendor.usb.acm_enable=0 && property:sys.usb.configfs=1
       ### main function : mtp ###
       on property:sys.usb.config=mtp && property:vendor.usb.acm_cnt=0 && \
       property:sys.usb.configfs=1
      -    setprop vendor.usb.pid 0x2008
      +    setprop vendor.usb.pid 0x4041
       on property:sys.usb.config=mtp && property:vendor.usb.acm_cnt=1 && \
       property:sys.usb.configfs=1
           setprop vendor.usb.pid 0x2012
      ```

   3. 修改 mtp,adb 的 PID 值：

      ```diff
      @@ -201,7 +201,7 @@ property:sys.usb.configfs=1
       ### start adbd at init.usb.configfs.rc ###
       on property:sys.usb.config=mtp,adb && property:vendor.usb.acm_cnt=0 && \
       property:sys.usb.configfs=1
      -    setprop vendor.usb.pid 0x201D
      +    setprop vendor.usb.pid 0x4042
       on property:sys.usb.config=mtp,adb && property:vendor.usb.acm_cnt=1 && \
       property:sys.usb.configfs=1
           setprop vendor.usb.pid 0x200A
      ```

   4. 修改 ptp 的 PID 值

      ```diff
      @@ -236,7 +236,7 @@ property:vendor.usb.acm_enable=0 && property:sys.usb.configfs=1
       ### main function : ptp ###
       on property:sys.usb.config=ptp && property:vendor.usb.acm_cnt=0 && \
       property:sys.usb.configfs=1
      -    setprop vendor.usb.pid 0x200B
      +    setprop vendor.usb.pid 0x4043
       on property:sys.usb.config=ptp && property:vendor.usb.acm_cnt=1 && \
       property:sys.usb.configfs=1
           setprop vendor.usb.pid 0x2013
      ```

   5. 修改 ptp,adb 的 PID 值

      ```diff
      @@ -267,7 +267,7 @@ property:sys.usb.configfs=1
       ### start adbd at init.usb.configfs.rc ###
       on property:sys.usb.config=ptp,adb && property:vendor.usb.acm_cnt=0 && \
       property:sys.usb.configfs=1
      -    setprop vendor.usb.pid 0x200C
      +    setprop vendor.usb.pid 0x4044
       on property:sys.usb.config=ptp,adb && property:vendor.usb.acm_cnt=1 && \
       property:sys.usb.configfs=1
           setprop vendor.usb.pid 0x200D
      ```

   6. 修改 rndis 的 PID 值

      ```diff
      @@ -300,7 +300,7 @@ property:vendor.usb.acm_enable=0 && property:sys.usb.configfs=1
       ### main function : rndis ###
       on property:sys.usb.config=rndis && property:vendor.usb.acm_cnt=0 && \
       property:sys.usb.configfs=1
      -    setprop vendor.usb.pid 0x2004
      +    setprop vendor.usb.pid 0x4045
       on property:sys.usb.config=rndis && property:vendor.usb.acm_cnt=1 && \
       property:sys.usb.configfs=1
           setprop vendor.usb.pid 0x2011
      ```

   7. 修改 rndis,adb 的 PID 值

      ```diff
      @@ -332,7 +332,7 @@ property:sys.usb.configfs=1
       
       on property:sys.usb.config=rndis,adb && property:vendor.usb.acm_cnt=0 && \
       property:sys.usb.configfs=1
      -    setprop vendor.usb.pid 0x2005
      +    setprop vendor.usb.pid 0x4046
       on property:sys.usb.config=rndis,adb && property:vendor.usb.acm_cnt=1 && \
       property:sys.usb.configfs=1
           setprop vendor.usb.pid 0x2010
      ```

2. 修改 fastboot 的 VID 和 PID，是通过修改 `vendor/mediatek/proprietary/bootable/bootloader/lk/target/tb8788p1_64_bsp_k419/include/target/cust_usb.h` 文件如下代码：

   ```diff
   @@ -3,10 +3,10 @@
    
    #define CONFIG_USBD_LANG       "0409"
    
   -#define USB_VENDORID           (0x0E8D)
   -#define USB_PRODUCTID          (0x201C)
   +#define USB_VENDORID           (0x0502)
   +#define USB_PRODUCTID          (0x4047)
    #define USB_VERSIONID          (0x0100)
   -#define USB_MANUFACTURER       "MediaTek"
   +#define USB_MANUFACTURER       "Acer"
    #define USB_PRODUCT_NAME       "Android"
    #define FASTBOOT_DEVNAME       "mt6752_device"
    #define SN_BUF_LEN             64
   ```

   