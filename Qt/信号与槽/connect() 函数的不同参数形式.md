`QObject::connect()` 函数有多重参数形式，一种参数形式的函数原型是：

```cpp
QMetaObject::Connection QObject::connect(const QObject *sender, const char *signal, const QObject *receiver, const char *method, Qt::ConnectionType type = Qt::AutoConnection)
```

使用这种参数形式的 `connect()` 进行信号与槽函数的连接时，一般句法如下：

```cpp
connect(sender, SIGNAL(signal()), receiver, SLOT(slot()));
```

这里使用了宏 `SIGNAL()` 和 `SLOT()` 指定信号和槽函数，而且如果信号和槽函数带有参数，还需注明参数类型，如：

```cpp
connect(spinNum, SIGNAL(valueChanged(int)), this, SLOT(updateStatus(int)));
```

另外一种参数形式的 `connect()` 函数的原型是：

```cpp
QMetaObject::Connection QObject::connect(const QObject *sender,  const QMetaMethod &signal, const QObject *receiver, const QMetaMethod &method, Qt::ConnectionType type = Qt::AutoConnection)
```

对于具有默认参数的信号与槽（即信号名称是唯一的，没有参数不同而同名的两个信号），可以使用这种函数指针形式进行关联，如：

```cpp
connect(lineEdit, &QLineEdit::textChanged, this, &widget::on_textChanged);
```

`QLineEdit` 只有一个信号 `textChanged(QString)`，在自定义窗体类 widget 里定义一个槽函数 `on_textChanged(QString)`，就可以用上面的语句将此信号与槽关联起来。

而对于具有不同参数的同名信号就不能采用函数指针的方式进行信号与槽的关联，例如 `QSpinBox` 有两个 `valueChanged()` 信号，分别是：

```cpp
void QSpinBox::valueChanged(int i);
void QSpinBox::valueChanged(const QString &text);
```

即使在自定义窗体 widget 里定义了一个槽函数，如：

```cpp
void onValueChanged(int i);
```

不管是哪种参数形式的 `connect()` 函数，最后都有一个参数 `Qt::ConnectionType type`，缺省值为 `Qt::AutoConnection`。枚举类型 `Qt::ConnectionType` 表示了信号与槽之间的关联方式，有以下几种取值：

+ `Qt::AutoConnection`（缺省值）：如果信号的接收者与发射者在同一个线程，就使用 `Qt::DirectConnection` 方式；否则使用 `Qt::QueuedConnection` 方式，在信号发射时自动确定关联方式。

+ `Qt::DirectConnection`：信号被发射时槽函数立即执行，槽函数与信号在同一个线程。

+ `Qt::QueuedConnection`：在事件循环回到接收者线程后执行槽函数，槽函数与信号在不同的线程。

+ `Qt::BlockingQueuedConnection`：与 `Qt::QueuedConnection` 相似，只是信号线程会阻塞直到槽函数执行完毕。当信号与槽函数在同一个线程时绝对不能使用这种方式，否则会造成死锁。

  