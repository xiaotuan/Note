可以从这个地址下载 `Node` 源代码及安装包：<https://nodejs.org/download/release/>。 `Wiki` 关于多种环境中安装 `Node` 的说明：<https://github.com/nodejs/node/blob/master/BUILDING.md>。

在 `Linux` 下安装 `Node` 之前，需要确认是否安装 `Python`，如果计划使用 SSL/TLS (Secure Sockets Layer) 还需要安装 libssl-dev。

对于 Ubuntu 和 Debian 系统，还需要安装需要的库：

```console
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential openssl libssl-dev pkg-config
```

下载 `Node` 源代码包，并编译安装 `Node`：

```console
wget http://nodejs.org/dist/v0.8.2/node-v0.8.2.tar.gz
tar -zxf node-v0.8.2.tar.gz
./configure
make
sudo make insell
```

如果需要指定安装目录可以通过如下命令安装 `Node`：

```console
mkdir ~/working
./configure --prefix=~/working
make
make install
echo 'export PATH=~/working/bin:${PATH}' >> ~/.bashrc
. ~/.bashrc
```
