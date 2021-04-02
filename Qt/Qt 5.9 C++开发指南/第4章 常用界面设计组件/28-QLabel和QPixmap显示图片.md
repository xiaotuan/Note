### 4.7.4　QLabel和QPixmap显示图片

#### 1．显示节点关联的图片

在目录树上单击一个节点后，如果其类型为图片节点（itImageItem），就会调用displayImage (QTreeWidgetItem *item)函数显示节点的图片，当前节点作为函数的传递参数。displayImage()函数的代码如下：

```css
void MainWindow::displayImage(QTreeWidgetItem *item)
{//显示图片,节点item存储了图片文件名
   QString filename=item->data(colItem,Qt::UserRole).toString();//文件名
   LabFileName->setText(filename); 
   curPixmap.load(filename); 
   on_actZoomFitH_triggered(); //自动适应高度显示
}
```

QTreeWidgetItem::data()返回节点存储的数据，也就是用setData()设置的数据。前面在添加图片节点时，将文件名的带路径全名存储为节点的数据，这里的第一行语句就可以获得节点存储的图片文件全名。

curPixmap是在MainWindow 中定义的一个QPixmap类型的变量，用于操作图片。QPixmap::　load(QString &fileName)直接将一个图片文件载入。

最后调用函数on_actZoomFitH_triggered()显示图片，这是actZoomFitH的槽函数，以适应高度的形式显示图片。

#### 2．图片缩放与显示

有几个Action实现图片的缩放显示，包括适合宽度、适合高度、放大、缩小、实际大小，部分槽函数代码如下：

```css
void MainWindow::on_actZoomFitH_triggered()
{//适应高度显示图片
   int H=ui->scrollArea->height();
   int realH=curPixmap.height(); 
   pixRatio=float(H)/realH;  //当前显示比例，必须转换为浮点数
   QPixmap pix=curPixmap.scaledToHeight(H-30); //图片缩放到指定高度
   ui->LabPicture->setPixmap(pix); 
}
void MainWindow::on_actZoomIn_triggered()
{//放大显示
   pixRatio=pixRatio*1.2;
   int w=pixRatio*curPixmap.width();
   int h=pixRatio*curPixmap.height();
   QPixmap pix=curPixmap.scaled(w,h);
   ui->LabPicture->setPixmap(pix);
}
void MainWindow::on_actZoomRealSize_triggered()
{ //实际大小显示
   pixRatio=1; 
   ui->LabPicture->setPixmap(curPixmap);
}
```

QPixmap存储图片数据，可以缩放图片，有以下几个函数。

+ QPixmap scaledToHeight(int height)：返回一个缩放后的图片的副本，图片缩放到一个高度height。
+ QPixmap scaledToWidth(int width)：返回一个缩放后的图片的副本，图片缩放到一个宽度width。
+ QPixmap scaled(int width, int height)：返回一个缩放后的图片的副本，图片缩放到宽度width和高度height，缺省为不保持比例。

变量curPixmap保存了图片的原始副本，要缩放只需调用curPixmap的相应函数，返回缩放后的图片副本。

在界面上的一个标签LabPicture上显示图片，使用了QLabel的setPixmap(const QPixmap &)函数。

