下面以 Android 7.0 的根目录结构进行说明：

| Android 源码根目录 | 描述                                                    |
| ------------------ | ------------------------------------------------------- |
| abi                | 应用程序二进制接口                                      |
| art                | 全新的 ART 运行环境                                     |
| bionic             | 系统 C 库                                               |
| bootable           | 启动引导相关代码                                        |
| build              | 存放系统编译规则及 generic 等基础开发包配置             |
| cts                | Android 兼容性测试套件标准                              |
| dalvik             | Dalvik 虚拟机                                           |
| developers         | 开发者目录                                              |
| development        | 应用程序开发相关                                        |
| device             | 设备相关配置                                            |
| docs               | 参考文档目录                                            |
| external           | 开源模组相关文件                                        |
| frameworks         | 应用程序框架，Android 系统核心部分，由 Java 和 C++ 编写 |
| hardware           | 主要是硬件抽象层的代码                                  |
| libcore            | 核心库相关文件                                          |
| libnativehelper    | 动态库，实现 JNI 库的基础                               |
| ndk                | NDK 相关代码，帮助开发人员在应用程序中嵌入 C/C++ 代码   |
| out                | 编译完成后的代码输出在此目录                            |
| pdk                | Plug Development Kit 的缩写，本地开发套件               |
| platform_testing   | 平台测试                                                |
| prebuilts          | x86 和 arm 架构下预编译的一些资源                       |
| sdk                | SDK 和模拟器                                            |
| packages           | 应用程序包                                              |
| system             | 底层文件系统库、应用和组件                              |
| toolchain          | 工具链文件                                              |
| tools              | 工具文件                                                |
| Makefile           | 全局 Makefile 文件，用来定义编译规则                    |

<center><b>packages 目录</b></center>

| packages 目录 | 描述           |
| ------------- | -------------- |
| apps          | 核心应用程序   |
| experimental  | 第三方应用程序 |
| inputmethods  | 输入法目录     |
| providers     | 内容提供者目录 |
| screensavers  | 屏幕保护       |
| services      | 通信服务       |
| wallpapers    | 墙纸           |

<center><b>/frameworks/base 目录</b></center>

| /frameworks/base 目录 | 描述           | /frameworks/base 目录 | 描述                         |
| --------------------- | -------------- | --------------------- | ---------------------------- |
| api                   | 定义API        | cmds                  | 重要命令：am、app...proce 等 |
| core                  | 核心库         | data                  | 字体和声音等数据文件         |
| docs                  | 文档           | graphics              | 图形图像相关                 |
| include               | 头文件         | keystore              | 和数据签名证书相关           |
| libs                  | 库             | location              | 地理位置相关库               |
| media                 | 多媒体相关库   | native                | 本地库                       |
| nfc-extras            | NFC 相关       | obex                  | 蓝牙传输                     |
| opengl                | 2D/3D 图形 API | packages              | 设置、TTS、VPN程序           |
| sax                   | XML 解析器     | services              | 系统服务                     |
| telephony             | 电话通信管理   | test-runner           | 测试工具相关                 |
| tests                 | 测试相关       | tools                 | 工具                         |
| wifi                  | Wi-Fi 无线网络 |                       |                              |

<center><b>C/C++ 程序库部分</b></center>

| 目录位置                                   | 描述                                             |
| ------------------------------------------ | ------------------------------------------------ |
| bionic/                                    | Google 开发的系统 C 库，以 BSD 许可形式开源      |
| /frameworks/av/media                       | 系统媒体库                                       |
| /frameworks/native/opengl                  | 第三方图形渲染库                                 |
| /frameworks/native/services/surfaceflinger | 图形显示库，主要负责图形的渲染、叠加和绘制等功能 |
| external/sqlite                            | 轻型关系数据库 SQLite 的 C++ 实现                |

 