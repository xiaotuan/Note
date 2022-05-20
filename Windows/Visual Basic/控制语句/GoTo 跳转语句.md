`GoTo` 语句使程序无条件跳转到过程中指定的语句行执行，其语法格式如下所示：

```vb
GoTo <行号|行标签>
```

> 注意：
>
> （1）`GoTo` 语句只能跳转到它所在过程的行。
>
> （2）"行标签" 是任何字符的组合，不区分大小写，必须以字母开头，以冒号 ":" 结尾，且必须放在行的开始位置。
>
> （3）"行号" 是一个数字序列，且在使用行号的过程内该序列的唯一的。行号必须放在行的开始位置。
>
> （4）太多的 `GoTo` 语句会使程序代码不容易阅读及调试，应尽可能少用或不用 `GoTo` 语句。

例如：

```Vb
Private Sub CmdOk_Click(sender As Object, e As EventArgs) Handles CmdOk.Click
    GoTo l1
    End
    Exit Sub	
l1:
	MsgBox("没有退出")
End Sub
```

