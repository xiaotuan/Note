`Select Case` 语句可以方便、直观地处理多分支的控制结构。其语法结构如下所示：

```vb
Select Case 测试表达式
    Case 表达式1
        语句块1
    Case 表达式2
        语句块2
        ...
    Case 表达式n
        语句块n
    Case Else
        语句块n+1
End Select
```

"表达式" 的值称为域值，通过以下几种方式可以设定该值。

（1）表达式列表为表达式。例如：

```vb
Case x+100
表达式列表为表达式
```

（2）一组值（用逗号隔开）。例如：

```vb
Case 1,4,7
表示条件在 1, 4, 7 范围内取值
```

（3）表达式1 To 表达式2。例如：

```vb
Case 50 TO 60
表示条件取值范围为 50 ~ 60
```

（4）Is 关系表达式。例如：

```vb
Case Is<4
表示条件在小于 4 的范围内取值
```

例如：

```vb
Private Sub Command1_Click()
    Dim a As Integer
    a = Val(Text1.Text)
    Select Case a 
    Case Is = 100
        lblResult.Caption = "优"
    Case Is >= 80
        lblResult.Caption = "良"
    Case Is >= 60
        lblResult.Caption = "及格"
    Case Else
        lblResult.Caption = "不及格"
    End Select
End Sub
```

