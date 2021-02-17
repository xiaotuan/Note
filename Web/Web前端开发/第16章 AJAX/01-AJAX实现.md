[toc]

### 1. 案例：基于本地 XML 实现学生成绩册

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="AJAX" />
        <meta content="使用AJAX基于本地XML实现学生成绩册" />
        <title>使用AJAX基于本地XML实现学生成绩册</title>
        <link rel="stylesheet" type="text/css" href="css/16-01.css" />
        <script type="text/javascript">
            function loadXMLDoc(grade) {
                var xmlhttp;
                //声明xmlHttp对象
                if (window.XMLHttpRequest) {//IE7+, Firefox, Chrome, Opera, Safari使用
                    xmlhttp = new XMLHttpRequest();
                }
                else {//IE6, IE5使用
                    xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
                }
                xmlhttp.onreadystatechange = function () {
                    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                        var xml = xmlhttp.responseXML.documentElement;
                        var node = xml.getElementsByTagName('student');
                        var str = '';//初始化整个成绩册组合字符串
                        for (var i = 0; i < node.length; i++) {
                            var id = node[i].getElementsByTagName('id')[0].firstChild.nodeValue;
                            var name = node[i].getElementsByTagName('name')[0].firstChild.nodeValue;
                            var sex = node[i].getElementsByTagName('sex')[0].firstChild.nodeValue;
                            var major = node[i].getElementsByTagName('major')[0].firstChild.nodeValue;
                            var grades = node[i].getElementsByTagName('grades');
                            var web = grades[0].getElementsByTagName('web')[0].firstChild.nodeValue;//获取Web前端开发成绩
                            var os = grades[0].getElementsByTagName('os')[0].firstChild.nodeValue;//获取操作系统成绩
                            var network = grades[0].getElementsByTagName('network')[0].firstChild.nodeValue;//获取网络成绩
                            var database = grades[0].getElementsByTagName('database')[0].firstChild.nodeValue;//获取数据库成绩
                            if (i % 2 == 0) {
                                str += '<div class="gradeContent"><span class="studentID">' + id + '</span><span class="studentName">' + name + '</span><span class="studentSex">' + sex + '</span><span class="studentMajor">' + major + '</span><span class="studentLesson">' + web + '</span><span class="studentLesson">' + os + '</span><span class="studentLesson">' + network + '</span><span class="studentLesson">' + database + '</span></div>';
                            } else {
                                str += '<div class="gradeContent gradeContentOdd"><span class="studentID">' + id + '</span><span class="studentName">' + name + '</span><span class="studentSex">' + sex + '</span><span class="studentMajor">' + major + '</span><span class="studentLesson">' + web + '</span><span class="studentLesson">' + os + '</span><span class="studentLesson">' + network + '</span><span class="studentLesson">' + database + '</span></div>';
                            }


                        }

                        //输出内容到名称为grade的容器中，grade是一个参数
                        document.getElementById(grade).innerHTML = str;
                    }
                }
                xmlhttp.open("GET", "medias/data.xml", true);//打开XML文档
                xmlhttp.send();//发送XML文档
            }
        </script>
    </head>

    <body>
        <div class="center">
            <div><input type="button" onclick="loadXMLDoc('showGrade')" value="AJAX输出成绩册" /></div>
            <div class="gradeTitle"><span class="studentID">学号</span><span class="studentName">姓名</span><span
                    class="studentSex">性别</span><span class="studentMajor">专业</span><span
                    class="studentLesson">Web前端开发</span><span class="studentLesson">操作系统</span><span
                    class="studentLesson">网络</span><span class="studentLesson">数据库</span></div>
            <div class="gradeContent"></div>
            <div id="showGrade" class="gradeContent">点击按钮后加载成绩册</div>
        </div>
    </body>
