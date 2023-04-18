`FFmpeg` 的解封装（Demuxing）是指将读入的容器格式拆解开，将里面压缩的音频流、视频流、字幕流、数据流等提取出来，如果要查看 `FFmpeg` 的源代码中都可以支持哪些输入的容器格式，可以通过命令 `./configure --list-demuxers` 来查看：

```shell
$ ./configure --list-demuxers 
aa                      cdxl                    iff                     libopenmpt              pcm_s16be               srt
aac                     cine                    ifv                     live_flv                pcm_s16le               stl
aax                     codec2                  ilbc                    lmlm4                   pcm_s24be               str
ac3                     codec2raw               image2                  loas                    pcm_s24le               subviewer
ace                     concat                  image2_alias_pix        lrc                     pcm_s32be               subviewer1
acm                     dash                    image2_brender_pix      luodat                  pcm_s32le               sup
act                     data                    image2pipe              lvf                     pcm_s8                  svag
adf                     daud                    image_bmp_pipe          lxf                     pcm_u16be               svs
adp                     dcstr                   image_cri_pipe          m4v                     pcm_u16le               swf
ads                     derf                    image_dds_pipe          matroska                pcm_u24be               tak
adx                     dfa                     image_dpx_pipe          mca                     pcm_u24le               tedcaptions
aea                     dfpwm                   image_exr_pipe          mcc                     pcm_u32be               thp
afc                     dhav                    image_gem_pipe          mgsts                   pcm_u32le               threedostr
aiff                    dirac                   image_gif_pipe          microdvd                pcm_u8                  tiertexseq
aix                     dnxhd                   image_hdr_pipe          mjpeg                   pcm_vidc                tmv
alp                     dsf                     image_j2k_pipe          mjpeg_2000              pjs                     truehd
amr                     dsicin                  image_jpeg_pipe         mlp                     pmp                     tta
amrnb                   dss                     image_jpegls_pipe       mlv                     pp_bnk                  tty
amrwb                   dts                     image_jpegxl_pipe       mm                      pva                     txd
anm                     dtshd                   image_pam_pipe          mmf                     pvf                     ty
apac                    dv                      image_pbm_pipe          mods                    qcp                     v210
apc                     dvbsub                  image_pcx_pipe          moflex                  r3d                     v210x
ape                     dvbtxt                  image_pfm_pipe          mov                     rawvideo                vag
apm                     dxa                     image_pgm_pipe          mp3                     realtext                vapoursynth
apng                    ea                      image_pgmyuv_pipe       mpc                     redspark                vc1
aptx                    ea_cdata                image_pgx_pipe          mpc8                    rka                     vc1t
aptx_hd                 eac3                    image_phm_pipe          mpegps                  rl2                     vividas
aqtitle                 epaf                    image_photocd_pipe      mpegts                  rm                      vivo
argo_asf                ffmetadata              image_pictor_pipe       mpegtsraw               roq                     vmd
argo_brp                filmstrip               image_png_pipe          mpegvideo               rpl                     vobsub
argo_cvg                fits                    image_ppm_pipe          mpjpeg                  rsd                     voc
asf                     flac                    image_psd_pipe          mpl2                    rso                     vpk
asf_o                   flic                    image_qdraw_pipe        mpsub                   rtp                     vplayer
ass                     flv                     image_qoi_pipe          msf                     rtsp                    vqf
ast                     fourxm                  image_sgi_pipe          msnwc_tcp               s337m                   w64
au                      frm                     image_sunrast_pipe      msp                     sami                    wady
av1                     fsb                     image_svg_pipe          mtaf                    sap                     wav
avi                     fwse                    image_tiff_pipe         mtv                     sbc                     wavarc
avisynth                g722                    image_vbn_pipe          musx                    sbg                     wc3
avr                     g723_1                  image_webp_pipe         mv                      scc                     webm_dash_manifest
avs                     g726                    image_xbm_pipe          mvi                     scd                     webvtt
avs2                    g726le                  image_xpm_pipe          mxf                     sdns                    wsaud
avs3                    g729                    image_xwd_pipe          mxg                     sdp                     wsd
bethsoftvid             gdv                     imf                     nc                      sdr2                    wsvqa
bfi                     genh                    ingenient               nistsphere              sds                     wtv
bfstm                   gif                     ipmovie                 nsp                     sdx                     wv
bink                    gsm                     ipu                     nsv                     segafilm                wve
binka                   gxf                     ircam                   nut                     ser                     xa
bintext                 h261                    iss                     nuv                     sga                     xbin
bit                     h263                    iv8                     obu                     shorten                 xmd
bitpacked               h264                    ivf                     ogg                     siff                    xmv
bmv                     hca                     ivr                     oma                     simbiosis_imx           xvag
boa                     hcom                    jacosub                 paf                     sln                     xwma
bonk                    hevc                    jv                      pcm_alaw                smacker                 yop
brstm                   hls                     kux                     pcm_f32be               smjpeg                  yuv4mpegpipe
c93                     hnm                     kvag                    pcm_f32le               smush
caf                     ico                     laf                     pcm_f64be               sol
cavsvideo               idcin                   libgme                  pcm_f64le               sox
cdg                     idf                     libmodplug              pcm_mulaw               spdif
```

