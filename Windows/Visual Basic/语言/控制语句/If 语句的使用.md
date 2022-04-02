`If` 语句的通用格式如下所示：

``` vb
If condition Then
    statement
End If
```

例如：

```vb
' Show the open file dialog box.
If odfSelectPicture.ShowDialog = DialogResult.OK Then
    ' Load the picture into the picture box.
    picShowPicture.Image = Image.FromFile(odfSelectPicture.FileName)
    'Show the name of the file in the form's caption
    Me.Text = "Picture Viewer(" & odfSelectPicture.FileName & ")"
End If
```

