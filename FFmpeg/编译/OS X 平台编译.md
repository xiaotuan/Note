在 `OS X` 平台上编译 `FFmpeg` 之前，首先需要安装所需要的编译环境，在 `OS X` 平台上使用的编译工具链为 `LLVM`：

```shell
Configured with: --prefix=/Applications/Xcode.app/Contents/Developer/usr --with-gxx-include-dir=/usr/include/c++/4.2.1
Apple LLVM version 8.1.0 (clang-802.0.42)
Target: x86_64-apple-darwin16.6.0
Thread model: posix
InstalledDir:
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin
```

另外，还需要安装 `yasm` 汇编编译工具，否则在生成 `Makefile` 时会报错提示未安装 `yasm` 工具。

在 `LLVM` 下利用源码安装 `FFmpeg` 与其他平台基本相同，尤其是与 `Linux` 相同。

下面是编译步骤：

（1）进入 `FFmpeg` 源码目录，执行 `./configure`

（2）`configure` 成功后执行 `make`

（3）最后执行 `sudo make install` 命令安装 `ffmpeg`