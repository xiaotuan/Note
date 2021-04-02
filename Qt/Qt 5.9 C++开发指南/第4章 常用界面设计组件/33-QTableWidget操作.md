### 4.8.3　QTableWidget操作

#### 1．设置表头

界面上的“设置表头”按钮实现对表头的设置，其clicked()信号的槽函数代码如下：

```css
void MainWindow::on_btnSetHeader_clicked()
{ //设置表头
   QTableWidgetItem  *headerItem;
   QStringList  headerText;
   headerText<<"姓 名"<<"性 别"<<"出生日期"<<"民 族"<<"分数"<<"是否党员"; 
//   ui->tableInfo->setHorizontalHeaderLabels(headerText);
   ui->tableInfo->setColumnCount(headerText.count());
   for (int i=0;i<ui->tableInfo->columnCount();i++) 
   {
     headerItem=new  QTableWidgetItem(headerText.at(i));
     QFont font=headerItem->font();
     font.setBold(true);//设置为粗体
     font.setPointSize(12);//字体大小
     headerItem->setTextColor(Qt::red);//字体颜色
     headerItem->setFont(font);//设置字体
     ui->tableInfo->setHorizontalHeaderItem(i,headerItem); 
   }
}
```

行表头各列的文字标题由一个QStringList对象headerText初始化存储，如果只是设置行表头各列的标题，使用下面一行语句即可：

```css
ui->tableInfo->setHorizontalHeaderLabels(headerText);
```

如果需要进行更加具体的格式设置，需要为行表头的每个单元格创建一个QTableWidgetItem类型的变量，并进行相应设置。

在一个表格中，不管是表头还是工作区，每个单元格都是一个QTableWidgetItem对象。QTableWidgetItem对象存储了单元格的所有内容，包括字标题、格式设置，以及关联的数据。

上面程序中的for循环遍历headerText的每一行，用每一行的文字创建一个QTableWidgetItem对象headerItem，然后设置headerItem的字体大小为12、粗体、红色，然后将headerItem赋给表头的某一列：

```css
ui->tableInfo->setHorizontalHeaderItem(i,headerItem);
```

#### 2．初始化表格数据

界面上的“初始化表格数据”按钮根据表格的行数，生成数据填充表格，并为每个单元格生成QTableWidgetItem对象，设置相应属性。下面是btnIniData的clicked()信号的槽函数代码：

```css
void MainWindow::on_btnIniData_clicked()
{ //初始化表格内容
   QString strName,strSex;
   bool   isParty=false;
   QDate   birth;
   birth.setDate(1980,4,7);//初始化一个日期
   ui->tableInfo->clearContents();//只清除工作区，不清除表头
   int Rows=ui->tableInfo->rowCount(); //数据区行数
   for (int i=0;i<Rows;i++)
   {
      strName=QString::asprintf("学生%d",i); 
      if ((i % 2)==0) //分奇数、偶数行设置性别，及其图标
         strSex="男";
      else
         strSex="女";
      createItemsARow(i, strName, strSex, birth,"汉族",isParty,70);
      birth=birth.addDays(20); //日期加20天
      isParty =!isParty;
   }
}
```

QTableWidget::clearContents()函数清除表格数据区的所有内容，但是不清除表头。

QTableWidget ::rowCount()函数返回表格数据区的行数。

在for循环里为每一行生成需要显示的数据，然后调用自定义函数createItemsARow()，为表格一行的各个单元格生成QTableWidgetItem对象。

createItemsARow()是在窗体类里自定义的函数，其实现代码如下：

```css
void MainWindow::createItemsARow(int rowNo,QString Name,QString Sex,QDate birth,QString Nation,bool isPM,int score)
{ //为一行的单元格创建 Items
   QTableWidgetItem   *item;
   QString str;
   uint StudID=201605000; //学号基数
//姓名
   item=new  QTableWidgetItem(Name,MainWindow::ctName);
   item->setTextAlignment(Qt::AlignHCenter | Qt::AlignVCenter); 
   StudID  +=rowNo; //学号=基数+ 行号
   item->setData(Qt::UserRole,QVariant(StudID));  //设置studID为data
   ui->tableInfo->setItem(rowNo,MainWindow::colName,item);
//性别
   QIcon   icon;
   if (Sex=="男")
      icon.addFile(":/images/icons/boy.ico");
   else
      icon.addFile(":/images/icons/girl.ico");
   item=new  QTableWidgetItem(Sex,MainWindow::ctSex); 
   item->setIcon(icon);
   item->setTextAlignment(Qt::AlignHCenter | Qt::AlignVCenter);
   ui->tableInfo->setItem(rowNo,MainWindow::colSex,item);
//出生日期
   str=birth.toString("yyyy-MM-dd"); //日期转换为字符串
   item=new  QTableWidgetItem(str,MainWindow::ctBirth);
   item->setTextAlignment(Qt::AlignLeft | Qt::AlignVCenter); 
   ui->tableInfo->setItem(rowNo,MainWindow::colBirth,item);
//民族
   item=new  QTableWidgetItem(Nation,MainWindow::ctNation);
   item->setTextAlignment(Qt::AlignHCenter | Qt::AlignVCenter); 
   ui->tableInfo->setItem(rowNo,MainWindow::colNation,item);
//是否党员
   item=new  QTableWidgetItem("党员",MainWindow::ctPartyM);
   item->setTextAlignment(Qt::AlignHCenter | Qt::AlignVCenter);
   if (isPM)
      item->setCheckState(Qt::Checked);
   else
      item->setCheckState(Qt::Unchecked);
   item->setBackgroundColor(Qt::yellow);
   ui->tableInfo->setItem(rowNo,MainWindow::colPartyM,item);
//分数
   str.setNum(score);
   item=new  QTableWidgetItem(str,MainWindow::ctScore);
   item->setTextAlignment(Qt::AlignHCenter | Qt::AlignVCenter);
   ui->tableInfo->setItem(rowNo,MainWindow::colScore,item);
}
```

