你可以使用 `FileSystem.Print` 和 `FileSystem.PrintLine` 方法将日志打印到文件中，其定义如下：

```vb
Public Sub PrintLine(FileNumber As Integer, ParamArray Output() As Object)
Public Sub Print(FileNumber As Integer, ParamArray Output() As Object)
```

要使用上面两个方法需要先创建用于保存日志的文件指示符 `FileNumber`，可以通过 `FileSystem.FileOpen` 方法创建该值，其方法定义如下：

```vb
Public Sub FileOpen(FileNumber As Integer, FileName As String, Mode As OpenMode, Optional Access As OpenAccess = OpenAccess.Default, Optional Share As OpenShare = OpenShare.Default, Optional RecordLength As Integer = -1)
```

**示例代码：**

```vb
Module Program

    Sub Main(args As String())
        FileOpen(12, "log.txt", OpenMode.Output)
        PrintLine(12, "This is a test.")
    End Sub

End Module
```

