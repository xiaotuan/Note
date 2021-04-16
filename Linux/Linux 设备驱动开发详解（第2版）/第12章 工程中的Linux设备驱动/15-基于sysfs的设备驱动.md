### 12.6 基于sysfs的设备驱动

一些设备驱动以sysfs结点的形式存在，其本身没有对应的/dev结点；一些设备驱动虽然有对应的/dev结点，也依赖于sysfs结点进行一些工作。

Linux专门提供了一种类型的设备驱动，以结构体sysdev_driver进行描述，该结构体的定义如代码清单12.22所示。

代码清单12.22 sysdev.driver

1 struct sysdev_driver { 
 
 2 struct list_head entry; 
 
 3 int (*add)(struct sys_device *); 
 
 4 int (*remove)(struct sys_device *); 
 
 5 int (*shutdown)(struct sys_device *); 
 
 6 int (*suspend)(struct sys_device *, pm_message_t state); 
 
 7 int (*resume)(struct sys_device *); 
 
 8 };

注册和注销此类驱动的API为：

int sysdev_driver_register(struct sysdev_class *, struct sysdev_driver *); 
 
 void sysdev_driver_unregister(struct sysdev_class *, struct sysdev_driver *);

而此类驱动中通常会通过如下两个API来创建和移除sysfs的结点：

int sysdev_create_file(struct sys_device *, struct sysdev_attribute *); 
 
 void sysdev_remove_file(struct sys_device *, struct sysdev_attribute *);

而sysdev_create_file()最终调用的是sysfs_create_file ()，sysfs_create_file ()的第一个参数为kobject的指针，第二个参数是一个attribute结构体，每个attribute对应着sysfs中的一个文件，而读写一个attribute对应的文件通常需要show()和store()这两个函数，形如：

static ssize_t xxx_show(struct kobject * kobj, struct attribute * attr, char * buffer); 
 
 static ssize_t xxx_store(struct kobject * kobj, struct attribute * attr, 
 
 const char * buffer, size_t count);

典型的，如CPU频率驱动cpufreq（位于drivers/cpufreq）就是一个sysdev_driver形式的驱动，它的主要工作就是提供一些sysfs的结点，包括cpuinfo_cur_freq、cpuinfo_max_freq、cpuinfo_min_freq、scaling_ available_frequencies、scaling_available_governors、scaling_cur_freq、scaling_driver、scaling_governor、scaling_max_freq、scaling_min_freq等。用户空间可以手动cat、echo来操作这些结点或者使用cpufrequtils工具访问这些结点以与内核通信。

还有一类设备虽然不以sysdev_driver的形式存在，但是其本质上只是包含sysfs结点。典型例子包括I2C EEPROM，它以I2C Client驱动的形式存在（后续章节会进行介绍，类似于前文所说的SPI外设驱动），但该驱动drivers/i2c/chips/eeprom.c通过sysfs_create_bin_file()创建二进制sysfs文件，该二进制结点对应的bin_attribute如代码清单12.23所示。

代码清单12.23 EEPROM驱动的bin.attribute实例

1 static struct bin_attribute eeprom_attr = { 
 
 2 .attr = { 
 
 3 .name = "eeprom", 
 
 4 .mode = S_IRUGO, 
 
 5 }, 
 
 6 .size = EEPROM_SIZE, 
 
 7 .read = eeprom_read, 
 
 8 };

之后透过/sys目录里的“eeprom”文件即可访问该EEPROM。创建这个结点的语句是：

sysfs_create_bin_file(&client->dev.kobj, &eeprom_attr);

其中第1个参数是bin_attribute所对应设备的kobject指针，这预示着该“eeprom”在/sys中将位于client->dev这个device的目录之下。

drivers/leds/ leds-gpio.c的基于GPIO的LED驱动也提供了sysfs结点，针对此驱动，在LDD6410的板文件中只需要定义LED对应的GPIO信息并作为leds-gpio这个platform_device的platform_dat即可：

static struct gpio_led ldd6410_leds[] = { 
 
 [0] = { 
 
 .name = "LED1", 
 
 .gpio = S3C64XX_GPM(0), 
 
 }, 
 
 [1] = { 
 
 .name = "LED2", 
 
 .gpio = S3C64XX_GPM(1), 
 
 }, 
 
 [2] = { 
 
 .name = "LED3", 
 
 .gpio = S3C64XX_GPM(2), 
 
 }, 
 
 [3] = { 
 
 .name = "LED4", 
 
 .gpio = S3C64XX_GPM(3), 
 
 }, 
 
 }; 
 
 static struct gpio_led_platform_data ldd6410_gpio_led_pdata = { 
 
 .num_leds = ARRAY_SIZE(ldd6410_leds), 
 
 .leds = ldd6410_leds, 
 
 };



static struct platform_device ldd6410_device_led = { 
 
 .name = "leds-gpio", 
 
 .id = -1, 
 
 .dev = { 
 
 .platform_data = &ldd6410_gpio_led_pdata, 
 
 }, 
 
 };

通过如下命令可以点亮LDD6410右下角的LED1：

# echo 1 > /sys/devices/platform/leds-gpio/leds\:LED1/brightness

熄灭LED1：

# echo 0 > /sys/devices/platform/leds-gpio/leds\:LED1/brightness

