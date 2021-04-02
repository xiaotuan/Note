### 9.4.2　自定义QWChartView类

QChart和QChartView是基于Graphics View结构的绘图类，要对一个QChart图表进行鼠标和按键操作，需要在QChartView组件里对鼠标和按键事件进行处理，这就需要自定义一个从QChartView继承的类，这与实例samp8_5中从QGraphicsView继承一个自定义图形视图类，实现鼠标和按键操作的原理类似。

自定义一个QWChartView类，它从QChartView继承而来，对鼠标和按键事件进行处理。QWChartView类的定义如下：

```css
class QWChartView : public QChartView
{
   Q_OBJECT
private:
   QPoint  beginPoint; //选择矩形区的起点
   QPoint  endPoint;  //选择矩形区的终点
protected:
   void mousePressEvent(QMouseEvent *event); //鼠标左键按下
   void mouseMoveEvent(QMouseEvent *event); //鼠标移动
   void mouseReleaseEvent(QMouseEvent *event); //鼠标释放左键
   void keyPressEvent(QKeyEvent *event); //按键事件
public:
   explicit QWChartView(QWidget *parent = 0);
   ~QWChartView();
signals:
   void mouseMovePoint(QPoint point); //鼠标移动信号
};
```

QWChartView类中定义了两个私有变量beginPoint和endPoint用于鼠标框选矩形区域的起点和终点。QWChartView重定义了鼠标的3个事件函数和键盘按键事件的函数，定义了一个信号mouseMovePoint(QPoint point)，在mouseMoveEvent()事件里发射此信号并传递鼠标光标处的屏幕坐标，用于在主窗口里实现鼠标在图表上移动时显示当前位置的坐标。

下面是QWChartView类各个函数的实现。

```css
QWChartView::QWChartView(QWidget *parent):QChartView(parent)
{//构造函数
   this->setDragMode(QGraphicsView::RubberBandDrag);
   this->setMouseTracking(true);//必须开启此功能，缺省为false
}
void QWChartView::mousePressEvent(QMouseEvent *event)
{//鼠标左键按下，记录beginPoint
   if (event->button()==Qt::LeftButton)
      beginPoint=event->pos();
   QChartView::mousePressEvent(event);
}
void QWChartView::mouseMoveEvent(QMouseEvent *event)
{//鼠标移动事件
   QPoint  point=event->pos();
   emit mouseMovePoint(point);
   QChartView::mouseMoveEvent(event);
}
void QWChartView::mouseReleaseEvent(QMouseEvent *event)
{//鼠标左键释放事件
   if (event->button()==Qt::LeftButton)
   { //鼠标左键释放，获取矩形框的endPoint,进行缩放
      endPoint=event->pos();
      QRectF  rectF;
      rectF.setTopLeft(this->beginPoint);
      rectF.setBottomRight(this->endPoint);
      this->chart()->zoomIn(rectF);
   }
   else if (event->button()==Qt::RightButton)
      this->chart()->zoomReset(); //鼠标右键释放，resetZoom
   QChartView::mouseReleaseEvent(event);
}
void QWChartView::keyPressEvent(QKeyEvent *event)
{//按键控制
   switch (event->key()) {
   case Qt::Key_Plus:  
      chart()->zoom(1.2);      break;
   case Qt::Key_Minus:
      chart()->zoom(0.8);      break;
   case Qt::Key_Left:
      chart()->scroll(10, 0);      break;
   case Qt::Key_Right:
      chart()->scroll(-10, 0);     break;
   case Qt::Key_Up:
      chart()->scroll(0, -10);     break;
   case Qt::Key_Down:
      chart()->scroll(0, 10);      break;
   case Qt::Key_PageUp:
      chart()->scroll(0, 50);      break;
   case Qt::Key_PageDown:
      chart()->scroll(0, -50);      break;
   case Qt::Key_Home:
      chart()->zoomReset();       break;
   default:
      QGraphicsView::keyPressEvent(event);
    }
}
```

在构造函数里，setDragMode(QGraphicsView::RubberBandDrag)将视图组件鼠标拖动选择方式设置为“橡皮框”形式，即鼠标左键按下时，随着鼠标拖动显示一个矩形选择框。

setMouseTracking(true)将鼠标跟踪设置为true（缺省为false）。如果不设置为true，窗口组件只在某个鼠标按键按下时才接收鼠标移动事件，设置为true之后，只要鼠标移动就会发射mouseMoveEvent()事件。

mousePressEvent(QMouseEvent *event)是在鼠标左键或右键按下时发生的事件，在响应程序里先判断鼠标左键是否按下，如果是鼠标左键按下了，就用变量beginPoint记录鼠标在视图组件中的位置。

mouseReleaseEvent(QMouseEvent *event)是在鼠标左键或右键释放时发生的事件，若是鼠标左键释放，则用变量endPoint记录鼠标位置坐标，beginPoint和endPoint就定义了鼠标框选的矩形区域，用关联的chart组件的zoomIn()函数显示这个矩形区域实现放大。

mouseMoveEvent(QMouseEvent *event)是鼠标在图表上移动时发生的事件，通过event->pos()获取鼠标在视图组件中的坐标point，然后发射信号mouseMovePoint(point)。在使用QWChartView类组件的主窗口里，可以定义槽函数对此信号作出响应，通过传递的参数将视图坐标转换为图表的坐标，从而实现鼠标位置的数值显示。

keyPressEvent(QKeyEvent *event)是键盘按键按下时发生的事件，从event->key()可以获得按下按键的名称，判断按键，然后做出缩放、移动等操作。

QChart::zoom(qreal factor)函数对图表显示区的内容进行缩放，factor大于1是放大，小于1是缩小，缩放后坐标轴的范围会自动变化。

QChart::scroll(qreal dx, qreal dy)函数将图表内容在平面上平移，平移后坐标轴会自动变化。

QChart::zoomReset()函数将取消所有缩放变化，恢复原始的大小。

