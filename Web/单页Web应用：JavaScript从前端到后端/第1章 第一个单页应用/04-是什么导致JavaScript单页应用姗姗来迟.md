

#### 
  1.1.2 是什么导致JavaScript单页应用姗姗来迟


在 2000 年以前，Flash和Java小程序发展得很不错。Java被用来在浏览器中运行复杂的应用，甚至是完整的办公套装软件 <a class="my_markdown" href="['#anchor4']">[4]</a>。Flash成了运行富浏览器游戏的选择平台，还有后来的视频。另一方面，JavaScript主要致力于的，仍旧不过是按揭计算器、表单验证、翻转特效和弹窗而已。问题在于我们无法依靠JavaScript（或者是它使用的渲染方法）在所有流行的浏览器上提供一致的关键功能。尽管如此，JavaScript单页应用还是比Flash和Java小程序拥有很多引人入胜的优势。

不需要插件——用户不用关心插件的安装和维护以及操作系统的兼容性，就能访问应用。开发人员也同样不用为单独的安全模型而担心，这能减少开发和维护时令人头痛的问题<a class="my_markdown" href="['#anchor5']">[5]</a>。

不臃肿——使用JavaScript和HTML的单页应用，所需的资源要比需要额外运行环境的插件少得多。

一种客户端语言——Web架构师和大多数开发人员需要知道很多种语言和数据格式，HTML、CSS、JSON、XML、JavaScript、SQL、PHP/Java/Ruby/Perl 等。当我们已经在页面上的其他地方使用了JavaScript，为什么还要用Java编写小程序、或者是用ActionScript编写Flash应用呢？在客户端上的所有东西只使用一种编程语言，可以大大地降低复杂性。

更流畅和更具交互性的页面——我们已经看过了网页上的Flash和Java应用。应用通常只显示在某个小方盒内，小方盒周围的很多东西和HTML元素不同：图形widget不一样、右键不一样、声音不一样、与页面的其他部分交互也受到限制。而JavaScript单页应用的话，整个浏览器窗口都是应用界面。

随着JavaScript的成熟发展，它的大部分缺点不是被修复了，就是被缓解了，它的价值优势也水涨船高。

Web浏览器是世界上最广泛使用的应用——很多人会整天开着浏览器窗口并一直使用着。访问JavaScript应用只不过是在书签栏上点击一下罢了。

浏览器中的JavaScript是世界上分布最广的执行环境之一——到2011年12月，每天激活的Android和iOS移动设备差不多有一百万台。每台设备的系统都内置了稳健的 JavaScript 执行环境。最近三年，在世界各地的手机、平板、笔记本电脑和台式机上，发布了超过十亿个稳健的JavaScript实现。

部署JavaScript应用很简单——把JavaScript应用托管到HTTP服务器上后，就能被超过十亿的Web用户使用。

JavaScript对跨平台开发很有用一现在可以使用Windows、Mac OS X或者Linux来创建单页应用，部署了一个单独的应用，不但可以在所有的台式机设备上使用，而且可以在所有的平板和智能手机上使用。我们得感谢趋于一致的跨浏览器标准实现，还有诸如jQuery以及PhoneGap这样成熟的库消除了不一致性。

JavaScript的运行速度变得惊人的快并且有时能和编译型语言匹敌——它的快速发展得益于Mozilla Firefox、Google Chrome、Opera和Microsoft之间持续不断的激烈竞争。现代JavaScript实现利用了诸如即时编译（JIT）成本地机器码、分支预测、类型推断和多线程的高级优化技术 <a class="my_markdown" href="['#anchor6']">[6]</a>。

JavaScript 逐渐引入了高级功能——这些功能包括 JSON 原生对象、本地 jQuery风格的选择器和更加一致的AJAX功能。使用成熟的库，如Strophie和Socket.IO，推送消息要比以往容易得多。

HTML5、SVG 和CSS3的标准和支持已向前推进——这些进步可以完美地渲染像素级别的图形，这是可以和Java或Flash的生成速度和质量相媲美的。

