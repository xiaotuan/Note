Applet 可以处理图像和音频。图像必须是 GIF、PNG 或 JPEG 格式，音频文件必须是 AU、AIFF、WAV 或 MIDI。另外也支持动画 GIF，可以显示动画。

要用相对 URL 指定图象和音频文件的位置。通常可以通过调用 `getDocumentBase` 或 `getCodeBase` 方法得到基 URL。前一个方法会得到包含这个 applet 的 HTML 页面的 URL，后者会得到 applet 的 codebase 属性置顶的 URL。

可以为 `getImage` 或 `getAudioClip` 方法提供基 URL 和文件位置。例如：

```java
Image cat = getImage(getDocumentBase(), "images/cat.gif");
AudioClip meow = getAudioClip(getDocumentBase(), "audio/meow.au");
```

还可以调用 Applet 类的 `play` 方法而无须先加载这段音频：

```java
play(getDocumentBase(), "audio/meow.au");
```

