`FFmpeg` 源代码中可以包含的编码非常多，常见的和不常见的都可以在编译配置列表中见到，可以通过使用编译配置命令 `./configure --list-encoders` 参数来查看：

```shell
$ ./configure --list-encoders 
a64multi                cfhd                    hevc_v4l2m2m            mjpeg_qsv               pcm_s32le_planar        speedhq
a64multi5               cinepak                 hevc_vaapi              mjpeg_vaapi             pcm_s64be               srt
aac                     cljr                    hevc_videotoolbox       mlp                     pcm_s64le               ssa
aac_at                  comfortnoise            huffyuv                 movtext                 pcm_s8                  subrip
aac_mf                  dca                     ilbc_at                 mp2                     pcm_s8_planar           sunrast
ac3                     dfpwm                   jpeg2000                mp2fixed                pcm_u16be               svq1
ac3_fixed               dnxhd                   jpegls                  mp3_mf                  pcm_u16le               targa
ac3_mf                  dpx                     libaom_av1              mpeg1video              pcm_u24be               text
adpcm_adx               dvbsub                  libcodec2               mpeg2_qsv               pcm_u24le               tiff
adpcm_argo              dvdsub                  libfdk_aac              mpeg2_vaapi             pcm_u32be               truehd
adpcm_g722              dvvideo                 libgsm                  mpeg2video              pcm_u32le               tta
adpcm_g726              eac3                    libgsm_ms               mpeg4                   pcm_u8                  ttml
adpcm_g726le            exr                     libilbc                 mpeg4_mediacodec        pcm_vidc                utvideo
adpcm_ima_alp           ffv1                    libjxl                  mpeg4_omx               pcx                     v210
adpcm_ima_amv           ffvhuff                 libkvazaar              mpeg4_v4l2m2m           pfm                     v308
adpcm_ima_apm           fits                    libmp3lame              msmpeg4v2               pgm                     v408
adpcm_ima_qt            flac                    libopencore_amrnb       msmpeg4v3               pgmyuv                  v410
adpcm_ima_ssi           flashsv                 libopenh264             msvideo1                phm                     vbn
adpcm_ima_wav           flashsv2                libopenjpeg             nellymoser              png                     vc2
adpcm_ima_ws            flv                     libopus                 opus                    ppm                     vnull
adpcm_ms                g723_1                  librav1e                pam                     prores                  vorbis
adpcm_swf               gif                     libshine                pbm                     prores_aw               vp8_v4l2m2m
adpcm_yamaha            h261                    libspeex                pcm_alaw                prores_ks               vp8_vaapi
alac                    h263                    libsvtav1               pcm_alaw_at             prores_videotoolbox     vp9_mediacodec
alac_at                 h263_v4l2m2m            libtheora               pcm_bluray              qoi                     vp9_qsv
alias_pix               h263p                   libtwolame              pcm_dvd                 qtrle                   vp9_vaapi
amv                     h264_amf                libvo_amrwbenc          pcm_f32be               r10k                    wavpack
anull                   h264_mediacodec         libvorbis               pcm_f32le               r210                    wbmp
apng                    h264_mf                 libvpx_vp8              pcm_f64be               ra_144                  webvtt
aptx                    h264_nvenc              libvpx_vp9              pcm_f64le               rawvideo                wmav1
aptx_hd                 h264_omx                libwebp                 pcm_mulaw               roq                     wmav2
ass                     h264_qsv                libwebp_anim            pcm_mulaw_at            roq_dpcm                wmv1
asv1                    h264_v4l2m2m            libx262                 pcm_s16be               rpza                    wmv2
asv2                    h264_vaapi              libx264                 pcm_s16be_planar        rv10                    wrapped_avframe
av1_amf                 h264_videotoolbox       libx264rgb              pcm_s16le               rv20                    xbm
av1_nvenc               hap                     libx265                 pcm_s16le_planar        s302m                   xface
av1_qsv                 hdr                     libxavs                 pcm_s24be               sbc                     xsub
avrp                    hevc_amf                libxavs2                pcm_s24daud             sgi                     xwd
avui                    hevc_mediacodec         libxvid                 pcm_s24le               smc                     y41p
ayuv                    hevc_mf                 ljpeg                   pcm_s24le_planar        snow                    yuv4
bitpacked               hevc_nvenc              magicyuv                pcm_s32be               sonic                   zlib
bmp                     hevc_qsv                mjpeg                   pcm_s32le               sonic_ls                zmbv
```

