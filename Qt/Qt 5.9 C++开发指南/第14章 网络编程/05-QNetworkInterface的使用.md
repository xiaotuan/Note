### 14.1.3　QNetworkInterface的使用

QNetworkInterface可以获得应用程序所在主机的所有网络接口，包括其子网掩码和广播地址等。

静态函数QNetworkInterface::allInterfaces()获取所有网络接口的列表，函数原型为:

```css
QList<QNetworkInterface> QNetworkInterface::allInterfaces()
```

其返回结果是一个QNetworkInterface类的列表。

界面上“QNetworkInterface::allInterfaces()”按钮的响应代码如下：

```css
void Dialog::on_btnALLInterface_clicked()
{//QNetworkInterface::allInterfaces()函数的使用
  QList<QNetworkInterface>   list=QNetworkInterface::allInterfaces();
  for(int i=0;i<list.count();i++)
  {
   QNetworkInterface aInterface=list.at(i);
   if (!aInterface.isValid())
     continue;
   ui->plainTextEdit->appendPlainText("设备名称："+ aInterface.humanReadableName());
   ui->plainTextEdit->appendPlainText("硬件地址："+ aInterface.hardwareAddress());
   QList<QNetworkAddressEntry> entryList=aInterface.addressEntries();
   for(int j=0;j<entryList.count();j++)
   {
      QNetworkAddressEntry aEntry=entryList.at(j);
      ui->plainTextEdit->appendPlainText("  IP 地址："+ aEntry.ip().toString());
      ui->plainTextEdit->appendPlainText("  子网掩码："+ aEntry.netmask().toString());
      ui->plainTextEdit->appendPlainText("  广播地址："+ aEntry.broadcast(). toString()+"\n");
     }
   ui->plainTextEdit->appendPlainText("\n");
   }
}
```

通过QNetworkInterface::allInterfaces()获取网络接口列表list之后，显示每个接口的humanReadable Name()和hardwareAddress()。每个接口又有一个QNetworkAddressEntry类型的地址列表，通过addressEntries ()获得这个列表。

QNetworkAddressEntry包含了一个网络接口的IP地址、子网掩码和广播地址，分别用ip()、netmask()和broadcast()函数返回。

QNetworkInterface::allInterfaces()返回的网络接口的信息很多，如果无需知道子网掩码和广播地址等信息，可以使用QNetworkInterface::allAddresses()只获取IP地址。

界面上“QNetworkInterface ::allAddresses()”按钮的响应代码如下：

```css
void Dialog::on_btnDetail_clicked()
{//QNetworkInterface::allAddresses()的使用
   QList<QHostAddress> addList=QNetworkInterface::allAddresses();
   if (!addList.isEmpty())
   for (int i=0;i<addList.count();i++)
   {
     QHostAddress aHost=addList.at(i);
     bool show=ui->chkOnlyIPv4->isChecked();//只显示IPv4
     if (show)
      show=QAbstractSocket::IPv4Protocol==aHost.protocol();
     else
      show=true;
     if (show)  {
     ui->plainTextEdit->appendPlainText("协  议："+ protocolName(aHost.protocol()));
     ui->plainTextEdit->appendPlainText("IP地址："+aHost.toString());
     ui->plainTextEdit->appendPlainText("");
     }
   }
}
```

QNetworkInterface ::allAddresses()的功能与QHostInfo::addresses()函数功能相似，都是返回一个QHostAddress的列表。只是QNetworkInterface会返回更多地址，包括表示本机的127.0.0.1，而QHostInfo不会返回这个IP地址。

