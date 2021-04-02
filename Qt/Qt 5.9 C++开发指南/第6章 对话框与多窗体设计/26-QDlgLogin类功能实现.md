### 6.5.3　QDlgLogin类功能实现

#### 1．构造函数里的初始化

QDlgLogin类的构造函数代码如下：

```css
QDlgLogin::QDlgLogin(QWidget *parent) :   QDialog(parent),   ui(new Ui::dlgLogin)
{
   ui->setupUi(this);
   ui->editPSWD->setEchoMode(QLineEdit::Password); //设置为密码输入模式
   this->setAttribute(Qt::WA_DeleteOnClose);//设置为关闭时删除
   this->setWindowFlags(Qt::SplashScreen); //设置为SplashScreen 
// this->setWindowFlags(Qt::FramelessWindowHint);//无边框，但在任务栏显示标题
   readSettings(); //读取存储的用户名和密码
}
```

QLineEdit::setEchoMode()函数设置编辑框回显方式，参数为QLineEdit::EchoMode枚举类型，这里设置为QLineEdit::Password回显方式，用于将密码输入回显为一个符号，而不显示真实字符。

使用setWindowFlags()函数将窗口标志设置为Qt::SplashScreen，这样对话框显示为Splash窗口，无边框，且在Windows任务栏上没有显示。另外一个类似的标志是Qt::FramelessWindowHint，它会使对话框无边框，但是会在任务栏上显示对话框的标题。

初始设置后调用readSettings()函数读取存储的设置，根据存储的情况将用户名显示到窗口上的编辑框里。

#### 2．应用程序设置的存储

自定义成员函数readSettings()用于读取应用程序设置，writeSettings()用于保存设置，实现代码如下：

```css
void QDlgLogin::readSettings()
{//读取存储的用户名和密码, 密码是经过加密的
   QString  organization="WWB-Qt";//用于注册表，
   QString  appName="samp6_5"; 
   QSettings  settings(organization,appName);
   bool  saved=settings.value("saved",false).toBool();//读取 saved
   m_user=settings.value("Username", "user").toString();//读取Username 
   QString  defaultPSWD=encrypt("12345"); //缺省密码"12345"加密后的数据
   m_pswd=settings.value("PSWD",defaultPSWD).toString();//读取PSWD
   if (saved)
      ui->editUser->setText(m_user);
   ui->chkBoxSave->setChecked(saved);
}
void QDlgLogin::writeSettings()
{ //保存用户名，密码等设置
   QSettings   settings("WWB-Qt","samp6_5"); //注册表键组
   settings.setValue("Username",m_user); //用户名
   settings.setValue("PSWD",m_pswd);   //密码，经过加密的
   settings.setValue("saved",ui->chkBoxSave->isChecked());
}
```

应用程序的设置是指应用程序需要保存的一些信息，在Windows系统下，这些信息保存在注册表里。使用QSettings类可以实现设置信息的读取和写入。

创建QSettings对象时，需要传递organization和appName，例如：

```css
QSettings   settings("WWB-Qt","samp6_5");
```

指向的注册表目录是HKEY_CURRENT_USER/Software/WWB-Qt/samp6_5。

注册表里参数是以“键——键值”对来保存的。writeSettings()函数里使用setValue()函数写入键值，readSettings()里使用value()函数读取键值。读取键值时可以指定缺省值，即如果键不存在，就用缺省值作为读取的值。

在Windows的开始菜单的输入框里输入regedit，打开注册表，查找到目录HKEY_CURRENT_USER/Software/WWB-Qt/samp6_5，可以看到注册表里参数存储情况。其中，存储的密码是加密后的字符串。

#### 3．字符串加密

本实例中密码采用加密后的字符串保存，这样在实际应用中具有安全性。Qt提供了用于加密的类QCryptographicHash，自定义函数encrypt()就利用这个类进行字符串加密，实现代码如下：

```css
QString QDlgLogin::encrypt(const QString &str)
{ //字符串MD5算法加密
   QByteArray btArray;
   btArray.append(str); 
   QCryptographicHash hash(QCryptographicHash::Md5);  //Md5加密算法
   hash.addData(btArray);  //添加数据
   QByteArray resultArray =hash.result();  //返回最终的散列值
   QString md5 =resultArray.toHex();//转换为16进制字符串
   return  md5;
}
```

