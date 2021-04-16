### 17.5.4 ASoC板驱动

ASoC板驱动直接与板对应，对于一块确定的电路板，其SoC和Codec都是确定的，因此板驱动将ASoC Codec驱动和CPU端的平台驱动进行绑定，这个绑定用数据结构snd_soc_dai_link描述，其定义如代码清单17.33所示。

代码清单17.33 snd_soc_dai_link结构体

1 struct snd_soc_dai_link { 
 
 2 char *name; /* Codec name */ 
 
 3 char *stream_name; /* Stream name */ 
 
 4 
 
 5 /* DAI */ 
 
 6 struct snd_soc_dai *codec_dai; 
 
 7 struct snd_soc_dai *cpu_dai; 
 
 8 
 
 9 /* 板流操作 */ 
 
 10 struct snd_soc_ops *ops; 
 
 11 
 
 12 /* codec/machine特定的初始化 */ 
 
 13 int (*init)(struct snd_soc_codec *codec); 
 
 14 
 
 15 /* DAI pcm */ 
 
 16 struct snd_pcm *pcm; 
 
 17};

除此之外，板驱动还关心一些板特定的硬件操作，因此也存在一个snd_soc_ops的实例。

在板驱动的模块初始化函数中，会通过platform_device_add()注册一个名为“soc-audio”的platform设备，这是因为soc-core.c注册了一个名为“soc-audio”的platform驱动，因此，在板驱动中注册“soc-audio”设备会引起两者的匹配，从而引发一系列的初始化操作。尤其值得一提的是，“soc-audio”设备的私有数据需要为一个snd_soc_device的结构体实体，因此一个板驱动典型的模块加载函数将形如代码清单17.34。

代码清单17.34 ASoC板驱动模块加载函数及其访问的数据结构

1 static struct snd_soc_dai_link cpux_codecy_dai = { 
 
 2 .name = "codecy", 
 
 3 .stream_name = "CODECY", 
 
 4 .cpu_dai = &cpux_i2s_dai, 
 
 5 .codec_dai = &codecy_dai, 
 
 6 .ops = &cpux_codecy_ops, 
 
 7 }; 
 
 8



9 static struct snd_soc_machine cpux_codecy = { 
 
 10 .name = "cpux_codecy", 
 
 11 .probe = cpux_probe, 
 
 12 .dai_link = &cpux_codecy_dai, 
 
 13 .num_links = 1, 
 
 14 }; 
 
 15 
 
 16 static struct snd_soc_device cpux_codecy_snd_devdata = { 
 
 17 .machine = &cpux_codecy, 
 
 18 .platform = &cpux_i2s_soc_platform, 
 
 19 .codec_dev = &soc_codec_dev_codecy, 
 
 20 }; 
 
 21 
 
 22 static struct platform_device *cpux_codecy_snd_device; 
 
 23 
 
 24 static int __init cpux_codecy_init(void) 
 
 25 { 
 
 26 int ret; 
 
 27 
 
 28 cpux_codecy_snd_device = platform_device_alloc("soc-audio", -1); 
 
 29 if (!cpux_codecy_snd_device) 
 
 30 return -ENOMEM; 
 
 31 
 
 32 platform_set_drvdata(cpux_codecy_snd_device, &cpux_codecy_snd_devdata); 
 
 33 cpux_codecy_snd_devdata.dev = &cpux_codecy_snd_device->dev; 
 
 34 ret = platform_device_add(cpux_codecy_snd_device); 
 
 35 
 
 36 if (ret) 
 
 37 platform_device_put(cpux_codecy_snd_device); 
 
 38 
 
 39 return ret; 
 
 40 } 
 
 41 module_init(cpux_codecy_init);

上述代码中访问的snd_soc_device是对一个ASoC设备的整体封装，因此其中包括了封装板用的snd_soc_machine（machine成员）、封装ASoC Codec设备用的snd_soc_codec_device（codec_dev成员），封装ASoC平台设备用的snd_soc_platform（platform成员）。

ASoC驱动的Codec、平台和板驱动是3个独立的内核模块，在板驱动中，对ASoC Codec设备、ASoC平台设备实例的访问都通过被ASoC Codec驱动或ASoC平台驱动导出的全局变量执行，这使得ASoC难以同时支持两个以上的Codec。至本书截稿时，ASoC的其中一个维护者Liam Girdwood（lrg@slimlogic.co.uk）正在添加ASoC对多Codec的支持。

