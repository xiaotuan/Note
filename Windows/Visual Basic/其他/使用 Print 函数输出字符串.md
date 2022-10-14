`Print` 函数可以向指定文件写入数据，其定义如下所示：

```vb
public static void Print(int FileNumber, params object[] Output)
public static void PrintLine(int FileNumber, params object[] Output)
```

> 提示：`PrintLine` 会在数据末尾添加换行。

+ FileNumber：文件ID，可以通过 `FileOpen()` 获取。
+ Output：写入的数据。

例如：

```vb
Public Class Form1
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        FileOpen(1, "c:\WorkSpace\trash.txt", OpenMode.Output)   ' Open file for output.
        Print(1, "This is a test.")   ' Print text to file.
        PrintLine(1)   ' Print blank line to file.
        PrintLine(1, "Zone 1", TAB(), "Zone 2")   ' Print in two print zones.
        PrintLine(1, "Hello", "World")   ' Separate strings with a tab.
        PrintLine(1, SPC(5), "5 leading spaces ")   ' Print five leading spaces.
        PrintLine(1, TAB(10), "Hello")   ' Print word at column 10.

        ' Assign Boolean, Date, and Error values.
        Dim aBool As Boolean
        Dim aDate As DateTime
        aBool = False
        aDate = DateTime.Parse("February 12, 1969")

        ' Dates and booleans are translated using locale settings of your system.
        PrintLine(1, aBool, " is a Boolean value")
        PrintLine(1, aDate, " is a date")
        FileClose(1)   ' Close file.
    End Sub
End Class
```

