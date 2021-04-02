### 6.5.4　Splash登录窗口的使用

设计好启动和登录窗口QDlgLogin之后，在main()函数里使用启动与登录对话框。main()函数的代码如下：

```css
int main(int argc, char *argv[])
{
   QApplication a(argc, argv);
   QDlgLogin   *dlgLogin=new QDlgLogin; 
   if (dlgLogin->exec()==QDialog::Accepted)
   {
      QWMainWindow w;
      w.show();
      return a.exec();
   }
   else
      return  0;
}
```

在主窗口之前创建Splash登录对话框对象dlgLogin，并以模态显示的方式调用此对话框。如果对话框返回的是QDialog::Accepted，说明通过了用户名和密码验证，就创建主窗口并显示；否则退出应用程序。由于QDlgLogin设置为关闭时删除，验证关闭登录窗口后，对象会自动删除。



