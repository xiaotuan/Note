### 6.2.4　对话框QWDialogLocate的创建与使用

#### 1．非模态对话框

前面设计的两个对话框是以模态（Modal）方式显示的，即用QDialog::exec()函数显示。模态显示的对话框不允许鼠标再去单击其他窗口，直到对话框退出。

若使用QDialog::show()，则能以非模态（Modeless）方式显示对话框。非模态显示的对话框在显示后继续运行主程序，还可以在主窗口上操作，主窗口和非模态对话框之间可以交互控制，典型的例子是文字编辑软件里的“查找/替换”对话框。

图6-7中的单元格定位与文字设置对话框以非模态方式显示，对话框类是QWDialogLocate，它有如下的一些功能。

+ 主窗口每次调用此对话框时，就会创建此对话框对象，并以StayOnTop的方式显示，对话框关闭时自动删除。
+ 在对话框中可以定位主窗口上TableView组件的单元格，并设置单元格的文字。
+ 在主窗口的TableView组件中单击鼠标时，如果对话框已创建，则自动更新对话框上单元格的行号和列号SpinBox组件的值。
+ 主窗口上的actTab_Locate用于调用对话框，调用时actTab_Locate设置为禁用，当对话框关闭时自动使能actTab_Locate。这样避免对话框显示时，在主窗口上再次单击“定位单元格”按钮，而在对话框关闭和释放后，按钮又恢复为可用。

对话框QWDialogLocate的类定义代码如下，各接口函数的意义和实现在后面介绍。

```css
class QWDialogLocate : public QDialog
{
   Q_OBJECT
private:
   void closeEvent(QCloseEvent *event);
public:
   explicit QWDialogLocate(QWidget *parent = 0);
   ~QWDialogLocate();
   void   setSpinRange(int rowCount, int colCount); //设置最大值
   void   setSpinValue(int rowNo, int colNo);//设置初始值
private slots:
   void on_btnSetText_clicked();
private:
   Ui::QWDialogLocate *ui;
};
```

#### 2．对话框的创建与调用

对话框QWDialogLocate是从QDialog继承而来的可视化设计的对话框类，其界面设计不再详述。为了在主窗口中也能操作对话框，需要保留对话框实例对象名，所以在MainWindow定义对话框QWDialogLocate的一个指针dlgLocate，并初始化为NULL。

```css
private:
   QWDialogLocate  *dlgLocate=NULL; 
```

主窗口上的actTab_Locate用于调用此对话框，其triggered()信号槽函数代码如下：

```css
void MainWindow::on_actTab_Locate_triggered()
{//创建 StayOnTop的对话框，对话框关闭时自动删除
   ui->actTab_Locate->setEnabled(false); 
   dlgLocate = new QWDialogLocate(this);
   dlgLocate->setAttribute(Qt::WA_DeleteOnClose); //对话框关闭时自动删除
   Qt::WindowFlags   flags=dlgLocate->windowFlags(); //获取已有flags
   dlgLocate->setWindowFlags(flags | Qt::WindowStaysOnTopHint); //StayOnTop
   dlgLocate->setSpinRange(theModel->rowCount(),theModel->columnCount());
   QModelIndex curIndex=theSelection->currentIndex();
   if (curIndex.isValid())
      dlgLocate->setSpinValue(curIndex.row(),curIndex.column());
   dlgLocate->show();  //非模态显示对话框
}
```

在这段代码中，使用QWidget::setAttribute()函数将对话框设置为关闭时自动删除。

```css
dlgLocate->setAttribute(Qt::WA_DeleteOnClose);
```

setAttribute()用于对窗体的一些属性进行设置，当设置为Qt::WA_DeleteOnClose时，窗口关闭时会自动删除，以释放内存。这与前面两个对话框是不同的，前面两个对话框在关闭时缺省是隐藏自己，除非显式地使用delete进行删除。

程序还调用QWidget::setWindowFlags()将对话框设置为StayOnTop显示。

```css
dlgLocate->setWindowFlags(flags | Qt::WindowStaysOnTopHint);
```

对话框窗口效果设置后，再设置其初始数据，然后调用show()显示对话框。显示对话框后，主程序继续运行，不会等待对话框的返回结果。鼠标可以操作主窗口上的界面，但是因为actTab_Locate被禁用了，不能再重复单击“定位单元格”按钮。

#### 3．对话框中操作主窗口

在对话框上单击“设定文字”按钮，会在主窗口中定位到指定的单元格，并设定为输入的文字，按钮的代码如下：

```css
void QWDialogLocate::on_btnSetText_clicked()
{//定位到单元格，并设置字符串
   int row=ui->spinBoxRow->value(); //行号
   int col=ui->spinBoxColumn->value();//列号
   MainWindow *parWind = (MainWindow*)parentWidget(); //获取主窗口
   parWind->setACellText(row,col,ui->edtCaption->text()); //调用主窗口函数
   if (ui->chkBoxRow->isChecked()) //行增
      ui->spinBoxRow->setValue(1+ui->spinBoxRow->value());
   if (ui->chkBoxColumn->isChecked()) //列增
      ui->spinBoxColumn->setValue(1+ui->spinBoxColumn->value());
}
```

