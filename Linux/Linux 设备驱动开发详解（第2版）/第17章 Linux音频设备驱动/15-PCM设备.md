### 17.4.3 PCM设备

每个声卡最多可以有4个PCM实例，一个PCM实例对应一个设备文件。PCM实例由PCM播放和录音流组成，而每个PCM流又由一个或多个PCM子流组成。有的声卡支持多重播放功能，例如，emu10k1包含一个有32个立体声子流的PCM播放设备。

#### 1．PCM实例构造

int snd_pcm_new(struct snd_card *card, char *id, int device, 
 
 int playback_count, int capture_count, struct snd_pcm ** rpcm);

第1个参数是card指针，第2个是标识字符串，第3个是PCM设备索引（0表示第1个PCM设备），第4和第5个分别为播放和录音设备的子流数。当存在多个子流时，需要恰当地处理open()、close()和其他函数。在每个回调函数中，可以通过snd_pcm_substream的number成员得知目前操作的究竟是哪个子流，如下所示：

struct snd_pcm_substream *substream; 
 
 int index = substream->number;

一种习惯的做法是在驱动中定义一个PCM“构造函数”，负责PCM实例的创建，如代码清单17.7所示。

代码清单17.7 PCM设备的“构造函数”

1 static int _ _devinit snd_xxxchip_new_pcm(struct xxxchip *chip) 
 
 2 { 
 
 3 struct snd_pcm *pcm; 
 
 4 int err; 
 
 5 /* 创建PCM实例 */ 
 
 6 if ((err = snd_pcm_new(chip->card, "xxx Chip", 0, 1, 1, &pcm)) < 0) 
 
 7 return err; 
 
 8 pcm->private_data = chip; /* 置pcm->private_data为芯片特定数据*/ 
 
 9 strcpy(pcm->name, "xxx Chip"); 
 
 10 chip->pcm = pcm; 
 
 11 ... 
 
 12 return 0; 
 
 13 }

#### 2．设置PCM操作

void snd_pcm_set_ops(struct snd_pcm *pcm, int direction, struct snd_pcm_ops *ops);

第1个参数是snd_pcm的指针，第2个参数是SNDRV_PCM_STREAM_PLAYBACK或SNDRV_ PCM_STREAM_CAPTURE，而第3个参数是PCM操作结构体snd_pcm_ops，这个结构体的定义如代码清单17.8所示。

代码清单17.8 snd_pcm_ops结构体

1 struct snd_pcm_ops { 
 
 2 int (*open)(struct snd_pcm_substream *substream); 
 
 3 int (*close)(struct snd_pcm_substream *substream); 
 
 4 int (*ioctl)(struct snd_pcm_substream * substream, 
 
 5 unsigned int cmd, void *arg); 
 
 6 int (*hw_params)(struct snd_pcm_substream *substream, 
 
 7 struct snd_pcm_hw_params *params); 
 
 8 int (*hw_free)(struct snd_pcm_substream *substream); /* 资源释放*/ 
 
 9 int (*prepare)(struct snd_pcm_substream *substream); 
 
 10 /* 在PCM被开始、停止或暂停时调用*/ 
 
 11 int (*trigger)(struct snd_pcm_substream *substream, int cmd); 
 
 12 snd_pcm_uframes_t (*pointer)(struct snd_pcm_substream *substream);/ * 当前缓冲区的硬件位置*/ 
 
 13 /* 缓冲区复制*/ 
 
 14 int (*copy)(struct snd_pcm_substream *substream, int channel, 
 
 15 snd_pcm_uframes_t pos, 
 
 16 void _ _user *buf, snd_pcm_uframes_t count); 
 
 17 int (*silence)(struct snd_pcm_substream *substream, int channel, 
 
 18 snd_pcm_uframes_t pos, snd_pcm_uframes_t count); 
 
 19 struct page * (*page)(struct snd_pcm_substream *substream, 
 
 20 unsigned long offset); 
 
 21 int (*mmap)(struct snd_pcm_substream *substream, struct vm_area_struct *vma); 
 
 22 int (*ack)(struct snd_pcm_substream *substream); 
 
 23 };

