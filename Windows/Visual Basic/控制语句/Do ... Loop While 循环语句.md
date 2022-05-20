`Do ... Loop While` 语句的语法格式如下所示：

```vb
Do
    循环体1
    <Exit Do>
    循环体2
Loop While <循环条件>
```

当程序执行 `Do ... Loop While` 语句时，首先执行一次循环体，然后判断 While 后面的 `<循环条件>`。如果其值为 True，则返回到循环开始处再次执行循环体，否则跳出循环，执行 Loop 后面的语句。

例如：

```vb
Private Sub CmdOk_Click(sender As Object, e As EventArgs) Handles CmdOk.Click
    Dim i%, mySum%, myVal%
    myVal = Val(InputBox("请输入一个数："))
    Do
        i = i + 1
        mySum = mySum + i
    Loop While i < myVal
    MsgBox(mySum)
End Sub
```



