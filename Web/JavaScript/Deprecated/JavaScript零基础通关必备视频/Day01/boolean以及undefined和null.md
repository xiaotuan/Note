[toc]

#### 1. 布尔型

+ 布尔型 `true` 在数值运算中当 1 来看。
+ 布尔型 `false` 在数值运算中当 0 来看。

```js
console.log(true + 1);  // true 参与加法运算当 1 来看
console.log(false + 1); // false 参与加法运算当 0 来看
```

#### 2. undefined

+ 如果一个变量声明未赋值，其值就是 `undefined`。
+ 如果一个字符串与一个 undefined 变量使用 `+` 相连，得到的结果是 'undefined' + 字符串。
+ 如果一个 undefined 变量与数字进行运算，得到的值是 NaN。

```js
var variable = undefined;
console.log(variable + 'pink'); // undefinedpink
console.log(variable + 1);  // NaN  undefined 和数字相加 最后的结果是 NaN
```

#### 3. null

+ 如果一个字符串与一个值为 null 的变量使用 `+` 相连，得到的结果是 'null' + 字符串。
+ 如果一个值为 null  的变量与数字进行运算，得到的值是数字本身。

```js
// null 空值
var space = null;
console.log(space + 'pink');    // nullpink
console.log(space + 1); // 1
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
            var flag = true;    // flag 布尔型
            var flag1 = false;  // flag1 布尔型
            console.log(true + 1);  // true 参与加法运算当 1 来看
            console.log(false + 1); // false 参与加法运算当 0 来看
            // 如果一个变量声明未赋值，就是 undefined 未定义数据类型
            var str;
            console.log(str);
            var variable = undefined;
            console.log(variable + 'pink'); // undefinedpink
            console.log(variable + 1);  // NaN  undefined 和数字相加 最后的结果是 NaN
            // null 空值
            var space = null;
            console.log(space + 'pink');    // nullpink
            console.log(space + 1); // 1
        </script>
    </head>
    <body>
    </body>
</html>
```

