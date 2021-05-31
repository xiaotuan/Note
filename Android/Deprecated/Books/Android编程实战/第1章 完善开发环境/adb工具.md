在终端（Linux 或者 Mac OS X）或者命令提示符（Windows）键入 `adb help all`，就会列出所有可用的命令。

一些常用的 `adb` 命令如下：
+ `adb devices`，列出所有连接的 Android 设备和虚拟机；
+ `adb push <local> <remote>`，将电脑上的文件复制到设备（通常存到 SD 卡）；
+ `adb pull <remote> <local>`，将设备上的文件复制到电脑。

**1. adb 和多设备**

如果要在两台或者多台设备上同时开发和调试应用，比如多人游戏或者即时通信应用，需要将 `-s <serial number>` 作为 `adb` 的第一个参数来识别开发者想要的设备。`adb devices` 命令会列出已连接设备的序列号。下面的示例可在特定设备上运行 `logcat` 命令：

```shell
$ adb devices
List of devices attached
0070015947d30e4b    device
015d2856b8300a10    device

$ adb -s 015d2856b8300a10 logcat
```

**2. 掌握 logcat 过虑**

Android 日志消息前面会有一个标签和优先级。通常，开发者可以像下面这样为应用程序的每一个类定义一个单独的日志标签：

```java
private static final String TAG = "MyActivity";
```

接下来就可在类代码中用上面定义的标签类打印日志消息：

```java
Log.d(TAG, "Current value of moderation: " + moderation);
```

下面的命令只会打印以 MyActivity 为标签的日志消息：

```shell
$ adb logcat MyActivity:* *:S
```

`logcat` 后面的参数代表需要应用的过滤条件，他们被格式化为 `<tag>:<priority>`，其中星号（\*）表示任何可能的值。一件很容易被遗忘的重要事情是，开发者需要添加特殊的过虑 `*:S` 来过滤掉所有的消息。

如果使用过滤器查看 `logcat` 输出，建议加上 `AndroidRuntime:*` 参数，这样会显示 `Android` 系统相关的日志信息以及由平台引起的应用程序异常。

**3. 用 Wi-Fi 链接 adb**

要想通过 `Wi-Fi` 连接 `adb`，首先要像通常一样用 `USB` 线连接 `Android` 设备和电脑。同时，要确保电脑和设备连接的是同一个 `Wi-Fi`。接下来还要取得设备的 `IP` 地址，打开 `Setting -> Wi-Fi -> Advanced` （设置 -> Wi-Fi -> 高级）页面，列表底部会显示当前 `Wi-Fi` 的 `IP` 地址。

设置好以上步骤后，在终端运行如下命令：

```shell
$ adb devices
List of devices attached
0070015947d30e4b    device
$ adb tcpip 5555
$ adb connect 192.168.1.104
$ adb devices
List of devices attached
192.168.1.104:5555    device
```

`adb` 守护进程会一直保持 `TCP/IP` 模式，直到设备重新启动，或者运行了 `adb usb`，该命令会重启 `USB` 守护进程。

> 不是所有的设备都支持 `Wi-Fi` 连接。同样，`Wi-Fi` 连接下的通信性能会更糟，当需要部署更大的应用时可能会很麻烦。

**4. 在 Android 设备上执行命令**

运行一条特殊的 `adb` 命令可以在 `Android` 设备上启动标准的 `shell` ，然后就可以像其他 `Linux` 设备一样，执行命令操作了。

```shell
$ adb shell
```

当在 `Android` 设备上运行 `shell` 时， `am` 和 `pm` 命令会很有用，这两个命令和时间没关系。相反，开发者用它们跟应用程序（Application）和包管理器（Package Manager）交互，这在早期的开发以及测试环节会很有用。比如，在开发一个有外部 `Intent` 启动的 `Server` 时，可以用 `am` 命令手动发送该 `Intent`。

在命令行中输入如下命令，便可用 `Intent` 启动一个 `Server`：

```shell
$ adb shell am startserver -a <intent action>
```

除了能启动 `Service` 外，还可以启动 `Activity` 或者发送 `Intent` 广播。无参的 `adb shell am` 会列出所有可能的命令列表。

`pm` 命令更容易让开发者了解设备的相关细节。比如，下面的命令可列出所有已安装的包（也就是说，已安装的应用程序）：

```shell
$ adb shell pm list package
```

> 可在 http://developer.android.com/tools/help/adb.html 上找到 `adb` 命令列表以及他们的用法。