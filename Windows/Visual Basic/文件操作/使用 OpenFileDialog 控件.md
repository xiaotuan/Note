[toc]

### 1. 创建 OpenFileDialog 控件

`OpenFileDialog` 控件用于打开一个对话框，让用户能够浏览和选择文件。使用 `OpenFileDialog` 控件步骤如下：

1. 双击工具箱中的 `OpenFileDialog` 项，将一个新的 `OpenFileDialog` 控件添加到项目中。

2. 在窗体中添加一个按钮，并按如下设置它的属性：

   | 属性     | 值          |
   | -------- | ----------- |
   | Name     | btnOpenFile |
   | Location | 9,6         |
   | Size     | 80,23       |
   | Text     | Source      |

3. 双击按钮，并在它的 `Click` 事件中添加如下代码：

   ```vb
   OpenFileDialog.InitialDirectory = "C:\"
   OpenFileDialog.Title = "Select a File"
   OpenFileDialog.FileName = ""
   ```

   第一条语句指定对话框出现时显示的目录。如果没有为 `InitialDirectory` 属性指定目录，将使用活动的系统目录（如果使用其他 "打开文件" 对话框浏览的最后一个目录）。

   `Title` 属性指定了标题栏中显示的文本。如果没有指定 `Title` 属性， Visual Basic 将在标题栏中显示 “打开”。

   `FileName` 属性用于返回选定文件的文件名。如果在显示 `OpenFileDialog` 前没有改属性设置为空字符串。将默认使用控件的名称。

### 2. 创建文件过滤器

不同类型的文件有不同的扩展名，`Filter` 属性决定了哪些类型的文件可显示在 `OpenFileDialog` 中。过滤器通过如下格式指定：

```
Description|*.extension
```

在管道符号（`|`）前的文本时对要筛选的文件类型的说明，而管道符号后的文本是用于筛选文件的模式。例如，要只显示 Windows 位图文件，可使用如下过滤器：

```vb
OpenFileDialog.Filter = "Windows Bitmaps|*.bmp"
```

可以指定多个过滤器。为此，在过滤器之间添加一个管道符号，如下所示：

```vb
OpenFileDialog.Filter = "Windows Bitmaps|*.bmp|JPEG Files|*.jpg"
```

有多个过滤器时，可使用 `FilterIndex` 属性来指定哪个过滤器默认被选中。例如：

```vb
OpenFileDialog.FilterIndex = 1
```

> 注意：和其他大多数集合不同，`FilterIndex` 属性的索引是从 1  而不是 0 开始的，所以 1 是列表中的第一个过滤器。

### 2. 显示 OpenFileDialog

要显示 `OpenFileDialog` 控件，以根据用户是否选择了文件而采取相应的操作。`OpenFileDialog` 的 `ShowDialog()` 方法与窗体的同名方法类似，它返回用户在对话框中的选择结果：

```vb
If OpenFileDialog.ShowDialog() <> Windows.Forms.DialogResult.Cancel Then
    txtSource.Text = OpenFileDialog.FileName
Else
    txtSource.Text = ""
End If
```

> 提示：默认情况下，`OpenFileDialog` 不允许用户输入不存在的文件名。可以通过将 `OpenFileDialog` 控件的 `CheckFileExists` 属性设置为 `False` 来覆盖这种行为。

> 注意：`OpenFileDialog` 控件允许用户选择多个文件，可以通过设置 `MultiSelect` 属性来实现。