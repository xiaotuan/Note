使用代码创建 QHBoxLayout 控件的代码如下所示：

```cpp
// 创建确定，取消，退出 3 个 PushButton，并水平布局
btnOk = new QPushButton(tr("确定"));
btnCancel = new QPushButton(tr("取消"));
btnClose = new QPushButton(tr("退出"));
QHBoxLayout *HLay3 = new QHBoxLayout;
HLay3->addStretch();	// 添加弹性间隔
HLay3->addWidget(btnOk);
HLay3->addWidget(btnCancel);
HLay3->addStretch();
HLay3->addWidget(btnClose);
```

