### 20.1　Node基础

如果会写JavaScript，那么就能写Node。这并不是说可以直接把基于浏览器的JavaScript程序运行在Node上：因为浏览器端的JavaScript使用了浏览器专用的API。而且，Node中没有DOM（这也说得通：因为没有HTML）。同样，浏览器中也没有针对Node的API。还有一些对操作系统及文件系统的支持，也因为安全原因不能在浏览器中使用（大家能想象黑客通过浏览器删除个人电脑上文件的情形吗？）。其他像创建Web服务器这样的操作，在浏览器上也没有多大作用。

在Node中，区分哪些是JavaScript代码，哪些是API非常重要。经常编写浏览器端JavaScript的开发人员可能会想当然地认为window和document都属于JavaScript。但其实它们都是浏览器提供的API（在18章中讲过）。本章将会讨论Node所提供的API。

开始本章的学习之前，请确保计算机上安装了Node和npm（详情见第2章）。

