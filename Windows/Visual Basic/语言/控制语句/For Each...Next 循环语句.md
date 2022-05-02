`For Each ... Next` 语句用于依照一个数组或集合中的每个元素，循环执行一组语句。其语法格式如下所示：

```vb
For Each 数组或集合中的元素 In 数组或集合
	循环体
	[Exit For]
	循环体
Next 数组或集合中的元素
```

+ 数组或集合中元素：必要参数，用来遍历集合或数组中所有元素的变量。对于集合，可能是一个 Variant 类型变量、一个通用对象变量或任何特殊对象变量；对于数组，这个变量只能是一个 Variant 类型变量。
+ 数组或集合：必要参数，对象集合或数组的名称（不包括用户定义类型的数组）。
+ 循环体：可选参数，循环执行的一条或多条语句。

例如：

```vb
Private Sub CmdOk_Click(sender As Object, e As EventArgs) Handles CmdOk.Click
    Dim Myctl As Control
        For Each Myctl In Me.Controls
        MsgBox(Myctl.Name)
    Next Myctl
End Sub
```

