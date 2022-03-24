检测变量数据类型方法如下：

```js
typeof 变量
```

**示例：**

```js
<!DOCTYPE html>
<html lang="zh">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
        <style></style>
        <script>
            var num = 10;
            console.log(typeof num);    //  number
            var str = 'pink';
            console.log(typeof str);    //  string
            var flag = true;
            console.log(typeof flag);   //  boolean
            var vari = undefined;
            console.log(typeof vari);   //  undefined
            var timer = null;
            console.log(typeof timer);  //  object
            // prompt 要过来的值是 字符型的
            var age = prompt('请输入您的你年龄');
            console.log(age);
            console.log(typeof age);   
        </script>
    </head>
    <body>
    </body>
</html>
```

> 提示：在 Chrome 浏览器控制台中，字符串型数据以**黑色** 显示，数字型和布尔型以**蓝色**显示。

