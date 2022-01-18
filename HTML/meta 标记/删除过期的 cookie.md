如果网页过期，则删除存盘的 cookie。

**语法**

```html
<meta http-equiv="set-cookie" content="到期时间" />
```

> 注意
>
> 这里的到期时间是 GMT 时间格式。

**示例**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>删除过期的 cookie</title>
        <meta http-equiv="set-cookie" content="Web,14 september 2011 16:20:00 GMT" />
    </head>
    <body>
        
    </body>
</html>
```

