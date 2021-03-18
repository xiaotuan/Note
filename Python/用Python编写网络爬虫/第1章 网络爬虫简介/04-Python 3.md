[toc]

### 1.3　Python 3

在本书中，我们将完全使用Python 3进行开发。Python软件基金会已经宣布Python 2将会被逐步淘汰，并且只支持到2020年；出于该原因，我们和许多其他Python爱好者一样，已经将开发转移到对Python 3的支持当中，在本书中我们将使用3.6版本。本书代码将兼容Python 3.4+的版本。

如果你熟悉 `Python Virtual Environments` 或 `Anaconda` 的使用，那么你可能已经知道如何在一个新环境中创建Python 3了。如果你希望以全局形式安装Python 3，那么我们推荐你搜索自己使用的操作系统的特定文档。就我而言，我会直接使用 **Virtual Environment Wrapper** （ `https://virtualenvwrapper.readthedocs.io/en/latest` ），这样就可以很容易地对不同项目和Python版本使用多个不同的环境了。使用Conda环境或虚拟环境是最为推荐的，这样你就可以轻松变更基于项目需求的依赖，而不会影响到你正在做的其他工作了。对于初学者来说，我推荐使用Conda，因为其需要的安装工作更少一些。

Conda的介绍文档（ `https://conda.io/docs/intro.html` ）是一个不错的开始！

> <img class="my_markdown" src="../images/5.jpg" style="zoom:50%;" />
> 从此刻开始，所有代码和命令都假设你已正确安装Python 3并且正在使用Python 3.4+的环境。如果你看到了导入或语法错误，请检查你是否处于正确的环境当中，查看跟踪信息中是否存在Python 2.7的文件路径。

