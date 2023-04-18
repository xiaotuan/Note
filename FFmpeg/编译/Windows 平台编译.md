`FFmpeg` 在 `Windows` 平台中的编译需要使用 `MinGW-w64`，`MinGW` 是 `Minimalist GNU for Windows` 的缩写，它提供了一系列的工具链来辅助编译 `Windows` 的本地化程序，它的详细介绍和安装方法可以参照 <http://www.mingw.org/>。如果不希望使用 `MinGW` 而使用 `Visual Studio` 的话，则需要消化很多时间来支持 `Visual Studio` 平台。

`MinGW-w64` 单独使用起来会比较麻烦，但是其可以与 `MSYS` 环境配合使用， `MSYS` 是 `Minimal SYStem` 的缩写，其主要完成的工作为 `UNIX on Windows` 的功能。显而易见，这是一个仿生 UNIX 环境的 Windows 工具集，它的详细介绍和使用方法可以参照 <http://www.mingw.org/wiki/MSYS`。

下面是编译步骤：

（1）进入 `FFmpeg` 源码目录，执行 `./configure`，如果以前正常，我们会看到如下信息：

```shell
$ ./configure 
install prefix            /usr/local
source path               .
C compiler                gcc
C library                 glibc
ARCH                      x86 (generic)
big-endian                no
runtime cpu detection     yes
standalone assembly       yes
x86 assembler             nasm
MMX enabled               yes
MMXEXT enabled            yes
3DNow! enabled            yes
3DNow! extended enabled   yes
SSE enabled               yes
SSSE3 enabled             yes
AESNI enabled             yes
AVX enabled               yes
AVX2 enabled              yes
AVX-512 enabled           yes
AVX-512ICL enabled        yes
XOP enabled               yes
FMA3 enabled              yes
FMA4 enabled              yes
i686 features enabled     yes
CMOV is fast              yes
EBX available             yes
EBP available             yes
debug symbols             yes
strip symbols             yes
optimize for size         no
optimizations             yes
static                    yes
shared                    no
postprocessing support    no
network support           yes
threading support         pthreads
safe bitstream reader     yes
texi2html enabled         no
perl enabled              yes
pod2man enabled           yes
makeinfo enabled          no
makeinfo supports HTML    no
xmllint enabled           no

External libraries:
iconv

External libraries providing hardware acceleration:
v4l2_m2m

Libraries:
avcodec                 avformat                swscale
avdevice                avutil
avfilter                swresample

Programs:
ffmpeg                  ffprobe

Enabled decoders:
aac                     ffv1                    pcm_vidc
aac_fixed               ffvhuff                 pcx
aac_latm                ffwavesynth             pfm
aasc                    fic                     pgm
ac3                     fits                    pgmyuv
ac3_fixed               flac                    pgssub
acelp_kelvin            flic                    pgx
adpcm_4xm               flv                     phm
adpcm_adx               fmvc                    photocd
adpcm_afc               fourxm                  pictor
adpcm_agm               fraps                   pixlet
adpcm_aica              frwu                    pjs
adpcm_argo              ftr                     ppm
adpcm_ct                g723_1                  prores
adpcm_dtk               g729                    prosumer
adpcm_ea                gdv                     psd
adpcm_ea_maxis_xa       gem                     ptx
adpcm_ea_r1             gif                     qcelp
adpcm_ea_r2             gremlin_dpcm            qdm2
adpcm_ea_r3             gsm                     qdmc
adpcm_ea_xas            gsm_ms                  qdraw
adpcm_g722              h261                    qoi
adpcm_g726              h263                    qpeg
adpcm_g726le            h263_v4l2m2m            qtrle
adpcm_ima_acorn         h263i                   r10k
adpcm_ima_alp           h263p                   r210
adpcm_ima_amv           h264                    ra_144
adpcm_ima_apc           h264_v4l2m2m            ra_288
adpcm_ima_apm           hap                     ralf
adpcm_ima_cunning       hca                     rawvideo
adpcm_ima_dat4          hcom                    realtext
adpcm_ima_dk3           hdr                     rka
adpcm_ima_dk4           hevc                    rl2
adpcm_ima_ea_eacs       hnm4_video              roq
adpcm_ima_ea_sead       hq_hqa                  roq_dpcm
adpcm_ima_iss           hqx                     rpza
adpcm_ima_moflex        huffyuv                 rv10
adpcm_ima_mtf           hymt                    rv20
adpcm_ima_oki           iac                     rv30
adpcm_ima_qt            idcin                   rv40
adpcm_ima_rad           idf                     s302m
adpcm_ima_smjpeg        iff_ilbm                sami
adpcm_ima_ssi           ilbc                    sanm
adpcm_ima_wav           imc                     sbc
adpcm_ima_ws            imm4                    scpr
adpcm_ms                imm5                    sdx2_dpcm
adpcm_mtaf              indeo2                  sga
adpcm_psx               indeo3                  sgi
adpcm_sbpro_2           indeo4                  sgirle
adpcm_sbpro_3           indeo5                  sheervideo
adpcm_sbpro_4           interplay_acm           shorten
adpcm_swf               interplay_dpcm          simbiosis_imx
adpcm_thp               interplay_video         sipr
adpcm_thp_le            ipu                     siren
adpcm_vima              jacosub                 smackaud
adpcm_xa                jpeg2000                smacker
adpcm_xmd               jpegls                  smc
adpcm_yamaha            jv                      smvjpeg
adpcm_zork              kgv1                    snow
agm                     kmvc                    sol_dpcm
aic                     lagarith                sonic
alac                    loco                    sp5x
alias_pix               m101                    speedhq
als                     mace3                   speex
amrnb                   mace6                   srt
amrwb                   magicyuv                ssa
amv                     mdec                    stl
anm                     media100                subrip
ansi                    metasound               subviewer
anull                   microdvd                subviewer1
apac                    mimic                   sunrast
ape                     misc4                   svq1
aptx                    mjpeg                   svq3
aptx_hd                 mjpegb                  tak
arbc                    mlp                     targa
argo                    mmvideo                 targa_y216
ass                     mobiclip                text
asv1                    motionpixels            theora
asv2                    movtext                 thp
atrac1                  mp1                     tiertexseqvideo
atrac3                  mp1float                tiff
atrac3al                mp2                     tmv
atrac3p                 mp2float                truehd
atrac3pal               mp3                     truemotion1
atrac9                  mp3adu                  truemotion2
aura                    mp3adufloat             truemotion2rt
aura2                   mp3float                truespeech
av1                     mp3on4                  tscc2
avrn                    mp3on4float             tta
avrp                    mpc7                    twinvq
avs                     mpc8                    txd
avui                    mpeg1_v4l2m2m           ulti
ayuv                    mpeg1video              utvideo
bethsoftvid             mpeg2_v4l2m2m           v210
bfi                     mpeg2video              v210x
bink                    mpeg4                   v308
binkaudio_dct           mpeg4_v4l2m2m           v408
binkaudio_rdft          mpegvideo               v410
bintext                 mpl2                    vb
bitpacked               msa1                    vble
bmp                     msmpeg4v1               vbn
bmv_audio               msmpeg4v2               vc1
bmv_video               msmpeg4v3               vc1_v4l2m2m
bonk                    msnsiren                vc1image
brender_pix             msp2                    vcr1
c93                     msrle                   vmdaudio
cavs                    mss1                    vmdvideo
cbd2_dpcm               mss2                    vmnc
ccaption                msvideo1                vnull
cdgraphics              mszh                    vorbis
cdtoons                 mts2                    vp3
cdxl                    mv30                    vp4
cfhd                    mvc1                    vp5
cinepak                 mvc2                    vp6
clearvideo              mvdv                    vp6a
cljr                    mxpeg                   vp6f
cllc                    nellymoser              vp7
comfortnoise            notchlc                 vp8
cook                    nuv                     vp8_v4l2m2m
cpia                    on2avc                  vp9
cri                     opus                    vplayer
cscd                    paf_audio               vqa
cyuv                    paf_video               vqc
dca                     pam                     wady_dpcm
dds                     pbm                     wavarc
derf_dpcm               pcm_alaw                wavpack
dfa                     pcm_bluray              wbmp
dfpwm                   pcm_dvd                 webp
dirac                   pcm_f16le               webvtt
dnxhd                   pcm_f24le               wmalossless
dolby_e                 pcm_f32be               wmapro
dpx                     pcm_f32le               wmav1
dsd_lsbf                pcm_f64be               wmav2
dsd_lsbf_planar         pcm_f64le               wmavoice
dsd_msbf                pcm_lxf                 wmv1
dsd_msbf_planar         pcm_mulaw               wmv2
dsicinaudio             pcm_s16be               wmv3
dsicinvideo             pcm_s16be_planar        wmv3image
dss_sp                  pcm_s16le               wnv1
dst                     pcm_s16le_planar        wrapped_avframe
dvaudio                 pcm_s24be               ws_snd1
dvbsub                  pcm_s24daud             xan_dpcm
dvdsub                  pcm_s24le               xan_wc3
dvvideo                 pcm_s24le_planar        xan_wc4
dxtory                  pcm_s32be               xbin
dxv                     pcm_s32le               xbm
eac3                    pcm_s32le_planar        xface
eacmv                   pcm_s64be               xl
eamad                   pcm_s64le               xma1
eatgq                   pcm_s8                  xma2
eatgv                   pcm_s8_planar           xpm
eatqi                   pcm_sga                 xsub
eightbps                pcm_u16be               xwd
eightsvx_exp            pcm_u16le               y41p
eightsvx_fib            pcm_u24be               ylc
escape124               pcm_u24le               yop
escape130               pcm_u32be               yuv4
evrc                    pcm_u32le               zero12v
fastaudio               pcm_u8

Enabled encoders:
a64multi                hdr                     ppm
a64multi5               huffyuv                 prores
aac                     jpeg2000                prores_aw
ac3                     jpegls                  prores_ks
ac3_fixed               ljpeg                   qoi
adpcm_adx               magicyuv                qtrle
adpcm_argo              mjpeg                   r10k
adpcm_g722              mlp                     r210
adpcm_g726              movtext                 ra_144
adpcm_g726le            mp2                     rawvideo
adpcm_ima_alp           mp2fixed                roq
adpcm_ima_amv           mpeg1video              roq_dpcm
adpcm_ima_apm           mpeg2video              rpza
adpcm_ima_qt            mpeg4                   rv10
adpcm_ima_ssi           mpeg4_v4l2m2m           rv20
adpcm_ima_wav           msmpeg4v2               s302m
adpcm_ima_ws            msmpeg4v3               sbc
adpcm_ms                msvideo1                sgi
adpcm_swf               nellymoser              smc
adpcm_yamaha            opus                    snow
alac                    pam                     sonic
alias_pix               pbm                     sonic_ls
amv                     pcm_alaw                speedhq
anull                   pcm_bluray              srt
aptx                    pcm_dvd                 ssa
aptx_hd                 pcm_f32be               subrip
ass                     pcm_f32le               sunrast
asv1                    pcm_f64be               svq1
asv2                    pcm_f64le               targa
avrp                    pcm_mulaw               text
avui                    pcm_s16be               tiff
ayuv                    pcm_s16be_planar        truehd
bitpacked               pcm_s16le               tta
bmp                     pcm_s16le_planar        ttml
cfhd                    pcm_s24be               utvideo
cinepak                 pcm_s24daud             v210
cljr                    pcm_s24le               v308
comfortnoise            pcm_s24le_planar        v408
dca                     pcm_s32be               v410
dfpwm                   pcm_s32le               vbn
dnxhd                   pcm_s32le_planar        vc2
dpx                     pcm_s64be               vnull
dvbsub                  pcm_s64le               vorbis
dvdsub                  pcm_s8                  vp8_v4l2m2m
dvvideo                 pcm_s8_planar           wavpack
eac3                    pcm_u16be               wbmp
ffv1                    pcm_u16le               webvtt
ffvhuff                 pcm_u24be               wmav1
fits                    pcm_u24le               wmav2
flac                    pcm_u32be               wmv1
flv                     pcm_u32le               wmv2
g723_1                  pcm_u8                  wrapped_avframe
gif                     pcm_vidc                xbm
h261                    pcx                     xface
h263                    pfm                     xsub
h263_v4l2m2m            pgm                     xwd
h263p                   pgmyuv                  y41p
h264_v4l2m2m            phm                     yuv4

Enabled hwaccels:

Enabled parsers:
aac                     dvdsub                  opus
aac_latm                flac                    png
ac3                     ftr                     pnm
adx                     g723_1                  qoi
amr                     g729                    rv30
av1                     gif                     rv40
avs2                    gsm                     sbc
avs3                    h261                    sipr
bmp                     h263                    tak
cavsvideo               h264                    vc1
cook                    hdr                     vorbis
cri                     hevc                    vp3
dca                     ipu                     vp8
dirac                   jpeg2000                vp9
dnxhd                   misc4                   webp
dolby_e                 mjpeg                   xbm
dpx                     mlp                     xma
dvaudio                 mpeg4video              xwd
dvbsub                  mpegaudio
dvd_nav                 mpegvideo

Enabled demuxers:
aa                      idf                     pcm_s16be
aac                     iff                     pcm_s16le
aax                     ifv                     pcm_s24be
ac3                     ilbc                    pcm_s24le
ace                     image2                  pcm_s32be
acm                     image2_alias_pix        pcm_s32le
act                     image2_brender_pix      pcm_s8
adf                     image2pipe              pcm_u16be
adp                     image_bmp_pipe          pcm_u16le
ads                     image_cri_pipe          pcm_u24be
adx                     image_dds_pipe          pcm_u24le
aea                     image_dpx_pipe          pcm_u32be
afc                     image_exr_pipe          pcm_u32le
aiff                    image_gem_pipe          pcm_u8
aix                     image_gif_pipe          pcm_vidc
alp                     image_hdr_pipe          pjs
amr                     image_j2k_pipe          pmp
amrnb                   image_jpeg_pipe         pp_bnk
amrwb                   image_jpegls_pipe       pva
anm                     image_jpegxl_pipe       pvf
apac                    image_pam_pipe          qcp
apc                     image_pbm_pipe          r3d
ape                     image_pcx_pipe          rawvideo
apm                     image_pfm_pipe          realtext
apng                    image_pgm_pipe          redspark
aptx                    image_pgmyuv_pipe       rka
aptx_hd                 image_pgx_pipe          rl2
aqtitle                 image_phm_pipe          rm
argo_asf                image_photocd_pipe      roq
argo_brp                image_pictor_pipe       rpl
argo_cvg                image_png_pipe          rsd
asf                     image_ppm_pipe          rso
asf_o                   image_psd_pipe          rtp
ass                     image_qdraw_pipe        rtsp
ast                     image_qoi_pipe          s337m
au                      image_sgi_pipe          sami
av1                     image_sunrast_pipe      sap
avi                     image_svg_pipe          sbc
avr                     image_tiff_pipe         sbg
avs                     image_vbn_pipe          scc
avs2                    image_webp_pipe         scd
avs3                    image_xbm_pipe          sdns
bethsoftvid             image_xpm_pipe          sdp
bfi                     image_xwd_pipe          sdr2
bfstm                   ingenient               sds
bink                    ipmovie                 sdx
binka                   ipu                     segafilm
bintext                 ircam                   ser
bit                     iss                     sga
bitpacked               iv8                     shorten
bmv                     ivf                     siff
boa                     ivr                     simbiosis_imx
bonk                    jacosub                 sln
brstm                   jv                      smacker
c93                     kux                     smjpeg
caf                     kvag                    smush
cavsvideo               laf                     sol
cdg                     live_flv                sox
cdxl                    lmlm4                   spdif
cine                    loas                    srt
codec2                  lrc                     stl
codec2raw               luodat                  str
concat                  lvf                     subviewer
data                    lxf                     subviewer1
daud                    m4v                     sup
dcstr                   matroska                svag
derf                    mca                     svs
dfa                     mcc                     swf
dfpwm                   mgsts                   tak
dhav                    microdvd                tedcaptions
dirac                   mjpeg                   thp
dnxhd                   mjpeg_2000              threedostr
dsf                     mlp                     tiertexseq
dsicin                  mlv                     tmv
dss                     mm                      truehd
dts                     mmf                     tta
dtshd                   mods                    tty
dv                      moflex                  txd
dvbsub                  mov                     ty
dvbtxt                  mp3                     v210
dxa                     mpc                     v210x
ea                      mpc8                    vag
ea_cdata                mpegps                  vc1
eac3                    mpegts                  vc1t
epaf                    mpegtsraw               vividas
ffmetadata              mpegvideo               vivo
filmstrip               mpjpeg                  vmd
fits                    mpl2                    vobsub
flac                    mpsub                   voc
flic                    msf                     vpk
flv                     msnwc_tcp               vplayer
fourxm                  msp                     vqf
frm                     mtaf                    w64
fsb                     mtv                     wady
fwse                    musx                    wav
g722                    mv                      wavarc
g723_1                  mvi                     wc3
g726                    mxf                     webm_dash_manifest
g726le                  mxg                     webvtt
g729                    nc                      wsaud
gdv                     nistsphere              wsd
genh                    nsp                     wsvqa
gif                     nsv                     wtv
gsm                     nut                     wv
gxf                     nuv                     wve
h261                    obu                     xa
h263                    ogg                     xbin
h264                    oma                     xmd
hca                     paf                     xmv
hcom                    pcm_alaw                xvag
hevc                    pcm_f32be               xwma
hls                     pcm_f32le               yop
hnm                     pcm_f64be               yuv4mpegpipe
ico                     pcm_f64le
idcin                   pcm_mulaw

Enabled muxers:
a64                     h263                    pcm_s16le
ac3                     h264                    pcm_s24be
adts                    hash                    pcm_s24le
adx                     hds                     pcm_s32be
aiff                    hevc                    pcm_s32le
alp                     hls                     pcm_s8
amr                     ico                     pcm_u16be
amv                     ilbc                    pcm_u16le
apm                     image2                  pcm_u24be
apng                    image2pipe              pcm_u24le
aptx                    ipod                    pcm_u32be
aptx_hd                 ircam                   pcm_u32le
argo_asf                ismv                    pcm_u8
argo_cvg                ivf                     pcm_vidc
asf                     jacosub                 psp
asf_stream              kvag                    rawvideo
ass                     latm                    rm
ast                     lrc                     roq
au                      m4v                     rso
avi                     matroska                rtp
avif                    matroska_audio          rtp_mpegts
avm2                    md5                     rtsp
avs2                    microdvd                sap
avs3                    mjpeg                   sbc
bit                     mkvtimestamp_v2         scc
caf                     mlp                     segafilm
cavsvideo               mmf                     segment
codec2                  mov                     smjpeg
codec2raw               mp2                     smoothstreaming
crc                     mp3                     sox
dash                    mp4                     spdif
data                    mpeg1system             spx
daud                    mpeg1vcd                srt
dfpwm                   mpeg1video              stream_segment
dirac                   mpeg2dvd                streamhash
dnxhd                   mpeg2svcd               sup
dts                     mpeg2video              swf
dv                      mpeg2vob                tee
eac3                    mpegts                  tg2
f4v                     mpjpeg                  tgp
ffmetadata              mxf                     truehd
fifo                    mxf_d10                 tta
fifo_test               mxf_opatom              ttml
filmstrip               null                    uncodedframecrc
fits                    nut                     vc1
flac                    obu                     vc1t
flv                     oga                     voc
framecrc                ogg                     w64
framehash               ogv                     wav
framemd5                oma                     webm
g722                    opus                    webm_chunk
g723_1                  pcm_alaw                webm_dash_manifest
g726                    pcm_f32be               webp
g726le                  pcm_f32le               webvtt
gif                     pcm_f64be               wsaud
gsm                     pcm_f64le               wtv
gxf                     pcm_mulaw               wv
h261                    pcm_s16be               yuv4mpegpipe

Enabled protocols:
async                   gopher                  rtmp
cache                   hls                     rtmpt
concat                  http                    rtp
concatf                 httpproxy               srtp
crypto                  icecast                 subfile
data                    md5                     tcp
fd                      mmsh                    tee
ffrtmphttp              mmst                    udp
file                    pipe                    udplite
ftp                     prompeg                 unix

Enabled filters:
a3dscope                concat                  noformat
abench                  convolution             noise
abitscope               convolve                normalize
acompressor             copy                    null
acontrast               corr                    nullsink
acopy                   crop                    nullsrc
acrossfade              crossfeed               oscilloscope
acrossover              crystalizer             overlay
acrusher                cue                     pad
acue                    curves                  pal100bars
addroi                  datascope               pal75bars
adeclick                dblur                   palettegen
adeclip                 dcshift                 paletteuse
adecorrelate            dctdnoiz                pan
adelay                  deband                  perms
adenorm                 deblock                 photosensitivity
aderivative             decimate                pixdesctest
adrawgraph              deconvolve              pixelize
adrc                    dedot                   pixscope
adynamicequalizer       deesser                 premultiply
adynamicsmooth          deflate                 prewitt
aecho                   deflicker               pseudocolor
aemphasis               dejudder                psnr
aeval                   derain                  qp
aevalsrc                deshake                 random
aexciter                despill                 readeia608
afade                   detelecine              readvitc
afdelaysrc              dialoguenhance          realtime
afftdn                  dilation                remap
afftfilt                displace                removegrain
afifo                   dnn_classify            removelogo
afir                    dnn_detect              replaygain
afirsrc                 dnn_processing          reverse
aformat                 doubleweave             rgbashift
afreqshift              drawbox                 rgbtestsrc
afwtdn                  drawgraph               roberts
agate                   drawgrid                rotate
agraphmonitor           drmeter                 scale
ahistogram              dynaudnorm              scale2ref
aiir                    earwax                  scdet
aintegral               ebur128                 scharr
ainterleave             edgedetect              scroll
alatency                elbg                    segment
alimiter                entropy                 select
allpass                 epx                     selectivecolor
allrgb                  equalizer               sendcmd
allyuv                  erosion                 separatefields
aloop                   estdif                  setdar
alphaextract            exposure                setfield
alphamerge              extractplanes           setparams
amerge                  extrastereo             setpts
ametadata               fade                    setrange
amix                    feedback                setsar
amovie                  fftdnoiz                settb
amplify                 fftfilt                 shear
amultiply               field                   showcqt
anequalizer             fieldhint               showcwt
anlmdn                  fieldmatch              showfreqs
anlmf                   fieldorder              showinfo
anlms                   fifo                    showpalette
anoisesrc               fillborders             showspatial
anull                   firequalizer            showspectrum
anullsink               flanger                 showspectrumpic
anullsrc                floodfill               showvolume
apad                    format                  showwaves
aperms                  fps                     showwavespic
aphasemeter             framepack               shuffleframes
aphaser                 framerate               shufflepixels
aphaseshift             framestep               shuffleplanes
apsyclip                freezedetect            sidechaincompress
apulsator               freezeframes            sidechaingate
arealtime               gblur                   sidedata
aresample               geq                     sierpinski
areverse                gradfun                 signalstats
arnndn                  gradients               silencedetect
asdr                    graphmonitor            silenceremove
asegment                grayworld               sinc
aselect                 greyedge                sine
asendcmd                guided                  siti
asetnsamples            haas                    smptebars
asetpts                 haldclut                smptehdbars
asetrate                haldclutsrc             sobel
asettb                  hdcd                    spectrumsynth
ashowinfo               headphone               speechnorm
asidedata               hflip                   split
asoftclip               highpass                sr
aspectralstats          highshelf               ssim
asplit                  hilbert                 ssim360
astats                  histogram               stereotools
astreamselect           hqx                     stereowiden
asubboost               hstack                  streamselect
asubcut                 hsvhold                 superequalizer
asupercut               hsvkey                  surround
asuperpass              hue                     swaprect
asuperstop              huesaturation           swapuv
atadenoise              hwdownload              tblend
atempo                  hwmap                   telecine
atilt                   hwupload                testsrc
atrim                   hysteresis              testsrc2
avectorscope            identity                thistogram
avgblur                 idet                    threshold
avsynctest              il                      thumbnail
axcorrelate             inflate                 tile
backgroundkey           interleave              tiltshelf
bandpass                join                    tlut2
bandreject              kirsch                  tmedian
bass                    lagfun                  tmidequalizer
bbox                    latency                 tmix
bench                   lenscorrection          tonemap
bilateral               life                    tpad
biquad                  limitdiff               transpose
bitplanenoise           limiter                 treble
blackdetect             loop                    tremolo
blend                   loudnorm                trim
blockdetect             lowpass                 unpremultiply
blurdetect              lowshelf                unsharp
bm3d                    lumakey                 untile
bwdif                   lut                     v360
cas                     lut1d                   varblur
cellauto                lut2                    vectorscope
channelmap              lut3d                   vflip
channelsplit            lutrgb                  vfrdet
chorus                  lutyuv                  vibrance
chromahold              mandelbrot              vibrato
chromakey               maskedclamp             vif
chromanr                maskedmax               vignette
chromashift             maskedmerge             virtualbass
ciescope                maskedmin               vmafmotion
codecview               maskedthreshold         volume
color                   maskfun                 volumedetect
colorbalance            mcompand                vstack
colorchannelmixer       median                  w3fdif
colorchart              mergeplanes             waveform
colorcontrast           mestimate               weave
colorcorrect            metadata                xbr
colorhold               midequalizer            xcorrelate
colorize                minterpolate            xfade
colorkey                mix                     xmedian
colorlevels             monochrome              xstack
colormap                morpho                  yadif
colorspace              movie                   yaepblur
colorspectrum           msad                    yuvtestsrc
colortemperature        multiply                zoompan
compand                 negate
compensationdelay       nlmeans

Enabled bsfs:
aac_adtstoasc           h264_redundant_pps      opus_metadata
av1_frame_merge         hapqa_extract           pcm_rechunk
av1_frame_split         hevc_metadata           pgs_frame_merge
av1_metadata            hevc_mp4toannexb        prores_metadata
chomp                   imx_dump_header         remove_extradata
dca_core                media100_to_mjpegb      setts
dts2pts                 mjpeg2jpeg              text2movsub
dump_extradata          mjpega_dump_header      trace_headers
dv_error_marker         mov2textsub             truehd_core
eac3_core               mp3_header_decompress   vp9_metadata
extract_extradata       mpeg2_metadata          vp9_raw_reorder
filter_units            mpeg4_unpack_bframes    vp9_superframe
h264_metadata           noise                   vp9_superframe_split
h264_mp4toannexb        null

Enabled indevs:
fbdev                   oss
lavfi                   v4l2

Enabled outdevs:
fbdev                   oss                     v4l2

License: LGPL version 2.1 or later
```