snd_pcm_ops中的所有操作都需事先通过snd_pcm_substream_chip()获得xxxchip指针，例如：

int xxx() 
 
 { 
 
 struct xxxchip *chip = snd_pcm_substream_chip(substream); 
 
 ... 
 
 }

当一个PCM子流被打开时，snd_pcm_ops中的open()函数将被调用，在这个函数中，至少需要初始化runtime->hw字段，代码清单17.9所示为open()函数的范例。

代码清单17.9 snd_pcm_ops结构体中的open()函数

1 static int snd_xxx_open(struct snd_pcm_substream *substream) 
 
 2 { 
 
 3 /* 从子流获得xxxchip指针*/ 
 
 4 struct xxxchip *chip = snd_pcm_substream_chip(substream); 
 
 5 /* 获得PCM运行时信息指针*/ 
 
 6 struct snd_pcm_runtime *runtime = substream->runtime; 
 
 7 ... 
 
 8 /* 初始化runtime->hw */ 
 
 9 runtime->hw = snd_xxxchip_playback_hw; 
 
 10 return 0; 
 
 11 }

上述代码中的snd_xxxchip_playback_hw是预先定义的硬件描述。在open()函数中，可以分配一段私有数据。如果硬件配置需要更多的限制，也需设置硬件限制。

当PCM子流被关闭时，close()函数将被调用。如果open()函数中分配了私有数据，则在close()函数中应该释放substream的私有数据，代码清单17.10所示为close()函数的范例。

代码清单17.10 snd_pcm_ops结构体中的close()函数

1 static int snd_xxx_close(struct snd_pcm_substream *substream) 
 
 2 { 
 
 3 /* 释放子流私有数据*/ 
 
 4 kfree(substream->runtime->private_data); 
 
 5 ... 
 
 6 }

驱动中通常可以给snd_pcm_ops的ioctl()成员函数传递通用的snd_pcm_lib_ioctl()函数。

snd_pcm_ops的hw_params()成员函数将在应用程序设置硬件参数（PCM子流的周期大小、缓冲区大小和格式等）的时候被调用，它的形式如下：

static int snd_xxx_hw_params(struct snd_pcm_substream *substream,struct snd_pcm_hw_params 
 
 *hw_params);

在这个函数中，将完成大量硬件设置，甚至包括缓冲区分配，这时可调用如下辅助函数：

snd_pcm_lib_malloc_pages(substream, params_buffer_bytes(hw_params));

仅当DMA缓冲区已被预先分配的情况下，上述调用才可成立。

与hw_params()对应的函数是hw_free()，它释放由hw_params()分配的资源，例如，通过如下调用释放snd_pcm_lib_malloc_pages()缓冲区：

snd_pcm_lib_free_pages(substream);

当PCM被“准备”时，prepare()函数将被调用，在其中可以设置采样率、格式等。prepare()函数与hw_params()函数的不同在于对prepare()的调用发生在snd_pcm_prepare()每次被调用的时候。prepare()的形式如下：

static int snd_xxx_prepare(struct snd_pcm_substream *substream);

trigger()成员函数在PCM被开始、停止或暂停时调用，函数的形式如下：

static int snd_xxx_trigger(struct snd_pcm_substream *substream, int cmd);

cmd参数定义了具体的行为，在trigger()成员函数中至少要处理SNDRV_PCM_TRIGGER_ START和SNDRV_PCM_TRIGGER_STOP命令，如果PCM支持暂停，还应处理SNDRV_PCM_ TRIGGER_PAUSE_PUSH和SNDRV_PCM_TRIGGER_PAUSE_RELEASE命令。如果设备支持挂起/恢复，当能量管理状态发生变化时将处理SNDRV_PCM_TRIGGER_SUSPEND和SNDRV_PCM_ TRIGGER_RESUME 这两个命令。注意trigger()函数是原子的，中途不能睡眠。代码清单17.11所示为trigger()函数的范例。

