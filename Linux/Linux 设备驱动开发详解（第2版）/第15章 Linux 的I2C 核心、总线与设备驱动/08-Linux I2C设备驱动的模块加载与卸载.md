### 15.4.1 Linux I2C设备驱动的模块加载与卸载

I2C设备驱动的模块加载函数通用的方法是在I2C设备驱动的模块加载函数进行通过I2C核心的i2c_add_driver()函数添加i2c_driver的工作，而在模块卸载函数中需要做相反的工作：通过I2C核心的i2c_del_driver()函数删除i2c_driver。代码清单15.14所示为I2C设备驱动的加载工作与卸载函数模板。

1 static int __init yyy_init(void) 
 
 2 { 
 
 2 rern i2c_add_driver(&yyy_driver); 
 
 3 }; 
 
 4 void __exit yyy_exit(void) 
 
 5 { 
 
 6 i2c_del_driver(&yyy_driver); 
 
 7 };

