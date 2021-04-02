### 14.2.3　TCP客户端程序设计

#### 1．主窗口定义与构造函数

客户端程序TCPClient只需要使用一个QTcpSocket对象，就可以和服务器端程序TCPServer进行通信。

TCPClient也是一个窗口基于QMainWindow的应用程序，其主窗口的定义如下：

```css
class MainWindow : public QMainWindow
{
   Q_OBJECT
private:
   QTcpSocket  *tcpClient;  //socket
   QLabel  *LabSocketState;  //状态栏显示标签
   QString getLocalIP();//获取本机IP地址
protected:
   void   closeEvent(QCloseEvent *event);
public:
   explicit MainWindow(QWidget *parent = 0);
   ~MainWindow();
private slots:
//自定义槽函数   
   void   onConnected();
   void   onDisconnected();
   void   onSocketStateChange(QAbstractSocket::SocketState socketState);
   void   onSocketReadyRead();//读取socket传入的数据
private:
   Ui::MainWindow *ui;
};
```

这里只定义了一个用于socket连接和通信的QTcpSocket变量tcpClient，自定义了几个槽函数，用于与tcpClient的相关信号关联。

下面是MainWindow的构造函数，主要功能是创建tcpClient，并建立信号与槽函数的关联。

```css
MainWindow::MainWindow(QWidget *parent) :   QMainWindow(parent),
   ui(new Ui::MainWindow)
{
   ui->setupUi(this);
   tcpClient=new QTcpSocket(this); //创建socket变量
   LabSocketState=new QLabel("Socket状态：");//状态栏标签
   LabSocketState->setMinimumWidth(250);
   ui->statusBar->addWidget(LabSocketState);
   QString localIP=getLocalIP();//本机IP
   this->setWindowTitle(this->windowTitle()+"----本机IP："+localIP);
   ui->comboServer->addItem(localIP);
   connect(tcpClient,SIGNAL(connected()),this,SLOT(onConnected()));
   connect(tcpClient,SIGNAL(disconnected()),this,SLOT(onDisconnected()));
   connect(tcpClient,SIGNAL(stateChanged(QAbstractSocket::SocketState)),
          this,SLOT(onSocketStateChange(QAbstractSocket::SocketState)));
   connect(tcpClient,SIGNAL(readyRead()),
          this,SLOT(onSocketReadyRead()));
}
```

#### 2．与服务器端建立socket连接

在窗口上设置服务器IP地址和端口后，调用QTcpSocket的函数connectToHost()连接到服务器，也可以使用disconnectFromHost()函数断开与服务器的连接。

下面是两个按钮的响应代码，以及两个相关槽函数的代码：

```css
void MainWindow::on_actConnect_triggered()
{//“连接到服务器”按钮
   QString    addr=ui->comboServer->currentText();
   quint16    port=ui->spinPort->value();
   tcpClient->connectToHost(addr,port);
}
void MainWindow::on_actDisconnect_triggered()
{//“断开连接”按钮
   if (tcpClient->state()==QAbstractSocket::ConnectedState)
      tcpClient->disconnectFromHost();
}
void MainWindow::onConnected()
{ //connected()信号槽函数
   ui->plainTextEdit->appendPlainText("**已连接到服务器");
   ui->plainTextEdit->appendPlainText("**peer address:"+
                         tcpClient->peerAddress().toString());
   ui->plainTextEdit->appendPlainText("**peer port:"+
                         QString::number(tcpClient->peerPort()));
   ui->actConnect->setEnabled(false);
   ui->actDisconnect->setEnabled(true);
}
void MainWindow::onDisconnected()
{//disConnected()信号槽函数
   ui->plainTextEdit->appendPlainText("**已断开与服务器的连接");
   ui->actConnect->setEnabled(true);
   ui->actDisconnect->setEnabled(false);
}
```

槽函数onSocketStateChange()的功能和代码与TCPServer中的完全一样，这里不再赘述。

#### 3．与TCPServer的数据收发

TCPClient与TCPServer之间采用基于行的数据通信协议。单击“发送消息”按钮将发送一行字符串。在readyRead()信号的槽函数里读取行字符串，其相关代码如下：

```css
void MainWindow::on_btnSend_clicked()
{//发送数据
   QString  msg=ui->editMsg->text();
   ui->plainTextEdit->appendPlainText("[out] "+msg);
   ui->editMsg->clear();
   ui->editMsg->setFocus();
   QByteArray  str=msg.toUtf8();
   str.append('\n');
   tcpClient->write(str);
}
void MainWindow::onSocketReadyRead()
{//readyRead()信号槽函数
   while(tcpClient->canReadLine())
      ui->plainTextEdit->appendPlainText("[in] "+tcpClient->readLine());
}
```

实例TCPServer和TCPClient只是简单演示了TCP通信的基本原理，TCPServer只允许一个TCPClient客户端接入。而一般的TCP服务器程序允许多个客户端接入，为了使每个socket连接独立通信互不影响，一般采用多线程，即为一个socket连接创建一个线程。

实例TCPServer和TCPClient之间的数据通信采用基于行的通信协议，只能传输字符串数据。QTcpSocket间接继承于QIODevice，可以使用数据流的方式传输二进制数据流，例如传输图片、任意格式文件等，但是这涉及到服务器端和客户端之间通信协议的定义，本书不具体介绍了。

