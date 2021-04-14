### 技巧65　在Docker内部运行Selenium测试

本书尚未深入讲解的Docker用例之一是运行图形化应用程序。在第3章中，在开发环境的“保存游戏”中VNC被用来连接容器（见技巧19），但这可能过于笨重了——窗口被包含在VNC Viewer窗口里面，并且桌面互动性可能比较有限。这里介绍一种替代方法，将演示如何使用Selenium来编写图形化测试。我们还会展示如何作为CI工作流的一部分使用这个镜像来运行测试。

#### 问题

想要在CI过程中运行图形化程序，同时能将这些图形化程序显示到自己的屏幕上。

#### 解决方案

共享X11服务器套接字以便在自己的屏幕上查看程序，同时在CI过程中使用xvfb。

不管启动容器需要做什么其他事情，都必须把X11用来显示窗口的Unix套接字作为一个卷挂载到容器里，同时需要指定窗口要显示到哪个显示器上。可以通过执行以下命令确认这两样东西在宿主机上是否被设置为其默认值：

```c
~ $ ls /tmp/.X11-unix/
X0
~ $ echo $DISPLAY
:0
```

第一个命令检查的是X11服务器Unix套接字正运行在本技巧后续内容所假定的位置上。第二个命令检查的是应用程序用于查找X11套接字的环境变量。如果执行这些命令的输出与这里的输出不一致，可能需要修改本技巧中的某些命令参数。

检查好机器设置，现在要把运行在一个容器内的应用程序无缝地显示在容器外。需要解决的主要问题是：计算机为了防止其他人连接该机器、接管显示器以及悄悄记录按键动作所实施的安全性。在技巧29中我们已经大致看到如何完成这一步，不过当时并未说明它的工作原理以及其替代方案。

X11具有多种对使用X套接字的容器进行认证的方式。先来看一下.Xauthority文件——它应该存在于用户的主目录中。它包含了主机名（hostname）以及每台主机连接时必须使用的“私密cookie”。通过赋予Docker容器与机器相同的主机名，并使用与容器外一致的用户名，就可以使用现有的X认证文件，如代码清单8-7所示。

代码清单8-7　启动启用Xauthority显示器的容器

```c
$ ls $HOME/.Xauthority
/home/myuser/.Xauthority
$ docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix \
    --hostname=$HOSTNAME -v $HOME/.Xauthority:$HOME/.Xauthority \
    -it -e EXTUSER=$USER ubuntu:16.04 bash -c 'useradd $USER && exec bash'
```

第二种允许Docker访问该套接字的方法是一个较为低级的工具，但它具有安全问题，因为它会禁用 X 带来的所有防护措施。如果无人能访问该电脑，那么这是一个可以接受的解决方案，不过应该优先尝试使用X认证文件。可以通过运行 `xhost -` ，在尝试代码清单8-8所示的步骤之后恢复安全性（不过这会把Docker容器阻挡在外）。

代码清单8-8　启动启用xhost显示器的容器

```c
$ xhost +
access control disabled, clients can connect from any host
$ docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix \
    -it ubuntu:16.04 bash
```

代码清单8-8的第一行禁用了对X的所有访问控制，而第二行将运行容器。值得注意的是无须设置主机名或挂载X套接字的任何部分。

一旦容器启动，接下来就要检查一下它是否工作正常。如果用的是.Xauthority方式，可以通过执行如下命令来进行这一步：

```c
root@myhost:/# apt-get update && apt-get install -y x11-apps
[...]
root@myhost:/# su - $EXTUSER -c "xeyes"
```

如果用的是xhost方式，则可以使用以下略微不同的命令，因为无须以特定用户来执行命令：

```c
root@ef351febcee4:/# apt-get update && apt-get install -y x11-apps
[...]
root@ef351febcee4:/# xeyes
```

这将启动检测X是否正常工作的一个经典的应用程序——xeyes。我们可以看到跟随鼠标在屏幕上移动的一双眼睛。需要注意的是，（与VNC不同）该应用程序是整合到桌面里的——如果多次启动xeyes，将看到多个窗口。

现在可以开始使用 Selenium 了。假如读者之前从未使用过它，它是一个能够实现浏览器动作自动化的工具，常常用于测试网站代码——它需要一个用于运行浏览器的图形显示器。尽管它最经常与Java一起使用，但为了获取更多互动性，这里将使用Python。

代码清单8-9首先安装Python、Firefox和Python包管理器，然后使用Python包管理器安装Selenium Python包。同时下载了Selenium用于控制Firefox的“驱动器”二进制文件。接着启动了一个Python交互式解释器（Read Eval Print Loop，REPL），并使用Selenium库创建了一个Firefox实例。

为简单起见，这里选择只覆盖xhost的方式——要使用Xauthority方式，你需要为用户创建一个主目录以便Firefox有地方可以保存其配置文件，如代码清单8-9所示。

代码清单8-9　安装Selenium必备项目并启动一个浏览器

```c
root@myhost:/# apt-get install -y python2.7 python-pip firefox wget
[...]
root@myhost:/# pip install selenium
Collecting selenium
[...]
Successfully installed selenium-3.5.0
root@myhost:/# url=https://github.com/mozilla/geckodriver/releases/download
➥ /v0.18.0/geckodriver-v0.18.0-linux64.tar.gz
root@myhost:/# wget -qO- $url | tar -C /usr/bin -zxf -
root@myhost:/# python
Python 2.7.6 (default, Mar 22 2014, 22:59:56)
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from selenium import webdriver
>>> b = webdriver.Firefox()
```

