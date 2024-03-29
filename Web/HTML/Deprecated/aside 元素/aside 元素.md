`<aside>` 元素一般用来表示网站当前页面或文章的附属信息部分，它可以包含与当前页面或主要内容相关的广告、导航条、引用、侧边栏评论部分，以及其他区别于主要内容的部分。

`<aside>` 元素主要有以下两种使用方法：

（1）被包含在 `<article>` 元素中作为主要内容的附属信息部分，其中的内容可以是与当前文章有关的资料、名词解释等。

（2）在 `<article>` 元素之外使用，作为页面或站点全局的附属信息部分。最典型的是侧边栏，其中的内容可以是友情链接，博客中的其他文章列表、广告单元等。

> 提示：`<aside>` 元素可位于布局的任意部分，用于表示任何非文档主要内容的部分。

例如：

```html
<!DOCTYPE html>
<html>
	<head> 
		<meta charset="utf-8"> 
		<title>元素的应用</title> 
	</head>
	<body>
		<p>人在一起叫聚餐，心在一起叫团队！</p>
		<aside>
			<h4>微笑</h4>
			<p>微笑是春日里的一场小雨，是寒冬里的一缕阳光!</p>
		</aside>
	</body>
</html>
```

效果如下：

<p>人在一起叫聚餐，心在一起叫团队！</p>
<aside>
    <h4>微笑</h4>
    <p>微笑是春日里的一场小雨，是寒冬里的一缕阳光!</p>
</aside>

