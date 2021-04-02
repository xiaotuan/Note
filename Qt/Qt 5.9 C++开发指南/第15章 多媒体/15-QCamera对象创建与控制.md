### 15.5.3　QCamera对象创建与控制

iniCamera()函数进行QCamera对象的创建与初始化，在MainWindow的构造函数里调用，下面是iniCamera()函数的代码：

```css
void MainWindow::iniCamera()
{//  创建 QCamera对象
   QCameraInfo curCameraInfo=QCameraInfo::defaultCamera(); //获取缺省摄像头
   ui->comboCamera->addItem(curCameraInfo.description());  
   ui->comboCamera->setCurrentIndex(0);
   curCamera=new QCamera(curCameraInfo, this); //创建摄像头对象
   QCameraViewfinderSettings viewfinderSettings;
   viewfinderSettings.setResolution(640, 480);
   viewfinderSettings.setMinimumFrameRate(15.0);
   viewfinderSettings.setMaximumFrameRate(30.0);
   curCamera->setViewfinderSettings(viewfinderSettings);
   curCamera->setViewfinder(ui->viewFinder); //设置预览框
   curCamera->setCaptureMode(QCamera::CaptureViewfinder); 
//判断摄像头是否支持抓图、录制视频
   ui->checkStillImage->setChecked(   
    curCamera->isCaptureModeSupported(QCamera::CaptureStillImage)); //抓图
   ui->checkVideo->setChecked(
    curCamera->isCaptureModeSupported(QCamera::CaptureVideo));//视频录制
   connect(curCamera,SIGNAL(stateChanged(QCamera::State)),
         this,SLOT(on_cameraStateChanged(QCamera::State)));
//Windows平台上不支持captureModeChanged()信号
   connect(curCamera,SIGNAL(captureModeChanged(QCamera::CaptureModes)),
     this,SLOT(on_cameraCaptureModeChanged(QCamera::CaptureModes)));
}
```

这里用QCameraInfo::defaultCamera()获取缺省的摄像头设备，然后用于创建QCamera对象实例curCamera。

QCamera::setViewfinder()函数用于设置取景框预览组件。

QCamera::setCaptureMode()函数设置摄像头的抓取模式。

然后查询curCamera是否支持抓图、支持录像，并更新界面上的复选框的状态。

为curCamera的两个信号分别设置了关联的槽函数。stateChanged()在摄像头状态变化时发射，captureModeChanged()则在摄像头抓取模式变化时发射，不过在Windows平台上不会发射captureModeChanged()信号。这两个槽函数的代码如下：

```css
void MainWindow::on_cameraStateChanged(QCamera::State state)
{
  switch (state)
  {
   case QCamera::UnloadedState:
     LabCameraState->setText("摄像头state: UnloadedState");   break;
   case QCamera::LoadedState:
     LabCameraState->setText("摄像头state: LoadedState");     break;
   case QCamera::ActiveState:
     LabCameraState->setText("摄像头state: ActiveState");
  }
  ui->actStartCamera->setEnabled(state!=QCamera::ActiveState);
  ui->actStopCamera->setEnabled(state==QCamera::ActiveState);
}
void MainWindow::on_cameraCaptureModeChanged(QCamera::CaptureModes mode)
{
   if (mode==QCamera::CaptureStillImage)
      LabCameraMode->setText("抓取模式: StillImage");
   else if (mode==QCamera::CaptureVideo)
      LabCameraMode->setText("抓取模式: Video");
   else
      LabCameraMode->setText("抓取模式: Viewfinder");
}
```

窗口工具栏上的“开启摄像头”和“关闭摄像头”两个按钮控制摄像头的开启和关闭，其关联Action的槽函数代码如下：

```css
void MainWindow::on_actStartCamera_triggered()
{//开启摄像头
   curCamera->start();
}
void MainWindow::on_actStopCamera_triggered()
{//关闭摄像头
   curCamera->stop();
}
```

开启和关闭摄像头时，QCamera对象会发射stateChanged()信号。开启摄像头之后，摄像头状态为QCamera::ActiveState，关闭之后状态会变成QCamera::LoadedState。

