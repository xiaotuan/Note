### 14.2.2　TCP服务器端程序设计

#### 1．主窗口定义与构造函数

TCPServer是一个窗口基于QMainWindow的应用程序，界面由UI设计器设计，MainWindow类的定义如下（忽略了UI设计器自动生成的actions和按钮的槽函数）：

```css
class MainWindow : public QMainWindow
{
   Q_OBJECT
private:
   QLabel  *LabListen;//状态栏标签
   QLabel  *LabSocketState;//状态栏标签
   QTcpServer *tcpServer; //TCP服务器
   QTcpSocket *tcpSocket;//TCP通信的Socket
   QString getLocalIP();//获取本机IP地址
protected:
   void   closeEvent(QCloseEvent *event);
public:
   explicit MainWindow(QWidget *parent = 0);
   ~MainWindow();
private slots:
//自定义槽函数
   void   onNewConnection();//QTcpServer的newConnection()信号
   void   onSocketStateChange(QAbstractSocket::SocketState socketState);
   void   onClientConnected(); //Client Socket connected
   void   onClientDisconnected();//Client Socket disconnected
   void   onSocketReadyRead();//读取socket传入的数据
private:
   Ui::MainWindow *ui;
};
```

MainWindow中定义了私有变量tcpServer用于建立TCP服务器，定义了tcpSocket用于与客户端进行socket连接和通信。

定义了几个槽函数，用于与QTcpServer和QTcpSocket的相关信号连接，实现相应的处理。MainWindow构造函数代码如下：

```css
MainWindow::MainWindow(QWidget *parent) :   QMainWindow(parent),
   ui(new Ui::MainWindow)
{
   ui->setupUi(this);
   LabListen=new QLabel("监听状态:");
   LabListen->setMinimumWidth(150);
   ui->statusBar->addWidget(LabListen);
   LabSocketState=new QLabel("Socket状态：");
   LabSocketState->setMinimumWidth(200);
   ui->statusBar->addWidget(LabSocketState);
   QString localIP=getLocalIP();//本机IP
   this->setWindowTitle(this->windowTitle()+"----本机IP："+localIP);
   ui->comboIP->addItem(localIP);
   tcpServer=new QTcpServer(this);
  connect(tcpServer,SIGNAL(newConnection()),this,SLOT(onNewConnection()));
}
QString MainWindow::getLocalIP()
{//获取本机IPv4地址
   QString  hostName=QHostInfo::localHostName();//本地主机名
   QHostInfo   hostInfo=QHostInfo::fromName(hostName);
   QString   localIP="";
   QList<QHostAddress> addList=hostInfo.addresses();
   if (!addList.isEmpty())
   for (int i=0;i<addList.count();i++)
   {
      QHostAddress aHost=addList.at(i);
      if (QAbstractSocket::IPv4Protocol==aHost.protocol())
      {  localIP=aHost.toString();  break; }
   }
   return localIP;
}
```

MainWindow的构造函数创建状态栏上的标签用于信息显示，调用自定义函数getLocalIP()获取本机IP地址，并显示到标题栏上。创建QTcpServer实例tcpServer，并将其newConnection()信号与onNewConnection()槽函数关联。

#### 2．网络监听与socket连接的建立

作为TCP服务器，QTcpServer类需要调用listen()在本机某个IP地址和端口上开始TCP监听，以等待TCP客户端的接入。单击主窗口上“开始监听”按钮可以开始网络监听，其代码如下：

```css
void MainWindow::on_actStart_triggered()
{//开始监听
   QString    IP=ui->comboIP->currentText();//IP地址
   quint16    port=ui->spinPort->value();//端口
   QHostAddress   addr(IP);
   tcpServer->listen(addr,port);//开始监听
   ui->plainTextEdit->appendPlainText("**开始监听...");
   ui->plainTextEdit->appendPlainText("**服务器地址："
                   +tcpServer->serverAddress().toString());
   ui->plainTextEdit->appendPlainText("**服务器端口："
                   +QString::number(tcpServer->serverPort()));
   ui->actStart->setEnabled(false);
   ui->actStop->setEnabled(true);
   LabListen->setText("监听状态：正在监听");
}
```

程序读取窗口上设置的监听地址和监听端口，然后调用QTcpServer的listen()函数开始监听。TCP服务器在本机上监听，所以IP地址可以是表示本机的“127.0.0.1”，或是本机的实际IP，亦或是常量QHostAddress::LocalHost，即在本机上监听某个端口也可以写成：

```css
tcpServer->listen(QHostAddress::LocalHost,port);
```

tcpServer开始监听后，TCPClient就可以通过IP地址和端口连接到此服务器。当有客户端接入时，tcpServer会发射newConnection()信号，此信号关联的槽函数onNewConnection()的代码如下：

```css
void MainWindow::onNewConnection()
{
   tcpSocket = tcpServer->nextPendingConnection(); //获取socket
   //connect(tcpSocket, SIGNAL(connected()), this, SLOT(onClientConnected()));
   onClientConnected();
   connect(tcpSocket, SIGNAL(disconnected()),
              this, SLOT(onClientDisconnected()));
   connect(tcpSocket,SIGNAL(stateChanged(QAbstractSocket::SocketState)),
         this,SLOT(onSocketStateChange(QAbstractSocket::SocketState)));
   onSocketStateChange(tcpSocket->state());
   connect(tcpSocket,SIGNAL(readyRead()), this,SLOT(onSocketReadyRead()));
}
```

