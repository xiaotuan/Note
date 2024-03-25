使用 `qDebug()` 打印日志需要导入 `#include <qDebug>` 头文件，具体使用方法如下：

```cpp
#include <QCoreApplication>
#include <QtGlobal>
#include <QDebug>

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    QByteArray bal("Hello");
    if ('\0' == bal[5])
        printf("bal[5]=\'\\0\'\n");

    QByteArray ba;
    ba.resize(6);
    ba[0] = 0x3c;
    ba[1] = 0xb8;
    ba[2] = 0x64;
    ba[3] = 0x18;
    ba[4] = 0xca;
    ba.data()[5] = 0x31;
    qDebug() << "[]" << ba[2];  // [] d
    qDebug() << "at() " << ba.at(2);    // at() d
    qDebug() << "data() " << ba.data()[2];  // data() d
    qDebug() << "constData() " << ba.constData()[2];    // constData() d
    qDebug() << "constData() " << ba.constData()[5];    // constData() 1

    return a.exec();
}
```

