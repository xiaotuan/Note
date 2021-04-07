### 3.1.3　Linux

和前面提及的两个操作系统一样，如果你想按照本书操作，那么Vagrant就是最为推荐的方式。

由于在很多场景下，你需要在Linux服务器中安装Scrapy，因此更详尽的指引可能会很有用。

> <img class="my_markdown" src="../images/2.png" style="width:69px;  height: 87px; " width="8%"/>
> 确切的依赖条件经常会发生变更。本书编写时，我们安装的Scrapy版本是1.0.3，下面的内容是针对不同主流系统的操作指南。

#### 1．Ubuntu或Debian Linux

为了在Ubuntu（使用Ubuntu 14.04 Trust Tahr 64位版本测试）或其他使用 `apt` 的发布版本中安装Scrapy，需要执行如下3个命令。

```python
$ sudo apt-get update
$ sudo apt-get install python-pip python-lxml python-crypto python-
cssselect python-openssl python-w3lib python-twisted python-dev libxml2-
dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
$ sudo pip install scrapy

```

上述过程需要一些编译工作，而且可能会被不时打断，不过它将会为你安装PyPI源上最新版本的Scrapy。如果你想避免某些编译工作，并且能够忍受使用稍微过时一些的版本的话，可以通过Google搜索“install Scrapy Ubuntu packages”，并跟随Scrapy官方文档的指引进行操作。

#### 2．Red Hat或CentOS Linux

在Red Hat或其他使用 `yum` 的发布版本中安装Scrapy相对来说比较容易。你只需按照如下3行操作即可。

```python
sudo yum update
sudo yum -y install libxslt-devel pyOpenSSL python-lxml python-devel gcc
sudo easy_install scrapy

```

