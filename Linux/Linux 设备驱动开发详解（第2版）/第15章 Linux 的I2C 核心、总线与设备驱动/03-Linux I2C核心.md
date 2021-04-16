### 15.2 Linux I2C核心

I2C核心（drivers/i2c/i2c-core.c）中提供了一组不依赖于硬件平台的接口函数，这个文件一般不需要被工程师修改，但是理解其中的主要函数非常关键，因为I2C总线驱动和设备驱动之间依赖于I2C核心作为纽带。I2C核心中的主要函数如下。

（1）增加/删除i2c_adapter。

int i2c_add_adapter(struct i2c_adapter *adap); 
 
 int i2c_del_adapter(struct i2c_adapter *adap);

（2）增加/删除i2c_driver。

int i2c_register_driver(struct module *owner, struct i2c_driver *driver); 
 
 int i2c_del_driver(struct i2c_driver *driver); 
 
 inline int i2c_add_driver(struct i2c_driver *driver);

（3）i2c_client依附/脱离。

int i2c_attach_client(struct i2c_client *client); 
 
 int i2c_detach_client(struct i2c_client *client);

当一个具体的client被侦测到并被关联的时候，设备和sysfs文件将被注册。相反地，在client被取消关联的时候，sysfs文件和设备也被注销，如代码清单15.6所示。

代码清单15.6 I2C核心的client attach/detach函数

1 int i2c_attach_client(struct i2c_client *client) 
 
 2 { 
 
 3 ... 
 
 4 device_register(&client->dev); 
 
 5 ... 
 
 6 } 
 
 7 
 
 8 int i2c_detach_client(struct i2c_client *client) 
 
 9 { 
 
 10 ... 
 
 11 device_unregister(&client->dev); 
 
 12 ... 
 
 13 }

（4）I2C传输、发送和接收。

int i2c_transfer(struct i2c_adapter * adap, struct i2c_msg *msgs, int num); 
 
 int i2c_master_send(struct i2c_client *client,const char *buf ,int count); 
 
 int i2c_master_recv(struct i2c_client *client, char *buf ,int count);

i2c_transfer()函数用于进行I2C适配器和I2C设备之间的一组消息交互，i2c_master_send()函数和i2c_master_recv()函数内部会调用i2c_transfer()函数分别完成一条写消息和一条读消息，如代码清单15.7、代码清单15.8所示。

代码清单15.7 I2C核心的i2c_master_send函数

1 int i2c_master_send(struct i2c_client *client,const char *buf ,int count) 
 
 2 { 
 
 3 int ret; 
 
 4 struct i2c_adapter *adap=client->adapter; 
 
 5 struct i2c_msg msg; 
 
 6 /*构造一个写消息*/ 
 
 7 msg.addr = client->addr; 
 
 8 msg.flags = client->flags & I2C_M_TEN; 
 
 9 msg.len = count; 
 
 10 msg.buf = (char *)buf; 
 
 11 /*传输消息*/ 
 
 12 ret = i2c_transfer(adap, &msg, 1);



13 
 
 14 rern (ret == 1) ? count : ret; 
 
 15 }

代码清单15.8 I2C核心的i2c_master_recv函数

1 int i2c_master_recv(struct i2c_client *client, char *buf ,int count) 
 
 2 { 
 
 3 struct i2c_adapter *adap=client->adapter; 
 
 4 struct i2c_msg msg; 
 
 5 int ret; 
 
 6 /*构造一个读消息*/ 
 
 7 msg.addr = client->addr; 
 
 8 msg.flags = client->flags & I2C_M_TEN; 
 
 9 msg.flags |= I2C_M_RD; 
 
 10 msg.len = count; 
 
 11 msg.buf = buf; 
 
 12 /*传输消息*/ 
 
 13 ret = i2c_transfer(adap, &msg, 1); 
 
 14 
 
 15 /* 成功（1条消息被处理）， 返回读的字节数 */ 
 
 16 rern (ret == 1) ? count : ret; 
 
 17 }

i2c_transfer()函数本身不具备驱动适配器物理硬件完成消息交互的能力，它只是寻找到i2c_adapter对应的i2c_algorithm，并使用i2c_algorithm的master_xfer()函数真正驱动硬件流程，如代码清单15.9所示。

代码清单15.9 I2C核心的i2c_transfer函数

1 int i2c_transfer(struct i2c_adapter * adap, struct i2c_msg *msgs, int num) 
 
 2 { 
 
 3 int ret; 
 
 4 
 
 5 if (adap->algo->master_xfer) { 
 
 6 ... 
 
 7 ret = adap->algo->master_xfer(adap,msgs,num); /* 消息传输 */ 
 
 8 ... 
 
 9 return ret; 
 
 10 } else { 
 
 11 dev_dbg(&adap->dev, "I2C level transfers not supported\n"); 
 
 12 return -ENOSYS; 
 
 13 } 
 
 14 }

