使用代码创建 QVBoxLayout 控件的代码如下所示：

```cpp
QHBoxLayout *HLay1 = new QHBoxLayout;
QHBoxLayout *HLay2 = new QHBoxLayout;
QHBoxLayout *HLay3 = new QHBoxLayout;
// 创建文本框，并设置初始字体
txtEdit = new QPlainTextEdit;
txtEdit->setPlainText("Hello world\n\nIt is my demo");
QFont font = txtEdit->font();   // 获取字体
font.setPointSize(20);  // 修改字体大小
txtEdit->setFont(font); // 设置字体
// 创建垂直布局，并设置为主布局
QVBoxLayout *VLay = new QVBoxLayout;
VLay->addLayout(HLay1); // 添加字体类型组
VLay->addLayout(HLay2); // 添加字体颜色组
VLay->addWidget(txtEdit);   // 添加 PlainTextEdit
VLay->addLayout(HLay3); // 添加按键组
```

