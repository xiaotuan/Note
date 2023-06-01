可以通过在参数前面添加 `Optional` 关键字，使其在调用过程时允许传递 `Nothing` 值给它。

> 注意：一旦定义可为 `Nothing` 的参数后，其后所有参数都是 `Optional` 参数。因此需要将 `Optional` 参数放置在参数列表的最后。

```vb
Public Function IsEmptyText(Optional value As String = Nothing) As Boolean
    If value Is Nothing Or Len(value.Trim) = 0 Then
        Return True
    End If
    Return False
End Function
```