QCryptographicHash创建时需要指定一种加密算法，加密算法变量是枚举类型QCryptographicHash:: Algorithm，常用的常量值有QCryptographicHash::Md4、QCryptographicHash::Md5、QCryptographicHash:: Sha512等，完整的描述可参考Qt的帮助文档。

QCryptographicHash只提供了加密功能，没有提供解密功能。

#### 4．用户名和密码输入判断

登录窗口运行后，单击“确定”按钮，程序会对输入内容进行判断，“确定”按钮的槽函数代码如下：

```css
void QDlgLogin::on_btnOK_clicked()
{//"确定"按钮
   QString  user=ui->editUser->text().trimmed();//输入用户名
   QString  pswd=ui->editPSWD->text().trimmed(); //输入密码
   QString  encrptPSWD=encrypt(pswd); //对输入密码进行加密
   if ((user==m_user)&&(encrptPSWD==m_pswd)) 
   {   writeSettings();
      this->accept(); //对话框 accept()，关闭对话框
   }
   else
   {   m_tryCount++; //错误次数
      if (m_tryCount>3)
      {   QMessageBox::critical(this, "错误", "输入错误次数太多，强行退出");
         this->reject(); //退出
      }
      else
         QMessageBox::warning(this, "错误提示", "用户名或密码错误");
   }
}
```

由于QCryptographicHash只提供了加密功能，没有提供解密功能，所以，在读取应用程序设定后，无法将加密后的密码解密并显示在窗口上，程序只能回显用户名，而不能回显密码。

这段程序会对输入的密码进行加密，因为从注册表读取的是加密后的密码，所以能够对比输入的用户名和密码与存储的用户名和密码是否匹配。

如果输入正确，调用窗口的accept()槽函数关闭对话框，对话框返回值为QDialog::Accepted，否则试错次数加一；如果试错次数大于3次，就调用窗口的reject()槽函数关闭对话框，对话框返回值为QDialog:: Rejected。

#### 5．窗口拖动功能的实现

由于Splash窗口没有边框，因此不能像普通的窗口那样通过拖动窗口的标题栏来拖动窗口。为了实现窗口的拖动功能，对窗口的3个鼠标事件进行处理，实现的代码如下：

```css
void QDlgLogin::mousePressEvent(QMouseEvent *event)
{ //鼠标按键被按下
   if (event->button() == Qt::LeftButton)
   {   m_moving = true;
      m_lastPos = event->globalPos() - pos();//记录下鼠标相对于窗口的位置
   }
   return QDialog::mousePressEvent(event);  
}
void QDlgLogin::mouseMoveEvent(QMouseEvent *event)
{//鼠标按下左键移动
   if (m_moving && (event->buttons() && Qt::LeftButton) && (event->globalPos()-m_lastPos).manhattanLength() > QApplication::startDragDistance())
   {
      move(event->globalPos()-m_lastPos);
      m_lastPos = event->globalPos() - pos();
   }
   return QDialog::mouseMoveEvent(event);
}
void QDlgLogin::mouseReleaseEvent(QMouseEvent *event)
{//鼠标按键释放
   m_moving=false; //停止移动
}
```

mousePressEvent(QMouseEvent *event)事件在鼠标按键按下时发生，传递的参数event有鼠标按键和坐标信息，判断如果是鼠标左键按下，就设置变量m_moving值为true，表示开始移动，并记录下鼠标坐标。event->globalPos()与对话框的pos()是不同坐标系下的坐标，在绘图这一章再详细介绍。

mouseMoveEvent(QMouseEvent *event)事件在鼠标移动时发射，程序里判断是否已经开始移动并且按下鼠标左键；如果是，则调用窗口的move()函数，横向和纵向移动一定的距离，并再次记录坐标点。

mouseReleaseEvent(QMouseEvent *event)事件在鼠标按键释放时发生，左键释放时停止窗口移动。

所以，当在窗口上按下鼠标左键并移动时，窗口就会随之移动。

