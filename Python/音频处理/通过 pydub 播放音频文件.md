安装 `pydub` 模块命令如下：

```shell
pip install pydub
```

使用 `pydub` 模块播放音频文件代码如下：

```python
from pydub import AudioSebment
from pydub.playback import play

path = "C:\\Users\\xiaotuan\\Desktop\\曾经的你.mp3"
song = AudioSegment.from_mp3(path)
play(song)
```

> 注意：要使用 `pydub` 模块播放音频文件，需要在系统中预先安装 `PyAudio` 和 `ffmpeg` 库。