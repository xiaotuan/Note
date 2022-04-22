HTML 5 新增属性，规定当前文档与目标 URL 之间的关系。可用值有：

| alternate | author   | bookmark   | help     | license |
| --------- | -------- | ---------- | -------- | ------- |
| next      | nofollow | noreferrer | prefetch | prev    |
| search    | tag      |            |          |         |

例如：

```html
<!DOCTYPE html>
<html>
    <head> 
        <meta charset="utf-8"> 
        <title>W3Cschool(w3cschool.cn)</title> 
    </head>
    <body>

        <p>点击太阳查看大图:</p>

        <img src="/statics/images/course/planets.gif" tppabs="http://www.w3cschool.cn/statics/images/course/planets.gif" width="145" height="126" alt="Planets" usemap="#planetmap">

        <map name="planetmap">
          <area shape="rect" coords="0,0,82,126" alt="Sun" target="_blank" href="/statics/images/course/sun.gif" rel="alternate">
        </map>

    </body>
</html>
```

