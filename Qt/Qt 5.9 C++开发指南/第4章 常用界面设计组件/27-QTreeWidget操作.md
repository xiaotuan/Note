### 4.7.3　QTreeWidget操作

#### 1．本实例的目录树节点操作规则

本实例的目录树节点操作定义如下一些规则。

+ 将目录树的节点分为3种类型，顶层节点、分组节点和图片节点。
+ 窗口创建时初始化目录树，它只有一个顶层节点，这个顶层节点不能被删除，而且不允许再新建顶层节点。
+ 顶层节点下允许添加分组节点和图片节点。
+ 分组节点下可以添加分组节点和图片节点，分组节点的级数无限制。
+ 图片节点是终端节点，可以在图片节点同级再添加图片节点。
+ 每个节点创建时设置其类型信息，图片节点存储其完整文件名作为自定义数据。
+ 单击一个图片文件节点时，显示其关联文件的图片。

为便于后面说明代码的实现，将主窗口类MainWindow中增加的自定义内容先列出来，代码如下。这些枚举类型、变量和函数的功能在后面再具体介绍。

```css
class MainWindow : public QMainWindow
{
private:
//枚举类型treeItemType，创建节点时用作type参数，自定义类型必须大于1000
   enum   treeItemType{itTopItem=1001, itGroupItem, itImageItem};
   enum   treeColNum{colItem=0, colItemType=1}; //目录树列的编号
   QLabel  *LabFileName; //用于状态栏文件名显示
   QPixmap curPixmap;   //当前的图片
   float   pixRatio;    //当前图片缩放比例
   void   iniTree();//目录树初始化
   void   addFolderItem(QTreeWidgetItem *parItem, QString dirName);//添加目录
   QString  getFinalFolderName(const QString &fullPathName); //提取目录名称
   void   addImageItem(QTreeWidgetItem *parItem,QString aFilename);//添加图片
   void   displayImage(QTreeWidgetItem *item); //显示一个图片节点的图片
   void   changeItemCaption(QTreeWidgetItem *item); //遍历改变节点标题
};
```

#### 2．目录树初始化添加顶层节点

主窗口MainWindow的构造函数会调用自定义函数iniTree()，对目录树进行初始化，窗口构造函数和iniTree()代码如下：

```css
MainWindow::MainWindow(QWidget *parent) :   QMainWindow(parent),
   ui(new Ui::MainWindow)
{
   ui->setupUi(this);
   LabFileName=new QLabel("");
   ui->statusBar->addWidget(LabFileName);
   this->setCentralWidget(ui->scrollArea); 
   iniTree();//初始化目录树
}
void MainWindow::iniTree()
{ //初始化目录树
   QString   dataStr=""; // Item的Data 存储的string
   ui->treeFiles->clear();
   QIcon   icon;
   icon.addFile(":/images/icons/15.ico");  
   QTreeWidgetItem* item=new QTreeWidgetItem(MainWindow::itTopItem); 
   item->setIcon(MainWindow::colItem,icon); //第1列的图标
   item->setText(MainWindow::colItem,"图片文件"); //第1列的文字
   item->setText(MainWindow::colItemType,"type=itTopItem");  //第2列
   item->setFlags(Qt::ItemIsSelectable | Qt::ItemIsUserCheckable | Qt::ItemIsEnabled | Qt::ItemIsAutoTristate);
   item->setCheckState(colItem,Qt::Checked);
   item->setData(MainWindow::colItem,Qt::UserRole,QVariant(dataStr));
   ui->treeFiles->addTopLevelItem(item);//添加顶层节点
}
```

QTreeWidget的每个节点都是一个QTreeWidgetItem对象，添加一个节点前需先创建它，并做好相关设置。

创建节点的语句是：

```css
item=new QTreeWidgetItem(MainWindow::itTopItem);
```

传递了一个枚举常量MainWindow::itTopItem作为构造函数的参数，表示节点的类型。在构造函数里传递一个类型值之后，就可以用QTreeWidgetItem::type()返回这个节点的类型值。

itTopItem是在MainWindow里定义的枚举类型treeItemType的一个常量值。枚举类型treeItemType定义了节点的类型，自定义的节点类型值必须大于1000。

QTreeWidgetItem的setIcon()和setText()都需要传递一个列号作为参数，指定对哪个列进行设置。列号可以直接用数字，但是为了便于理解代码和统一修改，在MainWindow里定义了枚举类型treeColNum，colItem表示第1列，colItemType表示第2列。

setFlags()函数设置节点的一些属性标记，是Qt::ItemFlag枚举类型常量的组合。

setData()函数为节点的某一列设置一个角色数据，setData()函数原型为：

```css
void QTreeWidgetItem::setData(int column, int role, const QVariant &value)
```

其中，column是列号，role是角色的值，value是一个QVariant类型的数。

代码中设置节点数据的语句是：

```css
item->setData(MainWindow::colItem,Qt::UserRole,QVariant(dataStr)); 
```

