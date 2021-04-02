### 4.4.3　QCalendarWidget日历组件

图4-5窗体右侧是一个QCalendarWidget组件，它以日历的形式显示日期，可以用于日期选择。

QCalendarWidget有一个信号selectionChanged()，在日历上选择的日期变化后会发射此信号，为此信号创建槽函数，编写代码如下：

```css
void Dialog::on_calendarWidget_selectionChanged()
{ //在日历上选择日期
   QDate dt=ui->calendarWidget->selectedDate();
   QString str=dt.toString("yyyy年M月d日"); 
   ui->editCalendar->setText(str);
}
```

