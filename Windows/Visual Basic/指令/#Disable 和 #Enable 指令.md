`#Disable` 和 `#Enable`指令是 Visual Basic 源代码编译器指令。 这两条指令用于禁用和重新启用代码区域的所有或特定警告。

```vb
Dim variable1    'warning BC42024: Unused local variable: 'variable1'.
#Disable Warning
    Dim variable2    'no warning
#Enable Warning
    Dim variable3    'warning BC42024: Unused local variable: 'variable3'.
```

```vb
' Suppress warning about no awaits in this method.
#Disable Warning BC42356
    Async Function TestAsync() As Task
        Console.WriteLine("testing")
    End Function
#Enable Warning BC42356
```

还可以禁用和启用以逗号分隔的警告代码列表。