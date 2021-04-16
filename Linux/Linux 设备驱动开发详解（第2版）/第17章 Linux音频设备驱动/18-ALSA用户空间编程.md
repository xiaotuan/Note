### 17.4.6 ALSA用户空间编程

ALSA驱动的声卡在用户空间不宜直接使用文件接口，而应使用alsa-lib，代码清单17.26所示为基于ALSA音频驱动的最简单的播放应用程序。

代码清单17.26 ALSA用户空间播放程序

1 #include <stdio.h> 
 
 2 #include <stdlib.h> 
 
 3 #include <alsa/asoundlib.h> 
 
 4 
 
 5 main(int argc, char *argv[]) 
 
 6 { 
 
 7 int i; 
 
 8 int err; 
 
 9 short buf[128]; 
 
 10 snd_pcm_t *playback_handle; /* PCM设备句柄*/ 
 
 11 snd_pcm_hw_params_t *hw_params; /* 硬件信息和PCM流配置*/ 
 
 12 /* 打开PCM，最后一个参数为0意味着标准配置*/ 
 
 13 if ((err = snd_pcm_open(&playback_handle, argv[1], SND_PCM_STREAM_PLAYBACK, 0) 
 
 14 ) < 0) { 
 
 15 fprintf(stderr, "cannot open audio device %s (%s)\n", argv[1], snd_strerror 
 
 16 (err)); 
 
 17 exit(1); 
 
 18 } 
 
 19 /* 分配snd_pcm_hw_params_t结构体*/ 
 
 20 if ((err = snd_pcm_hw_params_malloc(&hw_params)) < 0) { 
 
 21 fprintf(stderr, "cannot allocate hardware parameter structure (%s)\n", 
 
 22 snd_strerror(err)); 
 
 23 exit(1); 
 
 24 } 
 
 25 /* 初始化hw_params */ 
 
 26 if ((err = snd_pcm_hw_params_any(playback_handle, hw_params)) < 0) { 
 
 27 fprintf(stderr, "cannot initialize hardware parameter structure (%s)\n", 
 
 28 snd_strerror(err)); 
 
 29 exit(1); 
 
 30 } 
 
 31 /* 初始化访问权限*/ 
 
 32 if ((err = snd_pcm_hw_params_set_access(playback_handle, hw_params, 
 
 33 SND_PCM_ACCESS_RW_INTERLEAVED)) < 0) { 
 
 34 fprintf(stderr, "cannot set access type (%s)\n", snd_strerror(err)); 
 
 35 exit(1); 
 
 36 } 
 
 37 /* 初始化采样格式*/ 
 
 38 if ((err = snd_pcm_hw_params_set_format(playback_handle, hw_params, 
 
 39 SND_PCM_FORMAT_S16_LE)) < 0) { 
 
 40 fprintf(stderr, "cannot set sample format (%s)\n", snd_strerror(err)); 
 
 41 exit(1); 
 
 42 } 
 
 43 /* 设置采样率，如果硬件不支持我们设置的采样率，将使用最接近的*/ 
 
 44 if ((err = snd_pcm_hw_params_set_rate_near(playback_handle, hw_params, 44100, 
 
 45 0)) < 0) { 
 
 46 fprintf(stderr, "cannot set sample rate (%s)\n", snd_strerror(err)); 
 
 47 exit(1); 
 
 48 } 
 
 49 /* 设置通道数量*/ 
 
 50 if ((err = snd_pcm_hw_params_set_channels(playback_handle, hw_params, 2)) < 0) { 
 
 51 fprintf(stderr, "cannot set channel count (%s)\n", snd_strerror(err));



52 exit(1); 
 
 53 } 
 
 54 /* 设置hw_params */ 
 
 55 if ((err = snd_pcm_hw_params(playback_handle, hw_params)) < 0) { 
 
 56 fprintf(stderr, "cannot set parameters (%s)\n", snd_strerror(err)); 
 
 57 exit(1); 
 
 58 } 
 
 59 /* 释放分配的snd_pcm_hw_params_t结构体*/ 
 
 60 snd_pcm_hw_params_free(hw_params); 
 
 61 /* 完成硬件参数设置，使设备准备好*/ 
 
 62 if ((err = snd_pcm_prepare(playback_handle)) < 0) { 
 
 63 fprintf(stderr, "cannot prepare audio interface for use (%s)\n", 
 
 64 snd_strerror(err)); 
 
 65 exit(1); 
 
 66 } 
 
 67 
 
 68 for (i = 0; i < 10; ++i) { 
 
 69 /* 写音频数据到PCM设备*/ 
 
 70 if ((err = snd_pcm_writei(playback_handle, buf, 128)) != 128) { 
 
 71 fprintf(stderr, "write to audio interface failed (%s)\n", snd_strerror 
 
 72 (err)); 
 
 73 exit(1); 
 
 74 } 
 
 75 } 
 
 76 /* 关闭PCM设备句柄*/ 
 
 77 snd_pcm_close(playback_handle); 
 
 78 exit(0); 
 
 79 }

由上述代码可以看出，ALSA用户空间编程的流程与17.3.4小节给出的OSS驱动用户空间编程的流程基本是一致的，都经过了“打开―设置参数―读写音频数据”的过程，不同在于OSS打开的是设备文件，设置参数使用的是ioctl()系统调用，读写音频数据使用的是read()、write()文件API，而ALSA则全部使用alsa-lib中的API。

把上述代码第70行的snd_pcm_writei()函数替换为snd_pcm_readi()，变成了一个最简单的录音程序。

