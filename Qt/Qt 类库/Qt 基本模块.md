> 提示：Qt 官方模块文档网址：https://doc.qt.io/qt-5.15/qtmodules.html。

Qt 基本模块是 Q 在所有平台上的基本功能，它们在所有的开发平台和目标平台上都可用，在 Qt 5 所有版本上是源代码和二进制兼容的。这些具体的基本模块如下所示：

<center class="my_markdown"><b class="my_markdown">Qt基本模块</b></center>

| 模块                  | 描述                                             |
| :-------------------- | :----------------------------------------------- |
| Qt Core               | 其他模块都用到的核心非图形类                     |
| Qt GUI                | 设计GUI界面的基础类，包括OpenGL                  |
| Qt Multimedia         | 音频、视频、摄像头和广播功能的类                 |
| Qt Multimedia Widgets | 实现多媒体功能的界面组件类                       |
| Qt Network            | 使网络编程更简单和轻便的类                       |
| Qt QML                | 用于QML和JavaScript语言的类                      |
| Qt Quick              | 用于构建具有定制用户界面的动态应用程序的声明框架 |
| Qt Quick Controls     | 创建桌面样式用户界面，基于Qt Quick的用户界面控件 |
| Qt Quick Dialogs      | 用于Qt Quick的系统对话框类型                     |
| Qt Quick Layouts      | 用于Qt Quick 2界面元素的布局项                   |
| Qt SQL                | 使用SQL用于数据库操作的类                        |
| Qt Test               | 用于应用程序和库进行单元测试的类                 |
| Qt Widgets            | 用于构建GUI界面的C++图形组件类                   |

Qt Core模块是Qt类库的核心，所有其他模块都依赖于此模块，如果使用qmake构建项目，则Qt Core模块是自动被加入项目的。

Qt GUI模块提供了用于开发GUI应用程序的必要的类，使用qmake构建应用程序时，Qt GUI模块是自动被加入项目的。如果项目中不使用GUI功能，则需要在项目配置文件中加入如下的一行：

```css
QT -= gui
```

其他的模块一般不会被自动加入到项目，如果需要在项目中使用某个模块，则可以在项目配置中添加此模块。例如，如果需要在项目中使用Qt Multimedia和Qt Multimedia Widgets模块，需要在项目配置文件中加入如下的语句：

```css
QT += multimedia multimediawidgets
```

需要在项目中使用Qt SQL模块，就在项目配置文件中加入如下的语句：

```css
QT += sql
```

