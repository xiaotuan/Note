将图片格式转换成 8 位索引 BMP 图片代码如下所示：

```vb
Private Sub convertButton_Click(sender As Object, e As EventArgs) Handles convertButton.Click
    If imagePathTextBox.Text.Length > 0 Then
        Dim tmp As Bitmap = New Bitmap(imagePathTextBox.Text)
        Dim bitmap As Bitmap = tmp.Clone(New Rectangle(0, 0, tmp.Width, tmp.Height), PixelFormat.Format8bppIndexed)
        bitmap.Save("C:\Users\xiaotuan\Desktop\test.bmp", ImageFormat.Bmp)

    End If
End Sub
```

> 警告：使用该方法转换图片会出现轻微的颜色失真问题。