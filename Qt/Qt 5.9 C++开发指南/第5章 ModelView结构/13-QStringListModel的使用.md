### 5.3.2　QStringListModel的使用

#### 1．Model/View结构对象和组件初始化

实例samp5_2的窗口是从QWidget继承而来的类Widget，界面采用可视化设计。在Widget类中定义一个QStringListModel类的变量：

```css
QStringListModel   *theModel;
```

在Widget类的构造函数中进行变量的创建，完成数据模型与界面视图组件的关联，下面是Widget类构造函数的代码：

```css
Widget::Widget(QWidget *parent) :   QWidget(parent),   ui(new Ui::Widget)
{
   ui->setupUi(this);
   QStringList   theStrList; 
   theStrList<<"北京"<<"上海"<<"天津"<<"河北"<<"山东"<<"四川"<<"重庆";
   theModel=new QStringListModel(this);
   theModel->setStringList(theStrList); //导入theStrList的内容
   ui->listView->setModel(theModel); //设置数据模型
   ui->listView->setEditTriggers(QAbstractItemView::DoubleClicked |
              QAbstractItemView::SelectedClicked);
}
```

QStringListModel的setStringList()函数将一个字符串列表的内容作为数据模型的初始数据内容。

QListView的setModel()函数为界面视图组件设置一个数据模型。

程序运行后，界面上ListView组件里就会显示初始化的字符串列表的内容。

#### 2．编辑、添加、删除项的操作

+ 编辑项

QListView::setEditTriggers()函数设置QListView的条目是否可以编辑，以及如何进入编辑状态，函数的参数是QAbstractItemView::EditTrigger枚举类型值的组合。构造函数中设置为：

```css
ui->listView->setEditTriggers(QAbstractItemView::DoubleClicked | 
                  QAbstractItemView::SelectedClicked);
```

表示在双击，或选择并单击列表项后，就进入编辑状态。

若要设置为不可编辑，则可以设置为：

```css
ui->listView->setEditTriggers(QAbstractItemView:: NoEditTriggers);
```

+ 添加项

添加项是要在列表的最后添加一行，界面上“添加项”按钮的槽函数代码如下：

```css
void Widget::on_btnListAppend_clicked()
{ //添加一行
   theModel->insertRow(theModel->rowCount()); //在尾部插入一空行
   QModelIndex index=theModel->index(theModel->rowCount()-1,0);
   theModel->setData(index,"new item",Qt::DisplayRole);
   ui->listView->setCurrentIndex(index); //设置当前选中的行
}
```

对数据的操作都是针对数据模型的，所以，插入一行使用的是QStringListModel的insertRow (int row)函数，其中row是一个行号，表示在row行之前插入一行。要在列表的最后插入一行，参数row设置为列表当前的行数即可。

这样只是在列表尾部添加一个空行，没有任何文字。为了给添加的项设置一个缺省的文字标题，首先要获得新增项的模型索引，即：

```css
QModelIndex  index=theModel->index(theModel->rowCount()-1,0);
```

QStringListModel的index()函数根据传递的行号、列号、父项的模型索引生成一个模型索引，这行代码为新增的最后一个项生成一个模型索引index。

为新增的项设置一个文字标题“new item”，使用setData()函数，并用到前面生成的模型索引index。代码如下：

```css
theModel->setData(index,"new item",Qt::DisplayRole);
```

在使用setData()函数时，必须指定设置数据的角色，这里的角色是Qt::DisplayRole，它是用于显示的角色，即项的文字标题。

+ 插入项

“插入项”按钮的功能是在列表的当前行前面插入一行，其实现代码如下：

```css
void Widget::on_btnListInsert_clicked()
{//插入一行
   QModelIndex  index=ui->listView->currentIndex();
   theModel->insertRow(index.row());  
   theModel->setData(index,"inserted item",Qt::DisplayRole); 
   ui->listView->setCurrentIndex(index);
}
```

QListView::currentIndex()获得当前项的模型索引index，index.row()则返回这个模型索引的行号。

+ 删除当前项

使用QStringListModel的removeRow()函数删除某一行的代码如下：

```css
void Widget::on_btnListDelete_clicked()
{//删除当前行
   QModelIndex   index=ui->listView->currentIndex(); 
   theModel->removeRow(index.row());  
}
```

+ 删除列表

删除列表的所有项可使用QStringListModel的removeRows(int row, int count)函数，它表示从行号row开始删除count行。代码如下：

```css
void Widget::on_btnListClear_clicked()
{//清除所有项
   theModel->removeRows(0,theModel->rowCount());
}
```

#### 3．以文本显示数据模型的内容

以上在对界面上ListView的项进行编辑时，实际操作的都是其关联的数据模型theModel，在对数据模型进行插入、添加、删除项操作后，内容立即在ListView上显示出来，这是数据模型与视图组件之间信号与槽的作用，当数据模型的内容发生改变时，通知视图组件更新显示。

同样的，当在ListView上双击一行进入编辑状态，修改一个项的文字内容后，这部分内容也保存到数据模型里了，这就是图5-1所表示的过程。

那么，数据模型内部应该保存有最新的数据内容，对于QStringListModel模型来说，通过stringList()函数可以得到其最新的数据副本。界面上的“显示数据模型的StringList”按钮获取数据模型的stringList，并用多行文本的形式显示其内容，以检验对数据模型修改数据，特别是在界面上修改列表项的文字后，其内部的数据是否同步更新了。

以下是界面上的“显示数据模型的StringList”按钮的clicked()信号的槽函数代码，它通过数据模型的stringList()函数获取字符串列表，并在plainTextEdit里逐行显示：

```css
void Widget::on_btnTextImport_clicked()
{//显示数据模型的StringList
   QStringList  tmpList=theModel->stringList();
   ui->plainTextEdit->clear(); 
   for (int i=0; i<tmpList.count();i++)
      ui->plainTextEdit->appendPlainText(tmpList.at(i)); 
}
```

程序运行时，无论对ListView的列表做了什么编辑和修改，单击“显示数据模型的StringList”按钮，在文本框里显示的文字内容与ListView里总是完全相同的，说明数据模型的数据与界面上显示的内容是同步的。

#### 4．其他功能

QListView的clicked()信号会传递一个QModelIndex类型的参数，利用该参数，可以显示当前项的模型索引的行和列的信息，实现代码如下：

```css
void Widget::on_listView_clicked(const QModelIndex &index)
{ //显示QModelIndex的行、列号
   ui->LabInfo->setText(QString::asprintf("当前条目:row=%d, column=%d",
              index.row(),index.column()));
}
```

在这个实例中，通过QStringListModel和QListView说明了数据模型与视图组件之间构成Model/View结构的基本原理。

第4章的实例samp4_7中采用QListWidget设计了一个列表编辑器，对比这两个实例，可以发现如下两点。

+ 在Model/View结构中，数据模型与视图组件是分离的，可以直接操作数据模型以修改数据，在视图组件中做的修改也会自动保存到数据模型里。
+ 在使用QListWidget的例子中，每个列表项是一个QListWidgetItem类型的变量，保存了项的各种数据，数据和显示界面是一体的，对数据的修改操作就是对项关联的变量的修改。

所以，这是Model/View结构与便利组件之间的主要区别。

