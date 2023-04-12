`FFmpeg` 的封装（Muxing）是指将压缩后的编码封装到一个容器格式中，如果要查看 `FFmpeg` 源代码中都可以支持哪些容器格式，可以通过命令 `./configure --list-muxers` 来查看：

```shell
$ ./configure --list-muxers
a64                     crc                     h264                    mpeg1system             pcm_s32be               stream_segment
ac3                     dash                    hash                    mpeg1vcd                pcm_s32le               streamhash
adts                    data                    hds                     mpeg1video              pcm_s8                  sup
adx                     daud                    hevc                    mpeg2dvd                pcm_u16be               swf
aiff                    dfpwm                   hls                     mpeg2svcd               pcm_u16le               tee
alp                     dirac                   ico                     mpeg2video              pcm_u24be               tg2
amr                     dnxhd                   ilbc                    mpeg2vob                pcm_u24le               tgp
amv                     dts                     image2                  mpegts                  pcm_u32be               truehd
apm                     dv                      image2pipe              mpjpeg                  pcm_u32le               tta
apng                    eac3                    ipod                    mxf                     pcm_u8                  ttml
aptx                    f4v                     ircam                   mxf_d10                 pcm_vidc                uncodedframecrc
aptx_hd                 ffmetadata              ismv                    mxf_opatom              psp                     vc1
argo_asf                fifo                    ivf                     null                    rawvideo                vc1t
argo_cvg                fifo_test               jacosub                 nut                     rm                      voc
asf                     filmstrip               kvag                    obu                     roq                     w64
asf_stream              fits                    latm                    oga                     rso                     wav
ass                     flac                    lrc                     ogg                     rtp                     webm
ast                     flv                     m4v                     ogv                     rtp_mpegts              webm_chunk
au                      framecrc                matroska                oma                     rtsp                    webm_dash_manifest
avi                     framehash               matroska_audio          opus                    sap                     webp
avif                    framemd5                md5                     pcm_alaw                sbc                     webvtt
avm2                    g722                    microdvd                pcm_f32be               scc                     wsaud
avs2                    g723_1                  mjpeg                   pcm_f32le               segafilm                wtv
avs3                    g726                    mkvtimestamp_v2         pcm_f64be               segment                 wv
bit                     g726le                  mlp                     pcm_f64le               smjpeg                  yuv4mpegpipe
caf                     gif                     mmf                     pcm_mulaw               smoothstreaming
cavsvideo               gsm                     mov                     pcm_s16be               sox
chromaprint             gxf                     mp2                     pcm_s16le               spdif
codec2                  h261                    mp3                     pcm_s24be               spx
codec2raw               h263                    mp4                     pcm_s24le               srt
```

