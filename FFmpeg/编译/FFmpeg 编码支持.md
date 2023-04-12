`FFmpeg` 本身支持一些音视频编码格式、文件封装格式与流媒体传输协议，但是支持的数量依然有限，`FFmpeg` 所做的只是提供一套基础的框架，所有的编码格式、文件封装格式与流媒体协议均可以作为 `FFmpeg` 的一个模块挂载在 `FFmpeg` 框架中。这些模块以第三方的外部库的方式提供支持，可以通过 `FFmpeg` 源码的 `configure` 命令查看 `FFmpeg` 所支持的音频编码格式、文件封装格式与流媒体传输协议，对于 `FFmpeg` 不支持的格式，可以通过 `configure --help` 查看所需要的第三方外部库，然后通过证件对应的编译参数选项进行支持。帮助信息内容输出如下：

```shell
External library support:

  Using any of the following switches will allow FFmpeg to link to the
  corresponding external library. All the components depending on that library
  will become enabled, if all their other dependencies are met and they are not
  explicitly disabled. E.g. --enable-libopus will enable linking to
  libopus and allow the libopus encoder to be built, unless it is
  specifically disabled with --disable-encoder=libopus.

  Note that only the system libraries are auto-detected. All the other external
  libraries must be explicitly enabled.

  Also note that the following help text describes the purpose of the libraries
  themselves, not all their features will necessarily be usable by FFmpeg.

  --disable-alsa           disable ALSA support [autodetect]
  --disable-appkit         disable Apple AppKit framework [autodetect]
  --disable-avfoundation   disable Apple AVFoundation framework [autodetect]
  --enable-avisynth        enable reading of AviSynth script files [no]
  --disable-bzlib          disable bzlib [autodetect]
  --disable-coreimage      disable Apple CoreImage framework [autodetect]
  --enable-chromaprint     enable audio fingerprinting with chromaprint [no]
  --enable-frei0r          enable frei0r video filtering [no]
  --enable-gcrypt          enable gcrypt, needed for rtmp(t)e support
                           if openssl, librtmp or gmp is not used [no]
  --enable-gmp             enable gmp, needed for rtmp(t)e support
                           if openssl or librtmp is not used [no]
  --enable-gnutls          enable gnutls, needed for https support
                           if openssl, libtls or mbedtls is not used [no]
  --disable-iconv          disable iconv [autodetect]
  --enable-jni             enable JNI support [no]
  --enable-ladspa          enable LADSPA audio filtering [no]
  --enable-lcms2           enable ICC profile support via LittleCMS 2 [no]
  --enable-libaom          enable AV1 video encoding/decoding via libaom [no]
  --enable-libaribb24      enable ARIB text and caption decoding via libaribb24 [no]
  --enable-libaribcaption  enable ARIB text and caption decoding via libaribcaption [no]
  --enable-libass          enable libass subtitles rendering,
                           needed for subtitles and ass filter [no]
  --enable-libbluray       enable BluRay reading using libbluray [no]
  --enable-libbs2b         enable bs2b DSP library [no]
  --enable-libcaca         enable textual display using libcaca [no]
  --enable-libcelt         enable CELT decoding via libcelt [no]
  --enable-libcdio         enable audio CD grabbing with libcdio [no]
  --enable-libcodec2       enable codec2 en/decoding using libcodec2 [no]
  --enable-libdav1d        enable AV1 decoding via libdav1d [no]
  --enable-libdavs2        enable AVS2 decoding via libdavs2 [no]
  --enable-libdc1394       enable IIDC-1394 grabbing using libdc1394
                           and libraw1394 [no]
  --enable-libfdk-aac      enable AAC de/encoding via libfdk-aac [no]
  --enable-libflite        enable flite (voice synthesis) support via libflite [no]
  --enable-libfontconfig   enable libfontconfig, useful for drawtext filter [no]
  --enable-libfreetype     enable libfreetype, needed for drawtext filter [no]
  --enable-libfribidi      enable libfribidi, improves drawtext filter [no]
  --enable-libglslang      enable GLSL->SPIRV compilation via libglslang [no]
  --enable-libgme          enable Game Music Emu via libgme [no]
  --enable-libgsm          enable GSM de/encoding via libgsm [no]
  --enable-libiec61883     enable iec61883 via libiec61883 [no]
  --enable-libilbc         enable iLBC de/encoding via libilbc [no]
  --enable-libjack         enable JACK audio sound server [no]
  --enable-libjxl          enable JPEG XL de/encoding via libjxl [no]
  --enable-libklvanc       enable Kernel Labs VANC processing [no]
  --enable-libkvazaar      enable HEVC encoding via libkvazaar [no]
  --enable-liblensfun      enable lensfun lens correction [no]
  --enable-libmodplug      enable ModPlug via libmodplug [no]
  --enable-libmp3lame      enable MP3 encoding via libmp3lame [no]
  --enable-libopencore-amrnb enable AMR-NB de/encoding via libopencore-amrnb [no]
  --enable-libopencore-amrwb enable AMR-WB decoding via libopencore-amrwb [no]
  --enable-libopencv       enable video filtering via libopencv [no]
  --enable-libopenh264     enable H.264 encoding via OpenH264 [no]
  --enable-libopenjpeg     enable JPEG 2000 de/encoding via OpenJPEG [no]
  --enable-libopenmpt      enable decoding tracked files via libopenmpt [no]
  --enable-libopenvino     enable OpenVINO as a DNN module backend
                           for DNN based filters like dnn_processing [no]
  --enable-libopus         enable Opus de/encoding via libopus [no]
  --enable-libplacebo      enable libplacebo library [no]
  --enable-libpulse        enable Pulseaudio input via libpulse [no]
  --enable-librabbitmq     enable RabbitMQ library [no]
  --enable-librav1e        enable AV1 encoding via rav1e [no]
  --enable-librist         enable RIST via librist [no]
  --enable-librsvg         enable SVG rasterization via librsvg [no]
  --enable-librubberband   enable rubberband needed for rubberband filter [no]
  --enable-librtmp         enable RTMP[E] support via librtmp [no]
  --enable-libshaderc      enable GLSL->SPIRV compilation via libshaderc [no]
  --enable-libshine        enable fixed-point MP3 encoding via libshine [no]
  --enable-libsmbclient    enable Samba protocol via libsmbclient [no]
  --enable-libsnappy       enable Snappy compression, needed for hap encoding [no]
  --enable-libsoxr         enable Include libsoxr resampling [no]
  --enable-libspeex        enable Speex de/encoding via libspeex [no]
  --enable-libsrt          enable Haivision SRT protocol via libsrt [no]
  --enable-libssh          enable SFTP protocol via libssh [no]
  --enable-libsvtav1       enable AV1 encoding via SVT [no]
  --enable-libtensorflow   enable TensorFlow as a DNN module backend
                           for DNN based filters like sr [no]
  --enable-libtesseract    enable Tesseract, needed for ocr filter [no]
  --enable-libtheora       enable Theora encoding via libtheora [no]
  --enable-libtls          enable LibreSSL (via libtls), needed for https support
                           if openssl, gnutls or mbedtls is not used [no]
  --enable-libtwolame      enable MP2 encoding via libtwolame [no]
  --enable-libuavs3d       enable AVS3 decoding via libuavs3d [no]
  --enable-libv4l2         enable libv4l2/v4l-utils [no]
  --enable-libvidstab      enable video stabilization using vid.stab [no]
  --enable-libvmaf         enable vmaf filter via libvmaf [no]
  --enable-libvo-amrwbenc  enable AMR-WB encoding via libvo-amrwbenc [no]
  --enable-libvorbis       enable Vorbis en/decoding via libvorbis,
                           native implementation exists [no]
  --enable-libvpx          enable VP8 and VP9 de/encoding via libvpx [no]
  --enable-libwebp         enable WebP encoding via libwebp [no]
  --enable-libx264         enable H.264 encoding via x264 [no]
  --enable-libx265         enable HEVC encoding via x265 [no]
  --enable-libxavs         enable AVS encoding via xavs [no]
  --enable-libxavs2        enable AVS2 encoding via xavs2 [no]
  --enable-libxcb          enable X11 grabbing using XCB [autodetect]
  --enable-libxcb-shm      enable X11 grabbing shm communication [autodetect]
  --enable-libxcb-xfixes   enable X11 grabbing mouse rendering [autodetect]
  --enable-libxcb-shape    enable X11 grabbing shape rendering [autodetect]
  --enable-libxvid         enable Xvid encoding via xvidcore,
                           native MPEG-4/Xvid encoder exists [no]
  --enable-libxml2         enable XML parsing using the C library libxml2, needed
                           for dash and imf demuxing support [no]
  --enable-libzimg         enable z.lib, needed for zscale filter [no]
  --enable-libzmq          enable message passing via libzmq [no]
  --enable-libzvbi         enable teletext support via libzvbi [no]
  --enable-lv2             enable LV2 audio filtering [no]
  --disable-lzma           disable lzma [autodetect]
  --enable-decklink        enable Blackmagic DeckLink I/O support [no]
  --enable-mbedtls         enable mbedTLS, needed for https support
                           if openssl, gnutls or libtls is not used [no]
  --enable-mediacodec      enable Android MediaCodec support [no]
  --enable-mediafoundation enable encoding via MediaFoundation [auto]
  --disable-metal          disable Apple Metal framework [autodetect]
  --enable-libmysofa       enable libmysofa, needed for sofalizer filter [no]
  --enable-openal          enable OpenAL 1.1 capture support [no]
  --enable-opencl          enable OpenCL processing [no]
  --enable-opengl          enable OpenGL rendering [no]
  --enable-openssl         enable openssl, needed for https support
                           if gnutls, libtls or mbedtls is not used [no]
  --enable-pocketsphinx    enable PocketSphinx, needed for asr filter [no]
  --disable-sndio          disable sndio support [autodetect]
  --disable-schannel       disable SChannel SSP, needed for TLS support on
                           Windows if openssl and gnutls are not used [autodetect]
  --disable-sdl2           disable sdl2 [autodetect]
  --disable-securetransport disable Secure Transport, needed for TLS support
                           on OSX if openssl and gnutls are not used [autodetect]
  --enable-vapoursynth     enable VapourSynth demuxer [no]
  --disable-vulkan         disable Vulkan code [autodetect]
  --disable-xlib           disable xlib [autodetect]
  --disable-zlib           disable zlib [autodetect]

  The following libraries provide various hardware acceleration features:
  --disable-amf            disable AMF video encoding code [autodetect]
  --disable-audiotoolbox   disable Apple AudioToolbox code [autodetect]
  --enable-cuda-nvcc       enable Nvidia CUDA compiler [no]
  --disable-cuda-llvm      disable CUDA compilation using clang [autodetect]
  --disable-cuvid          disable Nvidia CUVID support [autodetect]
  --disable-d3d11va        disable Microsoft Direct3D 11 video acceleration code [autodetect]
  --disable-dxva2          disable Microsoft DirectX 9 video acceleration code [autodetect]
  --disable-ffnvcodec      disable dynamically linked Nvidia code [autodetect]
  --enable-libdrm          enable DRM code (Linux) [no]
  --enable-libmfx          enable Intel MediaSDK (AKA Quick Sync Video) code via libmfx [no]
  --enable-libvpl          enable Intel oneVPL code via libvpl if libmfx is not used [no]
  --enable-libnpp          enable Nvidia Performance Primitives-based code [no]
  --enable-mmal            enable Broadcom Multi-Media Abstraction Layer (Raspberry Pi) via MMAL [no]
  --disable-nvdec          disable Nvidia video decoding acceleration (via hwaccel) [autodetect]
  --disable-nvenc          disable Nvidia video encoding code [autodetect]
  --enable-omx             enable OpenMAX IL code [no]
  --enable-omx-rpi         enable OpenMAX IL code for Raspberry Pi [no]
  --enable-rkmpp           enable Rockchip Media Process Platform code [no]
  --disable-v4l2-m2m       disable V4L2 mem2mem code [autodetect]
  --disable-vaapi          disable Video Acceleration API (mainly Unix/Intel) code [autodetect]
  --disable-vdpau          disable Nvidia Video Decode and Presentation API for Unix code [autodetect]
  --disable-videotoolbox   disable VideoToolbox code [autodetect]
```

