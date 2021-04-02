### 15.5.4　QCameraImageCapture抓取静态图片

QCameraImageCapture类对象imageCapture用于通过摄像头抓取静态图片，iniImageCapture()函数用于创建imageCapture并进行初始化设置，MainWindow构造函数调用此函数。IniImage　Capture()函数的代码如下：

```css
void MainWindow::iniImageCapture()
{//创建 QCameraImageCapture对象
   imageCapture = new QCameraImageCapture(curCamera,this);
   imageCapture->setBufferFormat(QVideoFrame::Format_Jpeg); //缓冲区格式
   imageCapture->setCaptureDestination(
                  QCameraImageCapture:: CaptureToFile);  //保存目标
   connect(imageCapture, SIGNAL(readyForCaptureChanged(bool)),
         this, SLOT(on_imageReadyForCapture(bool)));
   connect(imageCapture,SIGNAL(imageCaptured(int, const QImage &)),
         this,SLOT(on_imageCaptured(int, const QImage &)));
   connect(imageCapture,SIGNAL(imageSaved(int, const QString &)),
         this,SLOT(on_imageSaved(int, const QString &)));
}
```

创建QCameraImageCapture对象imageCapture时传递QCamera对象curCamera作为输入参数，建立与摄像头设备的关联。

setBufferFormat(QVideoFrame::Format_Jpeg)设置缓冲区里图片为JPG格式。

setCaptureDestination(QCameraImageCapture::CaptureToFile)设置抓图存储目标为文件，抓取的图片文件会自动保存到用户目录的“图片”文件夹里。

为imageCapture的3个信号关联了自定义槽函数，这3个槽函数的代码如下：

```css
void MainWindow::on_imageReadyForCapture(bool ready)
{ //可以抓图了
  ui->actCapture->setEnabled(ready);
}
void MainWindow::on_imageCaptured(int id, const QImage &preview)
{ //抓取图片后显示
   Q_UNUSED(id);
   QImage scaledImage = preview.scaled(ui->LabCapturedImage->size(),
               Qt::KeepAspectRatio,  Qt::SmoothTransformation);
   ui->LabCapturedImage->setPixmap(QPixmap::fromImage(scaledImage));
}
void MainWindow::on_imageSaved(int id, const QString &fileName)
{ //文件保存后显示保存的文件名
   Q_UNUSED(id);
   LabInfo->setText("图片保存为： "+fileName);
}
```

单击窗口工具栏上的“抓图”按钮可实现抓取静态图片功能，其代码如下：

```css
void MainWindow::on_actCapture_triggered()
{//抓图 按钮
   if (curCamera->captureMode()!=QCamera::CaptureStillImage)
      curCamera->setCaptureMode(QCamera::CaptureStillImage);
   imageCapture->capture();
}
```

这里首先将curCamera的抓取模式设置为QCamera::CaptureStillImage，然后使用QCameraImage Capture::capture()函数抓图。

