[toc]

### 1. 报错代码

```vb
Private Sub btnRename_Click(sender As Object, e As EventArgs) Handles btnRename.Click
    btnRename.Enabled = False
    Dim prefix = tbPrefix.Text.Trim()
    Dim startNumber = tbNumber.Text.Trim()
    If Len(prefix) > 0 And IsNumeric(startNumber) Then
        Dim start = Int(startNumber)
        Dim bitNumber = Str(Animation.Pictures.Count).Length
        Dim numFormat = ""
        Dim i%
        For i = 1 To bitNumber
        numFormat += "0"
    Next
    For i = 0 To Animation.Pictures.Count - 1
        Dim item = Animation.Pictures.Item(i).ToString()
        Dim path = item.Substring(0, item.LastIndexOf("\"))
        Debug.WriteLine("Path: " + path)
        Dim number = Format(start + i, numFormat)
        path += String.Concat("/", prefix, number, item.AsSpan(item.LastIndexOf(".")))
        Debug.WriteLine("Number: " + number)
        Debug.WriteLine("Source path: " + Animation.Pictures.Item(i) + ", Dest path: " + path)
        System.IO.File.Move(Animation.Pictures.Item(i), path)
    Next
    update_Pictures()
    update_ListView()
    Else
    MessageBox.Show("前缀不能为空，或者起始字符串不是数字", "提示"， MessageBoxButtons.OK, MessageBoxIcon.Information)
    End If
    btnRename.Enabled = True
End Sub
```

执行上面方法的如下语句出现报错：

```vb
System.IO.File.Move(Animation.Pictures.Item(i), path)
```

### 2. 报错信息

```
System.IO.IOException
  HResult=0x80070020
  Message=The process cannot access the file because it is being used by another process.
  Source=System.Private.CoreLib
  StackTrace:
   在 System.IO.FileSystem.MoveFile(String sourceFullPath, String destFullPath, Boolean overwrite)
   在 System.IO.File.Move(String sourceFileName, String destFileName, Boolean overwrite)
   在 System.IO.File.Move(String sourceFileName, String destFileName)
   在 AnimationMaker.AnimationMaker.btnRename_Click(Object sender, EventArgs e) 在 C:\WorkSpace\GitSpace\Xiaotuan\AnimationMaker\AnimationMaker.vb 中: 第 109 行
   在 System.Windows.Forms.Control.OnClick(EventArgs e)
   在 System.Windows.Forms.Button.OnClick(EventArgs e)
   在 System.Windows.Forms.Button.OnMouseUp(MouseEventArgs mevent)
   在 System.Windows.Forms.Control.WmMouseUp(Message& m, MouseButtons button, Int32 clicks)
   在 System.Windows.Forms.Control.WndProc(Message& m)
   在 System.Windows.Forms.ButtonBase.WndProc(Message& m)
   在 System.Windows.Forms.Button.WndProc(Message& m)
   在 System.Windows.Forms.Control.ControlNativeWindow.OnMessage(Message& m)
   在 System.Windows.Forms.Control.ControlNativeWindow.WndProc(Message& m)
   在 System.Windows.Forms.NativeWindow.Callback(IntPtr hWnd, WM msg, IntPtr wparam, IntPtr lparam)
```

### 3. 报错原因分析

在重命名前，程序在其他方法中使用该图片资源来获取图片的尺寸，调用方法结束前并未释放该图片资源造成的。在显示图片界面，关闭界面后也未释放该图片资源。

### 4. 解决办法

1. 在使用 `PictureBox` 控件显示图片时不能使用如下代码：

   ```vb
   pbImageView.Image = Image.imageFromFile(imagePath)
   ```

   应该使用如下代码：

   ```vb
   Dim img = Image.imageFromFile(imagePath)
   pbImageView.Image = img
   ```

2. 不再使用图片后应该调用如下方法：

   ```vb
   img.Dispose()
   img = Nothing
   ```

> 提示：参考官方文档对 `Image.FromFile()` 方法的介绍，有如下说明：
>
> ```
> 在释放 之前， Image 文件将保持锁定状态。
> ```