正如所看到的，Firefox浏览器已经启动并出现在屏幕上。

现在可以对Selenium进行尝试。下面是一个针对GitHub运行的示例会话——要理解这里的内容，需要对CSS选择器有一个基本的了解。值得注意的是，网站经常会变，因此要让这段特定的代码正确地工作，可能需要做一些修改：

```c
>>> b.get('https://github.com/search')
>>> searchselector = '#search_form input[type="text"]'
>>> searchbox = b.find_element_by_css_selector(searchselector)
>>> searchbox.send_keys('docker-in-practice')
>>> searchbox.submit()
>>> import time
>>> time.sleep(2) # wait for page JS to run
>>> usersxpath = '//nav//a[contains(text(), "Users")]'
>>> userslink = b.find_element_by_xpath(usersxpath)
>>> userslink.click()
>>> dlinkselector = '.user-list-info a'
>>> dlink = b.find_elements_by_css_selector(dlinkselector)[0]
>>> dlink.click()
>>> mlinkselector = '.meta-item a'
>>> mlink = b.find_element_by_css_selector(mlinkselector)
>>> mlink.click()
```

这里的细节并不重要，不过通过在命令间切换到Firefox还是能了解发生了什么——我们浏览了GitHub上的docker-in-practice组织，并点击了组织链接。主要的收获是，我们在容器里使用Python编写命令，并看到它们在运行于容器内部的Firefox窗口中生效，却显示在桌面上。

这对于调试用户编写的测试非常有用，但要如何使用同一个Docker镜像将它们整合到一个CI流水线里呢？一个CI服务器通常不需要图形显示器，因此无须挂载自己的X服务器套接字即可工作，但Firefox仍然需要运行在一个X服务器里。有一个很有用的工具应运而生，它的名字叫xvfb，它会伪装运行一个可供应用程序使用的X服务器。但它不需要显示器。

为了看一下这是如何工作的，现在来安装xvfb，提交这个容器，给它打上 `selenium` 标签，并创建一个测试脚本，如代码清单8-10所示。

代码清单8-10　创建一个Selenium测试脚本

```c
>>> exit()
root@myhost:/# apt-get install -y xvfb
[...]
root@myhost:/# exit
$ docker commit ef351febcee4 selenium
d1cbfbc76790cae5f4ae95805a8ca4fc4cd1353c72d7a90b90ccfb79de4f2f9b
$ cat > myscript.py << EOF
from selenium import webdriver
b = webdriver.Firefox()
print 'Visiting github'
b.get('https://github.com/search')
print 'Performing search'
searchselector = '#search_form input[type="text"]'
searchbox = b.find_element_by_css_selector(searchselector)
searchbox.send_keys('docker-in-practice')
searchbox.submit()
print 'Switching to user search'
import time
time.sleep(2) # wait for page JS to run
usersxpath = '//nav//a[contains(text(), "Users")]'
userslink = b.find_element_by_xpath(usersxpath)
userslink.click()
print 'Opening docker in practice user page'
dlinkselector = '.user-list-info a'
dlink = b.find_elements_by_css_selector(dlinkselector)[99]
dlink.click()
print 'Visiting docker in practice site'
mlinkselector = '.meta-item a'
mlink = b.find_element_by_css_selector(mlinkselector)
mlink.click()
print 'Done!'
EOF
```

注意 `dlink` 变量赋值语句的细微差异（索引位置为 `99` 而非 `0` ）。通过尝试获取包含文本“Docker in Practice”的第100个结果，将触发一个错误，这将导致Docker容器以非零状态退出，然后在CI流水线中触发故障。

马上来试试：

```c
$ docker run --rm -v $(pwd):/mnt selenium sh -c \
"xvfb-run -s '-screen 0 1024x768x24 -extension RANDR'\
python /mnt/myscript.py"
Visiting github
Performing search
Switching to user search
Opening docker in practice user page
Traceback (most recent call last):
  File "myscript.py", line 15, in <module>
      dlink = b.find_elements_by_css_selector(dlinkselector)[99]
      IndexError: list index out of range
$ echo $?
1
```

上面运行了一个自我删除的容器，它将执行这个运行在虚拟X服务器之下的Python测试脚本。和预期一样，它失败了，并返回一个非零的退出码。



**注意**

`sh -c`  "命令字符串"是Docker对 `CMD` 值的默认处理方式的一个不良后果。如果通过Dockerfile来构建这个镜像，就可以删除 `sh -c` 而将 `xvfb-run-s '-screen 0 1024x768x24-extension RANDR'` 作为入口点，这样就可以作为镜像参数传递测试命令了。



#### 讨论

Docker是一个灵活的工具，可以实现一些乍看起来很神奇的用途（如这里的图形化应用）。有人在Docker内部运行 **所有** 的图形化应用，包括游戏！

我们不会这么疯狂（至少对于你的开发者工具，技巧40确实这么做了，不过我们发现重新审视对于Docker的假设可能会带来令人意想不到的使用场景。例如，附录A所讨论的在Windows安装Docker之后，在Windows上运行图形化Linux应用程序。