`FFmpeg` 所支持的外部库相对来说比较多，主要包含如下列表：

```
bzip2 1.0.6 <http://bzip.org/>
Fontconfig 2.11.94 <http://freedesktop.org/wiki/Software/fontconfig>
Frei0r 20130909-git-10d8360 <http://frei0r.dyne.org/>
GnuTLS 3.3.15 <http://gnutls.org/>
libiconv 1.14 <http://gnu.org/software/libiconv/>
libass 0.12.2 <http://code.google.com/p/libass/>
libbluray 0.8.1 <http://videolan.org/developers/libbluray.html>
libbs2b 3.1.0 <http://bs2b.sourceforge.net/>
libcaca 0.99.beta18 <http://caca.zoy.org/wiki/libcaca>
dcadec 20150506-git-98fb3b6 <https://github.com/foo86/dcadec>
FreeType 2.5.5 <http://freetype.sourceforge.net/>
Game Music Emu 0.6.0 <http://code.google.com/p/game-music-emu/>
GSM 1.0.13-4 <http://packages.debian.org/source/squeeze/libgsm>
iLBC 20141214-git-ef04ebe <https://github.com/dekkers/libilbc/>
Modplug-XMMS 0.8.8.5 <http://modplug-xmms.sourceforge.net/>
LAME 3.99.5 <http://lame.sourceforge.net/>
OpenCORE AMR 0.1.3 <http://sourceforge.net/projects/opencore-amr/>
OpenJPEG 1.5.2 <http://www.openjpeg.org/>
Opus 1.1 <http://opus-codec.org/>
RTMPDump 20140707-git-a1900c3 <http://rtmpdump.mplayerhq.hu/>
Schroedinger 1.0.11 <http://diracvideo.org/>
libsoxr 0.1.1 <http://sourceforge.net/projects/soxr/>
Speex 1.2rc2 <http://speex.org/>
Theora 1.1.1 <http://theora.org/>
TwoLAME 0.3.13 <http://twolame.org/>
vid.stab 0.98 <http://public.hronopik.de/vid.stab/>
VisualOn AAC 0.1.3 <https://github.com/mstorsjo/vo-aacenc>
VisualOn AMR-WB 0.1.2 <https://github.com/mstorsjo/vo-amrwbenc>
Vorbis 1.3.5 <http://vorbis.com/>
vpx 1.4.0 <http://webmproject.org/>
WavPack 4.75.0 <http://wavpack.com/>
WebP 0.4.3 <https://developers.google.com/speed/webp/>
x264 20150223-git-121396c <http://videolan.org/developers/x264.html>
x265 1.7 <http://x265.org/>
XAVS svn-r55 <http://xavs.sourceforge.net/>
Xvid 1.3.3 <http://xvid.org/>
XZ Utils 5.2.1 <http://tukaani.org/xz>
zlib 1.2.8 <http://zlib.net/>
```

