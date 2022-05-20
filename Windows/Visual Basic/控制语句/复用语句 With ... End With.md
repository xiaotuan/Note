`With` 语句是在一个定制的对象或一个用户定义的类型上执行的一系列语句，其语法格式如下所示：

```vb
With <对象>
	[<语句组>]
End With
```

`With` 语句可以嵌套使用，但是外层 `With` 语句的对象或用户定义类型会在内层的 `With` 语句中被屏蔽，所以必须在内层的 `With` 语句中使用完整的对象或用户自定义类型名称来引用在外层的 `With` 语句中的对象或用户自定义类型。例如：

```vb
Private Sub CmdOk_Click(sender As Object, e As EventArgs) Handles CmdOk.Click
    With Me
        .Height = 10000 : .Width = 10000
        With CmdOk
            .Height = 2000 : .Width = 2000
            .Text = "按钮高度与宽度都是 2000"
            Me.Text = "窗体高度与宽度都是 10000"
        End With
    End With
End Sub
```

