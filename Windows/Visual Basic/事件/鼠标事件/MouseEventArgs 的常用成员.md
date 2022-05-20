在鼠标事件方法中都会有一个 `MouseEventArgs` 参数，例如单击事件：

```vb
Private Sub picText_MouseDown(sender As Object, e As MouseEventArgs) Handles picText.MouseDown

End Sub
```

`System.Windows.Forms.MouseEventArgs` 的常用成员有：

| 属性     | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| Clicks   | 返回单击鼠标按钮的次数                                       |
| Button   | 返回单击的按键（左、中、右）                                 |
| Delta    | 返回一个正数或负数，指出向前或向后滚动鼠标滑轮的次数         |
| X        | 返回用户单击时广播所处位置的水平坐标                         |
| Y        | 返回用户单击时光标所处位置的垂直坐标                         |
| Location | 返回一个 Point 对象，其中包含用户单击时鼠标所处位置的 X 坐标和 Y 坐标 |