想要在对话框中操作主窗口，就需要获取主窗口对象，调用主窗口的函数并传递参数。在上面的代码中，通过下面一行语句获得主窗口对象：

```css
MainWindow *parWind = (MainWindow*)parentWidget();
```

parentWidget()是QWidget类的一个函数，指向父窗口。在创建此对话框时，将主窗口的指针传递给对话框的构造函数，即：

```css
dlgLocate = new QWDialogLocate(this);
```

所以，对话框的parentWidget指向主窗口。

然后调用主窗口的一个自定义的public函数setACellText()，传递行号、列号和字符串，由主窗口更新指定单元格的文字。下面是主窗口的setACellText()函数的代码。

```css
void MainWindow::setACellText(int row, int column, QString text)
{//定位到单元格，并设置字符串
   QModelIndex index=theModel->index(row,column);//获取模型索引
   theSelection->clearSelection();
   theSelection->setCurrentIndex(index,QItemSelectionModel::Select); 
   theModel->setData(index,text,Qt::DisplayRole);//设置单元格字符串
}
```

这样就实现了在对话框里对主窗口进行的操作，主要是获取主窗口对象，然后调用相应的函数。

#### 4．主窗口中操作对话框

在主窗口上用鼠标单击TableView组件的某个单元格时，如果单元格定位对话框dlgLocate已经存在，就将单元格的行号、列号更新到对话框上，实现代码如下：

```css
void MainWindow::on_tableView_clicked(const QModelIndex &index)
{//单击单元格时，将单元格的行号、列号设置到对话框上
   if (dlgLocate!=NULL) 
      dlgLocate->setSpinValue(index.row(),index.column());
}
```

因为主窗口中定义了对话框的指针，只要它不为NULL，就说明对话框存在，调用对话框的一个自定义函数setSpinValue()，刷新对话框显示界面。QWDialogLocate的setSpinValue()函数实现如下：

```css
void QWDialogLocate::setSpinValue(int rowNo, int colNo)
{//设置SpinBox组件的数值
   ui->spinBoxRow->setValue(rowNo);
   ui->spinBoxColumn->setValue(colNo);
}
```

#### 5．窗口的CloseEvent事件

对话框和主窗口之间互相操作的关键是要有对方对象的指针，然后才能传递参数并调用对方的函数。在对话框关闭时，还需要做一些处理：将主窗口的actTab_Locate重新设置为使能，将主窗口的指向对话框的指针dlgLocate重新设置为NULL。

由于对话框dlgLocate是以非模态方式运行的，程序无法等待对话框结束后作出响应，但是可以利用窗口的CloseEvent事件。

事件（event）是由窗口系统产生的由某些操作触发的特殊函数，例如鼠标操作、键盘操作的一些事件，还有窗口显示、关闭、绘制等相关的事件。从QWidget继承的窗口部件常用的事件函数有如下几种。

+ closeEvent()：窗口关闭时触发的事件，通常在此事件做窗口关闭时的一些处理，例如显示一个对话框询问是否关闭窗口。
+ showEvent()：窗口显示时触发的事件。
+ paintEvent()：窗口绘制事件，第8章介绍绘图时会用到。
+ mouseMoveEvent()：鼠标移动事件。
+ mousePressEvent()：鼠标键按下事件。
+ mouseReleaseEvent()：鼠标键释放事件。
+ keyPressEvent()：键盘按键按下事件。
+ keyReleaseEvent()：键盘按键释放事件。 要利用某个事件进行一些处理，需要在窗口类里重定义事件函数并编写响应代码。在后面的例子中，将逐渐演示一些事件的用法。

在本例中，要利用对话框的closeEvent()事件，在类定义中声明了此事件的函数，其实现代码如下：

```css
void QWDialogLocate::closeEvent(QCloseEvent *event)
{ //窗口关闭 event
   MainWindow *parWind = (MainWindow*)parentWidget(); //获取父窗口指针
   parWind->setActLocateEnable(true);//使能 actTab_Locate
   parWind->setDlgLocateNull(); //将窗口指针设置为NULL
}
```

在closeEvent()事件里，调用主窗口的两个函数，将actTab_Locate重新使能，将主窗口内指向对话框的指针设置为NULL。主窗口中这两个函数的实现代码如下：

```css
void MainWindow::setActLocateEnable(bool enable)
{   ui->actTab_Locate->setEnabled(enable);
}
void MainWindow::setDlgLocateNull()
{   dlgLocate=NULL;
}
```

利用closeEvent()事件，可以询问窗口是否退出，例如为主窗口添加closeEvent()事件的处理，代码如下：

```css
void MainWindow::closeEvent(QCloseEvent *event)
{ //窗口关闭时询问是否退出
   QMessageBox::StandardButton result=QMessageBox::question(this,
               "确认", "确定要退出本程序吗？",
               QMessageBox::Yes|QMessageBox::No |QMessageBox::Cancel,
               QMessageBox::No);
   if (result==QMessageBox::Yes)
      event->accept();
   else
      event->ignore();
}
```

这样，主窗口关闭时就会出现一个询问对话框，如果不单击“Yes”按钮，程序就不关闭；否则应用程序结束。