它为节点的第1列，角色Qt::UserRole，设置了一个字符串数据dataStr。Qt::UserRole是枚举类型Qt::ItemDataRole中一个预定义的值，关于节点的角色和Qt::ItemDataRole在5.1节详细介绍。

创建并设置好节点后，用QTreeWidget:: addTopLevelItem()函数将节点作为顶层节点添加到目录树。

#### 3．添加目录节点

actAddFolder是用于添加组节点的Action，当目录树上的当前节点类型是itTopItem或itGroupItem类型时，才可以添加组节点。actAddFolder的triggered()信号的槽函数，以及相关自定义函数的代码如下：

```css
void MainWindow::on_actAddFolder_triggered()
{// 添加组节点
  QString dir=QFileDialog::getExistingDirectory();//选择目录
  if (!dir.isEmpty())
  {
     QTreeWidgetItem  *parItem=ui->treeFiles->currentItem(); //当前节点
     addFolderItem(parItem,dir);//在父节点下面添加一个组节点
  }
}
void MainWindow::addFolderItem(QTreeWidgetItem *parItem, QString dirName)
{//添加一个组节点
   QIcon   icon(":/images/icons/open3.bmp");
   QString  NodeText=getFinalFolderName(dirName); //获得最后的文件夹名称
   QTreeWidgetItem *item; 
   item=new QTreeWidgetItem(MainWindow::itGroupItem); //节点类型itGroupItem
   item->setIcon(colItem,icon); 
   item->setText(colItem,NodeText); 
   item->setText(colItemType,"type=itGroupItem"); 
   item->setFlags(Qt::ItemIsSelectable | Qt::ItemIsUserCheckable | Qt::ItemIsEnabled | Qt::ItemIsAutoTristate); 
   item->setCheckState(colItem,Qt::Checked); 
   item->setData(colItem,Qt::UserRole,QVariant(dirName)); 
   parItem->addChild(item); //在父节点下面添加子节点
}
QString MainWindow::getFinalFolderName(const QString &fullPathName)
{//从一个完整目录名称里，获得最后的文件夹名称
   int cnt=fullPathName.length();
   int i=fullPathName.lastIndexOf("/");
   QString str=fullPathName.right(cnt-i-1);
   return str;
}
```

actAddFolder的槽函数首先用文件对话框获取一个目录名称，再获取目录树的当前节点，然后调用自定义函数addFolderItem()添加一个组节点，新添加的节点将会作为当前节点的子节点。

addFolderItem()函数根据传递来的父节点parItem和目录全称dirName，创建并添加节点。首先用自定义函数getFinalFolderName()获取目录全称的最后一级的文件夹名称，这个文件夹名称将作为新建节点的标题；然后创建一个节点，创建时设置其节点类型为itGroupItem，表示分组节点，再设置属性和关联数据，关联数据就是目录的全路径字符串；最后调用QTreeWidgetItem:: addChild()函数，将创建的节点作为父节点的一个子节点添加到目录树。

#### 4．添加图片文件节点

actAddFiles是添加图片文件节点的Action，目录树的当前节点为任何类型时这个Action都可用。actAddFiles的槽函数，以及相关自定义函数的代码如下：

```css
void MainWindow::on_actAddFiles_triggered()
{//添加图片文件节点
QStringList files=QFileDialog::getOpenFileNames(this,
               "选择一个或多个文件","","Images(*.jpg)");
   if (files.isEmpty())
      return;
   QTreeWidgetItem *parItem,*item; 
   item=ui->treeFiles->currentItem(); 
   if (item->type()==itImageItem)  //当前节点是图片节点
      parItem=item->parent();
   else 
      parItem=item;
   for (int i = 0; i < files.size(); ++i)
   {
      QString aFilename=files.at(i); //得到一个文件名
      addImageItem(parItem,aFilename); //添加一个图片节点
   }
}
void MainWindow::addImageItem(QTreeWidgetItem *parItem, QString aFilename)
{//添加一个图片文件节点
   QIcon   icon(":/images/icons/31.ico"); 
   QString NodeText=getFinalFolderName(aFilename); //获得最后的文件名称
   QTreeWidgetItem *item; 
   item=new QTreeWidgetItem(MainWindow::itImageItem); //节点类型itImageItem
   item->setIcon(colItem,icon);
   item->setText(colItem,NodeText);
   item->setText(colItemType,"type=itImageItem");
   item->setFlags(Qt::ItemIsSelectable | Qt::ItemIsUserCheckable | Qt::ItemIsEnabled | Qt::ItemIsAutoTristate);
   item->setCheckState(colItem,Qt::Checked); 
   item->setData(colItem,Qt::UserRole,QVariant(aFilename));//完整文件名称
   parItem->addChild(item); //在父节点下面添加子节点
}
```

