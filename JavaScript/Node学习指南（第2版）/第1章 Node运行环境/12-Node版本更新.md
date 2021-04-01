[toc]

### 1.4.2　Node版本更新

随着发布计划的增加，使 Node 版本保持最新版尤为重要。幸运的是，升级过程毫不费劲，而且还有替代方案。

你可以通过下面这条命令来检查 Node 版本：

```python
node -v
```

如果你用的是一个包安装软件，那么运行包更新程序就可以更新 Node 了，这同时也会更新你的服务器上的其他程序（Windows 上不需要 sudo）：

```python
sudo apt-get update
sudo apt-get upgrade --show-upgraded
```

如果你用的是安装软件，那么请遵循 Node 网站上提供的相关说明，否则你可能无法更新 Node。

你也可以使用 npm 来更新 Node，命令如下：

```python
sudo npm cache clean -f
sudo npm install -g
sudo n stable
```

如果要在 Windows、OS X 或者你的树莓派上安装最新版 Node，请在 Node 网站的下载页面中下载安装程序，并且运行。它会用新版覆盖旧版。

> <img class="my_markdown" src="../images/23.png" style="zoom:50%;" />
> **Node 版本管理器**
> 在 Linux 或者 OS X 环境中，你也可以使用 Node 版本管理器（Node Version Manager, nvm）工具来更新Node。

Node 包管理器（Node package manager, npm）本身的更新频率甚至比 Node 还高。要更新 npm，只需执行：

```python
sudo npm install npm -g n
```

这个命令将会安装所有需要的软件的最新版。你可以通过这条命令检查 npm 的版本：

```python
npm -v
```

请注意，这可能会导致某些问题，尤其是在团队环境中。如果你的团队成员使用的 Node 是用 npm 安装的，而你手动将 npm 升级到更新的版本，那么可能出现不一致的构建结果，而且这个问题不易被发现。

我将在第 3 章更详细地介绍 npm，但现在请先记住，你可以使用以下命令将所有 Node 模块更新到最新版本：

```python
sudo npm update -g
```

