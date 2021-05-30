常用的语句如下：

| 方法             | 说明                           | 归属   |
| ---------------- | ------------------------------ | ------ |
| alert(msg)       | 浏览器弹出警告框               | 浏览器 |
| console.log(msg) | 浏览器控制台打印输出信息       | 浏览器 |
| prompt(info)     | 浏览器弹出输入框，用户可以输入 | 浏览器 |

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
        <script>
        //    这是一个输入框
        prompt('请输入您的年龄');
        // alert 弹出警告框 输出的 展示给用户
        alert('计算的结果是');
        // console 控制台输出 给程序员测试用的
        console.log('我是程序员能看到的');
        </script>
    </head>
    <body>
    </body>
</html>
```

