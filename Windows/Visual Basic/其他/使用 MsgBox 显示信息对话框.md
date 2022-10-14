可以使用 `MsgBox()` 方法显示消息对话框，其定义如下：

```vb
public static MsgBoxResult MsgBox(object Prompt, MsgBoxStyle Buttons = MsgBoxStyle.ApplicationModal, object? Title = null)
```

+ Prompt：信息对话框内容
+ Buttons：对话框风格
+ Title：对话框标题

例如：

```vb
Public Class Form1
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Dim MyValue As String
        MyValue = InputBox("请输入电话号码", "电话号码", "84978981")
        MsgBox(MyValue, MsgBoxStyle.OkOnly, "电话号码")
    End Sub
End Class
```

