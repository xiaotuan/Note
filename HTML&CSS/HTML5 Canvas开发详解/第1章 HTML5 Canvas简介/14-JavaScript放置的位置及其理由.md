### JavaScript放置的位置及其理由

使用JavaScript为Canvas编程会产生一个问题：在创建的页面中，从哪里启动JavaScript程序？

把JavaScript放进HTML页面的 <head> 标签中是个不错的主意，这样做的好处是很容易找到它。但是，把JavaScript程序放在这里就意味着整个HTML页面要加载完JavaScrpit才能配合HTML运行，这段JavaScript代码也会在整个页面加载前就开始执行了。结果就是，运行JavaScript程序之前必须检查HTML页面是否已经加载完毕。

最近有一个趋势是将JavaScript放在HTML文档结尾处的</body>标签里，这样就可以确保在JavaScript运行时整个页面已经加载完毕。然而，由于在运行<canvas>程序前需要使用JavaScript测试页面是否加载，因此最好还是将JavaScript放在<head>中。如果读者不喜欢这样，也可以采用适合自己的代码习惯。

代码放在哪儿都行——可以放在HTML页面代码行内，也可以加载一个外部 .js文件。加载外部JavaScript文件的代码大致如下。

```javascript
<script type="text/javascript" src="canvasapp.js"></script>
```

简单起见，这里将把代码写在HTML页面行内。不过，如果读者有把握，把它放在一个外部文件再加载运行也未尝不可。

提示

> HTML5不需要再指定脚本类型。

