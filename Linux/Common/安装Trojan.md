<center><font size="5"><b>安装Trojan</b></font></center>

> 摘自：<https://github.com/trojan-gfw/trojan/wiki/Binary-&-Package-Distributions>

## Linux

### Quickstart Script

```
sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/trojan-gfw/trojan-quickstart/master/trojan-quickstart.sh)"
```

or

```
sudo bash -c "$(wget -O- https://raw.githubusercontent.com/trojan-gfw/trojan-quickstart/master/trojan-quickstart.sh)"
```

> trojan安装的相关环境路径：
>
> + 可执行文件:  /usr/local/bin/trojan
> + 配置文件：/usr/local/etc/trojan/config.json
> + 系统服务：/etc/systemd/system/trojan.service

### AOSC OS

```
sudo apt-get install trojan
```

### Arch Linux

```
sudo pacman -S trojan
```

#### AUR

```
$(AURHelper) -S trojan-git
```

### Debian

#### 10

```
sudo apt install trojan
```

#### <= 9

```
TROJAN_DEBIAN_VERSION="1.10.0-3"

sudo apt update
sudo apt install build-essential devscripts debhelper cmake libboost-system-dev libboost-program-options-dev libssl-dev default-libmysqlclient-dev python3 curl openssl
dget http://ftp.us.debian.org/debian/pool/main/t/trojan/trojan_${TROJAN_DEBIAN_VERSION}.dsc
dpkg-source -x trojan_${TROJAN_DEBIAN_VERSION}.dsc trojan-${TROJAN_DEBIAN_VERSION}
cd trojan-${TROJAN_DEBIAN_VERSION}/
dpkg-buildpackage -us -uc -d
sudo dpkg -i ../trojan_${TROJAN_DEBIAN_VERSION}_$(dpkg-architecture -q DEB_BUILD_ARCH).deb
sudo apt purge devscripts debhelper cmake # you can remove it now
```

### Gentoo

```
sudo emerge --sync
sudo emerge -av trojan
```

### Ubuntu

**Not for Debian**

#### 18.10 & 19.04

```
sudo add-apt-repository ppa:greaterfire/trojan
sudo apt-get update
sudo apt-get install trojan
```

#### >= 19.04

```
sudo apt-get install trojan
```

### Pre-compiled binary

https://github.com/trojan-gfw/trojan/releases/latest

## Chrome OS

There are two ways:

1. Use [crouton](https://github.com/dnschneid/crouton) to install a linux chroot environment, and install trojan just like in a normal linux.

2. Enable Google's

    

   ```
   Linux (beta)
   ```

    

   in the settings, and run the following commands in the terminal:

   ```
   sudo -i
   apt update
   apt -y install git g++ cmake libboost-system-dev libboost-program-options-dev libssl-dev default-libmysqlclient-dev
   git clone https://github.com/trojan-gfw/trojan.git
   cd trojan/
   cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -DSYSTEMD_SERVICE=ON .
   make install
   ```

   or you can upgrade it to Debian Buster:

   ```
   sudo -i
   apt update && apt dist-upgrade
   cp /etc/apt/sources.list /etc/apt/sources.list.bak
   sed  -i 's/stretch/buster/g' /etc/apt/sources.list
   apt update && apt dist-upgrade
   apt install trojan
   ```

**Note: The IP address of the SOCKS5 proxy is not `127.0.0.1`, check it by running `ifconfig` or `ip addr`.**

## Windows (>=Vista)

https://github.com/trojan-gfw/trojan/releases/latest

Download and install [vc_redist.x64.exe](https://aka.ms/vs/16/release/vc_redist.x64.exe) before running the Windows binary.

## macOS

Install [homebrew](https://brew.sh/) and run commands

```
brew tap trojan-gfw/homebrew-trojan
brew install trojan
```

Use `brew services` to launch at login.

Alternatively, download the [binary release](https://github.com/trojan-gfw/trojan/releases/latest)