代码清单17.11 snd_pcm_ops结构体中的trigger()函数

1 static int snd_xxx_trigger(struct snd_pcm_substream *substream, int cmd) 
 
 2 { 
 
 3 switch (cmd) { 
 
 4 case SNDRV_PCM_TRIGGER_START: 
 
 5 /* 开启PCM引擎*/ 
 
 6 break; 
 
 7 case SNDRV_PCM_TRIGGER_STOP: 
 
 8 /* 停止PCM引擎*/



9 break; 
 
 10 ... /* 其他命令*/ 
 
 11 default: 
 
 12 return - EINVAL; 
 
 13 } 
 
 14 }

pointer()函数用于PCM中间层查询目前缓冲区的硬件位置，该函数以帧的形式返回0～buffer_size – 1的位置（ALSA 0.5.x中为字节形式），此函数也是原子的。

copy()和silence()函数一般可以省略，但是，当硬件缓冲区不处于常规内存中时需要。例如，一些设备有自己的不能被映射的硬件缓冲区，这种情况下，我们不得不将数据从内存缓冲区复制到硬件缓冲区。当内存缓冲区在物理和虚拟地址上都不连续时，这两个函数也必须被实现。

#### 3．分配缓冲区

分配缓冲区的最简单方法是调用如下函数：

int snd_pcm_lib_preallocate_pages_for_all(struct snd_pcm *pcm, 
 
 int type, void *data, size_t size, size_t max);

type参数是缓冲区的类型，包含SNDRV_DMA_TYPE_UNKNOWN（未知）、SNDRV_DMA_ TYPE_CONTINUOUS（连续的非DMA内存）、SNDRV_DMA_TYPE_DEV（连续的通用设备），SNDRV_DMA_TYPE_DEV_SG（通用设备SG-buffer）和SNDRV_DMA_TYPE_SBUS（连续的SBUS）。如下代码将分配64KB的缓冲区：

snd_pcm_lib_preallocate_pages_for_all(pcm, SNDRV_DMA_TYPE_DEV, 
 
 snd_dma_pci_data(chip->pci),64*1024, 64*1024);

#### 4．设置标志

在构造PCM实例、设置操作集并分配缓冲区之后，如果有需要，应设置PCM的信息标志，例如，如果PCM设备只支持半双工，则这样定义标志：

pcm->info_flags = SNDRV_PCM_INFO_HALF_DUPLEX;

#### 5．PCM实例析构

PCM实例的“析构函数”并非是必须的，因为PCM实例会被PCM中间层代码自动释放，如果驱动中分配了一些特别的内存空间，则必须定义“析构函数”，代码清单17.12所示为PCM“析构函数”与对应的“构造函数”，“析构函数”会释放“构造函数”中创建的xxx_private__pcm_data。

代码清单17.12 PCM设备“析构函数”

1 static void xxxchip_pcm_free(struct snd_pcm *pcm) 
 
 2 { 
 
 3 /* 从pcm实例得到chip */ 
 
 4 struct xxxchip *chip = snd_pcm_chip(pcm); 
 
 5 /* 释放自定义用途的内存 */ 
 
 6 kfree(chip->xxx_private_pcm_data); 
 
 7 ... 
 
 8 } 
 
 9 
 
 10 static int __devinit snd_xxxchip_new_pcm(struct xxxchip *chip) 
 
 11 { 
 
 12 struct snd_pcm *pcm; 
 
 13 ... 
 
 14 /* 分配自定义用途的内存 */ 
 
 15 chip->xxx_private_pcm_data = kmalloc(...);



16 pcm->private_data = chip; 
 
 17 /* 设置“析构函数” */ 
 
 18 pcm->private_free = xxxchip_pcm_free; 
 
 19 ... 
 
 20 }

上述代码第4行的snd_pcm_chip()从PCM实例指针获得xxxchip指针，实际上它就是返回第16行给PCM实例赋予的xxxchip指针。

#### 6．PCM信息运行时结构体