（2）`configure` 成功后执行 `make`，在 `MinGW` 环境下编译 `ffmpeg` 是一个比较漫长的过程。

（3）执行 `make install`，到此为止，`FFmpeg` 在 `Windows` 上的编译已全部完成，此时我们可以尝试执行 `FFmpeg` 命令来验证编译结果。执行 `./ffmpeg.exe -h`：

```shell
$ ./ffmpeg -h
ffmpeg version N-110228-g4dffa56 Copyright (c) 2000-2023 the FFmpeg developers
  built with gcc 5.4.0 (Ubuntu 5.4.0-6ubuntu1~16.04.12) 20160609
  configuration: 
  libavutil      58.  6.100 / 58.  6.100
  libavcodec     60.  9.100 / 60.  9.100
  libavformat    60.  4.101 / 60.  4.101
  libavdevice    60.  2.100 / 60.  2.100
  libavfilter     9.  5.100 /  9.  5.100
  libswscale      7.  2.100 /  7.  2.100
  libswresample   4. 11.100 /  4. 11.100
Hyper fast Audio and Video encoder
usage: ffmpeg [options] [[infile options] -i infile]... {[outfile options] outfile}...
```

> 注意：以上编译配置方式编译出来的 `ffmpeg` 仅仅只是最简易的 `ffmpeg`，并没有 `H.264`、`H.265`、加字幕等编码支持，如果需要支持更多的模块和参数，还需要进行更加详细的定制。