1. 行内式的 JavaScript

   ```html
   <input type="button" value="唐伯虎" onclick="alert('秋香姐')">
   ```

2. 内嵌式的 JavaScript

   ```html
   <script>
       alert('沙漠骆驼');
   </script>
   ```

3. 外部的 JavaScript

   ```html
   <script src="main.js"></script>
   ```

   > 注意：在 `<script>` 和 `</script>` 标签之间不能写代码，会被浏览器忽略掉。

**index.html**

```html
<!DOCTYPE html>
<html lang="zh">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
        <style></style>
        <!--    2. 内嵌式的js   -->
        <script>
            alert('沙漠骆驼');
        </script>
        <!--    3. 外部js script 双标签 -->
        <script src="main.js"></script>
    </head>
    <body>
        <!--    1. 行内式的js 直接写到元素的内部    -->
        <input type="button" value="唐伯虎" onclick="alert('秋香姐')">
    </body>
</html>
```

**main.js**

```js
alert('如果我是DJ，你还爱我吗？');
```

