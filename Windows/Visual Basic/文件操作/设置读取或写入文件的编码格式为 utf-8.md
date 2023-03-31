[toc]

> 注意：如果以如下方式设置文件读取或写入的编码格式为 UTF-8，实际上其编码格式为  UTF-8 BOM：
>
> ```vb
> Dim fs As FileStream = Nothing
> fs = New FileStream(customFingerprintPath, FileMode.Open)
> Dim utf8 = New System.Text.UTF8Encoding(False)
> Dim fileReader As New System.IO.StreamReader(backPath, System.Text.Encoding.UTF8)
> Dim fileWriter As New System.IO.StreamWriter(fs, System.Text.Encoding.UTF8)
> ```

### 1. 以 utf-8 编码格式读取文件

```vb
Dim utf8 = New System.Text.UTF8Encoding(False)
Dim fileReader As New System.IO.StreamReader(backPath, utf8)
```

### 2. 以 utf-8 编码格式写入文件

```vb
Dim fs As FileStream = Nothing
fs = New FileStream(customFingerprintPath, FileMode.Open)
Dim utf8 = New System.Text.UTF8Encoding(False)
Dim fileWriter As New System.IO.StreamWriter(fs, utf8)
```

