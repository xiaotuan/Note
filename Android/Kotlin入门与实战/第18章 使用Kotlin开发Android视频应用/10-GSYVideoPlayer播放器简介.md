### 18.3.5　GSYVideoPlayer播放器简介

在Android视频应用开发中，大多数情况下并不会直接使用Android系统提供的MediaPlayer视频播放器，而是选择一些自主研发的或者成熟的开源视频播放器框架（如ijkplayer、PLDroidPlayer和Vitamio等）。这是因为Android原生的MediaPlayer采用的是硬解码，速度快但兼容性差，而FFmpeg等框架则采用的是软解码，虽然速度慢但兼容好。

本项目采用开源的GSYVideoPlayer库作为基础播放框架。作为一款优秀的视频播放器，它具有与ijkplayer一样出色的性能，而且使用上也异常简单。同时，GSYVideoPlayer还可以无缝支持MediaPlayer与EXOPlayer2等传统播放器，而且GSYVideoPlayer支持基本的拖动操作，声音、亮度调节，边播边缓存，视频加载速度、多分辨率切换等诸多功能，是一款名副其实的多功能视频播放器。

在使用GSYVideoPlayer播放器之前，需要在项目中添加GSYVideoPlayer依赖支持，它提供了Jcenter和JitPack两种仓库引入方式，其中，官方推荐使用Jcenter仓库来集成GSYVideoPlayer开发环境。Jcenter主要提供3种依赖方式，可以根据实际情况自由选取，其中，较为简单的方法是将完整版直接引入。

```python
compile 'com.shuyu:GSYVideoPlayer:4.1.1'
```

如果需要添加Java和SO支持，还可以使用如下集成方式。

```python
compile 'com.shuyu:gsyVideoPlayer-java:4.1.1'
//根据项目实际需求
compile 'com.shuyu:gsyVideoPlayer-armv5:4.1.1'
compile 'com.shuyu:gsyVideoPlayer-armv7a:4.1.1'
compile 'com.shuyu:gsyVideoPlayer-arm64:4.1.1'
compile 'com.shuyu:gsyVideoPlayer-x64:4.1.1'
compile 'com.shuyu:gsyVideoPlayer-x86:4.1.1'
```

通过上面两种方式集成的GSYVideoPlayer只支持263/264/265等编码，对于MPEG编码会出现有声音无画面的异常情况。如果需要支持MPEG编码和其他补充协议，需要引入如下库。

```python
compile 'com.shuyu:gsyVideoPlayer-java:4.1.1'
compile 'com.shuyu:gsyVideoPlayer-ex_so:4.1.1'
```

不过需要注意的是，新引入的库可能会带来APK文件增大的问题，因此需要根据实际情况合理地选择库的引入方式。

集成GSYVideoPlayer库之后，只需要在具体的界面添加GSYVideoPlayer播放器即可。代码如下。

```python
<com.shuyu.gsyvideoplayer.video.StandardGSYVideoPlayer
     android:id="@+id/mVideoView"
     android:layout_width="match_parent"
     android:layout_height="250dp"
     android:background="@color/color_black" />
```

StandardGSYVideoPlayer是GSYVideoPlayer提供的一种标准模式的播放器控件，只需要获取GSYVideoPlayer的实例，为GSYVideoPlayer添加视频源并调用启动函数即可。代码如下。

```python
mVideoView.setUp(url, false, "")
mVideoView.startPlayLogic()
```