</html>
```

> 注意：现在的浏览器已经禁止请求本地数据，Firefox 浏览器可以参考 《[解决Firefox请求本地数据报错问题](../../Common/解决Firefox请求本地数据报错问题.md)》

### 2. 案例：AJAX 获取远程数据

**index.php**

```php
<?php
$url = 'http://news.163.com/special/00011K6L/rss_newstop.xml';
$xmlContent = file_get_contents($url);//获取远程文件内容
$xmlArray = json_decode(json_encode((array) simplexml_load_string($xmlContent)), true);//将字符串转换为数组
echo json_encode($xmlArray);//格式化为JSON数据返回
?>
```

**案例：示例 16-02：AJAX 获取远程数据**

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta keywords="AJAX" />
        <meta content="使用AJAX读取网易新闻列表" />
        <title>使用AJAX读取网易新闻列表</title>
        <link rel="stylesheet" type="text/css" href="css/16-02.css" />
        <script type="text/javascript">
            function loadXMLDoc(grade) {
                var xmlhttp;
                //声明xmlHttp对象
                if (window.XMLHttpRequest) {//IE7+, Firefox, Chrome, Opera, Safari使用
                    xmlhttp = new XMLHttpRequest();
                }
                else {//IE6, IE5使用
                    xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
                }
                xmlhttp.onreadystatechange = function () {
                    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                        console.log("response: " + xmlhttp.response);
                        var jsonObj = JSON.parse(xmlhttp.response);//将返回的数据格式化为JSON对象
                        var channelObj = jsonObj['channel'];//提取键值为channel的对象
                        var str = '';
                        for (var key in channelObj) {
                            var itemObj = channelObj[key];
                            if (key == 'item') {
                                var i = 0;
                                for (var itemkey in itemObj) {
                                    var listObj = itemObj[itemkey];
                                    var itemTitle = listObj['title'];//新闻标题
                                    var itemLink = listObj['link'];//新闻链接
                                    var itemDesc = listObj['description'];//新闻描述
                                    var itemPubData = listObj['pubDate'];//发布时间
                                    var time = new Date(itemPubData);
                                    var pubtime = time.getFullYear() + "-" + (((time.getMonth() + 1).toString().length == 1) ? '0' + (time.getMonth() + 1) : (time.getMonth() + 1)) + "-" + ((time.getDate().toString().length == 1) ? '0' + time.getDate() : time.getDate()) + " " + (time.getHours().toString().length == 1 ? '0' + time.getHours() : time.getHours()) + ":" + (time.getMinutes().toString().length == 1 ? '0' + time.getMinutes() : time.getMinutes());

                                    if (i % 2 == 0) {
                                        str += '<div class="listContent"><span class="title"><a href="' + itemLink + '" target="_blank">' + itemTitle + '</a></span><span class="pubtime">' + pubtime + '</span></div>';
                                    } else {
                                        str += '<div class="listContent listContentOdd"><span class="title"><a href="' + itemLink + '" target="_blank">' + itemTitle + '</a></span><span class="pubtime">' + pubtime + '</span></div>';
                                    }

                                    i++;

                                }
                            }
                        }

                        //输出内容到名称为grade的容器中，grade是一个参数
                        document.getElementById(grade).innerHTML = str;
                    }
                }
                xmlhttp.open("GET", "index.php", true);//请求服务器端PHP程序，将从网易获取的新闻列表处理为JSON后返回
                xmlhttp.send();//发送请求
            }
        </script>
    </head>

    <body>
        <div class="center">
            <div><input type="button" onclick="loadXMLDoc('showNewsList')" value="AJAX输出网易新闻" /></div>
            <div class="listTitle"><span class="title">标题</span><span class="pubtime">发布时间</span></div>
            <div id="showNewsList" class="listContent">点击按钮后输出新闻列表</div>
        </div>
    </body>
</html>
```

> 提示：上面的例子会请求失败，因为 http://news.163.com/special/00011K6L/rss_newstop.xml 链接已经失效。