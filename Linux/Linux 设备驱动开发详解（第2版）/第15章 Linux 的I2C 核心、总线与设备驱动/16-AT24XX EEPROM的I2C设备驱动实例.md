### 15.6 AT24XX EEPROM的I2C设备驱动实例

drivers/i2c/chips/at24.c文件支持大多数I2C接口的EEPROM，正如我们之前所述，一个具体的I2C设备个驱动由两部分组成，一部分是i2c_driver，用于将设备挂接于I2C总线，一类是设备本身的驱动。对于EEPROM而言，设备本身的驱动以bin_attribute二进制sysfs结点形式呈现。代码清单15.26给出了该驱动的框架。

代码清单15.26 AT24XX EEPROM驱动

1 /* bin_attribute部分 */ 
 
 2 
 
 3 static ssize_t at24_bin_read(struct kobject *kobj, struct bin_attribute *attr, 
 
 4 char *buf, loff_t off, size_t count) 
 
 5 { 
 
 6 struct at24_data *at24; 
 
 7 ssize_t retval = 0; 
 
 8 
 
 9 at24 = dev_get_drvdata(container_of(kobj, struct device, kobj)); 
 
 10 
 
 11 ... 
 
 12 
 
 13 while (count) { 
 
 14 ssize_t status; 
 
 15 
 
 
 16 
 status = at24_eeprom_read(at24, buf, off, count); 
 
 17 ... 
 
 18 } 
 
 19 
 
 20 return retval; 
 
 21 } 
 
 22 
 
 23 static ssize_t at24_bin_write(struct kobject *kobj, struct bin_attribute *attr, 
 
 24 char *buf, loff_t off, size_t count) 
 
 25 { 
 
 26 struct at24_data *at24; 
 
 27 ssize_t retval = 0; 
 
 28 
 
 29 at24 = dev_get_drvdata(container_of(kobj, struct device, kobj)); 
 
 30 
 
 31 ... 
 
 32 
 
 33 while (count) { 
 
 34 ssize_t status; 
 
 35 
 
 36 
 status = at24_ 
 eeprom_ 
 write(at24, buf, off, count); 
 
 37 ... 
 
 38 } 
 
 39 
 
 40 ... 
 
 41 } 
 
 42 
 
 43 /* i2c_driver部分 */ 
 
 44 
 
 45 static const struct i2c_device_id at24_ids[] = { 
 
 46 { "24c00", AT24_DEVICE_MAGIC(128 / 8, AT24_FLAG_TAKE8ADDR) }, 
 
 47 { "24c01", AT24_DEVICE_MAGIC(1024 / 8, 0) }, 
 
 48 ...



49 { "at24", 0 }, 
 
 50 { /* END OF LIST */ } 
 
 51 }; 
 
 52 MODULE_DEVICE_TABLE(i2c, at24_ids); 
 
 53 
 
 54 static int at24_probe(struct i2c_client *client, const struct i2c_device_id *id) 
 
 55 { 
 
 56 ... 
 
 57 /* 以sysfs二进制结点的形式呈现eeprom数据 */ 
 
 58 at24->bin.attr.name = "eeprom"; 
 
 59 at24->bin.attr.mode = chip.flags & AT24_FLAG_IRUGO ? S_IRUGO : S_IRUSR; 
 
 60 at24->bin.read = at24_bin_read; 
 
 61 at24->bin.size = chip.byte_len; 
 
 62 ... 
 
 63 at24->bin.write = at24_bin_write; 
 
 64 
 
 65 ... 
 
 
 66 err = sysfs_ 
 create_ 
 bin_ 
 file(&client->dev.kobj, &at24->bin); 
 
 67 if (err) 
 
 68 goto err_clients; 
 
 69 
 
 70 i2c_set_clientdata(client, at24); 
 
 71 
 
 72 ... 
 
 73 } 
 
 74 
 
 75 static int __devexit at24_remove(struct i2c_client *client) 
 
 76 { 
 
 77 struct at24_data *at24; 
 
 78 int i; 
 
 79 
 
 80 at24 = i2c_get_clientdata(client); 
 
 
 81 sysfs_ 
 remove_ 
 bin_ 
 file(&client->dev.kobj, &at24->bin); 
 
 82 
 
 83 for (i = 1; i < at24->num_addresses; i++) 
 
 84 i2c_unregister_device(at24->client[i]); 
 
 85 
 
 86 ... 
 
 87 } 
 
 88 
 
 89 static struct i2c_driver at24_driver = { 
 
 90 .driver = { 
 
 91 .name = "at24", 
 
 92 .owner = THIS_MODULE, 
 
 93 }, 
 
 94 .probe = at24_probe, 
 
 95 .remove = __devexit_p(at24_remove), 
 
 96 .id_table = at24_ids, 
 
 97 }; 
 
 98 
 
 99 static int __init at24_init(void) 
 
 100 { 
 
 101 io_limit = rounddown_pow_of_two(io_limit); 
 
 102 return i2c_add_driver(&at24_driver); 
 
 103 }



104 module_init(at24_init); 
 
 105 
 
 106 static void __exit at24_exit(void) 
 
 107 { 
 
 108 i2c_del_driver(&at24_driver); 
 
 109 } 
 
 110 module_exit(at24_exit);

上述代码中的1～40行对应EEPROM驱动本身的读写实现即bin_attribute驱动，之后的一部分是i2c_driver，两者在i2c_driver的probe()、remove()函数中建立关联。i2c_driver的probe()函数中初始化并通过第66行的sysfs_create_bin_file()注册了二进制sysfs结点，而remove()函数则通过第81行的sysfs_remove_bin_file()注销了sysfs结点。

第16行调用的at24_eeprom_read()和第36行调用的at24_eeprom_write()通过i2c_msg和i2c_ transfer完成实际的数据传输。

drivers/i2c/chips/at24.c不依赖于具体的CPU和I2C控制器硬件特性，因此，如果某一电路板包含该外设，只需要在板文件中添加对应的i2c_board_info，如对于LDD6410在arch/arm/machs3c6410/ mach-ldd6410.c中添加的信息为：

static struct i2c_board_info i2c_devs0[] __initdata = { 
 
 { I2C_BOARD_INFO("24c02", 0x50), }, 
 
 };

此后，我们在LDD6410上透过/sys/class/i2c-adapter/i2c-0/0-0050/eeprom文件结点即可操作连接的EEPROM。

