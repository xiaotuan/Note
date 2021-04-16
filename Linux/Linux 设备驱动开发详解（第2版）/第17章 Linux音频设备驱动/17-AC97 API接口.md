### 17.4.5 AC97 API接口

ALSA AC97编解码层被很好地定义，利用它，驱动工程师只需编写少量底层的控制函数。



#### 1．AC97实例构造

为了创建一个AC97实例，首先需要调用snd_ac97_bus()函数构建AC97总线及其操作，这个函数的原型为：

int snd_ac97_bus(struct snd_card *card, int num, struct snd_ac97_bus_ops *ops, 
 
 void *private_data, struct snd_ac97_bus **rbus);

该函数的第3个参数ops是一个snd_ac97_bus_ops结构体，其定义如代码清单17.23所示。

代码清单17.23 snd_ac97_bus_ops结构体

1 struct snd_ac97_bus_ops { 
 
 2 void(*reset)(struct snd_ac97 *ac97); /* 复位函数*/ 
 
 3 /* 写入函数*/ 
 
 4 void(*write)(struct snd_ac97 *ac97, unsigned short reg, unsigned short val); 
 
 5 /* 读取函数*/ 
 
 6 unsigned short(*read)(struct snd_ac97 *ac97, unsigned short reg); 
 
 7 void(*wait)(struct snd_ac97 *ac97); 
 
 8 void(*init)(struct snd_ac97 *ac97); 
 
 9 };

接下来，调用snd_ac97_mixer()函数注册混音器，这个函数的原型为：

int snd_ac97_mixer(struct snd_ac97_bus *bus, struct snd_ac97_template *template, struct 
 
 snd_ac97 **rac97);

代码清单17.24所示为AC97实例的创建过程。

代码清单17.24 AC97实例的创建过程范例

1 struct snd_ac97_bus *bus; 
 
 2 /* AC97总线操作*/ 
 
 3 static struct snd_ac97_bus_ops ops = { 
 
 4 .write = snd_mychip_ac97_write, 
 
 5 .read = snd_mychip_ac97_read, 
 
 6 }; 
 
 7 /* AC97总线与操作创建*/ 
 
 8 snd_ac97_bus(card, 0, &ops, NULL, &bus); 
 
 9 /* AC97模板*/ 
 
 10 struct snd_ac97_template ac97; 
 
 11 int err; 
 
 12 memset(&ac97, 0, sizeof(ac97)); 
 
 13 ac97.private_data = chip;/* 私有数据*/ 
 
 14 /* 注册混音器*/ 
 
 15 snd_ac97_mixer(bus, &ac97, &chip->ac97);

上述代码第一行的snd_ac97_bus结构体指针bus的指针被传入第8行的snd_ac97_bus()函数并被赋值，chip->ac97的指针被传入第15行的snd_ac97_mixer()并被赋值，chip->ac97将成员新创建AC97实例的指针。

如果一个声卡上包含多个编解码器，这种情况下，需要多次调用snd_ac97_mixer()并对snd_ac97的num成员（编解码器序号）赋予相应的序号。驱动中可以为不同的编解码器编写不同的snd_ac97_bus_ops成员函数中，或者只是在相同的一套成员函数中通过ac97.num获得序号后再区分进行具体的操作。

#### 2．snd_ac97_bus_ops成员函数

snd_ac97_bus_ops结构体中的read()和write()成员函数完成底层的硬件访问，reset()函数用于复位编解码器，wait()函数用于编解码器标准初始化过程中的特定等待，如果芯片要求额外的等待时间，则应实现这个函数，init()用于完成编解码器附加的初始化。代码清单17.25所示为read()和write()函数的范例。

代码清单17.25 snd_ac97_bus_ops结构体中的read()和write()函数范例

1 static unsigned short snd_xxxchip_ac97_read(struct snd_ac97 *ac97, unsigned 
 
 2 short reg) 
 
 3 { 
 
 4 struct xxxchip *chip = ac97->private_data; 
 
 5 ... 
 
 6 return the_register_value; /* 返回寄存器值*/ 
 
 7 } 
 
 8 
 
 9 static void snd_xxxchip_ac97_write(struct snd_ac97 *ac97, unsigned short reg, 
 
 10 unsigned short val) 
 
 11 { 
 
 12 struct xxxchip *chip = ac97->private_data; 
 
 13 ... 
 
 14 /* 将被给的寄存器值写入codec 
 
 15 }

#### 3．修改寄存器

如果需要在驱动中访问编解码器，可使用如下函数：

void snd_ac97_write(struct snd_ac97 *ac97, unsigned short reg, unsigned short value); 
 
 int snd_ac97_update(struct snd_ac97 *ac97, unsigned short reg, unsigned short value); 
 
 int snd_ac97_update_bits(struct snd_ac97 *ac97, unsigned short reg, unsigned short mask, 
 
 unsigned short value); 
 
 unsigned short snd_ac97_read(struct snd_ac97 *ac97, unsigned short reg);

snd_ac97_update()与void snd_ac97_write()的区别在于前者在值已经设置的情况下不会再设置，而后者则会再写一次。snd_ac97_update_bits()用于更新寄存器的某些位，由mask决定。

除此之外，还有一个函数可用于设置采样率：

int snd_ac97_set_rate(struct snd_ac97 *ac97, int reg, unsigned int rate);

这个函数的第二个参数reg可以是AC97_PCM_MIC_ADC_RATE、AC97_PCM_FRONT_DAC_ RATE、AC97_PCM_LR_ADC_RATE和AC97_SPDIF，对于AC97 _SPDIF而言，寄存器并非真地被改变了，只是相应的IEC958状态位将被更新。

#### 4．时钟调整

在一些芯片上，编解码器的时钟频率不是48000Hz，而是使用PCI时钟以节省一个晶振，在这种情况下，我们应该改变bus->clock为相应的值，例如intel8x0和es1968包含时钟的自动测量函数。

#### 5．proc文件

ALSA AC97接口会创建如/proc/asound/card0/codec97#0/ac97#0-0和ac97#0-0+regs这样的proc文件，通过这些文件可以查看编解码器目前的状态和寄存器。

如果一个芯片上有多个codecs，可多次调用snd_ac97_mixer()。

