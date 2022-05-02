使用 `Until` 关键字的 `Do ... Loop` 循环被称为 "直到型循环"，其语法格式如下所示：

```vb
Do Until <循环条件>
    循环体1
    <Exit Do>
    循环体2
Loop
```

用 `Until` 关键字代替 `While` 关键字的区别在于，当循环条件的值为 `False` 时才进行循环，否则退出循环。例如：

```vb
Private Sub CmdOk_Click(sender As Object, e As EventArgs) Handles CmdOk.Click
    Dim i%, n%, mySum%
    n = Val(InputBox("请输入一个数："))
    Do Until i = n
        i = i + 1
        mySum = mySum + i
        If n > 12 Then Exit Do
    Loop
    MsgBox(mySum)
End Sub
```

