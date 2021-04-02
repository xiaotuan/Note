### 6.2.3　对话框QWDialogHeaders的创建和使用

#### 1．对话框的生存期

对话框的生存期是指它从创建到删除的存续区间。前面介绍的设置表格行数和列数的对话框的生存期只在调用它的按钮的槽函数里，因为对话框是动态创建的，调用结束后就会被删除。

而对于图6-6所示的设置表头标题对话框，我们希望在主窗口里首次调用时创建它，对话框关闭时并不删除，只是隐藏，下次调用时再次显示此对话框。只有在主窗口释放时该对话框才释放，所以这个对话框的生存期在主窗口存续期间。

#### 2．QWDialogHeaders的定义和实现

设置表头标题的对话框类是QWDialogHeaders，它也是从QDialog继承的可视对话框类。其界面显示使用QListView组件，用QStringListModel变量管理字符串列表数据，构成Model/View结构。对话框上同样有“确定”和“取消”两个按钮，设置与对话框的accept()和reject()槽关联。

QWDialogHeaders类的定义如下：

```css
class QWDialogHeaders : public QDialog
{
   Q_OBJECT
private:
   QStringListModel  *model;
public:
   explicit QWDialogHeaders(QWidget *parent = 0);
   ~QWDialogHeaders();
   void   setHeaderList(QStringList& headers);
   QStringList   headerList();
private:
   Ui::QWDialogHeaders *ui;
};
```

QWDialogSize类接口函数实现的代码如下：

```css
QWDialogHeaders::QWDialogHeaders(QWidget *parent) :   QDialog(parent),
   ui(new Ui::QWDialogHeaders)
{
   ui->setupUi(this);
   model= new QStringListModel;
   ui->listView->setModel(model);
}
QWDialogHeaders::~QWDialogHeaders()
{
   QMessageBox::information(this,"提示","设置表头标题对话框被删除");
   delete ui;
}
void QWDialogHeaders::setHeaderList(QStringList &headers)
{//初始化数据模型的字符串列表
   model->setStringList(headers);
}
QStringList QWDialogHeaders::headerList()
{//返回字符串列表
   return  model->stringList();
}
```

#### 3．QWDialogHeaders对话框的使用

因为要在主窗口中重复调用此对话框，所以在MainWindow的private部分定义一个QWDialog　Headers类型的指针变量，并且将此指针初始化设置为NULL，用于判断对话框是否已经被创建。在MainWindow中的定义如下：

```css
private:
   QWDialogHeaders *dlgSetHeaders=NULL;
```

下面是主窗口工具栏上的“设置表头标题”按钮的响应代码。

```css
void MainWindow::on_actTab_SetHeader_triggered()
{//一次创建，多次调用，对话框关闭时只是隐藏
   if (dlgSetHeaders==NULL) 
     dlgSetHeaders = new QWDialogHeaders(this);
   if (dlgSetHeaders->headerList().count()!=theModel->columnCount())
   {//如果表头列数变化，重新初始化
     QStringList strList;
     for (int i=0;i<theModel->columnCount();i++)//获取现有的表头标题
       strList.append(theModel->headerData(i,Qt::Horizontal,
             Qt::DisplayRole).toString());
     dlgSetHeaders->setHeaderList(strList);//对话框初始化显示
   }
   int ret=dlgSetHeaders->exec();// 以模态方式显示对话框
   if (ret==QDialog::Accepted) //OK键被按下
   {
      QStringList strList=dlgSetHeaders->headerList();
      theModel->setHorizontalHeaderLabels(strList);// 设置模型的表头标题
   }
}
```

在这段代码中，首先判断主窗口的成员变量dlgSetHeaders是否为NULL，如果为NULL（初始化为NULL），说明对话框还没有被创建，就创建对话框。

初始化的工作是获取主窗口数据模型现有的表头标题，然后调用对话框的自定义函数setHeaderList()，设置其为对话框的数据源。

使用exec()函数模态显示对话框，然后在“确定”按钮被单击时获取对话框上输入的字符串列表，设置为主窗口数据模型的表头标题。

> **注意**
> 这里在结束对话框操作后，并没有使用delete操作删除对话框对象，这样对话框就只是隐藏，它还在内存中。关闭对话框时不会出现析构函数里的消息提示对话框。

对话框创建时，传递主窗口的指针作为对话框的父对象，即：

```css
dlgSetHeaders = new QWDialogHeaders(this);
```

所以，主窗口释放时才会自动删除此对话框对象，也就是程序退出时才删除此对话框，才会出现QWDialogHeaders析构函数里的消息提示对话框。

