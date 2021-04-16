### 14.8.3 S3C6410串口console驱动

在使能内核配置选项CONFIG_SERIAL_SAMSUNG_CONSOLE的情况下，S3C6410串口驱动的console部分会被包含，它位于drivers/serial/samsung.c，如代码清单16.27所示。

代码清单16.27 S3C6410串口console驱动

1 static struct console s3c24xx_serial_console = { 
 
 2 .name = S3C24XX_SERIAL_NAME, 
 
 3 .device = uart_console_device, 
 
 4 .flags = CON_PRINTBUFFER, 
 
 5 .index = -1, 
 
 6 .write = s3c24xx_serial_console_write, 
 
 7 .setup = s3c24xx_serial_console_setup 
 
 8 }; 
 
 9 
 
 10 int s3c24xx_serial_initconsole(struct platform_driver *drv, 
 
 11 struct s3c24xx_uart_info *info) 
 
 12 
 
 13 { 
 
 14 struct platform_device *dev = s3c24xx_uart_devs[0]; 
 
 15 
 
 24 ... 
 
 25 if (strcmp(dev->name, drv->driver.name) != 0) 
 
 26 return 0; 
 
 27 
 
 28 s3c24xx_serial_console.data = &s3c24xx_uart_drv;



29 s3c24xx_serial_init_ports(info); 
 
 30 
 
 31 register_console(&s3c24xx_serial_console); 
 
 32 return 0; 
 
 33 }

而在drivers/serial/samsung.h文件中，通过如下方法将s3c24xx_serial_initconsole放入了.con_initcall.init代码段。这样console_init()即会调用该函数。

