要解析 JSON 文件可以使用 `JsonDocument` 类来解析：

```vb
Dim jsonFilePath As String = "..."
Dim jsonContent As String = File.ReadAllText(jsonFilePath)
Dim jsonDocument As JsonDocument = JsonDocument.Parse(jsonContent)
Dim rootElement As JsonElement = jsonDocument.RootElement
For Each item As JsonProperty In rootElement.EnumerateObject()
	If item.NameEquals("Projects") Then
    	Debug.WriteLine("Name: " & item.Name & ", Value: " & item.Value.GetString)
	End If
Next
```

可以使用下面代码遍历 JSON 数组：

```vb
For Each project As JsonElement In projectElement.EnumerateArray()
	'......
Next
```

可以通过 `JsonProperty` 对象的 `GetXXX()` 方法获取 JSON 正确类型的值：

```vb
Public Sub InitProject(ByRef form As AndroidSettingsForm, ByRef projectElement As JsonElement)
    For Each project As JsonElement In projectElement.EnumerateArray()
        Debug.WriteLine("[AndroidProjectInit] InitProject=>project: " & project.ToString)
        Dim info = New ProjectInfo()
        For Each item As JsonProperty In project.EnumerateObject()
            If item.NameEquals("ProjectId") Then
                info.ProjectId = item.Value.GetString
            ElseIf item.NameEquals("AndroidVersion") Then
                info.AndroidVersion = item.Value.GetString
            ElseIf item.NameEquals("ProjectPath") Then
                info.ProjectPath = item.Value.GetString
            ElseIf item.NameEquals("PublicDirName") Then
                info.PublicDirName = item.Value.GetString
            ElseIf item.NameEquals("MssiDirName") Then
                info.MssiDirName = item.Value.GetString
            ElseIf item.NameEquals("DriveDirName") Then
                info.DriveDirName = item.Value.GetString
            ElseIf item.NameEquals("CustomDirName") Then
                info.CustomDirName = item.Value.GetString
            ElseIf item.NameEquals("Gms") Then
                info.Gms = item.Value.GetInt32
            ElseIf item.NameEquals("Go") Then
                info.Go = item.Value.GetInt32
            ElseIf item.NameEquals("ChiperMaker") Then
                info.ChiperMaker = item.Value.GetString
            ElseIf item.NameEquals("ChiperModel") Then
                info.ChiperModel = item.Value.GetString
            End If
        Next
        Debug.WriteLine("[AndroidProjectInit] InitProject=>info: " & info.ToString)
        form.Projects.Add(info)
    Next
    form.Projects.Sort(New ProjectComparer())
End Sub
```

