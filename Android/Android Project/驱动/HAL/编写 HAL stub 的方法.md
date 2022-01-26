编写 HAL stub 的基本流程如下：

1. 自定义 HAL 结构体，编写头文件 led.h 和 hardware/hardware.h：

   ```c
   struct led_module_t {
       struct hw_module_t common;
   };
   
   struct led_control_device_t {
       struct hw_device_t common;
       int fd;	/* LED 设备文件标码 */
       /* 支持的控制 APIs 来到这里 */
       int (*set_on)(struct led_control_device_t *dev, int32_t, led);
   };
   ```

2. 编写文件 led.c 实现 HAL stub 注册功能

3. 设置 led_module_methods 继承于 hw_module_methods_t，并实现对 `open()` 方法的回调。

   ```c
   struct hw_module_methods_t led_module_methods = {
       open: led_device_open
   };
   ```

4. 使用 HAL_MODULE_INFO_SYM 实例化 led_module_t，注意这个名称不可以修改。

   ```c
   const struct led_module_t HAL_MODULE_INFO_SYM = {
       common: {
           tag: HARDWARE_MODULE_TAG,
           version_major: 1,
           version_minor: 0,
           id: LED_HARDWARE_MODULE_ID,
           name: "Sample LED Stub",
           author: "The Mokoid Open Source Project",
           methods: &led_module_methods,
       }
   };
   ```

   + **tag：**表示需要指定为 HARDWARE_MODULE_TAG.
   + **id：**表示指定为 HAL Stub 的 module ID。
   + **methods：**为 HAL 所定义的方法。

5. `open()` 是一个必须实现的回调 API，用于负责申请结构体空间并填充信息，并且可以注册具体操作 API 接口，打开 Linux 驱动。但是因为存在多重继承关系，所以只需对子结构体 `hw_device_t` 对象申请空间即可。

   ```c
   int led_device_open(const struct hw_module_t* module, const char* name, struct hw_device_t** device) 
   {
       struct led_control_device_t *dev;
       dev = (struct led_control_device_t *)malloc(sizeof(*dev));
       memset(dev, 0, sizeof(*dev));
       dev->common.tag = HARDWARE_DEVICE_TAG;
       dev->common.version = 0;
       dev->common.module = module;
       dev->common.close = led_device_close;
       dev->set_on = led_on;
       dev-->set_off = led_off;
       *device = $dev->common;
       /*
        * 初始化 Led 硬件
        */
       dev->fd = open(LED_DEVICE, O_RDONLY);
       if (dev->fd < 0) {
           return -1;
       }
       led_off(dev, LED_C608);
       led_off(dev, LED_C609);
   success:
       return 0;
   }
   ```

6. 填充具体 API 操作

   ```c
   int led_on(struct led_control_device_t *dev, int32_t led) 
   {
       int fd;
       LOGI("LED Stub: set %d on.", led);
       fd = dev->fd;
       switch (led) {
           case LED_C608:
               ioctl(fd, 1, $led);
               break;
           case LED_C609:
               ioctl(fd, 1, &led);
               break;
           default:
               return -1;
       }
       return 0;
   }
   
   int led_off(struct led_control_device_t *dev, int32_t led) 
   {
       int fd;
       LOGI("LED Stub: set %d on.", led);
       fd = dev->fd;
       switch (led) {
           case LED_C608:
               ioctl(fd, 2, &led);
               break;
           case LED_C609:
               ioctl(fd, 2, &led);
               break;
           default:
               return -1;
       }
       return 0;
   }
   ```

   

