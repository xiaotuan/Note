`InputBox` 函数提供一个简单的对话框工用户输入。其定义如下所示：

```vb
public static string InputBox(string Prompt, string Title = "", string DefaultResponse = "", int XPos = -1, int YPos = -1)
```

+ Prompt：提示信息
+ Title：标题
+ DefaultReponse：默认值
+ XPos：输入窗口顶部 X 轴坐标
+ YPos：输入窗口顶部 Y 轴坐标

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

有关函数 `InputBox()` 的返回值，有两点需要牢记。首先，结果总是一个字符串；其次，如果用户单击 "取消" 按钮，将返回一个空字符串。`InputBox()` 只能返回字符串，而不能返回数字，这是其局限性，但可以避开这种局限性。
