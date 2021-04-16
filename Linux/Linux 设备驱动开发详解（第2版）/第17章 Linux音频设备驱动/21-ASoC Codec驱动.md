### 17.5.2 ASoC Codec驱动

在ASoC架构下，Codec驱动负责如下工作。

（1）Codec DAI（Digital Audio Interfaces）和PCM配置，由结构体snd_soc_ dai（如代码清单17.28）来描述，形容playback、capture的属性以及DAI接口的操作。

代码清单17.28 DAI结构体snd_soc_dai定义

1 struct snd_soc_dai { 
 
 2 /* DAI的描述 */ 
 
 3 char *name; 
 
 4 unsigned int id; 
 
 5 unsigned char type; 
 
 6 
 
 7 /* DAI callbacks */ 
 
 8 int (*probe)(struct platform_device *pdev,



9 struct snd_soc_dai *dai); 
 
 10 void (*remove)(struct platform_device *pdev, 
 
 11 struct snd_soc_dai *dai); 
 
 12 int (*suspend)(struct platform_device *pdev, 
 
 13 struct snd_soc_dai *dai); 
 
 14 int (*resume)(struct platform_device *pdev, 
 
 15 struct snd_soc_dai *dai); 
 
 16 
 
 17 /* ops */ 
 
 18 struct snd_soc_ops ops; 
 
 19 struct snd_soc_dai_ops dai_ops; 
 
 20 
 
 21 /* DAI的能力 */ 
 
 22 struct snd_soc_pcm_stream capture; 
 
 23 struct snd_soc_pcm_stream playback; 
 
 24 
 
 25 /* DAI运行时信息 */ 
 
 26 struct snd_pcm_runtime *runtime; 
 
 27 struct snd_soc_codec *codec; 
 
 28 unsigned int active; 
 
 29 unsigned char pop_wait:1; 
 
 30 void *dma_data; 
 
 31 
 
 32 /* DAI 私有数据 */ 
 
 33 void *private_data; 
 
 34 };

第22、23行的snd_soc_pcm_stream类型成员capture、playback分别描述录音和放音的能力，snd_soc_pcm_stream结构体主要包含formats、rates、rate_min、rate_max、channels_min、channels_max这几个字段。

（2）Codec IO操作、动态音频电源管理以及时钟、PLL等控制。

代码清单17.28中第27行的snd_soc_codec结构体是对Codec本身I/O控制以及动态音频电源管理（Dynamic Audio Power Management，DAPM）的描述。它描述I2C、SPI或AC '97如何读写Codec寄存器并容纳DAPM链表，其定义如代码清单17.29，核心成员为read()、write()、hw_write()、hw_read()、dapm_widgets、dapm_paths等。

代码清单17.29 snd_soc_codec结构体定义

1 struct snd_soc_codec { 
 
 2 char *name; 
 
 3 struct module *owner; 
 
 4 struct mutex mutex; 
 
 5 
 
 6 /* callbacks */ 
 
 7 int (*set_bias_level)(struct snd_soc_codec *, 
 
 8 enum snd_soc_bias_level level); 
 
 9 
 
 10 /* runtime */ 
 
 11 struct snd_card *card; 
 
 12 struct snd_ac97 *ac97; /* for ad-hoc ac97 devices */ 
 
 13 unsigned int active; 
 
 14 unsigned int pcm_devs; 
 
 15 void *private_data;



16 
 
 17 /* codec IO */ 
 
 18 void *control_data; /* codec control (i2c/3wire) data */ 
 
 19 unsigned int (*read)(struct snd_soc_codec *, unsigned int); 
 
 20 int (*write)(struct snd_soc_codec *, unsigned int, unsigned int); 
 
 21 int (*display_register)(struct snd_soc_codec *, char *, 
 
 22 size_t, unsigned int); 
 
 23 hw_write_t hw_write; 
 
 24 hw_read_t hw_read; 
 
 25 void *reg_cache; 
 
 26 short reg_cache_size; 
 
 27 short reg_cache_step; 
 
 28 
 
 29 /* dapm */ 
 
 30 struct list_head dapm_widgets; 
 
 31 struct list_head dapm_paths; 
 
 32 enum snd_soc_bias_level bias_level; 
 
 33 enum snd_soc_bias_level suspend_bias_level; 
 
 34 struct delayed_work delayed_work; 
 
 35 
 
 36 /* codec DAI's */ 
 
 37 struct snd_soc_dai *dai; 
 
 38 unsigned int num_dai; 
 
 39 };

