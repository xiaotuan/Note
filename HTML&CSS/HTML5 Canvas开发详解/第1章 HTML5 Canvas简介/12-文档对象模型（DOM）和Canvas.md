### 1.4　文档对象模型（DOM）和Canvas

文档对象模型代表了在HTML页面上的所有对象。它是语言中立且平台中立的。它允许页面的内容和样式被Web浏览器渲染之后再次更新。用户可以通过JavaScript访问DOM。从20世纪90年代末以来，文档对象模型已经成为JavaScript、DHTML和CSS开发最重要的一部分。

画布元素本身可以通过DOM，在Web浏览器中经由Canvas 2D环境访问。但是，在Canvas中创建的单个图形元素是不能通过DOM访问的。正如本章前面讲到的，画布工作在即时模式，它并不保存自己的对象，只是说明在每个单个帧里绘制什么。

例1-2在HTML5页面上使用DOM定位<canvas>标签，这也可以用JavaScript来操作。在开始使用<canvas>前，首先需要了解两个特定的DOM对象：window和document。

window对象是DOM的最高一级，需要对这个对象进行检测来确保开始使用Canvas应用程序之前，已经加载了所有的资源和代码。

document对象包含所有在HTML页面上的HTML标签。需要对这个对象进行检索来找出用JavaScript操纵<canvas>的实例。