当PCM子流被打开后，PCM运行时实例（定义为结构体snd_pcm_runtime，如代码清单17.13所示）将被分配给这个子流，这个指针通过substream->runtime获得。运行时指针包含各种各样的信息：hw_params及sw_params配置的拷贝、缓冲区指针、mmap记录、自旋锁等，几乎PCM的所有控制信息均能从中取得。

代码清单17.13 snd_pcm_runtime结构体

1 struct snd_pcm_runtime { 
 
 2 /* 状态 */ 
 
 3 struct snd__pcm_substream *trigger_master; 
 
 4 snd_timestamp_t trigger_tstamp; /* 触发时间戳 */ 
 
 5 int overrange; 
 
 6 snd_pcm_uframes_t avail_max; 
 
 7 snd_pcm_uframes_t hw_ptr_base; /* 缓冲区复位时的位置 */ 
 
 8 snd_pcm_uframes_t hw_ptr_interrupt; /* 中断时的位置*/ 
 
 9 /* 硬件参数 */ 
 
 10 snd_pcm_access_t access; /* 存取模式 */ 
 
 11 snd_pcm_format_t format; /* SNDRV_PCM_FORMAT_* */ 
 
 12 snd_pcm_subformat_t subformat; /* 子格式 */ 
 
 13 unsigned int rate; /* rate in Hz */ 
 
 14 unsigned int channels; /* 通道 */ 
 
 15 snd_pcm_uframes_t period_size; /* 周期大小 */ 
 
 16 unsigned int periods; /* 周期数 */ 
 
 17 snd_pcm_uframes_t buffer_size; /* 缓冲区大小 */ 
 
 18 unsigned int tick_time; /* tick time */ 
 
 19 snd_pcm_uframes_t min_align; /* 格式对应的最小对齐*/ 
 
 20 size_t byte_align; 
 
 21 unsigned int frame_bits; 
 
 22 unsigned int sample_bits; 
 
 23 unsigned int info; 
 
 24 unsigned int rate_num; 
 
 25 unsigned int rate_den; 
 
 26 /* 软件参数 */ 
 
 27 struct timespec tstamp_mode; /* mmap时间戳被更新*/ 
 
 28 unsigned int period_step; 
 
 29 unsigned int sleep_min; /* 睡眠的最小节拍 */ 
 
 30 snd_pcm_uframes_t xfer_align; 
 
 31 snd_pcm_uframes_t start_threshold; 
 
 32 snd_pcm_uframes_t stop_threshold; 
 
 33 snd_pcm_uframes_t silence_threshold; /* Silence填充阈值 */ 
 
 34 snd_pcm_uframes_t silence_size; /* Silence填充大小 */ 
 
 35 snd_pcm_uframes_t boundary; 
 
 36 snd_pcm_uframes_t silenced_start; 
 
 37 snd_pcm_uframes_t silenced_size;



38 snd_pcm_sync_id_t sync; /* 硬件同步ID */ 
 
 39 /* mmap */ 
 
 40 volatile struct snd_pcm_mmap_status *status; 
 
 41 volatile struct snd_pcm_mmap_control *control; 
 
 42 atomic_t mmap_count; 
 
 43 /* 锁/调度 */ 
 
 44 spinlock_t lock; 
 
 45 wait_queue_head_t sleep; 
 
 46 struct timer_list tick_timer; 
 
 47 struct fasync_struct *fasync; 
 
 48 /* 私有段 */ 
 
 49 void *private_data; 
 
 50 void(*private_free)(struct snd_pcm_runtime *runtime); 
 
 51 /* 硬件描述 */ 
 
 52 struct snd_pcm_hardware hw; 
 
 53 struct snd_pcm_hw_constraints hw_constraints; 
 
 54 /* 中断回调函数 */ 
 
 55 void(*transfer_ack_begin)(struct snd_pcm_substream*substream); 
 
 56 void(*transfer_ack_end)(struct snd_pcm_substream *substream); 
 
 57 /* 定时器 */ 
 
 58 unsigned int timer_resolution; /* timer resolution */ 
 
 59 /* DMA */ 
 
 60 unsigned char *dma_area; /* DMA区域*/ 
 
 61 dma_addr_t dma_addr; /* 总线物理地址*/ 
 
 62 size_t dma_bytes; /* DMA区域大小 */ 
 
 63 struct snd_dma_buffer *dma_buffer_p; /* 被分配的缓冲区 */ 
 
 64 #if defined(CONFIG_SND_PCM_OSS) || defined(CONFIG_SND_PCM_OSS_MODULE) 
 
 65 /* OSS信息 */ 
 
 66 struct snd_pcm_oss_runtime oss; 
 
 67 #endif 
 
 68 };

