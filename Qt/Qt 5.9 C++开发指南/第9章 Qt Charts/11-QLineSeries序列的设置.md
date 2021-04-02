### 9.2.5　QLineSeries序列的设置

本实例图表的序列使用的是QLineSeries，它是QXYSeries的子类，用于绘制二维数据点的折线图。QLineSeries的主要函数见表9-4（包括从父类继承的函数，仅列出函数的返回数据类型，省略了输入参数）。

<center class="my_markdown"><b class="my_markdown">表9-4　QLineSeries类的主要函数</b></center>

| 分组 | 函数 | 功能描述 |
| :-----  | :-----  | :-----  | :-----  | :-----  |
| 序列名称 | void　setName() | 设置序列的名称，这个名称会显示在图例里，支持HTML格式 |
| 图表 | QChart*　chart() | 返回序列所属的图表对象 |
| 序列外观 | void　setVisible() | 设置序列可见性 |
| void　show() | 显示序列，使序列可见 |
| void　hide() | 隐藏序列，使其不可见 |
| void　setColor() | 设置序列线条的颜色 |
| void　setPen() | 设置绘制线条的画笔 |
| void　setBrush() | 设置绘制数据点的画刷 |
| void　setOpacity() | 设置序列的透明度，0表示完全透明，1表示不透明 |
| 数据点 | void　setPointsVisible() | 设置数据点的可见性 |
| void　append() | 添加一个数据点到序列 |
| void　insert() | 在某个位置插入一个数据点 |
| void　replace() | 替换某个数据点 |
| void　clear() | 清除所有数据点 |
| void　remove() | 删除某个数据点 |
| void　removePoints() | 从某个位置开始，删除指定个数的数据点 |
| int　count() | 数据点的个数 |
| 数据点 | QPointF&　at() | 返回某个位置的数据点 |
| QList<QPointF>　points() | 返回数据点的列表 |
| QVector<QPointF> pointsVector() | 返回数据点的，效率更高 |
| 数据点标签 | void　setPointLabelsVisible() | 设置数据点标签的可见性 |
| void　setPointLabelsColor() | 设置数据点标签的文字颜色 |
| void　setPointLabelsFont() | 设置数据点标签字体 |
| void　setPointLabelsFormat() | 设置数据点标签格式 |
| void　setPointLabelsClipping() | 设置标签的裁剪属性，缺省为True，即绘图区外的标签被裁剪掉 |
| 坐标轴 | bool　attachAxis() | 为序列附加一个坐标轴，通常需要一个X轴和一个Y轴 |
| bool　detachAxis() | 解除一个附加的坐标轴 |
| QList<QAbstractAxis *> attachedAxes() | 返回附加的坐标轴的列表 |

实例中对曲线序列进行属性设置的界面如图9-8所示。首先通过上方的“选择操作序列”里的两个RadioButton按钮选择当前操作序列，两个按钮的代码相同，代码如下：

```css
void MainWindow::on_radioSeries0_clicked()
{//获取当前数据序列
   if (ui->radioSeries0->isChecked())
      curSeries=(QLineSeries *)ui->chartView->chart()->series().at(0);
   else
      curSeries=(QLineSeries *)ui->chartView->chart()->series().at(1);
//获取序列的属性值，并显示到界面上
   ui->editSeriesName->setText(curSeries->name());
   ui->chkSeriesVisible->setChecked(curSeries->isVisible());
   ui->chkPointVisible->setChecked(curSeries->pointsVisible());
   ui->sliderSeriesOpacity->setValue(curSeries->opacity()*10);
   ui->chkPointLabelVisible->setChecked(curSeries->pointLabelsVisible());
}
```

curSeries是在MainWindow类里定义的私有变量，用于指向当前操作的序列。选择序列后，会将当前序列的一些属性值显示到界面上，如序列名称、序列可见性、序列数据点可见性等。

序列的一些常规属性的设置都很简单，例如序列名称设置、序列可见性设置、曲线pen属性设置等，调用相应函数即可。

数据点标签的格式设置使用函数setPointLabelsFormat()，有两种数据可以在数据点标签中显示，有固定的标签：

@xPoint，数据点的X值；

@yPoint，数据点的Y值。

例如，使数据点标签只显示Y值，设置语句为：

```css
curSeries->setPointLabelsFormat("@yPoint");
```

如果使数据点标签显示(X, Y)值，设置语句为：

```css
curSeries->setPointLabelsFormat("(@xPoint,@yPoint)");
```

为一个序列添加数据点，可以使用append()函数，也可以使用流操作符“<<”，如prepareData()函数中添加数据点的部分也可以改写为：

```css
*series0<<QPointF(t,y1);  //序列添加数据点
```

为序列指定坐标轴，在前面的createChart()函数中，使用QChart的函数为序列设置坐标轴：

```css
chart->setAxisX(axisX, series0); //添加X坐标轴
chart->setAxisX(axisX, series1); //添加X坐标轴
chart->setAxisY(axisY, series0); //添加Y坐标轴
chart->setAxisY(axisY, series1); //添加Y坐标轴
```

QChart:: setAxisX()函数为序列指定X坐标轴，并将坐标轴添加到图表里；QChart::setAxisY()函数为序列指定Y坐标轴，并将坐标轴添加到图表里。无需再调用序列的attachAxis()函数。若要使用序列的attachAxis()函数，则实现上述功能的代码如下：

```css
chart->addAxis(axisX,Qt::AlignBottom); //坐标轴添加到图表，并指定方向
chart->addAxis(axisY,Qt::AlignLeft);
series0->attachAxis(axisX); //序列 series0 附加坐标轴
series0->attachAxis(axisY);
series1->attachAxis(axisX);//序列 series1 附加坐标轴
series1->attachAxis(axisY);
```

即先用QChart:: addAxis()函数添加一个坐标轴到图表，并指定坐标轴的方向，然后用序列的attachAxis()函数附加坐标轴对象。

