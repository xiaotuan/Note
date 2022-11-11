[toc]

Visual Basic 包含一个功能强大的命名空间 `System.IO`（IO 对象就像命名空间 System 的一个对象属性）。使用 System.IO 的各种属性、方法和对象属性，可以对文件系统进行任何操作。具体地说，对象 `System.IO.File` 和 `System.IO.Directory` 提供了丰富的文件和目录操作功能。

### 1. 判断文件是否存在

可以使用 `System.IO.File` 对象的 `Exists()` 方法来判断文件是否存在：

```vb
Private Function SourceFileExists() As Boolean
    If Not (System.IO.File.Exists(txtSource.Text)) Then
        MessageBox.Show("The source file does not exist!")
        Return False
    Else
        Return True
    End If
End Function
```

### 2. 复制文件

要复制文件，可使用 `System.IO.File` 类的 `Copy()` 方法：

```vb
If Not (SourceFileExists()) Then Exit Sub
System.IO.File.Copy(txtSource.Text, txtDestination.Text)
MessageBox.Show("The file has been successfully copied.")
```

`Copy()` 方法有两个参数。第一个是要复制的文件，第二个是目标文件的文件名及路径。

### 3. 移动文件

移动文件是通过 `System.IO.File` 对象的 `Move()` 方法实现的：

```vb
If Not (SourceFileExists()) Then Exit Sub
System.IO.File.Move(txtSource.Text, txtDestination.Text)
MessageBox.Show("The file has been successfully moved.")
```

### 4. 重命名文件

要重命名文件，使用 `System.IO.File` 对象的 `Move()` 方法，指定新文件名，但保存在同一目录。

### 5. 删除文件

删除文件可能带来危险。`System.IO.File` 的 `Delete()` 方法将文件永久第删除——它并不将文件发送到回收站。

```vb
If Not(SourceFileExists()) Then Exit Sub
        
If MessageBox.Show("Are you sure you want to delete the source file?",
                "MyApp", MessageBoxButtons.YesNo, MessageBoxIcon.Question) = Windows.Forms.DialogResult.Yes Then
    System.IO.File.Delete(txtSource.Text)
    MessageBox.Show("The file has been successfully deleted.")
End If
```

> 注意：使用下面这样的 `My` 对象，可将文件发送到回收站，而不是将其永久性删除：
>
> ```vb
> My.Computer.FileSystem.DeleteFile("C:\test.txt", FileIO.UIOption.AllDialogs, FileIO.RecycleOption.SendToRecycleBin)
> ```