actAddFiles的槽函数首先用QFileDialog::getOpenFileNames()，获取图片文件列表，通过QTreeWidget:: currentItem()函数获得目录树的当前节点item。

item->type()将返回节点的类型，也就是创建节点时传递给构造函数的那个参数。如果当前节点类型是图片节点（itImageItem），就使用当前节点的父节点，作为将要添加的图片节点的父节点，否则就用当前节点作为父节点。

然后遍历所选图片文件列表，调用自定义函数addImageItem()逐一添加图片节点到父节点下。

addImageItem()根据图片文件名称，创建一个节点并添加到父节点下面，在使用setData()设置节点数据时，将图片带路径的文件名aFilename作为节点的数据，这个数据在单击节点打开图片时会用到。

#### 5．当前节点变化后的响应

目录树上当前节点变化时，会发射currentItemChanged()信号，为此信号创建槽函数，实现当前节点类型判断、几个Action的使能控制、显示图片等功能，代码如下：

```css
void MainWindow::on_treeFiles_currentItemChanged(QTreeWidgetItem *current, QTreeWidgetItem *previous)
{ //当前节点变化时的处理
   Q_UNUSED(previous);
   if  (current==NULL)
      return;
   int var=current->type();//节点的类型
   switch(var)
   {
      case  itTopItem: //顶层节点
        ui->actAddFolder->setEnabled(true);
        ui->actAddFiles->setEnabled(true);
        ui->actDeleteItem->setEnabled(false);  //顶层节点不能删除
        break;
      case  itGroupItem: //组节点
        ui->actAddFolder->setEnabled(true);
        ui->actAddFiles->setEnabled(true);
        ui->actDeleteItem->setEnabled(true);
        break;
      case  itImageItem: //图片文件节点
        ui->actAddFolder->setEnabled(false); //图片节点下不能添加目录节点
        ui->actAddFiles->setEnabled(true);
        ui->actDeleteItem->setEnabled(true);
        displayImage(current); //显示图片
        break;
   }
}
```

current是变化后的当前节点，通过current->type()获得当前节点的类型，根据节点类型控制界面上3个Action的使能状态。如果是图片文件节点，还调用displayImage ()函数显示节点关联的图片。

displayImage()函数的功能实现在后面介绍QLabel图片显示的部分会详细说明。

#### 6．删除节点

除了顶层节点之外，选中一个节点后也可以删除它。actDeleteItem实现节点删除，其代码如下：

```css
void MainWindow::on_actDeleteItem_triggered()
{//删除节点
   QTreeWidgetItem* item =ui->treeFiles->currentItem(); //当前节点
   QTreeWidgetItem* parItem=item->parent(); //父节点
   parItem->removeChild(item);//移除一个子节点，并不会删除
   delete item;
}
```

一个节点不能移除自己，所以需要获取其父节点，使用父节点的removeChild()函数来移除自己。removeChild()移除一个节点，但是不从内存中删除它，所以还需调用delete。

若要删除顶层节点，则使用QTreeWidget:: takeTopLevelItem(int index)函数。

#### 7．节点的遍历

目录树的节点都是QTreeWidgetItem类，可以嵌套多层。有时需要在目录树中遍历所有节点，比如按条件查找某些节点、统一修改节点的标题等。遍历节点需要用到QTreeWidgetItem类的一些关键函数，还需要设计嵌套函数。

actScanItems实现工具栏上“遍历节点”的功能，其槽函数及相关自定义函数代码如下：

```css
void MainWindow::on_actScanItems_triggered()
{//遍历节点
   for (int i=0;i<ui->treeFiles->topLevelItemCount();i++)
   {
      QTreeWidgetItem *item=ui->treeFiles->topLevelItem(i); //顶层节点
      changeItemCaption(item); //更改节点标题
   }
}
void MainWindow::changeItemCaption(QTreeWidgetItem *item)
{ //改变节点的标题文字
   QString str="*"+ item->text(colItem);  //节点标题前加“*”
   item->setText(colItem,str); 
   if (item->childCount()>0) 
   for (int i=0;i< item->childCount();i++) //遍历子节点
      changeItemCaption(item->child(i));  //调用自己，可重入的函数
}
```

QTreeWidget组件的顶层节点没有父节点，要访问所有顶层节点，用到两个函数。

+ int topLevelItemCount()：返回顶层节点个数。
+ QTreeWidgetItem* topLevelItem(int index)：返回序号为index的顶层节点。

on_actScanItems_triggered()函数的for循环访问所有顶层节点，获取一个顶层节点item之后，调用changeItemCaption(item)改变这个节点及其所有子节点的标题。

changeItemCaption(QTreeWidgetItem *item)是一个嵌套调用函数，即在这个函数里还会调用它自己。它的前两行更改传递来的节点item的标题，即在标题前加星号。后面的代码根据item->childCount()是否大于0，判断这个节点是否有子节点，如果有子节点，则在后面的for循环里，逐一获取，并作为参数调用changeItemCaption()函数。

