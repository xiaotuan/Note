`ffprobe` 是 `FFmpeg` 源码编译后生成的一个可执行程序。`ffprobe` 是一个非常强大的多媒体分析工具，可以从媒体文件或者媒体流中获得你想要了解的媒体信息，比如音频的参数、视频的参数、媒体容器的参数信息等。

下面列举一个简单的例子，以对 `ffprobe` 有一个基本的概念：

```shell
./ffprobe -show_streams output.mp4
```

命令执行后输出如下内容：

```
[STREAM]
index=0
codec_name=mpeg4
codec_long_name=MPEG-4 part 2
profile=Simple Profile
codec_type=video
codec_time_base=1/25
codec_tag_string=mp4v
codec_tag=0x7634706d
width=1280
height=714
coded_width=1280
coded_height=714
has_b_frames=0
sample_aspect_ratio=1:1
display_aspect_ratio=640:357
pix_fmt=yuv420p
level=1
color_range=N/A
chroma_location=left
field_order=unknown
timecode=N/A
refs=1
quarter_sample=false
divx_packed=false
r_frame_rate=25/1
avg_frame_rate=25/1
time_base=1/12800
start_pts=0
start_time=0.000000
duration_ts=170496
duration=13.320000
bit_rate=1146797
max_bit_rate=1146797
bits_per_raw_sample=N/A
nb_frames=333
nb_read_frames=N/A
nb_read_packets=N/A
[/STREAM]
[STREAM]
index=1
codec_name=aac
codec_long_name=AAC (Advanced Audio Coding)
profile=LC
codec_type=audio
codec_time_base=1/48000
codec_tag_string=mp4a
codec_tag=0x6134706d
sample_fmt=fltp
sample_rate=48000
channels=2
channel_layout=stereo
bits_per_sample=0
id=N/A
r_frame_rate=0/0
avg_frame_rate=0/0
time_base=1/48000
start_pts=0
start_time=0.000000
duration_ts=643056
duration=13.397000
bit_rate=128213
max_bit_rate=128213
bits_per_raw_sample=N/A
nb_frames=629
nb_read_frames=N/A
nb_read_packets=N/A
[/STREAM]
```

根据输出内容可以看到，使用 `ffprobe` 能够查看 MP4 文件容器中的流的信息，其中包含了一个视频流，由于该文件中只有视频流，流相关的信息是通过 `[STREAM][/STREAM]` 的方式展现出来的，在 `[STREAM][/STREAM]` 之间的信息即为该 MP4 文件的视频流信息。当视频文件容器中包含音频流与视频流或者更多路流时，会通过 `[STREAM][/STREAM]` 进行多个流的分隔，分隔后采用 `index` 来进行流的索引信息的区分。