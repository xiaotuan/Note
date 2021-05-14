**需求介绍：**

我想做一个脚本，该脚本一次性将 Android apk 通过 apktool 工具进行反编译，同时使用 dex2jar 工具将 dex 文件方便成 jar。但是 apk 的 dex 文件是在 apk 文件中的，apk 文件其实是一个 zip 压缩包，因此需要先将 dex 文件解压缩出来，然后再使用 dex2jar 工具将其反编译成 jar 文件。