snd_pcm_runtime中的大多数记录对被声卡驱动操作集中的函数是只读的，仅仅PCM中间层可从更新或修改这些信息，但是硬件描述、中断回调函数、DMA缓冲区信息和私有数据是例外的。

下面解释snd_pcm_runtime结构体中的几个重要成员。

（1）硬件描述。

硬件描述（snd_pcm_hardware结构体）包含了基本硬件配置的定义，需要在open()函数中赋值。runtime实例保存的是硬件描述的拷贝而非指针，这意味着在open()函数中可以修改被拷贝的描述（runtime->hw），例如：

struct snd_pcm_runtime *runtime = substream->runtime; 
 
 ... 
 
 runtime->hw = snd_xxchip_playback_hw; /* generic的硬件描述 */ 
 
 /* 特定的硬件描述 */ 
 
 if (chip->model == VERY_OLD_ONE) 
 
 runtime->hw.channels_max = 1;

snd_pcm_hardware结构体的定义如代码清单17.14所示。

代码清单17.14 snd_pcm_hardware结构体

1 struct snd_pcm_hardware { 
 
 2 unsigned int info; /* SNDRV_PCM_INFO_* /



3 u64 formats; /* SNDRV_PCM_FMTBIT_* */ 
 
 4 unsigned int rates; /* SNDRV_PCM_RATE_* */ 
 
 5 unsigned int rate_min; /* 最小采样率 */ 
 
 6 unsigned int rate_max; /* 最大采样率 */ 
 
 7 unsigned int channels_min; /* 最小的通道数 */ 
 
 8 unsigned int channels_max; /* 最大的通道数 */ 
 
 9 size_t buffer_bytes_max; /* 最大缓冲区大小 */ 
 
 10 size_t period_bytes_min; /* 最小周期大小 */ 
 
 11 size_t period_bytes_max; /* 最大奏曲大小 */ 
 
 12 unsigned int periods_min; /* 最小周期数 */ 
 
 13 unsigned int periods_max; /* 最大周期数 */ 
 
 14 size_t fifo_size; /* FIFO字节数 */ 
 
 15 };

snd_pcm_hardware结构体中的info字段标识PCM设备的类型和能力，形式为SNDRV_PCM_ INFO_XXX。info字段至少需要定义是否支持mmap，当支持时，应设置SNDRV_PCM_INFO_MMAP标志；当硬件支持interleaved或non-interleaved格式时，应设置SNDRV_PCM_INFO _INTERLEAVED 或SNDRV_PCM_INFO_NONINTERLEAVED标志；如果都支持，则两者都可设置。

MMAP_VALID和BLOCK_TRANSFER标志针对OSS mmap，只有mmap被真正支持时，才可设置MMAP_VALID；SNDRV_PCM_INFO_PAUSE意味着设备可支持暂停操作，而SNDRV_ PCM_INFO_RESUME意味着设备可支持挂起/恢复操作；当PCM子流能被同步，如同步播放和录音流的start/stop，可设置SNDRV_PCM_INFO_SYNC_START标志。

formats包含PCM设备支持的格式，形式为SNDRV_PCM_FMTBIT_XXX，如果设备支持多种模式，应将各种模式标志进行“或”操作。

rates包含了PCM设备支持的采样率，形式如SNDRV_PCM_RATE_XXX，如果支持连续的采样率，则传递CONTINUOUS。

