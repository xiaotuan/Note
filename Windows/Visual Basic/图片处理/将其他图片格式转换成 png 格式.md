可以通过 `Bitmap` 类对 `BMP`、`GIF`、`JPEG`、`PNG` 和 `TIFF` 图片进行相互转换（`GIF` 和 `TIFF` 未验证，暂不清楚是否可以相互转换），例如：

```vb
Dim jpgPath As String = "C:\Users\xiaotuan\Desktop\Logo.jpg"
Dim pngPath As String = "C:\Users\xiaotuan\Desktop\Logo.png"
Dim bmp As new Bitmap(jpgPath)
bmp.Save(pngPath, ImageFormat.Png)
```

