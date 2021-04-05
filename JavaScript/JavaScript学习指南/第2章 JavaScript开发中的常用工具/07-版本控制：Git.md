### 2.2.4　版本控制：Git

本书不会详细讲述版本控制工具，因为它是作为开发人员的必备技能。如果对Git不熟悉，那么本书和书中的例子就可以作为学习Git的良好材料。

首先，在项目的根目录下，初始化一个Git仓库：

```javascript
$ git init
```

这条命令创建了一个项目仓库（在项目的根目录下会有一个隐藏起来的.git文件）。

当然，一定会有一些文件是不想使用Git进行追踪的：构建包，临时文件等。这些文件可以在.gitignore文件中被显示地排除掉。创建一个.gitignore文件，添加以下内容：

```javascript
# npm debugging logs
npm-debug.log*
# project dependencies
node_modules
# OSX folder attributes
.DS_Store
# temporary files
*.tmp
*~
```

如果还有其他不需要被追踪的“垃圾”文件，尽管把它们添加进来（比如：有些编辑器会创建.bak的文件，通过*.bak可以将这些文件放进来）。

`git status` 是一个非常常用的命令，它可以显示仓库的当前状态。试着输入这个命令，看看结果是不是与下面的一样：

```javascript
$ git status
On branch master
Initial commit
Untracked files:
  (use "git add <file>..." to include in what will be committed)
       .gitignore
nothing added to commit but untracked files present (use "git add" to   
track)
```

Git会告诉程序员在当前目录下有一个新文件（.gitignore），但是它处于未被追踪的状态，这意味着Git并不会对它进行版本管理。这条信息很重要。

Git的基本工作单元是提交。当前仓库还没有任何提交（因为这个仓库刚刚被初始化，虽然添加了一个文件，但是这个文件不被Git管理）。如果不特殊声明，Git就不知道有哪些文件需要被追踪，所以必须把.gitignore文件添加到仓库中：

```javascript
$ git add .gitignore
```

现在还有没有进行任何提交；只是简单地把.gitignore放入下一个提交中。运行 `git status` ，可以看到：

```javascript
$ git status
On branch master
Initial commit
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   .gitignore
```

现在.gitignore的状态是待提交。到目前为止仍然没有提交，一旦提交，.gitignore就会包含在里面。也可以添加更多文件，先来做一次提交：

```javascript
$ git commit -m "Initial commit: added .gitignore."
```

这条命令中，-m后面的是提交信息：简单描述本次提交中包含的修改。它可以保存项目的提交历史，方便后期回顾。

可以把提交想象成项目快照，它表示项目在某一时刻的状态。这次提交好比做了一次项目快照（只把.gitignore放进来），在日后的任意时刻，都可以回顾这次提交。这时候运行git status看到的结果应该是：

```javascript
On branch master
nothing to commit, working directory clean
```

接下来，多做一些修改。在目前的.gitignore文件中，已经忽略了所有名为npm-debug.log的文件，这次试着忽略所有以 .log结尾的文件（这是一个比较好的实践）。编辑.gitignore文件，将npm-debug.log的那行修改为*.log。再添加一个叫作README.md的文件，这是一个用Marddown格式编写的文件，它是介绍项目的标准文件：

```javascript
= Learning JavaScript, 3rd Edition
== Chapter 2: JavaScript Development Tools
In this chapter we're learning about Git and other
development tools
```

再试试 `git status` :

```javascript
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working   
directory)
           modified:   .gitignore
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md
```

现在已经有两处修改：一个是被git追踪的文件（.gitignore），另一个是新文件（README.md）。如果重复之前添加文件的步骤，那么应该运行的命令是：

```javascript
$ git add .gitignore
$ git add README.md
```

不过这次尝试用快捷键一次性添加所有修改，然后做一次提交：

```javascript
$ git add -A
$ git commit -m "Ignored all .log files and added README.md."
```

以上这两个步骤在后面的例子中会经常重复（添加修改的文件和提交这些修改）。在提交时，试着把它们做的小且逻辑性强一些：就好像这些提交是在讲述一个关于项目进度的故事。任何时候，只要在项目仓库中做修改，都要遵循这个步骤：添加修改的文件，然后提交：

```javascript
$ git add -A
$ git commit -m "<brief description of the changes you just made>"
```

> <img class="my_markdown" src="../images/5.png" style="width:429px;  height: 573px; " width="10%"/>
> 初学者经常会对git add有些疑惑；顾名思义，add像是在给项目仓库中添加文件。有时候修改的内容确实是个新文件，不过这些新的修改早已经在代码库中完成了。换句话说，git add的时候是在添加新的修改，而非文件（增加文件只是一种特殊类型的修改）。

以上内容展示了Git中最简单的工作流；如果想了解更多关于Git的知识，推荐GitHub上的Git教程，以及由Jon Loeliger和Matthew McCullough编写的《Git版本控制》第二版。