rate_min和rate_max分别定义了最大和最小的采样率，注意：要与rates字段相符。

channel_min和channel_max定义了最大和最小的通道数量。

buffer_bytes_max定义最大的缓冲区大小，注意：没有buffer_bytes_min字段，这是因为它可以通过最小的周期大小和最小的周期数量计算出来。

period信息与OSS中的fragment对应，定义了PCM中断产生的周期。更小的周期大小意味着更多的中断，在录音时，周期大小定义了输入延迟，在播放时，整个缓冲区大小对应着输出延迟。

PCM可被应用程序通过alsa-lib发送hw_params来配置，配置信息将保存在运行时实例中。对缓冲区和周期大小的配置以帧形式存储，而frames_to_bytes()和bytes_to_frames()可完成帧和字节的转换，如：

period_bytes = frames_to_bytes(runtime, runtime->period_size);

（2）DMA缓冲区信息。

包含dma_area（逻辑地址）、dma_addr（物理地址）、dma_bytes（缓冲区大小）和dma_private（被ALSA DMA分配器使用）。可以由snd_pcm_lib_malloc_pages()实现，ALSA中间层会设置DMA缓冲区信息的相关字段，这种情况下，驱动中不能再写这些信息，只能读取。也就是说，如果使用标准的缓冲区分配函数snd_pcm_lib_malloc_pages()分配缓冲区，则我们不需要自己维护DMA缓冲区信息。如果缓冲区由自己分配，则需要在hw_params()函数中管理缓冲区信息，至少需管理dma_bytes和dma_addr，如果支持mmap，则必须管理dma_area，对dma_private的管理视情况而定。

（3）运行状态。

通过runtime->status可以获得运行状态，它是snd_pcm_mmap_status结构体的指针，例如，通过runtime->status->hw_ptr可以获得目前的DMA硬件指针。此外，通过runtime->control可以获得DMA应用指针，它指向snd_pcm_mmap_control结构体指针，但是不建议直接访问该指针。

（4）私有数据。

驱动中可以为子流分配一段内存并赋值给runtime->private_data，注意不要与pcm->private_ data混淆，后者一般指向xxxchip，而前者是在PCM设备的open()函数中分配的动态数据，例如：

static int snd_xxx_open(struct snd_pcm_substream *substream) 
 
 { 
 
 struct xxx_pcm_data *data; 
 
 .... 
 
 data = kmalloc(sizeof(*data), GFP_KERNEL); 
 
 substream->runtime->private_data = data; /* 赋值runtime->private_data */ 
 
 .... 
 
 }

（5）中断回调函数：

transfer_ack_begin()和transfer_ack_end()函数分别在snd_pcm_period_elapsed()的开始和结束时被调用。

根据以上分析，代码清单17.15给出了一个完整的PCM设备接口模板。

代码清单17.15 PCM设备接口模板

