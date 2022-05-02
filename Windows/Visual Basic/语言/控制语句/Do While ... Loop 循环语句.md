使用 `While` 关键字的 `Do ... Loop` 循环称为 "当型循环" ，它是指当循环条件的值为 True 时执行循环。其语法格式如下所示：

```vb
Do While <循环条件>
    循环体1
    [Exit Do]
    循环体2
Loop
```

当程序执行到 `Do While ... Loop` 语句时，首先判断 `While` 后面的 `<循环条件>`，如果其值为 True，则由上到下执行循环体中的语句。当执行到 Loop 关键字时，返回到循环开始处再次判断 While 后面的 `<循环条件>` 是否为 True。如果为 True，则继续执行循环体中的语句；否则跳出循环，执行 Loop 后面的语句。

例如：

```vb
Private Sub CmdOk_Click(sender As Object, e As EventArgs) Handles CmdOk.Click
    Dim i%, mySum%
    Do While i <= 50
        mySum = mySum + i
        i = i + 1
    Loop
    MsgBox(mySum)
End Sub
```