该表格的每一行有6列，为每一个单元格都创建一个QTableWidgetItem类型的变量item，并做相应的设置。

创建QTableWidgetItem使用的构造函数的原型为：

```css
QTableWidgetItem::QTableWidgetItem(const QString &text, int type = Type)
```

其中，第一个参数作为单元格的显示文字，第二个参数作为节点的类型。

例如创建“姓名”单元格对象时的语句是：

```css
cellItem=new  QtableWidgetItem(Name,MainWindow::ctName);
```

其中，MainWindow::ctName是定义的枚举类型CellType的一个常量值。

“姓名”单元格还调用setData()函数设置了一个自定义的数据，存储的是学生ID。

```css
cellItem->setData(Qt::UserRole,QVariant(StudID));
```

这个自定义数据是不显示在界面上的，但是与单元格相关联。

QTableWidgetItem有一些函数对单元格进行属性设置，如下。

+ setTextAlignment (int alignment)：设置文字对齐方式。
+ setBackground(const QBrush &brush)：设置单元格背景颜色。
+ setForeground(const QBrush &brush)：设置单元格前景色。
+ setIcon(const QIcon &icon)：为单元格设置一个显示图标。
+ setFont(const QFont &font)：为单元格显示文字设置字体。
+ setCheckState(Qt::CheckState state)：设置单元格勾选状态，单元格里出现一个QCheckBox组件。
+ setFlags(Qt::ItemFlags flags)：设置单元格的一些属性标记。

设置好item的各种属性之后，用QTableWidget的setItem函数将item设置为单元格的项，例如：

```css
ui->tableInfo->setItem(rowNo,MainWindow::colName,item);
```

其中，MainWindow::colName是定义的枚举类型FieldColNum的一个常量值。

这样初始化设置后，就可以得到如图4-18所示的运行时的表格内容。表格里并没有显示学号，学号是“姓名”单元格的关联数据。

#### 3．获得当前单元格数据

当鼠标在表格上单击单元格时，被选中的单元格是当前单元格。通过QTableWidget的currentColumn()和currentRow()可以获得当前单元格的列编号和行编号。

当前单元格发生切换时，会发射currentCellChanged()信号和currentItemChanged()信号，两个信号都可以利用，只是传递的参数不同。

对currentCellChanged()信号编写槽函数，用于获取当前单元格的数据，以及当前行的学生的学号信息，代码如下：

```css
void MainWindow::on_tableInfo_currentCellChanged(int currentRow, int currentColumn, int previousRow, int previousColumn)
{//当前选择单元格发生变化时的响应
   QTableWidgetItem* item=ui->tableInfo->item(currentRow,currentColumn); 
   if  (item==NULL) 
      return;
   labCellIndex->setText(QString::asprintf("当前单元格坐标：%d 行，%d 列", 
              currentRow,currentColumn));
   int cellType=item->type();//获取单元格的类型
   labCellType->setText(QString::asprintf("当前单元格类型：%d",cellType));
   item=ui->tableInfo->item(currentRow,MainWindow::colName); //第1列的item
   int ID=item->data(Qt::UserRole).toInt();//读取用户自定义数据
   labStudID->setText(QString::asprintf("学生ID：%d",ID));//学生ID
}
```

在currentCellChanged()信号中，传递的参数currentRow和currentColumn表示当前单元格的行号和列号，通过这两个编号可以得到单元格的QTableWidgetItem对象item。

获得item之后，通过type()函数得到单元格的类型参数，这个类型就是为单元格创建QTableWidgetItem对象时传递的类型参数。

再获取同一行的“姓名”单元格的项，用data()函数提取自定义数据，也就是创建单元格时存储的学生ID。

#### 4．插入、添加、删除行

QTableWidget处理行操作的函数如下。

+ insertRow(int row)：在行号为row的行前面插入一行，如果row等于或大于总行数，则在表格最后添加一行。insertRow()函数只是插入一个空行，不会为单元格创建QTableWidgetItem对象，需要手工为单元格创建。
+ removeRow(int row)：删除行号为row的行。

