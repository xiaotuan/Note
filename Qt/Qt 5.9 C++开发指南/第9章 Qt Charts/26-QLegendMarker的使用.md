### 9.4.5　QLegendMarker的使用

图表创建序列后会自动创建图例，QLegend有一个只读属性markers，是一个列表类型，存储了每个序列的QLegendMarker对象。markers函数的原型如下：

```css
QList<QLegendMarker *> QLegend::markers(QAbstractSeries *series = Q_NULLPTR) 
```

如果不指定序列，则返回图表所有序列的LegendMarker对象列表。

QLegendMarker是直接继承自QObject的类，用于在图例中对关联的序列进行操作。QLegendMarker有两个部分，一个反映了序列颜色的颜色框，一个是反映序列名称的标签。QLegendMarker类的主要函数见表9-11（省略了函数参数中的const关键字）。

<center class="my_markdown"><b class="my_markdown">表9-11　QLegendMarker类的主要函数</b></center>

| 函数原型 | 功能描述 |
| :-----  | :-----  | :-----  | :-----  |
| void　setVisible(bool visible) | 设置图例标记的可见性 |
| void　setLabel(QString &label) | 设置标签，即图例中的序列的名称 |
| void　setFont(QFont &font) | 设置标签的字体 |
| QAbstractSeries *　series() | 返回关联的序列 |
| LegendMarkerType　type() | 返回图例标记的类型，取决于关联的序列的类型，有： | QLegendMarker::LegendMarkerTypeArea | QLegendMarker::LegendMarkerTypeBar | QLegendMarker::LegendMarkerTypePie | QLegendMarker::LegendMarkerTypeXY | QLegendMarker::LegendMarkerTypeBoxPlot | LegendMarkerTypeXY用于所有从QXYSeries继承的序列类 |

QLegendMarker::visible属性控制图例标记的可见性，如果设置为false，在图例中就不会显示这个图例标记。可以将QLegendMarker当作一个QCheckBox使用，单击图例中相应的LegendMarker时，显示或隐藏相关联的序列，这只需要设计一个槽函数响应QLegendMarker的clicked()信号即可。

在createChart()函数中为图表创建两个QLineSeries序列后，在最后添加如下代码：

```css
foreach (QLegendMarker* marker, chart->legend()->markers())
   connect(marker, SIGNAL(clicked()), 
                this, SLOT(on_LegendMarkerClicked()));
```

该语句通过图例的markers()获取其QLegendMarker列表，然后为每个marker的clicked()信号关联自定义的槽函数on_LegendMarkerClicked()。

下面是槽函数on_LegendMarkerClicked()的代码：

```css
void MainWindow::on_LegendMarkerClicked()
{//单击图例的marker的响应
   QLegendMarker* marker = qobject_cast<QLegendMarker*> (sender());
   switch (marker->type()) //marker的类型
   {  case QLegendMarker::LegendMarkerTypeXY: //QLineSeries序列
      {  marker->series()->setVisible(!marker->series()->isVisible()); 
         marker->setVisible(true);
      }
   }
}
```

这里，首先将产生信号的对象sender()转换为QLegendMarker类对象marker，然后根据marker->type()判断图例标记的类型，本实例里创建的是QLineSeries序列，所以图例标记的类型是QLegendMarker::LegendMarkerTypeXY。

通过marker->series()获取关联的序列，然后交替设置其可见性，即：

```css
marker->series()->setVisible(!marker->series()->isVisible()); 
```

marker的可见性总是设置为true，因为若设置为false，图例标记也会被隐藏，就无法再用鼠标单击操作了。

