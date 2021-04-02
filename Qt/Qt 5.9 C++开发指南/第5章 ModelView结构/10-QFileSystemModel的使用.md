### 5.2.2　QFileSystemModel的使用

实例samp5_1的主窗口是基于QMainWindow的，在使用UI设计器做可视化设计时删除了工具栏和状态栏。主窗口界面布局采用了两个分割条的设计，ListView和TableView采用上下分割布局，然后和左边的TreeView采用水平分割布局，水平分割布局再和下方显示信息的groupBox在主窗口工作区水平布局。

在主窗口类中定义了一个QFileSystemModel类的成员变量model。

```css
QFileSystemModel   *model;
```

主窗口构造函数进行初始化，代码如下：

```css
MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent), ui(new Ui::MainWindow)
{
   ui->setupUi(this);
   model=new QFileSystemModel(this); 
   model->setRootPath(QDir::currentPath()); //设置根目录
   ui->treeView->setModel(model); //设置数据模型
   ui->listView->setModel(model); //设置数据模型
   ui->tableView->setModel(model); //设置数据模型
//信号与槽关联，treeView单击时，其目录设置为listView和tableView的根节点
   connect(ui->treeView,SIGNAL(clicked(QModelIndex)),
         ui->listView,SLOT(setRootIndex(QModelIndex)));
   connect(ui->treeView,SIGNAL(clicked(QModelIndex)),
         ui->tableView,SLOT(setRootIndex(QModelIndex)));
}
```

3个视图组件都使用setModel()函数，将QFileSystemModel数据模型model设置为自己的数据模型。

connect()函数设置信号与槽的关联，实现的功能是：在单击treeView的一个节点时，此节点就设置为listView和tableView的根节点，因为treeView的clicked(QModelIndex)信号会传递一个QModelIndex变量，是当前节点的模型索引，将此模型索引传递给listView和tableView的槽函数setRootIndex(QModelIndex)，listView和tableView就会显示此节点下的目录和文件。

在treeView上单击一个节点时，下方的一些标签里会显示节点的一些信息，这是为treeView的clicked(const QModelIndex &index)信号编写槽函数实现的，其代码如下：

```css
void MainWindow::on_treeView_clicked(const QModelIndex &index)
{
   ui->chkIsDir->setChecked(model->isDir(index)); //是否是目录
   ui->LabPath->setText(model->filePath(index));
   ui->LabType->setText(model->type(index));
   ui->LabFileName->setText(model->fileName(index));
   int sz=model->size(index)/1024;
   if (sz<1024)
      ui->LabFileSize->setText(QString("%1 KB").arg(sz));
   else
      ui->LabFileSize->setText(QString::asprintf("%.1f MB",sz/1024.0));
}
```

函数有一个传递参数QModelIndex &index，它是单击节点在数据模型中的索引。通过传递来的模型索引index，这段代码使用了QFileSystemModel的一些函数来获得节点的一些参数，包括以下几种。

+ bool isDir(QModelIndex &index)：判断节点是不是一个目录。
+ QString filePath(QModelIndex &index)：返回节点的目录名或带路径的文件名。
+ QString fileName(QModelIndex &index)：返回去除路径的文件夹名称或文件名。
+ QString type(QModelIndex &index)：返回描述节点类型的文字，如硬盘符是“Drive”，文件夹是“File Folder”，文件则用具体的后缀描述，如“txt File”“exe File”“pdf File”等。
+ qint64 size(QModelIndex &index)：如果节点是文件，返回文件大小的字节数：如果节点是文件夹，返回0。

而QFileSystemModel是如何获取磁盘目录文件结构的，3个视图组件是如何显示这些数据的，则是其底层实现的问题了。

