`FFmpeg` 默认支持的音视频编码格式、文件封装格式和流媒体传输协议相对来说比较多，因此编译出来的 `FFmpeg` 体积比较大，在有些应用场景中，并不需要 `FFmpeg` 所支持的一些编码、封装或者协议，可以通过 `./configure --help` 查看一些有用的裁剪操作，输出如下：

```shell
Individual component options:
    --disable-everything        disable all components listed below
    --disable-encoder=NAME      disable encoder NAME
    --enable-encoder=NAME       enable encoder NAME
    --disable-encoders  disable all encoders
    --disable-decoder=NAME      disable decoder NAME
    --enable-decoder=NAME       enable decoder NAME
    --disable-decoders  disable all decoders
    --disable-hwaccel=NAME      disable hwaccel NAME
    --enable-hwaccel=NAME       enable hwaccel NAME
    --disable-hwaccels  disable all hwaccels
    --disable-muxer=NAME        disable muxer NAME
    --enable-muxer=NAME enable muxer NAME
    --disable-muxers    disable all muxers
    --disable-demuxer=NAME      disable demuxer NAME
    --enable-demuxer=NAME       enable demuxer NAME
    --disable-demuxers  disable all demuxers
    --enable-parser=NAME        enable parser NAME
    --disable-parser=NAME       disable parser NAME
    --disable-parsers   disable all parsers
    --enable-bsf=NAME   enable bitstream filter NAME
    --disable-bsf=NAME  disable bitstream filter NAME
    --disable-bsfs      disable all bitstream filters
    --enable-protocol=NAME      enable protocol NAME
    --disable-protocol=NAME     disable protocol NAME
    --disable-protocols disable all protocols
    --enable-indev=NAME enable input device NAME
    --disable-indev=NAME        disable input device NAME
    --disable-indevs    disable input devices
    --enable-outdev=NAME        enable output device NAME
    --disable-outdev=NAME       disable output device NAME
    --disable-outdevs   disable output devices
    --disable-devices   disable all devices
    --enable-filter=NAME        enable filter NAME
    --disable-filter=NAME       disable filter NAME
    --disable-filters   disable all filters
```

可以通过这些选项关闭不需要用到的编码、封装与协议等模块，验证方法如下：

```shell
./configure --disable-encoders --disable-decoders --disable-hwaccels --disable-muxers --disable-demuxers --disable-parsers --disable-bsfs --disable-protocols --disable-indevs --disable-devices --disable-filters
```

关闭所有的模块之后，可以看到 `FFmpeg` 的编译配置项输出信息几乎为空，输出信息具体如下：

```shell
External libraries:
iconv   sdl2    videotoolbox    zlib
sdl     securetransport xlib

External libraries providing hardware acceleration:
audiotoolbox    vda     videotoolbox_hwaccel

Libraries:
avcodec avfilter        avutil  swscale
avdevice        avformat        swresample

Programs:
ffmpeg  ffplay  ffprobe ffserver

Enabled decoders:
Enabled encoders:
Enabled hwaccels:
Enabled parsers:
Enabled demuxers:
asf     mov     mpegts  rm      rtsp

Enabled muxers:
ffm

Enabled protocols:
http    rtp     tcp     udp

Enabled filters:
aformat crop    null    trim
anull   format  rotate  vflip
atrim   hflip   transpose

Enabled bsfs:
Enabled indevs:
Enabled outdevs:
License: LGPL version 2.1 or later
Creating configuration files ...
```

而且在关闭所有的模块之后，可以根据定制支持自己所需要的模块，例如希望支持 H.264 视频编码、AAC 音频编码、封装为 MP4，可以通过如下方法进行支持：

```shell
 ./configure --disable-filters --disable-encoders --disable-decoders --disable-hwaccels --disable-muxers --disable-demuxers --disable-parsers --disable-bsfs --disable-protocols --disable-indevs --disable-devices  --enable-libx264 --enable-libfdk-aac --enable-gpl --enable-nonfree --enable-muxer=mp4
```

