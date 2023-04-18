在 Linux 平台中，默认编译 `FFmpeg` 的时候，需要用到 `yasm/nasm` 汇编器对 `FFmpeg`中的汇编部分进行编译。如果不需要用到汇编部分的代码，则可以不安装 `yasm/nasm` 汇编器。如果没有安装 `yasm/nasm` ，则执行默认配置的时候，会提示错误：

```shell
$ ./configure 
nasm/yasm not found or too old. Use --disable-x86asm for a crippled build.

If you think configure made a mistake, make sure you are using the latest
version from Git.  If the latest version fails, report the problem to the
ffmpeg-user@ffmpeg.org mailing list or IRC #ffmpeg on irc.libera.chat.
Include the log file "ffbuild/config.log" produced by configure as this will help
solve the problem.
```

安装 `nasm` 命令如下：

```shell
sudo apt install nasm
```

安装 `yasm` 命令如下：

```shell
sudo apt install yasm
```

也可以根据以上的错误提示，可以使用 `--disable-x86asm` 来取消 `yasm` 编译配置，不过这么做的话就不会编译 `FFmpeg` 的汇编代码部分，相关的优化也会少一些。

下面是编译步骤：

（1）进入 `FFmpeg` 源码目录，执行 `./configure`

（2）`configure` 成功后执行 `make`

（3）最后执行 `sudo make install` 命令安装 `ffmpeg`