代码清单17.27的程序打开一个音频接口，配置它为立体声、16位、44.1kHz采样和基于interleave的读写。它阻塞等待直接接口准备好接收放音数据，这时候将数据复制到缓冲区。这种设计方法使得程序很容易移植到类似JACK、LADSPA、Coreaudio、VST等callback机制驱动的系统。

代码清单17.27 ALSA用户空间播放程序（基于“中断”）

1 #include ... 
 
 2 
 
 3 snd_pcm_t *playback_handle; 
 
 4 short buf[4096]; 
 
 5 
 
 6 int playback_callback(snd_pcm_sframes_t nframes) 
 
 7 { 
 
 8 int err; 
 
 9 printf("playback callback called with %u frames\n", nframes); 
 
 10 /* 填充缓冲区 */ 
 
 11 if ((err = snd_pcm_writei(playback_handle, buf, nframes)) < 0) {



12 fprintf(stderr, "write failed (%s)\n", snd_strerror(err)); 
 
 13 } 
 
 14 
 
 15 return err; 
 
 16 } 
 
 17 
 
 18 main(int argc, char *argv[]) 
 
 19 { 
 
 20 
 
 21 snd_pcm_hw_params_t *hw_params; 
 
 22 snd_pcm_sw_params_t *sw_params; 
 
 23 snd_pcm_sframes_t frames_to_deliver; 
 
 24 int nfds; 
 
 25 int err; 
 
 26 struct pollfd *pfds; 
 
 27 
 
 28 if ((err = snd_pcm_open(&playback_handle, argv[1], SND_PCM_STREAM_PLAYBACK, 0) 
 
 29 ) < 0) { 
 
 30 ... 
 
 31 } 
 
 32 
 
 33 if ((err = snd_pcm_hw_params_malloc(&hw_params)) < 0) { 
 
 34 ... 
 
 35 } 
 
 36 
 
 37 if ((err = snd_pcm_hw_params_any(playback_handle, hw_params)) < 0) { 
 
 38 ... 
 
 39 } 
 
 40 
 
 41 if ((err = snd_pcm_hw_params_set_access(playback_handle, hw_params, 
 
 42 SND_PCM_ACCESS_RW_INTERLEAVED)) < 0) { 
 
 43 ... 
 
 44 } 
 
 45 
 
 46 if ((err = snd_pcm_hw_params_set_format(playback_handle, hw_params, 
 
 47 SND_PCM_FORMAT_S16_LE)) < 0) { 
 
 48 ... 
 
 49 } 
 
 50 
 
 51 if ((err = snd_pcm_hw_params_set_rate_near(playback_handle, hw_params, 44100, 
 
 52 0)) < 0) { 
 
 53 ... 
 
 54 } 
 
 55 
 
 56 if ((err = snd_pcm_hw_params_set_channels(playback_handle,hw_params,2))<0) { 
 
 57 ... 
 
 58 } 
 
 59 
 
 60 if ((err = snd_pcm_hw_params(playback_handle, hw_params)) < 0) { 
 
 61 ... 
 
 62 } 
 
 63 
 
 64 snd_pcm_hw_params_free(hw_params); 
 
 65 
 
 66 /* 告诉ALSA当4096个以上帧可以传递时唤醒我们 */



67 if ((err = snd_pcm_sw_params_malloc(&sw_params)) < 0) { 
 
 68 ... 
 
 69 } 
 
 70 if ((err = snd_pcm_sw_params_current(playback_handle, sw_params)) < 0) { 
 
 71 ... 
 
 72 } 
 
 73 /* 设置4096帧传递一次数据 */ 
 
 74 if ((err = snd_pcm_sw_params_set_avail_min(playback_handle, sw_params, 4096)) 
 
 75 < 0) { 
 
 76 ... 
 
 77 } 
 
 78 /* 一旦有数据就开始播放 */ 
 
 79 if ((err = snd_pcm_sw_params_set_start_threshold(playback_handle, sw_params, 
 
 80 0U)) < 0) { 
 
 81 ... 
 
 82 } 
 
 83 if ((err = snd_pcm_sw_params(playback_handle, sw_params)) < 0) { 
 
 84 ... 
 
 85 } 
 
 86 
 
 87 /* 每4096帧接口将中断内核，ALSA将很快唤醒本程序 */ 
 
 88 
 
 89 if ((err = snd_pcm_prepare(playback_handle)) < 0) { 
 
 90 ... 
 
 91 } 
 
 92 
 
 93 while (1) { 
 
 94 /* 等待，直到接口准备好传递数据，或者1s超时发生 */ 
 
 95 if ((err = snd_pcm_wait(playback_handle, 1000)) < 0) { 
 
 96 ... 
 
 97 } 
 
 98 
 
 99 /* 查出有多少空间可放置playback数据 */ 
 
 100 if ((frames_to_deliver = snd_pcm_avail_update(playback_handle)) < 0) { 
 
 101 if (frames_to_deliver == - EPIPE) { 
 
 102 fprintf(stderr, "an xrun occured\n"); 
 
 103 break; 
 
 104 } else { 
 
 105 fprintf(stderr, "unknown ALSA avail update return value (%d)\n", 
 
 106 frames_to_deliver); 
 
 107 break; 
 
 108 } 
 
 109 } 
 
 110 
 
 111 frames_to_deliver = frames_to_deliver > 4096 ? 4096 : frames_to_deliver; 
 
 112 
 
 113 /* 传递数据 */ 
 
 114 if (playback_callback(frames_to_deliver) != frames_to_deliver) { 
 
 115 ... 
 
 116 } 
 
 117 } 
 
 118 
 
 119 snd_pcm_close(playback_handle); 
 
 120 exit(0); 
 
 121 }



