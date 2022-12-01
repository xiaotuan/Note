`Windows` 系统使用的换行符为 `\r\n` ，如果需要使用 `Linux` 系统的换行符 `\n`，可以通过设置 `StreamWriter` 类的 `NewLine` 属性值为 `vbLf` 即可。例如：

```vb
Dim descFile = animDir + "\desc.txt"
Dim file As New System.IO.StreamWriter(descFile) With {
    .NewLine = vbLf
}
```

