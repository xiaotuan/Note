If...Then...Else 语句的语法格式如下所示：

```vb
If 条件表达式 Then
    语句块1
Else
    语句块2
End If
```

或者

```vb
If 条件表达式 Then 语句1 Else 语句2
```

例如：

```vb
If Text1.Text = "11" Then MsgBox("登录成功！") Else MsgBox("密码错误，重新输入！")
```

或者

```vb
Private Sub Command1_Click()
    If Text1.Text = "11" Then
        MsgBox("登录成功！"， ， "提示")
    Else
        MsgBox("密码错误，请重新输入！", , "提示")
    End If
End Sub
```