1 #include <sound/pcm.h> 
 
 2 .... 
 
 3 /* 播放设备硬件定义 */ 
 
 4 static struct snd_pcm_hardware snd_xxxchip_playback_hw = { 
 
 5 .info = (SNDRV_PCM_INFO_MMAP | SNDRV_PCM_INFO_INTERLEAVED | 
 
 6 SNDRV_PCM_INFO_BLOCK_TRANSFER | SNDRV_PCM_INFO_MMAP_VALID), 
 
 7 .formats = SNDRV_PCM_FMTBIT_S16_LE, 
 
 8 .rates = SNDRV_PCM_RATE_8000_48000, 
 
 9 .rate_min = 8000, 
 
 10 .rate_max = 48000, 
 
 11 .channels_min = 2, 
 
 12 .channels_max = 2, 
 
 13 .buffer_bytes_max = 32768, 
 
 14 .period_bytes_min = 4096, 
 
 15 .period_bytes_max = 32768, 
 
 16 .periods_min = 1, 
 
 17 .periods_max = 1024, 
 
 18 }; 
 
 19 
 
 20 /* 录音设备硬件定义 */ 
 
 21 static struct snd_pcm_hardware snd_xxxchip_capture_hw = { 
 
 22 .info = (SNDRV_PCM_INFO_MMAP | SNDRV_PCM_INFO_INTERLEAVED | 
 
 23 SNDRV_PCM_INFO_BLOCK_TRANSFER | SNDRV_PCM_INFO_MMAP_VALID), 
 
 24 .formats = SNDRV_PCM_FMTBIT_S16_LE, 
 
 25 .rates = SNDRV_PCM_RATE_8000_48000, 
 
 26 .rate_min = 8000, 
 
 27 .rate_max = 48000, 
 
 28 .channels_min = 2, 
 
 29 .channels_max = 2,



30 .buffer_bytes_max = 32768, 
 
 31 .period_bytes_min = 4096, 
 
 32 .period_bytes_max = 32768, 
 
 33 .periods_min = 1, 
 
 34 .periods_max = 1024, 
 
 35 }; 
 
 36 
 
 37 /* 播放：打开函数 */ 
 
 38 static int snd_xxxchip_playback_open(struct snd_pcm_substream*substream) 
 
 39 { 
 
 40 struct xxxchip *chip = snd_pcm_substream_chip(substream); 
 
 41 struct snd_pcm_runtime *runtime = substream->runtime; 
 
 42 runtime->hw = snd_xxxchip_playback_hw; 
 
 43 ... /* 硬件初始化代码*/ 
 
 44 return 0; 
 
 45 } 
 
 46 
 
 47 /* 播放：关闭函数 */ 
 
 48 static int snd_xxxchip_playback_close(struct snd_pcm_substream*substream) 
 
 49 { 
 
 50 struct xxxchip *chip = snd_pcm_substream_chip(substream); 
 
 51 /* 硬件相关的代码*/ 
 
 52 return 0; 
 
 53 } 
 
 54 
 
 55 /* 录音：打开函数 */ 
 
 56 static int snd_xxxchip_capture_open(struct snd_pcm_substream*substream) 
 
 57 { 
 
 58 struct xxxchip *chip = snd_pcm_substream_chip(substream); 
 
 59 struct snd_pcm_runtime *runtime = substream->runtime; 
 
 60 runtime->hw = snd_xxxchip_capture_hw; 
 
 61 ... /* 硬件初始化代码*/ 
 
 62 return 0; 
 
 63 } 
 
 64 
 
 65 /* 录音：关闭函数 */ 
 
 66 static int snd_xxxchip_capture_close(struct snd_pcm_substream*substream) 
 
 67 { 
 
 68 struct xxxchip *chip = snd_pcm_substream_chip(substream); 
 
 69 ... /* 硬件相关的代码*/ 
 
 70 return 0; 
 
 71 } 
 
 72 /* hw_params函数 */ 
 
 73 static int snd_xxxchip_pcm_hw_params(struct snd_pcm_substream*substream, struct 
 
 74 snd_pcm_hw_params *hw_params) 
 
 75 { 
 
 76 return snd_pcm_lib_malloc_pages(substream, params_buffer_bytes(hw_params)); 
 
 77 } 
 
 78 /* hw_free函数 */ 
 
 79 static int snd_xxxchip_pcm_hw_free(struct snd_pcm_substream*substream) 
 
 80 { 
 
 81 return snd_pcm_lib_free_pages(substream); 
 
 82 } 
 
 83 /* prepare函数 */ 
 
 84 static int snd_xxxchip_pcm_prepare(struct snd_pcm_substream*substream)



