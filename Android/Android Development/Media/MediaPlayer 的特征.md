MediaPlayer 的一些特征：

+ 设置了 MediaPlayer 的数据源以后，就无法轻松地更改它——必须创建一个新 MediaPlayer 或调用 reset() 方法来重新初始化播放器的状态。
+ 调用 prepare() 之后，可以调用 getCurrentPosition()、getDuration() 和 isPlaying() 来获取播放器的当前状态。也可以在调用 prepare() 之后调用 setLooping() 和 setVolume() 方法。
+ 调用 start() 之后，可以调用 pause()、stop() 和 seekTo()。
+ 每个 MediaPlayer 创建一个新线程，所以请确保使用媒体播放器完成播放之后调用 release() 方法。