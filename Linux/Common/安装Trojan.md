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

#### trojan-quickstart.sh

```sh
#!/bin/bash
set -euo pipefail

function prompt() {
    while true; do
        read -p "$1 [y/N] " yn
        case $yn in
            [Yy] ) return 0;;
            [Nn]|"" ) return 1;;
        esac
    done
}

if [[ $(id -u) != 0 ]]; then
    echo Please run this script as root.
    exit 1
fi

if [[ $(uname -m 2> /dev/null) != x86_64 ]]; then
    echo Please run this script on x86_64 machine.
    exit 1
fi

NAME=trojan
VERSION=$(curl -fsSL https://api.github.com/repos/trojan-gfw/trojan/releases/latest | grep tag_name | sed -E 's/.*"v(.*)".*/\1/')
TARBALL="$NAME-$VERSION-linux-amd64.tar.xz"
DOWNLOADURL="https://github.com/trojan-gfw/$NAME/releases/download/v$VERSION/$TARBALL"
TMPDIR="$(mktemp -d)"
INSTALLPREFIX=/usr/local
SYSTEMDPREFIX=/etc/systemd/system

BINARYPATH="$INSTALLPREFIX/bin/$NAME"
CONFIGPATH="$INSTALLPREFIX/etc/$NAME/config.json"
SYSTEMDPATH="$SYSTEMDPREFIX/$NAME.service"

echo Entering temp directory $TMPDIR...
cd "$TMPDIR"

echo Downloading $NAME $VERSION...
curl -LO --progress-bar "$DOWNLOADURL" || wget -q --show-progress "$DOWNLOADURL"

echo Unpacking $NAME $VERSION...
tar xf "$TARBALL"
cd "$NAME"

echo Installing $NAME $VERSION to $BINARYPATH...
install -Dm755 "$NAME" "$BINARYPATH"

echo Installing $NAME server config to $CONFIGPATH...
if ! [[ -f "$CONFIGPATH" ]] || prompt "The server config already exists in $CONFIGPATH, overwrite?"; then
    install -Dm644 examples/server.json-example "$CONFIGPATH"
else
    echo Skipping installing $NAME server config...
fi

if [[ -d "$SYSTEMDPREFIX" ]]; then
    echo Installing $NAME systemd service to $SYSTEMDPATH...
    if ! [[ -f "$SYSTEMDPATH" ]] || prompt "The systemd service already exists in $SYSTEMDPATH, overwrite?"; then
        cat > "$SYSTEMDPATH" << EOF
[Unit]
Description=$NAME
Documentation=https://trojan-gfw.github.io/$NAME/config https://trojan-gfw.github.io/$NAME/
After=network.target network-online.target nss-lookup.target mysql.service mariadb.service mysqld.service

[Service]
Type=simple
StandardError=journal
ExecStart="$BINARYPATH" "$CONFIGPATH"
ExecReload=/bin/kill -HUP \$MAINPID
LimitNOFILE=51200
Restart=on-failure
RestartSec=1s

[Install]
WantedBy=multi-user.target
EOF

        echo Reloading systemd daemon...
        systemctl daemon-reload
    else
        echo Skipping installing $NAME systemd service...
    fi
fi

echo Deleting temp directory $TMPDIR...
rm -rf "$TMPDIR"

echo Done!
```

