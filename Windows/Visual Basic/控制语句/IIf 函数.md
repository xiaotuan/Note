`IIf` 函数的作用是根据表达式的值，返回两部分中的其中一个的值或表达式，其语法格式如下所示：

```vb
IIf(<表达式>, <值或表达式1>, <值或表达式2>)
```

> 注意：如果表达式 1 或表达式 2 中的任何一个在计算时发生错误，那么程序就会发生错误。

例如：

```vb
Private Sub CmdOk_Click(sender As Object, e As EventArgs) Handles CmdOk.Click
    Dim str As String
    str = IIf(FrmPwd.Text = "11", "输入正确！", "密码不正确，请重新输入！")
    MsgBox(str, , "提示")
End Sub
```

