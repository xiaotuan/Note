在槽函数里，使用 `QObject::sender()` 可以获取信号发射者的指针。如果知道信号发射者的类型，可以通过 指针投射为确定的类型，然后使用这个确定类的接口函数。例如：

```cpp
QSpinBox *spinBox = qobject_cast<QSpinBox *>(sender());
```

