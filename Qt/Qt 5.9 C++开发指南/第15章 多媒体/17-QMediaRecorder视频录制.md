### 15.5.5　QMediaRecorder视频录制

QMediaRecorder类对象mediaRecorder用于通过摄像头进行视频录制，iniVideoRecorder()函数创建mediaRecorder并进行初始化设置，MainWindow构造函数调用此函数。iniVideoRecorder()函数代码如下：

```css
void MainWindow::iniVideoRecorder()
{//创建QMediaRecorder对象
   mediaRecorder = new QMediaRecorder(curCamera,this);
   ui->chkMute->setChecked(mediaRecorder->isMuted());
   connect(mediaRecorder, SIGNAL(stateChanged(QMediaRecorder::State)),
         this, SLOT(on_videoStateChanged(QMediaRecorder::State)));
   connect(mediaRecorder, SIGNAL(durationChanged(qint64)),
         this, SLOT(on_videoDurationChanged(qint64)));
}
```

mediaRecorder创建时传递QCamera对象curCamera作为输入参数。

为mediaRecorder的两个信号设置了关联槽函数，两个槽函数的代码如下：

```css
void MainWindow::on_video_stateChanged(QMediaRecorder::State state)
{//状态变化
   ui->actVideoRecord->setEnabled(state!=QMediaRecorder::RecordingState);
   ui->actVideoStop->setEnabled(state==QMediaRecorder::RecordingState);
}
void MainWindow::on_video_durationChanged(qint64 duration)
{
   ui->LabDuration->setText(QString("录制时间:%1 秒").arg(duration/1000));
}
```

on_videoStateChanged()函数会根据当前状态控制界面按钮的使能状态，on_videoDuration Changed()函数用于录制视频时显示已录制的持续时间。

开始录像之前，需要单击“视频保存文件”按钮设置一个视频录制保存的文件。“开始录像”和“停止录像”两个按钮的代码如下：

```css
void MainWindow::on_actVideoRecord_triggered()
{//开始录像
   if (!mediaRecorder->isAvailable())
   {
      QMessageBox::critical(this,"错误",
            "不支持视频录制！\n mediaRecorder->isAvailable()==false");
      return;
   }
   if (curCamera->captureMode()!=QCamera::CaptureVideo)
      curCamera->setCaptureMode(QCamera::CaptureVideo);
   QString selectedFile=ui->editOutputFile->text().trimmed();
   if (selectedFile.isEmpty())
   {   QMessageBox::critical(this,"错误","请先设置录音输出文件");
      return;
   }
   if (QFile::exists(selectedFile))
    if (!QFile::remove(selectedFile))
    {  QMessageBox::critical(this,"错误","所设置录音输出文件被占用，无法删除");
      return;
    }
   mediaRecorder->setOutputLocation(QUrl::fromLocalFile(selectedFile));
   mediaRecorder->record();
}
void MainWindow::on_actVideoStop_triggered()
{//停止录像
   mediaRecorder->stop();
}
```

开始录像之前，还需要将摄像头的抓取状态设置为QCamera::CaptureVideo，然后检查设置的视频输出文件，当文件没问题后用setOutputLocation()函数设置视频录制输出文件。

调用QMediaRecorder的record()函数开始录像，stop()函数停止录像。