下面是界面上“插入行”“添加行”“删除当前行”按钮的响应代码。在插入行之后，会调用createItemsARow()函数，为新创建的空行的各单元格构造QTableWidgetItem对象。

```css
void MainWindow::on_btnInsertRow_clicked()
{ //插入一行
   int curRow=ui->tableInfo->currentRow();
   ui->tableInfo->insertRow(curRow); //插入一行，不会自动为单元格创建item
   createItemsARow(curRow, "新学生", "男",
        QDate::fromString("1990-1-1","yyyy-M-d"),"苗族",true ); 
}
void MainWindow::on_btnAppendRow_clicked()
{ //添加一行
   int curRow=ui->tableInfo->rowCount();
   ui->tableInfo->insertRow(curRow);//在表格尾部添加一行
   createItemsARow(curRow, "新生", "女",
        QDate::fromString("2000-1-1","yyyy-M-d"),"满族",false ); 
}
void MainWindow::on_btnDelCurRow_clicked()
{//删除当前行及其items
   int  curRow=ui->tableInfo->currentRow();
   ui->tableInfo->removeRow(curRow); //删除当前行及其items
}
```

#### 5．自动调整行高和列宽

QTableWidget有几个函数自动调整表格的行高和列宽，分别如下。

+ resizeColumnsToContents()：自动调整所有列的宽度，以适应其内容。
+ resizeColumnToContents(int column)：自动调整列号为column的列的宽度。
+ resizeRowsToContents()：自动调整所有行的高度，以适应其内容。
+ resizeRowToContents(int row)：自动调整行号为row的行的高度。

这几个函数实际上是QTableWidget的父类QTableView的函数。

#### 6．其他属性控制

+ 设置表格内容是否可编辑

QTableWidget的EditTriggers属性表示是否可编辑，以及进入编辑状态的方式。界面上的“表格可编辑”复选框的槽函数代码为：

```css
void MainWindow::on_chkBoxTabEditable_clicked(bool checked)
{ //设置编辑模式
   if (checked)
      ui->tableInfo->setEditTriggers(QAbstractItemView::DoubleClicked | QAbstractItemView::SelectedClicked); //双击或获取焦点后单击，进入编辑状态
   else
      ui->tableInfo->setEditTriggers(QAbstractItemView::NoEditTriggers); 
}
```

+ 设置行表头、列表头是否显示

horizontalHeader()获取行表头，verticalHeader()获取列表头，然后可设置其可见性。

```css
void MainWindow::on_chkBoxHeaderH_clicked(bool checked)
{//是否显示行表头
   ui->tableInfo->horizontalHeader()->setVisible(checked);
}
void MainWindow::on_chkBoxHeaderV_clicked(bool checked)
{//是否显示列表头
   ui->tableInfo->verticalHeader()->setVisible(checked);
}
```

+ 间隔行底色

setAlternatingRowColors()函数可以设置表格的行是否用交替底色显示，若为交替底色，则间隔的一行会用灰色作为底色。具体底色的设置需要用styleSheet，在16.2节有介绍。

```css
void MainWindow::on_chkBoxRowColor_clicked(bool checked)
{ 
   ui->tableInfo->setAlternatingRowColors(checked);
}
```

+ 选择模式

setSelectionBehavior()函数可以设置选择方式为单元格选择，还是行选择。

```css
void MainWindow::on_rBtnSelectItem_clicked()
{//选择行为：单元格选择
   ui->tableInfo->setSelectionBehavior(QAbstractItemView::SelectItems);
}
void MainWindow::on_rBtnSelectRow_clicked()
{//选择行为：行选择
   ui->tableInfo->setSelectionBehavior(QAbstractItemView::SelectRows);
}
```

#### 7．遍历表格读取数据

“读取表格内容到文本”按钮演示了将表格数据区的内容全部读出的方法，它将每个单元格的文字读出，同一行的单元格的文字用空格分隔开，作为文本的一行，然后将这行文字作为文本编辑器的一行内容，代码如下：

```css
void MainWindow::on_btnReadToEdit_clicked()
{//将所有单元格的内容提取字符串，显示在PlainTextEdit组件里
   QString  str;
   QtableWidgetItem  *cellItem;
   ui->textEdit->clear();
   for (int i=0;i<ui->tableInfo->rowCount();i++) 
   {
     str=QString::asprintf("第 %d 行： ",i+1);
     for (int j=0;j<ui->tableInfo->columnCount()-1;j++) 
     {
         cellItem=ui->tableInfo->item(i,j); //获取单元格的item
         str=str+cellItem->text()+"   "; //字符串连接
      }
     cellItem=ui->tableInfo->item(i,colNoPartyM);  //最后一列
     if (cellItem->checkState()==Qt::Checked) 
        str=str+"党员";
     else
        str=str+"群众";
     ui->textEdit->appendPlainText(str); 
   }
}
```



