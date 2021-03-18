

### 12.3.3　Node和树莓派2

树莓派2比Arduino复杂多了。你可以给它接上显示器、键盘和鼠标，把它当成计算机来用。微软提供了一个可以安装在设备上的Windows10版本，但大多数人用的还是Raspbian<sup class="my_markdown">[1]</sup>，一个基于Debian Jesse的Linux实现。

> <img class="my_markdown" src="../images/132.png" style="zoom:50%;" />
> **通过SSH连接到树莓派**
> 如果有Wi-Fi适配器，就可以通过SSH连接到树莓派上。Wi-Fi适配器很贵，我之前用过的那个连盒子都没有。一旦树莓派连上网，会默认激活SSH。随便给树莓派找一个IP地址，就可以使用SSH了。新版树莓派3中默认有Wi-Fi模块。

树莓派2是在一个微型SD卡上运行的。至少需要一个8G、Class 10的SD卡。树莓派官方提供了安装说明。但我建议格式化SD卡，并复制New Out Of Box（NOOBs，最新出厂）软件（它能让你自己选择要安装的操作系统），然后安装Raspbian。也可以直接安装从官网下载的Rasbian镜像文件。在编写本书时，最新的Rasbian是在2016年2月发布的。它预装了Node，因为它支持Node-RED（一个基于Node的应用程序），这个工具允许你直接通过拖曳来设计电路，并增强了Raspberry Pi的功能。但是，Node的版本较旧，还停留在v0.10.x。我们需要通过Johnny-Five来使用Node控制设备，这个版本应该不会有问题，但是最好还是升级一下。我建议使用LTS版本的Node（本书写成时是4.4.x版本），并遵循Node-RED的说明书来手动升级Node和Node-RED。

> <img class="my_markdown" src="../images/133.png" style="zoom:50%;" />
> **Node检查**
> Node应该已经安装好了，但是有时会因为Node-RED而使用不同的名字。如果是这样，你可以直接安装最新版本的Node，而不用卸载任何软件。

更新Node后，接着安装Johnny-Five。你还需要安装另一个模块，raspi-io，这是一个可以让Johnny-Five在树莓派上工作的插件。

```python
npm install johnny-five raspi-io
```

放心、大胆地去探索你的新计算机吧（包括桌面应用程序）。探索结束后，下一步就是搭建物理电路。在开始之前，关掉树莓派。

要构建“闪烁的灯”这个“Hello World”程序，需要一块面包板和一个电阻（最好是220Ω）。大多数树莓派套装中都有这样一个电阻，一般是一个四波段电阻：红色、红色、棕色和金色。

> <img class="my_markdown" src="../images/134.png" style="zoom:50%;" />
> **读懂电阻波段**
> Digi-Key Electronics提供了非常方便的计算器以及一个颜色图谱，用来确定你的电阻是多少欧的。如果你觉得自己很难区分颜色，就找周围人帮忙，或者直接使用万用表测量电阻值。

Fritzing草图如图12-6所示。将电阻和LED灯连接到面包板上，将LED灯的阴极（短腿）和电阻的后引脚并联。小心操作你的树莓派2套件中的两根导线，将其中一根接到树莓派电路板的GRND引脚（最上面一行，左数第三个），另外一根连接到13号引脚（第二行左数第七个引脚）。将另外一端接到面包板：连接GRND的导线和电阻的前引脚并联，连接GPIO引脚的导线和LED的阳极引脚（长腿）并联。

> <img class="my_markdown" src="../images/135.png" style="zoom:50%;" />
> 树莓派上的引脚都很脆弱，因此很多人都会用breakout。breakout是一根宽电缆（由一排导线组成），可以插入树莓派中，然后连接到面包板上。接下来的组件就可以连接到breakout上，而不用直接连到树莓派上。

重新给树莓派通电，然后就可以在Node应用中开始编程了。本应用的内容基本跟Arduino的应用一样，不同的是树莓派会用到raspi-io插件，以及用不同的方式表示引脚号。在Arduino中，引脚号用数字表示，而在树莓派中则是用字符串。下面的代码用粗体标出不同之处：

```python
var five = require("johnny-five");
var Raspi = require("raspi-io");
var board = new five.Board({
 io: new Raspi()
}); 
board.on("ready", function() { 
  var led = new five.Led("P1-13"); 
  led.blink(); 
}); 
```

跟Arduino的例子一样，运行程序后LED就会闪烁了，如图12-11所示。

![136.png](../images/136.png)
<center class="my_markdown"><b class="my_markdown">图12-11　用树莓派和Node实现LED闪烁</b></center>

你也可以在树莓派2上运行交互程序。在这个电路板上，PWM引脚是GPIO18，对Johnny-Five应用来说，也就是12号引脚。它是左上方第六个引脚。重新连接导线（从13号引脚换到12号）时，记得关闭树莓派的电源。这里我没有重复所有的代码，只列出了需要改动的部分，如下：

```python
var five = require("johnny-five");
var Raspi = require("raspi-io");
var board = new five.Board({
 io: new Raspi()
});
board.on("ready", function() {
 var led = new five.Led("P1-12");
  // add in animations and commands
  this.repl.inject({
     ... 
  });
}); 
```

因为LED的功率变大了，所以执行 `pulse()` 函数后的演示效果会更明显。

其他一些有趣的基于树莓派和Node的项目如下：

+ 轻松掌握基于树莓派的Node.js/WebSockets/LED控制器；
+ 用树莓派和Node实现家庭监控；
+ Heimcontrol.js，用树莓派和Node实现家庭自动化；
+ 用树莓派、Node和Socket.io实现自制智能电视；
+ 使用Node和MQTT来搭建一个车库门打开装置（使用Intel公司的Edison电路板）；
+ 亚马逊关于如何搭建自己的基于树莓派的Alexa设备的指南。

当你的Node程序可以触发一些现实中的、即时的物理反馈，你会非常高兴的。

[1]　Raspbian是为树莓派设计的，基于Debian的操作系统，由一个小团队开发。它不隶属于树莓派基金会，但被列为官方支持的操作系统。——译者注



