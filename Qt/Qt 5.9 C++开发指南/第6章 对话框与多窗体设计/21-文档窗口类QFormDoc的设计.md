### 6.4.2　文档窗口类QFormDoc的设计

以可视化方式创建一个基于QWidget的类QFormDoc，设计可视化界面时，只放置一个QPlainTextEdit组件，并以水平布局填充满整个窗口。这里不再用可视化的方式设计Action，因为QFormDoc窗口不需要创建自己的工具栏，而是使用主窗口上的工具栏按钮对QFormDoc窗体上的QPlainTextEdit组件进行操作。

为QFormDoc添加一些用于文件打开和编辑操作的接口函数，QFormDoc类的完整定义如下：

```css
class QFormDoc : public QWidget
{   Q_OBJECT
private:
   QString  mCurrentFile; //当前文件
   bool   mFileOpened=false; //文件已打开
public:
   explicit  QFormDoc(QWidget *parent = 0);
   ~QFormDoc();
   void   loadFromFile(QString& aFileName); //打开文件
   QString  currentFileName();//返回当前文件名
   bool   isFileOpened();//文件已经打开
   void   setEditFont();//设置字体
   void   textCut(); //cut
   void   textCopy(); //copy
   void   textPaste(); //paste
private:
   Ui::QFormDoc *ui;
};
```

这些接口函数是为了在主窗口里调用，实现对MDI子窗口的操作。实现代码如下：

```css
QFormDoc::QFormDoc(QWidget *parent) : QWidget(parent), ui(new Ui::QFormDoc)
{
   ui->setupUi(this);
   this->setWindowTitle("New Doc"); //窗口标题
   this->setAttribute(Qt::WA_DeleteOnClose); //关闭时自动删除
}
QFormDoc::~QFormDoc()
{
   QMessageBox::information(this,"信息","文档窗口被释放");
   delete ui;
}
void QFormDoc::loadFromFile(QString &aFileName)
{//打开文件
   QFile aFile(aFileName); 
   if (aFile.open(QIODevice::ReadOnly | QIODevice::Text)) 
   {
      QTextStream aStream(&aFile); //用文本流读取文件
      ui->plainTextEdit->clear();
      ui->plainTextEdit->setPlainText(aStream.readAll()); //读取文本文件
      aFile.close();//关闭文件
      mCurrentFile=aFileName;//保存当前文件名
      QFileInfo   fileInfo(aFileName); //文件信息
      QString str=fileInfo.fileName(); //去除路径后的文件名
      this->setWindowTitle(str);
      mFileOpened=true;
   }
}
QString QFormDoc::currentFileName()
{   return  mCurrentFile;  
}
bool QFormDoc::isFileOpened()
{  return mFileOpened; 
}
void QFormDoc::setEditFont()
{
   QFont   font=ui->plainTextEdit->font();
   bool   ok;
   font=QFontDialog::getFont(&ok,font);
   ui->plainTextEdit->setFont(font);
}
void QFormDoc::textCut()
{   ui->plainTextEdit->cut(); 
}
void QFormDoc::textCopy()
{   ui->plainTextEdit->copy();
}
void QFormDoc::textPaste()
{   ui->plainTextEdit->paste();
}
```

> **注意**
> 作为MDI子窗口，不管其是否设置为关闭时删除，在主窗口里关闭一个MDI子窗口时，都会删除子窗口对象。

