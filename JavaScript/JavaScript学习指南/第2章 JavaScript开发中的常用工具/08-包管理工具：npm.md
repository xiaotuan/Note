### 2.2.5　包管理工具：npm

npm对于JavaScript开发不是必须的，不过现在越来越多的前端开发人员都会选择npm作为项目的包管理工具。而对于Node开发，掌握npm是必不可少的。其实不管是Node开发还是基于浏览器的开发，npm都可以让开发工作变得更简单。出于这个原因，本书中将会使用npm来安装开发所需的构建工具和转换器。

npm一般会结合Node一起使用，如果还没安装Node，访问Node官网（https://nodejs.org/），点击大绿色“INSTALL”按钮即可。

安装Node之后，需要验证npm和Node是否生效。在命令行输入以下命令：

```javascript
$ node -v
v4.2.2
$ npm -v
2.14.7
```

机器上的版本号可能随着Node和npm的更新而变化。大体上讲，npm是用来管理安装包的。这里说的包可以是一个功能齐全的应用程序中的任何东西，从示例代码，到一个功能模块，或者一个库，都可以使用npm来管理。

npm支持两种级别的安装包：全局和本地。全局安装的包通常是一些用于开发中过程中的命令行工具，本地安装的包则是用于具体项目上的包。使用npm install命令就可以安装包。下面通过安装一个很常用的包Underscore来熟悉这个过程。切换到项目的根目录，运行下面命令：

```javascript
$ npm install underscore
underscore@1.8.3 node_modules\underscore
```

这些信息表明npm已经安装了最新版本的Underscore（1.8.3是作者运行命令时的最新版本；大家在运行时版本号可能会有更新）。Underscore这个功能模块没有其他依赖，所以npm的输出信息较简单；当安装一些复杂的功能模块时，npm可能输出多达好几页的信息！如果想安装指定版本的Underscore，可以显式指定版本号：

```javascript
$ npm install underscore@1.8.0
underscore@1.8.0 node_modules\underscore
```

那么这个模块安装到哪里去了呢？安装结束后，在项目的根目录里会看到一个名为node_modules的目录，所有本地安装的模块都会放在这个目录里。可以删掉node_modules目录，稍后会重新创建它。

安装模块之后，就需要管理这些模块；这些已安装的模块就是项目的依赖。在项目日趋成熟的时候，需要以简明的方式获得当前项目的依赖信息，npm通过一个名为package.json的文件来帮管理它们。这个文件不需要自己创建：在命令行里运行npm init，然后回答几个关于配置的问题（最简单的办法是一路回车，使用默认的配置；之后可以随时修改文件内容）。运行npm init命令，看看生成的package.json文件有哪些信息。

依赖分为常规依赖和开发依赖。开发依赖是指那些只在项目构建时需要的依赖（稍后会有例子），应用程序运行时不需要它们。从现在开始，每安装一个本地依赖时，都需要在命令行后面添加--save或者--saveDev的标签；否则这些包虽然会被安装，但是不会出现在package.json文件里。接下来使用--save标记重新安装Underscore：

```javascript
$ npm install --save underscore
npm WARN package.json lj@1.0.0 No description
npm WARN package.json lj@1.0.0 No repository field.
underscore@1.8.3 node_modules\underscore
```

这些警告是什么意思呢？这表示在准备安装的包里有一些组件找不到。由于本书不是专门讨论npm的书，所以可以暂时忽略这些警告。只有在使用npm公开自己的包的时候，才需要担心这些警告，但本书不会涉及这些内容。

此时package.json文件已经把Underscore加入到依赖列表中。依赖管理是因为那些被列在package.json里的有特定版本的依赖包需要被快速重建（下载和安装）。试着再删除node_modules目录，然后运行npm install（这一次不用输入任何包名）。npm就会下载所有在package.json文件里列出的包。看看新生成的node_modules目录，就知道下载的对不对了。

