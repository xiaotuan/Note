### 17.4.2 card和组件管理

对于每个声卡而言，必须创建一个card实例。card是声卡的“总部”，它管理这个声卡上的所有设备（组件），如PCM、mixers、MIDI、synthesizer等。因此，card和组件是ALSA声卡驱动中的主要组成元素。

#### 1．创建card

struct snd_card *snd_card_new(int idx, const char *xid, 
 
 struct module *module, int extra_size);

idx是card索引号，xid是标识字符串，module一般为THIS_MODULE，extra_size是要分配的额外数据的大小，分配的extra_size大小的内存将作为card->private_data。



#### 2．创建组件

int snd_device_new(struct snd_card *card, snd_device_type_t type, 
 
 void *device_data, struct snd_device_ops *ops);

当card被创建后，设备（组件）能够被创建并关联于该card。第1个参数是snd_card_new()创建的card指针，第2个参数type 指的是device-level即设备类型，形式为SNDRV_DEV_XXX，包括SNDRV_DEV_CODEC、SNDRV_DEV_CONTROL、SNDRV_DEV_PCM、SNDRV_DEV_ RAWMIDI等，用户自定义设备的device-level是SNDRV_DEV_LOWLEVEL，ops参数是1个函数集（定义为snd_device_ops结构体）的指针，device_data是设备数据指针，注意函数snd_device_ new()本身不会分配设备数据的内存，因此应事先分配。

#### 3．组件释放

每个ALSA预定义的组件在构造时需调用snd_device_new()，而每个组件的析构方法则在函数集中被包含。对于PCM、AC97此类预定义组件，我们不需关心它们的析构，而对于自定义的组件，则需要填充snd_device_ops中的析构函数指针dev_free，这样，当snd_card_free()被调用时，组件将自动被释放。

#### 4．芯片特定的数据（Chip-Specific Data）

芯片特定的数据一般以struct xxxchip结构体形式组织，这个结构体中包含芯片相关的I/O端口地址、资源指针、中断号等，其意义等同于字符设备驱动中的file->private_data。

定义芯片特定的数据主要有两种方法，一种方法是将sizeof(struct xxxchip)传入snd_card_new()作为extra_size参数，它将自动成为snd_card的private_data成员，如代码清单17.5所示；另一种方法是在snd_card_new()传入给extra_size参数0，再分配sizeof(struct xxxchip)的内存，将分配内存的地址传入snd_device_new()的device_data的参数，如代码清单17.6所示。

代码清单17.5 创建芯片特定的数据方法1

1 struct xxxchip {/* 芯片特定的数据结构体 */ 
 
 2 ... 
 
 3 }; 
 
 4 card = snd_card_new(index, id, THIS_MODULE, sizeof(struct 
 
 5 xxxchip)); /* 创建声卡并申请xxxchip内存作为card-> private_data */ 
 
 6 struct xxxchip *chip = card->private_data;

代码清单17.6 创建芯片特定的数据方法2

1 struct snd_card *card; 
 
 2 struct xxxchip *chip; 
 
 3 /* 使用0作为第4个参数，并动态分配xxx_chip的内存*/ 
 
 4 card = snd_card__new(index[dev], id[dev], THIS_MODULE, 0); 
 
 5 ... 
 
 6 chip = kzalloc(sizeof(*chip), GFP_KERNEL); 
 
 7 /* 在xxxchip结构体中，应该包括声卡指针*/ 
 
 8 struct xxxchip { 
 
 9 struct snd_card *card; 
 
 10 ... 
 
 11 }; 
 
 12 /* 并将其card成员赋值为snd_card_new()创建的card指针*/ 
 
 13 chip->card = card; 
 
 14 static struct snd_device_ops ops = { 
 
 15 . dev_free = snd_xxx_chip_dev_free, /* 组件析构*/



16 }; 
 
 17 ... 
 
 18 /* 创建自定义组件*/ 
 
 19 snd_device_new(card, SNDRV_DEV_LOWLEVEL, chip, &ops); 
 
 20 /* 在析构函数中释放xxxchip内存*/ 
 
 21 static int snd_xxx_chip_dev_free(struct snd_device *device) 
 
 22 { 
 
 23 return snd_xxx_chip_free(device->device_data); /* 释放*/ 
 
 24 }

#### 5．注册/释放声卡

当snd_card被准备好以后，可使用snd_card_register()函数注册这个声卡，如下所示：

int snd_card_register(struct snd_card *card)

对应的snd_card_free()完成相反的功能，如下所示：

int snd_card_free(struct snd_card *card);

