### 1. 报错请求代码

```js
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
```

### 2. 报错日志

```console
已拦截跨源请求：同源策略禁止读取位于 file:///Users/qintuanye/Desktop/Web%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91/02.%E6%A1%88%E4%BE%8B/16/16-01/medias/data.xml 的远程资源。（原因：CORS 请求不是 http）。
```

### 3. 解决办法

因此只要关闭浏览器的同源策略，就可以解决该跨域问题，关闭同源策略方法如下：

+ 浏览器地址栏输入：about:config ，接收风险并继续

+ 查询privacy.file_unique_origin首选项，双击或点击右边改为false，不开启该规则

+ 浏览器地址栏输入：about:restartrequired 重启浏览器

