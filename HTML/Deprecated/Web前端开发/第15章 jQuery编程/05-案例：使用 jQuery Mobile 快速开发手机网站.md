**案例：示例 15-28：jQuery Mobile 演示网站**

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="JavaScript" />
        <meta name="viewport" content="width=device-width,initial-scale=1" />
        <title>jQuery Mobile演示网站</title>
        <link rel="stylesheet" href="css/jquery.mobile.css" />
        <script language="javascript" type="text/javascript" src="jquery/jquery.js"></script>
        <script language="javascript" type="text/javascript" src="jquery/jquery.mobile.js"></script>
    </head>

    <body>
        <div data-role="page" id="pageone">
            <div data-role="header" data-theme="a">
                <h1>jQuery Mobile演示网站</h1>
            </div>
            <nav data-role="navbar">
                <ul>
                    <li><a href="#home" data-icon="home">首页</a></li>
                    <li><a href="#information" data-rel="dialog" data-icon="grid">新闻</a></li>
                    <li><a href="#calendar" data-rel="dialog" data-icon="star">日历</a></li>
                </ul>
            </nav>
            <div data-role="content">
                <p style="text-align:center;color:grey;">这是jQuery Mobile的首页</p>
            </div>
            <div data-role="footer" data-position="fixed" data-theme="a">
                <h1>Copyright Web前端开发技术与实践</h1>
            </div>
        </div>
        <!--弹出对话框-->
        <div data-role="page" id="information">
            <div data-role="header">
                <h1>新闻</h1>
            </div>
            <div data-role="content">
                <p>这是新闻列表</p>
            </div>
        </div>
        <!--弹出对话框-->
        <div data-role="page" id="calendar">
            <div data-role="header">
                <h1>日历</h1>
            </div>
            <div data-role="content">
                <p>这是日历</p>
            </div>
        </div>
    </body>
</html>
```

