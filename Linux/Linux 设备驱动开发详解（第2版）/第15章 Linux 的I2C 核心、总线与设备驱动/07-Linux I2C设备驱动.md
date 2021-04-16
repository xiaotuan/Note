### 15.4 Linux I2C设备驱动

I2C设备驱动要使用i2c_driver和i2c_client数据结构并填充i2c_driver中的成员函数。i2c_client一般被包含在设备的私有信息结构体yyy_data中，而i2c_driver则适合被定义为全局变量并初始化，代码清单15.13所示为已被初始化的i2c_driver。

代码清单15.13 已被初始化的i2c_driver

1 static struct i2c_driver yyy_driver = { 
 
 2 .driver = { 
 
 3 .name = "yyy", 
 
 4 } , 
 
 5 .probe = yyy_probe, 
 
 6 .remove = yyy_remove, 
 
 7 .id_table = yyy_id, 
 
 8 };

