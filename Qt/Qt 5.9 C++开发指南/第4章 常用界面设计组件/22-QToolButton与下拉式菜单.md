### 4.6.4　QToolButton与下拉式菜单

#### 1．QToolButton关联QAction

图4-9所示的界面上，在ToolBox里放置了几个QToolButton按钮，希望它们实现与工具栏上的按钮相同的功能；列表框上方放置了几个QToolButton按钮，希望它们完成列表项选择的功能。

这些功能都已经有相应的Actions来实现，要让ToolButton按钮实现这些功能，无需再为其编写代码，只需设置一个关联的QAction对象即可。

QToolButton有一个函数setDefaultAction()，其函数原型为：

```css
void QToolButton::setDefaultAction(QAction *action)
```

使用setDefaultAction()函数为一个QToolButton按钮设置一个Action之后，将自动获取Action的文字、图标、ToolTip等设置为按钮的相应属性。所以，在界面设计时无需为QToolButton做过多的设置。

在主窗体类里定义一个私有函数setActionsForButton()，用来为界面上的QToolButton按钮设置关联的Actions，setActionsForButton()在主窗口的构造函数里调用，其代码如下：

```css
void MainWindow::setActionsForButton()
{//为QToolButton按钮设置Action
   ui->tBtnListIni->setDefaultAction(ui->actListIni);
   ui->tBtnListClear->setDefaultAction(ui->actListClear);
   ui->tBtnListInsert->setDefaultAction(ui->actListInsert);
   ui->tBtnListAppend->setDefaultAction(ui->actListAppend);
   ui->tBtnListDelete->setDefaultAction(ui->actListDelete);
   ui->tBtnSelALL->setDefaultAction(ui->actSelALL);
   ui->tBtnSelNone->setDefaultAction(ui->actSelNone);
   ui->tBtnSelInvs->setDefaultAction(ui->actSelInvs);
}
```

在程序启动后，界面上的ToolButton按钮自动根据关联的Actions设置其按钮文字、图标和ToolTip。单击某个ToolButton按钮，就是执行了其关联的Action的槽函数代码。使用Actions集中设计功能代码，用于菜单、工具栏、ToolButton的设计，是避免重复编写代码的一种方式。

#### 2．为QToolButton按钮设计下拉菜单

还可以为QToolButton按钮设计下拉菜单，在图4-8的运行窗口中，单击工具栏上的“项选择”按钮，会在按钮的下方弹出一个菜单，有3个菜单项用于项选择。

在主窗口类里定义一个私有函数createSelectionPopMenu()，并在窗口的构造函数里调用，其代码如下：

```css
void MainWindow::createSelectionPopMenu()
{//创建下拉菜单
   QMenu* menuSelection=new QMenu(this); //创建弹出式菜单
   menuSelection->addAction(ui->actSelALL);
   menuSelection->addAction(ui->actSelNone);
   menuSelection->addAction(ui->actSelInvs);
//listWidget上方的tBtnSelectItem按钮
   ui->tBtnSelectItem->setPopupMode(QToolButton::MenuButtonPopup); 
   ui->tBtnSelectItem->setToolButtonStyle(Qt::ToolButtonTextBesideIcon); 
   ui->tBtnSelectItem->setDefaultAction(ui->actSelPopMenu);//关联Action
   ui->tBtnSelectItem->setMenu(menuSelection); //设置下拉菜单
//工具栏上的 下拉式菜单按钮
   QToolButton  *aBtn=new QToolButton(this);
   aBtn->setPopupMode(QToolButton::InstantPopup);
   aBtn->setToolButtonStyle(Qt::ToolButtonTextUnderIcon);//按钮样式
   aBtn->setDefaultAction(ui->actSelPopMenu); 
   aBtn->setMenu(menuSelection);//设置下拉菜单
   ui->mainToolBar->addWidget(aBtn); //工具栏添加按钮
//工具栏添加分隔条，和"退出"按钮
   ui->mainToolBar->addSeparator();
   ui->mainToolBar->addAction(ui->actQuit);
}
```

这段代码首先创建一个QMenu对象menuSelection，将3个用于选择列表项的Action添加作为菜单项。

tBtnSelectItem是窗体上ListWidget上方具有下拉菜单的QToolButton按钮的名称，调用了QToolButton类的4个函数对其进行设置。

+ setPopupMode(QToolButton::MenuButtonPopup)，设置其弹出菜单的模式。QToolButton::　MenuButtonPopup是一个枚举常量，这种模式下，按钮右侧有一个向下的小箭头，必须单击这个小按钮才会弹出下拉菜单，直接单击按钮会执行按钮关联的Action，而不会弹出下拉菜单。
+ setToolButtonStyle(Qt::ToolButtonTextBesideIcon)，设置按钮样式，按钮标题文字在图标右侧显示。
+ setDefaultAction(ui->actSelPopMenu)，设置按钮的关联Action，actSelPopMenu与actSelInvs有信号与槽的关联，所以，直接单击按钮会执行“反选”的功能。
+ setMenu(menuSelection)，为按钮设置下拉菜单对象。

工具栏上具有下拉菜单的按钮需要动态创建。先创建QToolButton对象aBtn，同样用以上4个函数进行设置，但是设置的参数稍微不同，特别是设置弹出菜单模式为：

```css
aBtn->setPopupMode(QToolButton::InstantPopup)
```

这种模式下，工具按钮的右下角显示一个小的箭头，单击按钮直接弹出下拉菜单，即使为这个按钮设置了关联的Action，也不会执行Action的功能。这是这两个具有下拉菜单的QToolButton按钮的区别。

setActionsForButton()和createSelectionPopMenu()函数在窗口的构造函数里调用，构造函数的完整代码如下：

```css
MainWindow::MainWindow(QWidget *parent) :  QMainWindow(parent),
   ui(new Ui::MainWindow)
{
   ui->setupUi(this);
   setCentralWidget(ui->splitter); 
   setActionsForButton();
   createSelectionPopMenu();
}
```

