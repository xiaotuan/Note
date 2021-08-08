`iOS` 多媒体播放组件包含：`VideoToolBox`、`AudioToolBox`、`AVPlayer` 等，下面分别进行介绍：

+ `VideoToolBox`：它是一个底层框架，提供对硬件编码器和解码器的直接访问。它为视频压缩和解压缩提供服务，并用于 `CoreVideo` 像素缓冲区中存储的栅格之间的转换。这些服务是以会话对象的形式（压缩、解压缩和像素传输），作为核心基础（CF）类型提供的。不需要直接访问硬件编码器和解码器的应用程序都不需要直接使用 `VideoToolBox`。
+ `AudioToolBox`：这个框架可以将比较短的声音注册到 `System Sound` 服务上。注册到 `System Sound` 服务上的声音被称为 `System Sounds`。它必须满足下面几个条件：
  + 播放时间不能超过 30s。
  + 数据必须是 PCM 或者 IMA4 流格式的。
  + 必须被打包成下面 3 种格式之一：Core Audio Format（.caf）、Waveform Audio（.wav）或者 Audio Interchange File（.aiff）。
+ `AVPlayer`：`AVPlayer` 既可以用来播放音频也可以用来播放视频，在使用 `AVPlayer` 的时候，我们需要导入 `AVFoundation.framework` 框架，再引入头文件 `#import<AVFoundation/AVFoundation.h>`。

