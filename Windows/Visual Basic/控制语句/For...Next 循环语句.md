当循环次数确定时，可以使用 `For...Next` 语句，其语法格式如下所示：

```vb
For 循环变量 = 初值 To 终值 [Step 步长]
	循环体
	[Exit For]
	循环体
Next 循环变量
```

+ 如果不指定 "步长"，则系统默认步长为 1；当 "初值 < 终值" 时，"步长" 为 0；当 "初值 > 终值" 时，"步长" 应小于 0。
+ `Exit For` 用来退出循环，执行 `Next` 后面的语句。
+ 如果出现循环变量的值总是不超出终值的情况，则会产生死循环。此时，可按 <kbd>Ctrl</kbd> + <kbd>Break</kbd> 快捷键，强制终止程序的运行。
+ 循环次数 N=Int （（终值 - 初值) / 步长 + 1)
+ Next 后面的循环变量名必须与 For 语句中的循环变量名相同，并且可以省略。

例如：

```vb
Private Sub CmdOk_Click(sender As Object, e As EventArgs) Handles CmdOk.Click
    Dim i%
    For i = 3 To 12
        cboUserName.Items.Add("操作员 " & i)
    Next i
End Sub
```

使用步长：

```vb
Dim intCounter As Integer
For intCounter = 1 To 100 Step 4
	Debug.WriteLine(intCounter)
Next intCounter
```

提前结束 `For` 循环：

```vb
Dim intCounter As Integer
For intCounter = 1 To 100
	If condition Then Exit For
    Debug.WriteLine(intCounter)
Next intCounter
```

