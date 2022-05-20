`End` 语句用来结束一个过程或块。`End` 语句与 `Exit` 语句容易混淆，`Exit` 语句是用来退出 `Do ... Loop`、`For ... Next`、`Function`、`Sub` 或 `Property` 代码块，并不说明一个结构的终止，而 `End` 语句是终止一个结构。`End` 语句的类型及作用如下所示：

| 语句类型      | 作用                                                         |
| ------------- | ------------------------------------------------------------ |
| End           | 停止执行。不是必要的，可以放在过程中的任何位置关闭程序       |
| End Function  | 必要的语句，用于结束一个 Function 语句                       |
| End If        | 必要的语句，用于结束一个 If 语句块                           |
| End Property  | 必要的语句，用于结束一个 `Property Let`、`Property Get` 或 `Property Set` 过程 |
| End Select    | 必要的语句，用于结束一个 `Select Case` 语句                  |
| End Sub       | 必要的语句，用于结束一个 `Sub` 语句                          |
| End Structure | 必要的语句，用于结束一个用户定义类型的语句（`Structure` 语句） |
| End With      | 必要的语句，用于结束一个 `With` 语句                         |

> 注意：在使用 `End` 语句关闭程序时，VB 不调用 `Unload`、`QueryUnload`、`Terminate` 事件或任何其他代码，而是直接终止程序（代码）执行。

