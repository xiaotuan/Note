`SaveFileDialog` 控件与 `OpenFileDialog` 控件类似，但它让用户浏览目录并将文件保存而不是要打开文件。`SaveFileDialog` 控件实际上并不保存文件，它只是让用户指定要保存文件的文件名。执行下列步骤来创建 `SaveFileDialog`：

1. 在窗体上创建一个新文本框，并按如下设置它的属性：

   | 属性     | 值             |
   | -------- | -------------- |
   | Name     | txtDestination |
   | Location | 95,34          |
   | Size     | 184,20         |

2. 创建一个这样的按钮，即用户通过单击它可指定要保存文件的文件名。在窗体上添加一个新按钮，并按如下设置它的属性：

   | 属性     | 值           |
   | -------- | ------------ |
   | Name     | btnSaveFile  |
   | Location | 9,31         |
   | Size     | 80,23        |
   | Text     | Destination: |

3. 在工具箱中双击 `SaveFileDialog` 项，将一个新控件添加到项目中。

4. 双击刚创建的按钮（`btnSaveFile`），在它的 `Click` 事件中添加如下代码：

   ```vb
   SaveFileDialog1.Title = "Secify Destination Fileename"
   SaveFileDialog1.Filter = "Text Files (*.txt)|*.txt"
   SaveFileDialog1.FilterIndex = 1
   SaveFileDialog1.OverwritePrompt = True
   ```

   `OverwritePrompt` 属性是 `SaveFileDialog` 特有的，该属性设置为 True 时，如果用户选择了已有的文件，Visual Basic 将要求用户确认。

   > 注意：如果希望在用户指定的文件不存在时提示用户，将 `SaveFileDialog` 控件的 `CreatePrompt` 属性设置为 `True`。

5. 最后还需要添加一段代码，将选中文件的文件名放在文本框 `txtDestination` 中。输入下面列出的代码：

   ```vb
   If SaveFileDialog1.ShowDialog() <> Windows.Forms.DialogResult.Cancel Then
       txtDestination.Text = SaveFileDialog1.FileName
   End If
   ```

   