安装 `playsound` 模块命令如下：

```shell
pip install playsound
```

使用 `playsound` 模块播放音频文件代码如下：

```python
from playsound import playsound

path = "C:\\Users\\xiaotuan\\Desktop\\曾经的你.mp3"
playsound(path)
```

> 注意：`playsound` 只支持播放功能，播放音频后无法进行其他操作，比如暂停、停止等。

如果音频文件路径中带有空格，可能会导致报无法找到文件错误，可以使用如此代码解决：

```shell
from playsound import playsound

path = "C:\\Users\\xiaotuan\\Desktop\\曾经的你.mp3"
path = path.replace(" ", "%20")
playsound(path)
```

