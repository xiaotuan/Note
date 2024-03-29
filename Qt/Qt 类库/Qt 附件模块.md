Qt附加模块可以实现一些特定目的。这些模块可能只在某些开发平台上有，或只能用于某些操作系统，或只是为了向后兼容。用户安装时可以选择性地安装这些附加模块。

表3-7是附加模块列表（未列出一些过时的模块，以及专门用于QML或Qt Quick的模块）。

<center class="my_markdown"><b class="my_markdown">表3-7　Qt附加模块</b></center>

| 模块                                                  | 描述                                                         |
| :---------------------------------------------------- | :----------------------------------------------------------- |
| Active Qt                                             | 用于开发使用ActiveX和COM的Windows应用程序                    |
| Qt 3D                                                 | 支持2D和3D渲染，提供用于开发近实时仿真系统的功能             |
| Qt Android Extras                                     | 提供Android平台相关的API                                     |
| Qt Bluetooth                                          | 提供访问蓝牙硬件的功能                                       |
| Qt Concurrent                                         | 提供一些类，无需使用底层的线程控制就可以编写多线程程序       |
| Qt D-Bus                                              | 使进程间通过D-Bus协议通信的一些类                            |
| Qt Gamepad                                            | 使Qt应用程序支持游戏手柄硬件的使用                           |
| Qt Image Formats                                      | 支持附加图片格式的插件，包括TIFF、MNG、TGA、WBMP             |
| Qt Mac Extras                                         | 提供macOS平台相关的API                                       |
| Qt NFC                                                | 提供访问NFC（近场通信）硬件的功能                            |
| Qt Positioning                                        | 提供一些类，用于通过GPS卫星、WiFi等定位                      |
| Qt Print Support                                      | 提供一些用于打印控制的类                                     |
| Qt Purchasing                                         | 提供一些类，在Qt应用程序内实现应用内购买的功能               |
| Qt Sensors                                            | 提供访问传感器硬件的功能，以识别运动和手势                   |
| Qt Serial Bus                                         | 访问串行工业总线的功能，目前只支持CAN和Modbus协议            |
| Qt SVG                                                | 提供显示SVG图片文件的类                                      |
| Qt WebChannel                                         | 用于实现服务器端（QML或C++应用程序）与客户端（HTML/ JavaScript或QML应用程序）之间的P2P通信 |
| Qt WebEngine                                          | 提供类和函数，实现在应用程序中嵌入网页内容                   |
| Qt WebSockets                                         | 提供兼容于RFC 6455的WebSocket通信，WebSocket是实现客户端程序与远端主机进行双向通信的基于Web的协议 |
| Qt Windows Extras                                     | 提供Windows平台相关的API                                     |
| Qt XML                                                | 该模块不再维护了，应使用Qt Core中的QXmlStreamReader 和 QXmlStreamWriter |
| Qt XML Patterns                                       | 提供对XPath、XQuery、XSLT 和 XML 等的支持                    |
| Qt Charts<sup class="my_markdown">①</sup>             | 用于数据显示的二维图表组件                                   |
| Qt Data Visualization<sup class="my_markdown">①</sup> | 用于3D数据可视化显示的界面组件                               |
| Qt Virtual Keyboard<sup class="my_markdown">①</sup>   | 实现不同输入法的虚拟键盘框架                                 |

下面的附加模块只在商业许可，或GPLv3许可的版本里才有。