整个Web项目从头到尾都可以使用 JavaScript——现在我们可以使用卓越的Node.js Web 服务器，使用诸如CouchDB 或者MongoDB来保存数据，它们都用JSON来通信，JSON是一种JavaScript数据格式。我们甚至可以在服务器和浏览器之间共享代码库。

台式机、笔记本甚至移动设备都越来越强大了——多核处理器的普及和G级别的内存，意味着过去在服务器上完成的处理工作，现在可以分给客户端的浏览器了。

有了这些优势，JavaScript单页应用已变得相当流行，对有丰富经验的JavaScript开发人员和架构师的需求也日益旺盛。曾经为多种操作系统（或者是为Java或Flash）开发的应用，如今只需运行一个JavaScript应用即可。创业公司选择使用Node.js作为Web服务器，移动应用开发人员使用JavaScript和PhoneGap为多种移动平台创建“原生的”应用，这只需要一份代码库。

JavaScript并不完美，我们轻而易举就能发现遗漏的、不一致的和其他不喜欢的东西。但所有的语言都一样。一旦适应了它的核心思想，采取最佳方法并学会了哪些部分应该避免使用，JavaScript开发就会变得愉悦和高效。

生成式的JavaScript：殊途同归

我们发现直接使用JavaScript开发单页应用更加容易。我们把这些应用叫做原生的单页应用。另外一种出人意料的流行方法是使用生成式的JavaScript，开发人员使用另一种语言来编写代码，然后再转换成 JavaScript。这种转换要么发生在运行时，要么发生在单独的生成阶段。著名的JavaScript生成器有以下几个。

Google Web Toolkit(GWT)——请查看http://code.google.com/webtoolkit/。GWT使用Java来生成JavaScript。

Cappuccino——请查看 http://www.cappuccino.org/。Cappuccino 使用 Objective-J， Objective-J是Mac OS X上的Objective-C的副本。Cappuccino自身是从Cocoa应用框架移植过来的，Cocoa也源自OS X。

CoffeeScript——请查看 http://coffeescript.org/。CoffeeScript 将一种自定义的语言转换成JavaScript，它提供了一些语法糖。

考虑到Google在Blogger、Google Groups 和其他许多网站上使用了GWT，我们可以放心地说生成式的JavaScript单页应用已被广泛地使用了。这就有个问题：何苦要用一种高级语言来编写代码，然后把它转换成其他语言？这儿有很多生成式的JavaScript仍然很受欢迎的理由，以及为什么这些理由已经没有原来那么令人信服了。

熟悉度——开发人员可以使用更熟悉或者更简单的语言。有了生成器和框架，他们不用学习JavaScript的古怪语法就能进行开发。问题在于，在转换的过程中，最终还是会丢失一些东西。当发生这样的情况时，开发人员不得不查看生成的JavaScript并弄懂它，从而使之正常工作。我们觉得使用抽象层级的语言，还不如直接使用 JavaScript 来得高效。

框架——开发人员明白，在服务端和客户端使用一致的构建库GWT，使得整个体系结构紧密地结合在了一起。这是一个很有说服力的论据，尤其当团队已经具备了很多专业知识和有很多正在研发中的产品。

多目标——开发人员可以用生成器为多个目标编写代码，比如一个文件给Internet Explorer使用，另一个文件给其余的浏览器使用。尽管为不同的目标生成代码听起来很不错，但是我们认为，为所有的浏览器只部署一份JavaScript源代码更加高效。幸亏是趋于一致的浏览器实现和成熟的跨浏览器库（如 jQuery），现在编写复杂的单页应用要简单得多了，无需修改就能在所有主流的浏览器上运行。

成熟度——开发人员认为开发大规模应用，JavaScript没什么结构化可言。然而JavaScript还是逐渐地成为一种更好的语言，有令人印象深刻的优势和容易控制的缺陷。从强类型语言（比如Java）转来的开发人员，有时候觉得类型安全的缺失是不可饶恕的。还有些从有配套框架（比如 Ruby on Rails）转来的开发人员，则对结构化的明显缺失而有所不满。令人欣慰的是，可以结合代码验证工具、代码标准和使用成熟的库来缓解这些问题。

今天，我们相信原生的JavaScript单页应用通常都是最佳选择。这也是我们在本书中要设计和构建的单页应用。

