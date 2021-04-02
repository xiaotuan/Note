### 4.7.5　QDockWidget的操作

程序运行时，主窗口上的DockWidget组件可以被拖动，在主窗口的左、右两侧停靠，或在桌面上浮动。工具栏上“窗体浮动”和“窗口可见”两个按钮可以用代码控制停靠区是否浮动、是否可见，其代码如下：

```css
void MainWindow::on_actDockVisible_toggled(bool arg1)
{// 停靠区的可见性
   ui->dockWidget->setVisible(arg1);
}
void MainWindow::on_actDockFloat_triggered(bool checked)
{//停靠区浮动性
   ui->dockWidget->setFloating(checked);
}
```

单击DockWidget组件标题栏的关闭按钮时，会隐藏停靠区并发射信号visibilityChanged(bool)；当拖动DockWidget组件，使其浮动或停靠时，会发射信号topLevelChanged(bool)。为这两个信号编写槽函数，可更新两个Actions的状态。

```css
void MainWindow::on_dockWidget_visibilityChanged(bool visible)
{//停靠区可见性变化
   ui->actDockVisible->setChecked(visible);
}
void MainWindow::on_dockWidget_topLevelChanged(bool topLevel)
{//停靠区浮动性变化
   ui->actDockFloat->setChecked(topLevel);
}
```

