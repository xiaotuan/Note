### 1.2　基础的HTML5页面

在开始讲解Canvas前，需要谈论一下HTML5的相关标准——这里将使用HTML5来创建Web页面。

HTML是用于在互联网上构建页面的标准语言。本书不会将很多时间花费在讲解HTML上，但HTML是<canvas>的基础，所以不能完全跳过它。

一个基本的HTML页面分成几个部分，通常有<head>和<body>，新的HTML5规范增加了一些新的部分，例如<nav>、<article>、<header>和<footer>。

<head>标签通常包含与使用<body>标签来创建HTML页面相关的信息。将JavaScript函数放在<head>中是约定俗成的，稍后讨论<canvas>标签时也会这样做。虽然有理由把JavaScript函数放在<body>中，但是简单起见，最好把JavaScript函数放在<head>中。

基本的HTML页面如例1-1所示。

例1-1　简单的HTML页面

```javascript
<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>CH1EX1: Basic Hello World HTML Page</title>
</head>
<body>
Hello World!
</body>
</html>
```

