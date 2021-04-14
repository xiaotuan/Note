### 技巧64　容器里的无头Chrome

运行测试是CI的一个关键部分，多数单元测试框架都能在Docker里很好地运行。不过，有时候需要引入更复杂的测试，从确保多个微服务正确协作到确保网站前端功能正常工作。访问网站前端需要某个类型的浏览器，为了解决这个问题，我们需要一种在容器中启动浏览器的方法，并以编程方式控制它。

#### 问题

无须GUI，在容器里使用Chrome浏览器做测试。

#### 解决方案

在容器里使用Puppeteer这个Node.js库实现Chrome动作自动化。

这个库由谷歌Chrome开发团队维护，允许你编写针对Chrome的脚本以便测试。它是“无头的”，这意味着你不需要GUI来使用它。



**注意**

我们也在GitHub上维护了该镜像：https://github.com/docker-in-practice/docker-puppeteer。同时也可以使用docker pull dockerinpractice/docker-puppeteer作为Docker镜像访问它。



代码清单8-5展示的Dockerfile将创建一个包含所有使用Puppeteer所需内容的镜像。

代码清单8-5　Puppeteer的Dockerfile

```c
FROM ubuntu:16.04　　⇽---　以Ubuntu基础镜像开始
RUN apt-get update -y && apt-get install -y \　　⇽---　
     npm python-software-properties curl git \
     libpangocairo-1.0-0 libx11-xcb1 \
     libxcomposite1 libxcursor1 libxdamage1 \
     libxi6 libxtst6 libnss3 libcups2 libxss1 \
     libxrandr2 libgconf-2-4 libasound2 \
     libatk1.0-0 libgtk-3-0 vim gconf-service \
     libappindicator1 libc6 libcairo2 libcups2 \
     libdbus-1-3 libexpat1 libfontconfig1 libgcc1 \
     libgdk-pixbuf2.0-0 libglib2.0-0 libnspr4 \
     libpango-1.0-0 libstdc++6 libx11-6 libxcb1 \
     libxext6 libxfixes3 libxrender1 libxtst6 \
     ca-certificates fonts-liberation lsb-release \
     xdg-utils wget　　⇽---　安装所有必需的软件。这是让Chrome可以在容器中操作所必需的大多数显示库
 RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -　　⇽---　设置最新的nodejs版本
 RUN apt-get install -y nodejs　　⇽---　安装Ubuntu的nodejs包
 RUN useradd -m puser　　⇽---　创建一个非root用户“puser”（库运行所必需）
 USER puser　　⇽---　创建一个node模块目录
 RUN mkdir -p /home/puser/node_modules　　⇽---　将NODE_PATH环境变量指向node_ modules目录
 ENV NODE_PATH /home/puppeteer/node_modules　　⇽---　设置当前工作目录为node_modules
 WORKDIR /home/puser/node_modules　　⇽---　安装webpack（Puppeteer的一个依赖项）
 RUN npm i webpack　　⇽---　克隆Puppeteer模块代码
 RUN git clone https://github.com/GoogleChrome/puppeteer　　⇽---　进入Puppeteer代码目录
 WORKDIR /home/puser/node_modules/puppeteer　　⇽---　安装Puppeteer nodejs库
 RUN npm i . 　　⇽---　进入Puppeteer示例目录
 WORKDIR /home/puser/node_modules/puppeteer/examples　　⇽---　添加一个no-sandbox参数到Puppeteer启动参数中，以规避在容器中运行时的一项安全设置
 RUN perl -p -i -e \
     "s/puppeteer.launch\(\)/puppeteer.launch({args: ['--no-sandbox']})/" *　　⇽---　以bash启动容器，包含了一个提供建议的echo命令
 CMD echo 'eg: node pdf.js' && bash
```

以如下命令构建或运行该Dockerfile：

```c
$ docker build -t puppeteer .
```

然后运行这个镜像：

```c
$ docker run -ti puppeteer
eg: node pdf.js
puser@03b9be05e81d:~/node_modules/puppeteer/examples$
```

你将看到一个终端以及运行 `node pdf.js` 的建议。

pdf.js文件包含了一个简单的脚本，以此演示Puppeteer库所能实现的功能，如代码清单8-6所示。

代码清单8-6　pdf.js

```c
'use strict'; 　　⇽---　在严格模式下运行Javascript解释器，它将捕获技术上允许的常见不安全操作
 const puppeteer = require('puppeteer'); 　　⇽---　导入Puppeteer库
 (async() => {　　⇽---　创建一个异步块，代码将在里面运行
   const browser = await puppeteer.launch();　　⇽---　使用puppeteer.launch函数运行一个浏览器。使用await关键字，代码将在启动完成前暂停
   const page = await browser.newPage();　　⇽---　使用newPage函数让浏览器等待页面（相当于浏览器的标签页）可用
   await page.goto(
     'https://news××××××.com', {waitUntil: 'networkidle'}
   ); 　　⇽---　使用page.goto函数打开Hacker News网站，并在继续前等待直到没有网络流量
   await page.pdf({　　⇽---　
     path: 'hn.pdf',
     format: 'letter'
   });　　⇽---　使用page.pdf函数以letter格式创建当前标签页的PDF文件，并将文件命名为hn.pdf
   await browser.close();　　⇽---　关闭浏览器，等待直到退出完成
})();　　⇽---　呼叫异步块返回的函数
```

在这个简单的例子之外，Puppeteer用户还拥有大量选项。详细解释Puppeteer API超出了本技巧的范围。如果你想更深入了解API并采用本技巧，请查阅GitHub上的Puppeteer API文档。

#### 讨论

本技巧展示的是如何使用Docker针对某个特定浏览器进行测试。

下一个技巧会使用两个方法对此进行扩充：使用Selenium，这是一个流行的、可以与多种浏览器配合的测试工具；将其与X11的一些研究相结合，就可以看到运行在图形窗口里的浏览器，而非本技巧使用的无头方法。

