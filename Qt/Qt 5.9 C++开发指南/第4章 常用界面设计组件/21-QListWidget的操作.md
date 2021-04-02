### 4.6.3　QListWidget的操作

#### 1．初始化列表

actListIni实现listWidget的列表项初始化，其trigger()信号槽函数代码如下：

```css
void MainWindow::on_actListIni_triggered()
{ //初始化列表
   QListWidgetItem *aItem; //每一行是一个QListWidgetItem
   QIcon aIcon;
   aIcon.addFile(":/images/icons/check2.ico"); 
   bool chk=ui->chkBoxListEditable->isChecked();//是否可编辑
   ui->listWidget->clear();
   for (int i=0; i<10; i++)
   {
      QString str=QString::asprintf("Item %d",i);
      aItem=new QListWidgetItem();
      aItem->setText(str);   //设置文字标签
      aItem->setIcon(aIcon);  //设置图标
      aItem->setCheckState(Qt::Checked);   //设置为选中状态
      if (chk) //可编辑, 设置flags
         aItem->setFlags(Qt::ItemIsSelectable | Qt::ItemIsEditable 
|Qt::ItemIsUserCheckable |Qt::ItemIsEnabled);
      else//不可编辑, 设置flags
         aItem->setFlags(Qt::ItemIsSelectable |Qt::ItemIsUserCheckable 
|Qt::ItemIsEnabled);
      ui->listWidget->addItem(aItem); //增加一个项
   }
}
```

列表框里一行是一个项，是一个QListWidgetItem类型的对象，向列表框添加一个项，就需要创建一个QListWidgetItem类型的实例aItem，然后设置aItem的一些属性，再用QListWidget::　AddItem()函数将该aItem添加到列表框里。

QListWidgetItem有许多函数方法，可以设置项的很多属性，如设置文字、图标、选中状态，还可以设置flags，就是图4-10对话框里设置功能的代码化。

#### 2．插入项

插入项使用QListWidget的insertItem(int row, QListWidgetItem *item)函数，在某一行row的前面插入一个QListWidgetItem对象item，也需要先创建这个item，并设置好其属性。actListInsert实现这个功能，其槽函数代码如下：

```css
void MainWindow::on_actListInsert_triggered()
{  //插入一个项
   QIcon aIcon;
   aIcon.addFile(":/images/icons/check2.ico"); 
   bool chk=ui->chkBoxListEditable->isChecked();  
   QListWidgetItem* aItem=new QListWidgetItem("New Inserted Item"); 
   aItem->setIcon(aIcon); 
   aItem->setCheckState(Qt::Checked); 
   if (chk) 
      aItem->setFlags(Qt::ItemIsSelectable | Qt::ItemIsEditable 
|Qt::ItemIsUserCheckable |Qt::ItemIsEnabled);
   else
      aItem->setFlags(Qt::ItemIsSelectable |Qt::ItemIsUserCheckable 
|Qt::ItemIsEnabled);
   ui->listWidget->insertItem(ui->listWidget->currentRow(),aItem);
}
```

这里设置新插入的项是可选择的、能用的、可复选的。还根据界面设置，确定项是否可编辑。

#### 3．删除当前项和清空列表

删除当前项的actListDelete的槽函数代码如下：

```css
void MainWindow::on_actListDelete_triggered()
{ //删除当前项
   int row=ui->listWidget->currentRow();
   QListWidgetItem* aItem=ui->listWidget->takeItem(row); 
   delete aItem; //手工删除对象
}
```

takeItem()函数只是移除一个项，并不删除项对象，所以还需要用delete从内存中删除它。

要清空列表框的所有项，只需调用QListWidget::clear()函数即可。

#### 4．遍历并选择项

界面上有“全选”“全不选”“反选”3个按钮，由3个Action实现，用于遍历列表框里的项，设置选择状态。用于“全选”的actSelALL的槽函数代码如下：

```css
void MainWindow::on_actSelALL_triggered()
{ //全选
   int cnt=ui->listWidget->count();//个数
   for (int i=0; i<cnt; i++)
   {
      QListWidgetItem *aItem=ui->listWidget->item(i);//获取一个项
      aItem->setCheckState(Qt::Checked);//设置为选中
   }
}
```

函数QListWidgetItem::setCheckState(Qt::CheckState state)设置列表项的复选状态，枚举类型Qt::CheckState有3种取值。

+ Qt::Unchecked，不被选中。
+ Qt::PartiallyChecked，部分选中。在目录树中的节点可能出现这种状态，比如其子节点没有全部被勾选时。
+ Qt::Checked，被选中。

#### 5．QListWidget的常用信号

QListWidget在当前项切换时发射两个信号，只是传递的参数不同。

+ currentRowChanged(int currentRow)：传递当前项的行号作为参数。
+ currentItemChanged(QListWidgetItem current, QListWidgetItem previous)：传递两个QList WidgetItem对象作为参数，current表示当前项，previous是前一项。

当前项的内容发生变化时发射信号currentTextChanged(const QString &currentText)。

为listWidget的currentItemChanged()信号编写槽函数，代码如下：

```css
void MainWindow::on_listWidget_currentItemChanged(QListWidgetItem *current, QListWidgetItem *previous)
{ //listWidget当前选中项发生变化
  QString str;
  if (current != NULL) 
  {
   if (previous==NULL) 
     str="当前项："+current->text();
   else
     str="前一项："+previous->text()+"; 当前项："+current->text();
   ui->editCutItemText->setText(str);
  }
}
```

响应代码里需要判断current和previous指针是否为空，否则使用对象时可能出现访问错误。

