### 14.1.2　QHostInfo的使用

#### 1．显示本机地址信息

图14-1窗口上的“QHostInfo 获取本机主机名和IP地址”按钮的响应代码如下：

```css
void Dialog::on_btnGetHostInfo_clicked()
{//QHostInfo获取主机信息
   QString hostName=QHostInfo::localHostName();//本地主机名
   ui->plainTextEdit->appendPlainText("本机主机名："+hostName+"\n");
   QHostInfo   hostInfo=QHostInfo::fromName(hostName); //本机IP地址
   QList<QHostAddress> addList=hostInfo.addresses();//IP地址列表
   if (!addList.isEmpty())
   for (int i=0;i<addList.count();i++)
   {
      QHostAddress aHost=addList.at(i); //每一项是一个QHostAddress
      bool show=ui->chkOnlyIPv4->isChecked();//只显示IPv4
      if (show)
        show=(QAbstractSocket::IPv4Protocol==aHost.protocol()); //IPv4协议
      else
        show=true;
      if (show) {
      ui->plainTextEdit->appendPlainText("协 议："+ protocolName(aHost.protocol()));
      ui->plainTextEdit->appendPlainText("本机IP地址："+aHost.toString());
      ui->plainTextEdit->appendPlainText("");
      }
   }
}
```

这段代码先通过静态函数QHostInfo::localHostName()获取本机主机名hostName，然后再使用主机名作为参数，用静态函数QHostInfo::fromName(hostName)获取主机的信息hostInfo。

hostInfo是QHostInfo类的实例，通过其函数addresses()获取主机的IP地址列表。

```css
QList<QHostAddress> addList=hostInfo.addresses();
```

返回的addList是QHostAddress类的列表，QHostAddress类提供一个IP地址的信息，包括IPv4地址和IPv6地址。QHostAddress有以下两个主要的函数。

+ protocol() 返回QAbstractSocket::NetworkLayerProtocol类型变量，表示当前IP地址的协议类型。QAbstractSocket::NetworkLayerProtocol枚举类型的取值见表14-3。

<center class="my_markdown"><b class="my_markdown">表14-3　QAbstractSocket::NetworkLayerProtocol枚举类型取值</b></center>

| 枚举值 | 表示的协议类型 |
| :-----  | :-----  | :-----  | :-----  |
| QAbstractSocket::IPv4Protocol | IPv4 |
| QAbstractSocket::IPv6Protocol | IPv6 |
| QAbstractSocket::AnyIPProtocol | IPv4 或 IPv6 |
| QAbstractSocket::UnknownNetworkLayerProtocol | 其他类型 |

+ toString () 返回IP地址的字符串，表示程序中显示了IP地址列表中每个IP地址的协议类型和IP地址字符串，为根据protocol()返回的QAbstractSocket::NetworkLayerProtocol枚举值显示协议名称字符串，自定义了一个函数protocolName()，代码如下：

```css
QString Dialog::protocolName(QAbstractSocket::NetworkLayerProtocol protocol)
{//通过协议类型返回协议名称
  switch(protocol)
  {
   case QAbstractSocket::IPv4Protocol:
      return "IPv4 Protocol";
   case QAbstractSocket::IPv6Protocol:
     return "IPv6 Protocol";
   case QAbstractSocket::AnyIPProtocol:
     return "Any IP Protocol";
   default:
     return "Unknown Network Layer Protocol";
   }
}
```

单击“QHostInfo 获取本机主机名和IP地址”按钮，如果勾选了“只显示 IPv4协议地址”复选框，就只显示本机的IPv4地址，否则显示所有IP地址信息。

#### 2．查找主机地址信息

QHostInfo的静态函数lookupHost()可以根据主机名、域名或IP地址查找主机的地址信息，lookupHost()函数原型如下：

```css
int QHostInfo::lookupHost(const QString &name, QObject *receiver, const char *member)
```

输入参数name是表示主机名的字符串，可以是一个主机名、一个域名，或者是一个IP地址。

lookupHost()以异步方式查找主机地址，参数receiver和member指定一个响应槽函数的接收者和槽函数名称。执行lookupHost()后，程序可能需要花一定时间来查找主机地址，但不会阻塞程序的运行。当查找到主机地址后，通过信号通知设定的槽函数，在槽函数里读取查找的结果。函数返回一个表示查找的ID。

图14-1中的“QHostInfo查找域名的IP地址”按钮的槽函数及lookupHost()函数关联槽函数代码如下：

```css
void Dialog::on_btnLookup_clicked()
{//查找主机信息
   QString hostname=ui->editHost->text(); //主机名
   ui->plainTextEdit->appendPlainText("正在查找查找主机信息："+hostname);
   QHostInfo::lookupHost(hostname,this,SLOT(lookedUpHostInfo(QHostInfo)));
}
void Dialog::lookedUpHostInfo(const QHostInfo &host)
{//查找主机信息的槽函数
   QList<QHostAddress> addList=host.addresses();
   if (!addList.isEmpty())
   for (int i=0;i<addList.count();i++)
   {
      QHostAddress aHost=addList.at(i);
      bool show=ui->chkOnlyIPv4->isChecked();//只显示IPv4
      if (show)
         show=QAbstractSocket::IPv4Protocol==aHost.protocol();
      else
         show=true;
      if (show) {
      ui->plainTextEdit->appendPlainText("协 议："+ protocolName(aHost.protocol()));
      ui->plainTextEdit->appendPlainText(aHost.toString());
      }
   }
}
```

