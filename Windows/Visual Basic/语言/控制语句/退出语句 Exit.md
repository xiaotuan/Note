`Exit` 语句用来退出 `Do ... Loop`、`For ... Next`、`Function`、`Sub` 或 `Property` 代码块，其类型及作用如下所示：

| 语句类型      | 作用                                                         |
| ------------- | ------------------------------------------------------------ |
| Exit Do       | 退出 `Do ... Loop` 循环的一种方法，只能在 `Do ... Loop` 循环语句中使用。`Exit Do` 语句会将控制权转移到 `Loop` 语句之后的语句。当 `Exit Do` 语句用在嵌套的 `Do ... Loop` 循环语句中时，`Exit Do` 语句会将控制权转移到其所在位置的外层循环。 |
| Exit For      | 退出 `For ... Next` 循环的一种方法，只能在 `For ... Next` 或 `For Each ... Next` 循环中使用。`Exit For` 语句会将控制权转移到 `Next` 语句之后的语句。当 `Exit For` 语句用在嵌套的 `For ... Next` 或 `For Each ... Next` 循环中时，`Exit For` 语句会将控制权转移到其所在位置的外层循环。 |
| Exit Function | 立即从包含该语句的 `Function` 过程中退出。程序会从调用 `Function` 过程的语句之后的语句继续执行 |
| Exit Property | 立即从包含该语句的 `Property` 过程中退出。程序会从调用 `Property` 过程的语句之后的语句继续执行 |
| Exit Sub      | 立即从包含该语句的 `Sub` 过程中退出。程序会从调用 `Sub` 过程语句之后的语句继续执行。 |

例如：

```vb
Private Sub CmdOk_Click(sender As Object, e As EventArgs) Handles CmdOk.Click
    Dim i As Integer
    For i = 1 To 100
        LabKind.Text = i
        If i = 50 Then Exit For
    Next
End Sub
```

