### 2.2.6　构建工具：Gulp和Grunt

大多数开发人员都会使用构建工具，可以在开发过程中自动化地运行一些重复任务。当下最火的两款的JavaScript构建工具分别是Grunt和Gulp。它们都可以胜任系统构建的工作。Grunt在几年前就已经为人们所熟知了，它比Gulp早一些出现，所以其社区也大一些，不过Gulp已经迎头赶上了。因为对于新的JavaScript开发人员来说，选择Gulp作为构建工具的比例正在迅速上升，本书中也会使用Gulp。但这并不意味着我觉得Gulp比Grunt更高级（或者Grunt比Gulp更高级）。

首先，用以下命令全局安装Gulp：

```javascript
$ npm install -g gulp
```

> <img class="my_markdown" src="../images/7.png" style="width:503px;  height: 479px; " width="10%"/>
> 如果读者在使用Liunx或者OS X，可能需要在运行-g（全局）的时候切换到高一级的权限，使用：sudo npm install -g gulp。在输入密码后就会获得超级用户权限（只针对这一行命令）。如果在使用被其他人管理的系统，那就需要让管理员把你添加到sudoers的文件里。

对于一个操作系统，只需全局安装一次Gulp即可。而每个项目都需要本地的Gulp，此时需要切换项目根目录下，运行 `npm install --save-dev gulp` （Gulp只是开发依赖的一个例子。程序的运行并不依赖它，但是在开发过程中却需要它的帮助）。现在Gulp已经安装好了，接下来创建一个Gulpfile（gulpfile.js）：

```javascript
const gulp = require('gulp');
// <em>Gulp dependencies go here</em>
gulp.task('default', function() {
    // <em>Gulp tasks go here</em>
});
```

到目前为止，并没有给gulp配置任何任务，不过现在可以验证gulp是否能够正常运行：

```javascript
$ gulp
[16:16:28] Using gulpfile /home/joe/work/lj/gulpfile.js
[16:16:28] Starting 'default'...
[16:16:28] Finished 'default' after 68 μs
```

> <img class="my_markdown" src="../images/7.png" style="width:503px;  height: 479px; " width="10%"/>
> 如果你是一个Windows用户，可能会看到这个错误“The build tools for Visual Studio 2010 (Platform Toolset = v100) cannot be found。”这是因为在Windows上很多npm的包都依赖于Visual Studio构建工具。可以从它的产品下载页面（https://www.visualstudio.com/en-us/visual-studio- homepage-vs.aspx）下载免费版的Visual Studio。安装之后，在program文件下找到“开发人员命令提示符（Developer Command Prompt）”。在命令行快捷方式里，切换到项目的根目录，然后尝试再安装Gulp，这一次应该会顺利很多。接下来并不需要一直使用Visual Studio的开发人员命令提示符，只是在安装对Visual Studio有依赖的npm的包时需要使用它，从而简化安装过程。

