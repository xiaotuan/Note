[toc]

### 1.1　安装 Node

要安装 Node，最好从 Node.js 的下载页面开始。在这里你可以下载到适用于 Windows、OS X、Sun OS、Linux 以及 ARM 等平台的二进制文件（预编译的可执行文件）。这个页面也提供了个别平台的安装文件，这些安装文件可以大幅简化安装过程——特别是 Windows 版。如果你本地有编译环境，也可以下载源代码，然后直接编译 Node。在我的 Ubuntu 服务器上，我就是这么做的。

你也可以使用平台对应的安装文件来安装 Node，这样不仅方便安装，也方便更新（我们会在1.4节中深入讨论）。

如果你准备直接在本地环境中编译 Node，那么必须先设置好本地的编译环境，并且安装合适的编译工具。比如在 Ubuntu（Linux）上，就需要运行下面这条命令来安装所需的工具：

```python
apt-get install make g++ libssl-dev git
```

在不同的平台上，第一次安装 Node 的过程会略有差异。比如，在 Windows 上安装 Node 时，安装文件不仅会安装 Node，同时也会在本地创建一个用来运行 Node 的命令窗口。这是因为 Node 是一个命令行程序，不像典型的 Windows 程序那样拥有一个图形界面。要想在 Arduino Uno 上面用 Node 来编程，那你就需要安装 Node 和 Johnny-Five，然后将二者结合起来对所连接的设备进行编程。

> <img class="my_markdown" src="../images/10.png" style="zoom:50%;" />
> **接受 Windows 世界中的默认设置**
> 在 Windows 上安装 Node 时，最好接受默认安装路径和安装功能的设置。因为安装文件会将 Node 加入到 PATH 环境变量中，之后就可以直接输入 node 来运行 Node，而不用输入整个安装路径。

在树莓派中安装 Node 时，需要下载对应的 ARM 版本，比如原版树莓派需要下载 ARMv6，新版树莓派2需要下载 ARMv7。下载好之后，从压缩包中将二进制文件解压出来，放在 `/usr/local` 目录下：

```python
wget https://nodejs.org/dist/v4.0.0/node-v4.0.0-linux-armv7l.tar.gz
tar -xvf node-v4.0.0-linux-armv7l.tar.gz
cd node-v4.0.0-linux-armv7l
sudo cp -R * /usr/local/
```

你也可以在本地搭建编译环境，然后直接编译 Node。

> <img class="my_markdown" src="../images/11.png" style="zoom:50%;" />
> **新的 Node 环境**
> 既然说到了 Arduino 和树莓派，我会在第12章介绍在一些非传统环境（如物联网）中的 Node 的使用。