85 { 
 
 86 struct xxxchip *chip = snd_pcm_substream_chip(substream); 
 
 87 struct snd_pcm_runtime *runtime = substream->runtime; 
 
 88 /* 根据目前的配置信息设置硬件 
 
 89 * 例如： 
 
 90 */ 
 
 91 xxxchip_set_sample_format(chip, runtime->format); 
 
 92 xxxchip_set_sample_rate(chip, runtime->rate); 
 
 93 xxxchip_set_channels(chip, runtime->channels); 
 
 94 xxxchip_set_dma_setup(chip, runtime->dma_addr, chip->buffer_size, chip 
 
 95 ->period_size); 
 
 96 return 0; 
 
 97 } 
 
 98 /* trigger函数 */ 
 
 99 static int snd_xxxchip_pcm_trigger(struct snd_pcm_substream*substream, int cmd) 
 
 100 { 
 
 101 switch (cmd) { 
 
 102 case SNDRV_PCM_TRIGGER_START: 
 
 103 /* do something to start the PCM engine */ 
 
 104 break; 
 
 105 case SNDRV_PCM_TRIGGER_STOP: 
 
 106 /* do something to stop the PCM engine */ 
 
 107 break; 
 
 108 default: 
 
 109 return - EINVAL; 
 
 110 } 
 
 111 } 
 
 112 
 
 113 /* pointer函数 */ 
 
 114 static snd_pcm_uframes_t snd_xxxchip_pcm_pointer(struct snd_pcm_substream 
 
 115 *substream) 
 
 116 { 
 
 117 struct xxxchip *chip = snd_pcm_substream_chip(substream); 
 
 118 unsigned int current_ptr; 
 
 119 /*获得当前的硬件指针*/ 
 
 120 current_ptr = xxxchip_get_hw_pointer(chip); 
 
 121 return current_ptr; 
 
 122 } 
 
 123 /* 放音设备操作集 */ 
 
 124 static struct snd_pcm_ops snd_xxxchip_playback_ops = { 
 
 125 .open = snd_xxxchip_playback_open, 
 
 126 .close = snd_xxxchip_playback_close, 
 
 127 .ioctl = snd_pcm_lib_ioctl, 
 
 128 .hw_params = snd_xxxchip_pcm_hw_params, 
 
 129 .hw_free = snd_xxxchip_pcm_hw_free, 
 
 130 .prepare = snd_xxxchip_pcm_prepare, 
 
 131 .trigger = snd_xxxchip_pcm_trigger, 
 
 132 .pointer = snd_xxxchip_pcm_pointer, 
 
 133 }; 
 
 134 /* 录音设备操作集 */ 
 
 135 static struct snd_pcm_ops snd_xxxchip_capture_ops = { 
 
 136 .open = snd_xxxchip_capture_open, 
 
 137 .close = snd_xxxchip_capture_close, 
 
 138 .ioctl = snd_pcm_lib_ioctl,



139 .hw_params = snd_xxxchip_pcm_hw_params, 
 
 140 .hw_free = snd_xxxchip_pcm_hw_free, 
 
 141 .prepare = snd_xxxchip_pcm_prepare, 
 
 142 .trigger = snd_xxxchip_pcm_trigger, 
 
 143 .pointer = snd_xxxchip_pcm_pointer, 
 
 144 }; 
 
 145 
 
 146 /* 创建一个PCM设备 */ 
 
 147 static int _ _devinit snd_xxxchip_new_pcm(struct xxxchip *chip) 
 
 148 { 
 
 149 struct snd_pcm *pcm; 
 
 150 int err; 
 
 151 if ((err = snd_pcm_new(chip->card, "xxx Chip", 0, 1, 1, &pcm)) < 0) 
 
 152 return err; 
 
 153 pcm->private_data = chip; 
 
 154 strcpy(pcm->name, "xxx Chip"); 
 
 155 chip->pcm = pcm; 
 
 156 /* 设置操作集 */ 
 
 157 snd_pcm_set_ops(pcm, SNDRV_PCM_STREAM_PLAYBACK, &snd_xxxchip_playback_ops); 
 
 158 snd_pcm_set_ops(pcm, SNDRV_PCM_STREAM_CAPTURE, &snd_xxxchip_capture_ops); 
 
 159 /* 分配缓冲区 */ 
 
 160 snd_pcm_lib_preallocate_pages_for_all(pcm, SNDRV_DMA_TYPE_DEV, 
 
 161 snd_dma_pci_data(chip - > pci), 64 *1024, 64 *1024); 
 
 162 return 0; 
 
 163 }