代码清单17.28中第19行的snd_soc_dai_ops则描述该Codec的时钟、PLL以及格式设置，主要包括set_sysclk()、set_pll()、set_clkdiv()、set_fmt()等成员函数，其定义如代码清单17.30。

代码清单17.30 snd_soc_dai_ops结构体定义

1 struct snd_soc_dai_ops { 
 
 2 /* DAI 时钟配置 */ 
 
 3 int (*set_sysclk)(struct snd_soc_dai *dai, 
 
 4 int clk_id, unsigned int freq, int dir); 
 
 5 int (*set_pll)(struct snd_soc_dai *dai, 
 
 6 int pll_id, unsigned int freq_in, unsigned int freq_out); 
 
 7 int (*set_clkdiv)(struct snd_soc_dai *dai, int div_id, int div); 
 
 8 
 
 9 /* DAI 格式配置 */ 
 
 10 int (*set_fmt)(struct snd_soc_dai *dai, unsigned int fmt); 
 
 11 int (*set_tdm_slot)(struct snd_soc_dai *dai, 
 
 12 unsigned int mask, int slots); 
 
 13 int (*set_tristate)(struct snd_soc_dai *dai, int tristate); 
 
 14 
 
 15 /* 数字静音 */ 
 
 16 int (*digital_mute)(struct snd_soc_dai *dai, int mute); 
 
 17 };

（3）Codec的mixer控制。

ASoC中定义了一组宏来描述Codec的mixer控制，这组宏可以方便地将mixer名和对应的寄存器进行绑定，主要包括：

SOC_SINGLE(xname, reg, shift, mask, invert) 
 
 SOC_DOUBLE(xname, reg, shift_left, shift_right, mask, invert) 
 
 SOC_ENUM_SINGLE(xreg, xshift, xmask, xtexts)

例如，对于宏SOC_SINGLE而言，参数xname是mixer的名字（如“Playback Volume”），reg是控制该mixer的寄存器，shift对应寄存器内的位，mask是进行操作时的屏蔽位，invert表明是否倒序或翻转。

（4）Codec音频操作。

在ASoC驱动的Codec部分，也需要关心音频流开始采集或播放时的一些动作，如hw_params()、hw_free()、prepare()、trigger()这些操作，不过与原始ALSA不同的是，在Codec驱动的这些函数中，不关心CPU端，而只关心Codec本身，由结构体snd_soc_ops描述，如代码清单17.31所示。

代码清单17.31 snd_soc_ops结构体定义

1 struct snd_soc_ops { 
 
 2 int (*startup)(struct snd_pcm_substream *); 
 
 3 void (*shutdown)(struct snd_pcm_substream *); 
 
 4 int (*hw_params)(struct snd_pcm_substream *, struct snd_pcm_hw_params *); 
 
 5 int (*hw_free)(struct snd_pcm_substream *); 
 
 6 int (*prepare)(struct snd_pcm_substream *); 
 
 7 int (*trigger)(struct snd_pcm_substream *, int); 
 
 8 };

ASoC的主要维护者Mark Brown（broonie@opensource.wolfsonmicro.com）是Wolfson公司的成员，因此从内核的drivers/sound/soc/codecs下容易发现Wolfson系列Codec芯片的驱动，此外，Analog Devices也是该目录源代码的主要贡献者。

