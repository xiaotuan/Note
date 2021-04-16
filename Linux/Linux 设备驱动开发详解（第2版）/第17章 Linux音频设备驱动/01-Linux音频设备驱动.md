### 第17章 Linux音频设备驱动

在Linux系统中，先后出现了音频设备的3种框架：OSS、ALSA和ASoC，本节将在介绍数字音频设备及音频设备硬件接口的基础上讲解OSS、ALSA和ASoC驱动的结构。

17.1～17.2节讲解了音频设备及PCM、IIS和AC'97硬件接口。

17.3节讲解了Linux OSS音频设备驱动的组成、mixer接口、dsp接口及用户空间编程方法。

17.4节讲解了Linux ALSA音频设备驱动的组成、card和组件管理、PCM设备、control接口、AC'97 API及用户空间编程方法。

17.5节讲解了Linux ASoC音频设备驱动的组成，Codec、CPU DAI和板驱动。

17.6节以LDD6410开发板上S3C6410通过AC'97接口外接WM9714的实例讲解了ASoC驱动。



