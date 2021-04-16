### 17.5.3 ASoC平台驱动

首先，在ASoC平台驱动部分，同样存在着Codec驱动中的snd_soc_dai、snd_soc_dai_ops、snd_soc_ops这3个结构体的实例用于描述DAI和DAI上的操作，不过不同的是，在平台驱动中，它们只描述CPU相关的部分而不描述Codec。除此之外，在ASoC平台驱动中，必须实现完整的DMA驱动，即传统ALSA的snd_pcm_ops结构体成员函数trigger()、pointer()等。因此ASoC平台驱动通常由DAI和DMA两部分组成，如代码清单17.32所示。

代码清单17.32 ASoC平台驱动的组成

1 /* DAI部分 */ 
 
 2 static int xxx_i2s_set_dai_fmt(struct snd_soc_dai *cpu_dai, 
 
 3 unsigned int fmt) 
 
 4 { 
 
 5 ... 
 
 6 } 
 
 7 
 
 8 static int xxx_i2s_startup(struct snd_pcm_substream *substream) 
 
 9 { 
 
 10 ... 
 
 11 } 
 
 12 
 
 13 static int xxx_i2s_hw_params(struct snd_pcm_substream *substream, 
 
 14 struct snd_pcm_hw_params *params) 
 
 15 { 
 
 16 ... 
 
 17 } 
 
 18



19 static void xxx_i2s_shutdown(struct snd_pcm_substream *substream) 
 
 20 { 
 
 21 ... 
 
 22 } 
 
 23 
 
 24 static int xxx_i2s_probe(struct platform_device *pdev, 
 
 25 struct snd_soc_dai *dai) 
 
 26 { 
 
 27 ... 
 
 28 } 
 
 29 
 
 30 static void xxx_i2s_remove(struct platform_device *pdev, 
 
 31 struct snd_soc_dai *dai) 
 
 32 { 
 
 33 ... 
 
 34 } 
 
 35 
 
 36 static int xxx_i2s_suspend(struct platform_device *dev, 
 
 37 struct snd_soc_dai *dai) 
 
 38 { 
 
 39 ... 
 
 40 } 
 
 41 
 
 42 static int xxx_i2s_resume(struct platform_device *pdev, 
 
 43 struct snd_soc_dai *dai) 
 
 44 { 
 
 45 ... 
 
 46 } 
 
 47 
 
 48 struct snd_soc_dai xxx_i2s_dai = { 
 
 49 .name = "xxx-i2s", 
 
 50 .id = 0, 
 
 51 .type = SND_SOC_DAI_I2S, 
 
 52 .probe = xxx_i2s_probe, 
 
 53 .remove = xxx_i2s_remove, 
 
 54 .suspend = xxx_i2s_suspend, 
 
 55 .resume = xxx_i2s_resume, 
 
 56 .playback = { 
 
 57 .channels_min = 1, 
 
 58 .channels_max = 2, 
 
 59 .rates = XXX_I2S_RATES, 
 
 60 .formats = XXX_I2S_FORMATS,}, 
 
 61 .capture = { 
 
 62 .channels_min = 1, 
 
 63 .channels_max = 2, 
 
 64 .rates = XXX_I2S_RATES, 
 
 65 .formats = XXX_I2S_FORMATS,}, 
 
 66 .ops = { 
 
 67 .startup = xxx_i2s_startup, 
 
 68 .shutdown = xxx_i2s_shutdown, 
 
 69 .hw_params = xxx_i2s_hw_params,}, 
 
 70 .dai_ops = { 
 
 71 .set_fmt = xxx_i2s_set_dai_fmt, 
 
 72 }, 
 
 73 };



74 
 
 75 /* DMA部分 */ 
 
 76 static void bf5xx_dma_irq(void *data) 
 
 77 { 
 
 78 struct snd_pcm_substream *pcm = data; 
 
 79 snd_pcm_period_elapsed(pcm); 
 
 80 } 
 
 81 
 
 82 static const struct snd_pcm_hardware xxx_pcm_hardware = { 
 
 83 ... 
 
 84 }; 
 
 85 
 
 86 static int xxx_pcm_hw_params(struct snd_pcm_substream *substream, 
 
 87 struct snd_pcm_hw_params *params) 
 
 88 { 
 
 89 ... 
 
 90 snd_pcm_lib_malloc_pages(substream, size); 
 
 91 
 
 92 return 0; 
 
 93 } 
 
 94 
 
 95 static int xxx_pcm_hw_free(struct snd_pcm_substream *substream) 
 
 96 { 
 
 97 snd_pcm_lib_free_pages(substream); 
 
 98 
 
 99 return 0; 
 
 100 } 
 
 101 
 
 102 static int xxx_pcm_prepare(struct snd_pcm_substream *substream) 
 
 103 { 
 
 104 ... 
 
 105 } 
 
 106 
 
 107 static int xxx_pcm_trigger(struct snd_pcm_substream *substream, int cmd) 
 
 108 { 
 
 109 ... 
 
 110 } 
 
 111 
 
 112 static snd_pcm_uframes_t xxx_pcm_pointer(struct snd_pcm_substream *substream) 
 
 113 { 
 
 114 ... 
 
 115 } 
 
 116 
 
 117 static int xxx_pcm_open(struct snd_pcm_substream *substream) 
 
 118 { 
 
 119 ... 
 
 120 } 
 
 121 
 
 122 static int xxx_pcm_mmap(struct snd_pcm_substream *substream, 
 
 123 struct vm_area_struct *vma) 
 
 124 { 
 
 125 ...; 
 
 126 } 
 
 127 
 
 128 struct snd_pcm_ops xxx_pcm_i2s_ops = {



129 .open = xxx_pcm_open, 
 
 130 .ioctl = snd_pcm_lib_ioctl, 
 
 131 .hw_params = xxx_pcm_hw_params, 
 
 132 .hw_free = xxx_pcm_hw_free, 
 
 133 .prepare = xxx_pcm_prepare, 
 
 134 .trigger = xxx_pcm_trigger, 
 
 135 .pointer = xxx_pcm_pointer, 
 
 136 .mmap = xxx_pcm_mmap, 
 
 137 };

