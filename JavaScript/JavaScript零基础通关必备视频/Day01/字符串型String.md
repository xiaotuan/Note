[toc]

#### 1. 字符串型可以是引号中的任意文本，其语法为 **双引号 `""`** 和 **单引号 `''`**。

例如：

```js
// 'pink'   'pink老师'  '12'    'true'
var str = '我是一个"高富帅"的程序员';
```

> 提示：推荐使用单引号。

**示例：**

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
            // 'pink'   'pink老师'  '12'    'true'
            var str = '我是一个"高富帅"的程序员';
            console.log(str);
            // 字符串转义符 都是用 \ 开头 但是这些转义符需要写到引号里面
            var str1 = "我是一个'高富帅'的\n程序员";
            console.log(str1);
        </script>
    </head>
    <body>
    </body>
</html>
```

#### 2. 获取字符串长度

```js
var str = "my name is andy";
console.log(str.length);
```

#### 3. 字符串拼接

可以是 "+" 将多个字符拼接起来。

```js
console.log('沙漠' + '骆驼');   // 字符串的 沙漠骆驼
```

**示例：**

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
            // 1. 检测获取字符串的长度 length
            var str = "my name is andy";
            console.log(str.length);    // 15
            // 2. 字符串的拼接 +    只要有字符串和其他类型相拼接 最终的结果是字符串类型
            console.log('沙漠' + '骆驼');   // 字符串的 沙漠骆驼
            console.log('pink老师' + 18);   // 'pink老师18'
            console.log('pink' + 'true');   // 'pinktrue'
            console.log(12 + 12);   // 24
            console.log('12' + 12); // '1212'
        </script>
    </head>
    <body>
    </body>
</html>
```



