[toc]

#### 1. 八机制

八进制的表示方法为在数字前面加 0。

```js
var num = 010;
```

#### 2. 十六进制

十六进制的表示方法为在数字前面加 0x。

```js
var num = 0xa;
```

#### 3. 获取数字型的最大值

```js
Number.MAX_VALUE;
```

#### 4. 获取数字型的最小值

```js
Number.MIN_VALUE;
```

#### 5. 无穷大数字的表示

```js
Infinity
```

#### 6. 无穷小数字的表示

```js
-Infinity
```

#### 7. 非数字的表示

```js
NaN
```

#### 8. 判断一个数字是否一个非数字值

```js
var num = NaN;
// isNaN() 这个方法用来判断非数字，并且返回一个值，如果是数字返回的是 false, 如果不是数字返回的是 true
var isNumber = isNaN(num);
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
            var num = 10;   // num 数字型
            var PI = 3.14;  // PI 数字型
            // 1. 八进制 0 ~ 7  我们程序里面数字前面加 0 表示八进制
            var num1 = 010;
            console.log(num1);  // 010 八进制 转换为 十进制 就是 8
            var num2 = 012;
            console.log(num2);
            // 2. 十六进制 0 ~ 9 a ~ f #ffffff 数字的前面加 0x 表示十六进制
            var num3 = 0x9;
            console.log(num3);
            var num4 = 0xa;
            console.log(num4);
            // 3. 数字型的最大值
            console.log(Number.MAX_VALUE);
            // 4. 数字的最小值
            console.log(Number.MIN_VALUE);
            // 5. 无穷大
            console.log(Number.MAX_VALUE * 2);  // Infinity 无穷大
            // 6. 无穷小    
            console.log(-Number.MAX_VALUE * 2); // -Infinity 无穷小
            // 7. 非数字
            console.log('pink老师' - 100);  // NaN
            // isNaN() 这个方法用来判断非数字，并且返回一个值，如果是数字返回的是 false, 如果不是数字返回的是 true
            console.log(isNaN(12)); // false
            console.log(isNaN('pink老师')); // true
        </script>
    </head>
    <body>
    </body>
</html>
```

