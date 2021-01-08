[toc]

### 1. 内联样式

**案例：示例 7-01：内联样式**

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>内联样式</title>
    </head>
    <body>
        <ul>
            <li style="float:left;padding:4px 5px 0px 5px;color:#F00;font-weight: bold;list-style: none;">首页</li>
            <li style="float: left;padding: 4px 5px 0px 5px;list-style: none;">Web 前端开发</li>
            <li style="float: left;padding: 4px 5px 0px 5px;list-style: none;">Linux 操作系统</li>
            <li style="float: left;padding: 4px 5px 0px 5px;list-style: none;">计算机网络</li>
            <li style="float: left;padding: 4px 5px 0px 5px;list-style: none;">MySQL 数据库管理</li>
        </ul>
    </body>
</html>
```

### 2. 嵌入样式

**案例：示例 7-02：嵌入样式**

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta keywords="HTML5 嵌入样式">
        <meta content="嵌入样式">
        <title>嵌入样式</title>
        <style type="text/css">
            body {
                margin: 20px 0px;
                color: #FFF;
                font-size: 13px;
                font-family: 微软雅黑, "Times New Roman", Times, serif;
            }

            nav {
                width: 100%;
                height: 30px;
                padding-left: 30px;
                background-color: #F63;
            }

            li {
                float: left;
                padding: 4px 5px 0px 5px;
                list-style: none;
            }
        </style>
    </head>

    <body>
        <nav>
            <ul>
                <li>首页</li>
                <li>Web前端开发</li>
                <li>Linux操作系统</li>
                <li>计算机网络</li>
                <li>MySQL数据库管理</li>
            </ul>
        </nav>
    </body>
</html>
```

### 3. 外部样式

外部样式是将所有样式写在一个外部文件中，在 HTML 文档中使用 `<link>` 元素，将文件链接到需要设置样式的文档上。

**案例：示例7-03：外部样式**

文件一：7-03.css（路径：style/7-03.css）

```css
@charset "utf-8";
/* CSS Document */
body {
	margin:20px 0px;
	color:#FFF;
	font-size:13px;
	font-family:微软雅黑, "Times New Roman", Times, serif;
}
nav {
	width:100%;
	height:30px;
	padding-left:30px;
	background-color:#F63;
}
li {
	float:left;
	padding:4px 5px 0px 5px;
	list-style:none;
}
```

文件二：7-03.html

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta keywords="HTML5 外部样式">
        <meta content="外部样式">
        <title>外部样式</title>
        <link type="text/css" href="style/07-03.css" rel="stylesheet">
    </head>

    <body>
        <nav>
            <ul>
                <li>首页</li>
                <li>Web前端开发</li>
                <li>Linux操作系统</li>
                <li>计算机网络</li>
                <li>MySQL数据库管理</li>
            </ul>
        </nav>
    </body>
</html>
```

### 4. 网站 CSS 文件的规划

常用的网站 CSS 文件规划的方法介绍如下：

（1）基于原型

基于原型页面进行 CSS 文件的构建是最为常用的策略。通常共享的 CSS 放到主样式文件，每个页面都载入，各子页面的样式文件单独存放，在需要时载入。

（2）基于页面元素或模块

对于基本的元素，例如 header、body、nav、link 等元素的定义，放到主样式文件。而 aside、article、address 等元素的定义，分别单独定义样式文件。

（3）基于标记

基于标记的规划是最为常见的方法。例如网站中所有的内容列表、网站版权、导航、Logo等，定义到主样式文件中。