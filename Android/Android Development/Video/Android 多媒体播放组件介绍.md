`Android` 多媒体播放组件包含 `MediaPlayer`、`MediaCodec`、`OMX`、`StageFright`、`AudioTrack` 等，下面分别进行介绍：

+ `MediaPlayer`：播放控件。
+ `MediaCodec`：音视频编解码。
+ `OMX`：多媒体部分采用的编解码标准。
+ `StageFright`：它是一个框架，替代之前的 `OpenCore`，主要做了一个 `OMX` 层，仅仅对 `OpenCore` 的 `omx-component` 部分做了引用。`StageFright` 是在 `MediaPlayerService` 这一层加入的，和 `OpenCore` 是并列的。`StageFright` 在 `Android` 中是以共享库的形式存在的（libstagefright.so），其中的 `module` —— `NuPlayer/AwesomePlayer` 可用来播放音视频。`NuPlayer/AwesomePlayer` 提供了许多 `API`，可以让上层的应用程序（Java/JNI）调用。
+ `AudioTrack`：音频播放。