程序首先通过nextPendingConnection()函数获取与接入连接进行通信的QTcpSocket对象实例tcpSocket，然后将tcpSocket的几个信号与相应的槽函数连接起来。QTcpSocket的这几个信号的作用是：

+ connected()信号，客户端socket连接建立时发射此信号；
+ disconnected()信号，客户端socket连接断开时发射此信号；
+ stateChanged()，本程序的socket状态变化时发射此信号；
+ readyRead()，本程序的socket的读取缓冲区有新数据时发射此信号。

涉及状态变化的几个信号的槽函数代码如下：

```css
void MainWindow::onClientConnected()
{//客户端接入时
   ui->plainTextEdit->appendPlainText("**client socket connected");
   ui->plainTextEdit->appendPlainText("**peer address:"+
                       tcpSocket->peerAddress().toString());
   ui->plainTextEdit->appendPlainText("**peer port:"+
                       QString::number(tcpSocket->peerPort()));
}
void MainWindow::onClientDisconnected()
{//客户端断开连接时
   ui->plainTextEdit->appendPlainText("**client socket disconnected");
   tcpSocket->deleteLater();
}
void MainWindow::onSocketStateChange(QAbstractSocket::SocketState socketState)
{//socket状态变化时
   switch(socketState)
   {
   case QAbstractSocket::UnconnectedState:
      LabSocketState->setText("scoket状态：UnconnectedState");    break;
   case QAbstractSocket::HostLookupState:
      LabSocketState->setText("scoket状态：HostLookupState");    break;
   case QAbstractSocket::ConnectingState:
      LabSocketState->setText("scoket状态：ConnectingState");    break;
   case QAbstractSocket::ConnectedState:
      LabSocketState->setText("scoket状态：ConnectedState");     break;
   case QAbstractSocket::BoundState:
      LabSocketState->setText("scoket状态：BoundState");        break;
   case QAbstractSocket::ClosingState:
      LabSocketState->setText("scoket状态：ClosingState");      break;
   case QAbstractSocket::ListeningState:
      LabSocketState->setText("scoket状态：ListeningState");
   }
}
```

TCP服务器停止监听，只需调用QTcpServer的close()函数即可。窗口上的“停止监听”响应代码如下：

```css
void MainWindow::on_actStop_triggered()
{//停止监听
   if (tcpServer->isListening()) //tcpServer正在监听
   {
      tcpServer->close();//停止监听
      ui->actStart->setEnabled(true);
      ui->actStop->setEnabled(false);
      LabListen->setText("监听状态：已停止监听");
   }
}
```

#### 3．与TCPClient的数据通信

TCP服务器端和客户端之间通过QTcpSocket通信时，需要规定两者之间的通信协议，即传输的数据内容如何解析。QTcpSocket间接继承于QIODevice，所以支持流读写功能。

Socket之间的数据通信协议一般有两种方式，基于行的或基于数据块的。

基于行的数据通信协议一般用于纯文本数据的通信，每一行数据以一个换行符结束。canReadLine()函数判断是否有新的一行数据需要读取，再用readLine()函数读取一行数据，例如：

```css
while(tcpClient-><em>canReadLine</em>())
   ui->plainTextEdit->appendPlainText("[in] "+tcpClient->readLine());
```

基于块的数据通信协议用于一般的二进制数据的传输，需要自定义具体的格式。

实例程序TCPServer和TCPClient只是进行字符串的信息传输，类似于一个简单的聊天程序，程序采用基于行的数据通信协议。

单击窗口上的“发送消息”，将文本框里的字符串发送给客户端，其实现代码如下：

```css
void MainWindow::on_btnSend_clicked()
{//发送一行字符串，以换行符结束
   QString  msg=ui->editMsg->text();
   ui->plainTextEdit->appendPlainText("[out] "+msg);
   ui->editMsg->clear();
   ui->editMsg->setFocus();
   QByteArray  str=msg.toUtf8();
   str.append('\n');//添加一个换行符
   tcpSocket->write(str);
}
```

从上面的代码中可以看到，读取文本框中的字符串到msg后，先将其转换为QByteArray类型字节数组str，然后在str最后面添加一个换行符，用QIODevice的write()函数写入缓冲区，这样就向客户端发送一行文字。

QTcpSocket接收到数据后，会发射readyRead()信号，在onNewConnection()槽函数中已经建立了这个信号与槽函数onSocketReadyRead()的连接。

槽函数onSocketReadyRead()实现缓冲区数据的读取，其代码如下：

```css
void MainWindow::onSocketReadyRead()
{//读取缓冲区行文本
   while(tcpSocket->canReadLine())
     ui->plainTextEdit->appendPlainText("[in] "+tcpSocket->readLine());
}
```

这样，TCPServer就可以与TCPClient之间进行双向通信了，且这个连接将一直存在，直到某一方的QTcpSocket对象调用disconnectFromHost()函数断开socket连接。

