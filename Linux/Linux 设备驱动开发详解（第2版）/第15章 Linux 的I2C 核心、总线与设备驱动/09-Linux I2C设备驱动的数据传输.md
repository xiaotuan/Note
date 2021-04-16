### 15.4.2 Linux I2C设备驱动的数据传输

在I2C设备上读写数据的时序和数据通常通过i2c_msg数组组织，最后通过i2c_transfer()函数完成，代码清单15.15所示为一个读取指定偏移offs寄存器的例子。

代码清单15.14 I2C设备驱动数据传输范例

1 struct i2c_msg msg[2]; 
 
 2 /*第一条消息是写消息*/ 
 
 3 msg[0].addr = client->addr; 
 
 4 msg[0].flags = 0;



5 msg[0].len = 1; 
 
 6 msg[0].buf = &offs; 
 
 7 /*第二条消息是读消息*/ 
 
 8 msg[1].addr = client->addr; 
 
 9 msg[1].flags = I2C_M_RD; 
 
 10 msg[1].len = sizeof(buf); 
 
 11 msg[1].buf = &buf[0]; 
 
 12 
 
 13 i2c_transfer(client->adapter, msg, 2);

