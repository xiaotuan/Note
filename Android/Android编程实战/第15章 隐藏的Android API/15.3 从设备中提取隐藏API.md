要做到编译时链接隐藏 API，开发者首先要提取和处理设备中的库文件。既可以从模拟器提取库文件，也可以从设备中提取这些文件，因为它们只是用来编译代码。由于这个过程需要提取出大量文件，建议单独创建一个空的工作目录。另外可能要提取多个版本的库文件，所以开发者还应为每个 API 级别创建一个工作目录。

```shell
$ adb pull /system/framework .
pull: building file list ...
pull: <files pulled from device>
63 files pulled. 0 files skipped.
4084 KB/s (35028810 bytes in 8.374s)
```

一旦知道需要转换的文件，就可以下载 Smail 的工具了，它能把优化后的 DEX 文件（.odex）转换为中间格式（.smali）。接下来使用 dex2Jar 工具再把这种中间格式转换回 `Java` 类文件。可在 <https://code.google.com/p/smali/> 下载 Smail，更多 dex2Jar 的内容请访问 <https://code.google.com/p/dex2jar>。下载并把它们解压缩到一个适当的位置。下面展示了如何把 ODEX 文件转化成中间格式：

```shell
$ mkdir android-apis-17
$ java -jar ~/Downloads/baksmali-2.0b5.jar -a 17 -x framework.odex -d . -o android-apis-17
```

在工作目录中运行上面的命令会把 framework.odex 文件转换成许多 SMALI 文件，这些文件会按包结构放在 android-apis-17 目录内。接下来，需要将这些文件转换成一个单独的 DEX 文件。

```shell
$ java -jar ~/Downloads/smali-2.0b5.jar -a 17 -o android-apis-17.dex android-apis-17
```

最后，需要使用 dex2Jar 工具把 DEX 文件转成包含所有 Java 类的 JAR 文件。

```shell
$ ~/Downloads/dex2jar-0.0.9.15/d2j-dex2jar.sh android-apis-17.dex
dex2jar android-apis-17.dex -> android-apis-17-dex2jar.jar
```

从原来的 ODEX 文件开始，最终的 JAR 文件包含了所有的类，既有隐藏的类也有公共的类。要在 SDK 中使用新生成的 JAR 文件，只需要把它重命名为 android.jar，并替换原有的文件即可。

**修改 SDK 的错误处理**

有几种方法可以处理这种情况。可以结合使用反射来检测是否存在隐藏 API。推荐使用这种方式因为它结合了两种方法的优点。另一种方法是简单地捕获异常，放止应用程序崩溃。