### 15.2.2　使用QSoundEffect和QSound播放音效文件

QSoundEffect用于播放低延迟的音效文件，如无压缩的WAV文件，用于实现一些音效效果，如按键音、提示音等。使用QSoundEffect播放音效文件的示例代码如下：

```css
QSoundEffect effect;
effect.setSource(QUrl::fromLocalFile("engine.wav"));
effect.setLoopCount(3);
effect.setVolume(1);
effect.play();
```

QSoundEffect不仅可以播放本地文件，还可以播放网络文件。

还有一个类QSound只能播放本地WAV文件，而且是异步方式播放。可以直接使用QSound的静态函数播放WAV文件，如：

```css
QSound::play("mysounds/bells.wav");
```

