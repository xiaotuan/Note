[toc]

> 注意：`step` 属性是 HTML5 中的新属性。

### 1. 支持浏览器

Internet Explorer 10、Opera、Chrome 和 Safari 支持 `step` 属性。

> **注意：**Firefox 或者 Internet Explorer 9 及之前的版本不支持 `<input>` 标签的 `step` 属性。

### 2. 定义和用法

`step` 属性规定 `<input>` 元素的合法数字间隔。

实例：如果 step="3"，则合法数字应该是 -3、0、3、6，以此类推。

**提示：**`step` 属性可以与 `max` 和 `min` 属性配合使用，以创建合法值的范围。

**注意：**`step` 属性适用于下面的 `input` 类型：number、range、date、datetime、datetime-local、month、time 和 week。

### 3. 语法

```html
<input step="number">
```

### 4. 属性值

| 值     | 描述                         |
| :----- | :--------------------------- |
| number | 规定输入字段的合法数字间隔。 |

### 5. 示例

```html
<!DOCTYPE html>
<html>
    <head> 
        <meta charset="utf-8"> 
        <title>W3Cschool(w3cschool.cn)</title> 
    </head>
    <body>

        <form action="/statics/demosource/demo-form.php">
          <input type="number" name="points" step="3">
          <input type="submit">
        </form>

        <p><strong>注意：</strong> Internet Explorer 9及更早IE版本，或Firefox不支持 input 标签的 step 属性。</p>

    </body>
</html>
```

