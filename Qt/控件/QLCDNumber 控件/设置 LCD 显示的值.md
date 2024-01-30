可以通过 `QLCDNumber` 的 `display(int num)` 方法设置控件要显示的数值：

```cpp
void MainWindow::on_Dial_valueChanged(int value)
{
    // 设置 LCD 的显示值等于 Dial 的值
    ui->LCDDisplay->display(value);
}
```



