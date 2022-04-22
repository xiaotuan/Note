HTML 5 新增属性，规定目标 URL 的语言。例如：

```html
<!DOCTYPE html>
<html>
    <head> 
        <meta charset="utf-8"> 
        <title>W3Cschool(w3cschool.cn)</title> 
    </head>
    <body>
        
        <p>点击查看大图</p>

        <img src="/statics/images/course/planets.gif" width="145" height="126" alt="Planets" usemap="#planetmap">

        <map name="planetmap">
          <area shape="rect" coords="0,0,82,126" target="_blank" alt="Sun" href="/statics/images/course/sun.gif" hreflang="en">
        </map>

    </body>
</html>
```

