[toc]

### 1. 测试命令

```shell
run vts -m VtsHalMediaOmxV1_0TargetMasterTest -t PerInstance/MasterHidlTest#ListNodes/0_default
```

### 2. 报错信息

```
hardware/interfaces/media/omx/1.0/vts/functional/master/VtsHalMediaOmxV1_0TargetMasterTest.cpp:407: Failure
Expected equality of these values:
status
Which is: NO_MEMORY
android::hardware::media::omx::V1_0::Status::OK
Which is: OK
```

### 3. 原因分析

这是由于设备部支持 wma 音频格式造成的，去掉 wma 音频格式即可。

### 4. 解决办法

#### 4.1 MTK 平台

修改 `device/mediatek/mt6771/mtk_omx_core_tablet.cfg` 文件的如下内容：

```diff
@@ -7,8 +7,6 @@ OMX.MTK.VIDEO.DECODER.VPX   video_decoder.vp8   libMtkOmxVdecEx.so  16
 OMX.MTK.VIDEO.DECODER.VP9   video_decoder.vp9   libMtkOmxVdecEx.so  16
 OMX.MTK.VIDEO.DECODER.VC1   video_decoder.vc1   libMtkOmxVdecEx.so  16
 OMX.MTK.AUDIO.DECODER.MP3   audio_decoder.mp3   libMtkOmxMp3Dec.so  32
-OMX.MTK.AUDIO.DECODER.WMA   audio_decoder.wma   libMtkOmxWmaDec.so  32
-OMX.MTK.AUDIO.DECODER.WMAPRO   audio_decoder.wma   libMtkOmxWmaProDec.so  32
 OMX.MTK.VIDEO.ENCODER.AVC   video_encoder.avc   libMtkOmxVenc.so    16
 OMX.MTK.VIDEO.ENCODER.H263  video_encoder.h263  libMtkOmxVenc.so    16
 OMX.MTK.VIDEO.ENCODER.MPEG4 video_encoder.mpeg4 libMtkOmxVenc.so    16
```

