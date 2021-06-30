[toc]

### 1. 安装 Git

```shell
sudo apt-get install git
```

### 2. 配置 Git 参数

```shell
git config --global user.name 用户名
git config --global user.email 用户邮箱
ssh-keygen -t rsa -C 用户邮箱	# 这步不是必须的
```

### 3. 安装 Python 2.x

首先确认系统是否已经存在 Python 2.x 版本，如果不存在可以通过如下命令安装 python 2.x：

```shell
sudo apt-get install python2.7
```

如果存在的话，它应该在 `/usr/bin/` 目录下。如果在 `/usr/bin/` 目录下有多个 Python 版本，则需要确认 Python 命令是否是 Python 2.x 版本，可以通过如下命令查看：

```shell
$ python
soft-server@softserver-PowerEdge-R730:~/workspace/work4/wunanshi/code$ python
Python 2.7.12 (default, Mar  1 2021, 11:38:31) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

如果当前的 python 命令不是 Python 2.x 版本，可以通过如下命令将 python 命令切换成 Python 2.x 版本：

```shell
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2 200
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 100
```

或者

```shell
sudo update-alternative --config java
```

### 4. 安装 OpenJDK-8

```shell
sudo apt-get install openjdk-8-jdk
```

如果电脑中存在多个 Java 版本，则通过如下命令选择 openjdk-8 即可：

```shell
sudo update-alternative --config java
sudo update-alternative --config javac
```

### 5. 配置 Java 环境变量

使用如下命令打开 `~/.bashrc` 文件，在文件末尾添加如下代码：

```
export JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
export PATH=.:$JAVA_HOME/bin:$PATH
```

### 6. 安装 GCC

```shell
sudo apt-get install gcc
```

### 7. 安装 make

```shell
sudo apt-get install make
```

### 8. 安装依赖库

```shell
sudo apt-get install libx11-dev:i386 libreadline6-dev:i386 libgl1-mesa-dev g++-multilib
sudo apt-get install -y git flex bison gperf build-essential libncurses5-dev:i386
sudo apt-get install tofrodos python-markdown libxml2-utils xsltproc zlib1g-dev:i386
sudo apt-get install dpkg-dev libsdl1.2-dev libesd0-dev
sudo apt-get install git-core gnupg flex bison gperf build-essential
sudo apt-get install zip curl zlib1g-dev gcc-multilib g++-multilib
sudo apt-get install libc6-dev-i386
sudo apt-get install lib32ncurses5 x11proto-core-dev libx11-dev
sudo apt-get install libgl1-mesa-dev libxml2-utils xsltproc unzip m4
sudo apt-get install lib32z-dev ccache
sudo apt-get install libssl-dev
```

> 注意：在安装 `libesd0-dev` 库时可能会报错，如果报错，可以参照如下方法解决：
>
> 在 `/etc/apt/source.list` 文件末尾添加如下内容：
>
> ```
> deb http://us.archive.ubuntu.com/ubuntu/ xenial main universe
> deb-src http://us.archive.ubuntu.com/ubuntu/ xenial main universe
> ```
>
> 然后执行如下命令安装 `libesd0-dev`：
>
> ```shell
> sudo apt-get update && sudo apt-get install libesd0-dev
> ```

