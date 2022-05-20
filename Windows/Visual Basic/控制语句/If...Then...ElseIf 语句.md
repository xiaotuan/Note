语法格式如下所示：

```vb
If 条件表达式1 Then
    语句块1
ElseIf 条件表达式2 Then
    语句块2
ElseIf 条件表达式3 Then
    语句块3
ElseIf 条件表示N Then
    语句块N
Else
    语句块N+1
End If
```

例如：

```vb
Private Sub Command1_Click()
    Dim a As Integer
    a = Val(Text1.Text)
    If a > 100 Or a < 0 Then
        MsgBox("只能输入 0-100 的数！")
        Exit Sub
    End If
    If a = 100 Then
        lblResult.Caption = "优"
    ElseIf a >= 80 Then
        lblResult.Caption = "良"
    ElseIf a >= 60 Then
        lblResult.Caption = "及格"
    Else
        lblResult.Caption = "不及格"
    End If
End Sub
```

