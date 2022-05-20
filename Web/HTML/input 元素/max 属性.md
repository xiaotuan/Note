[toc]

### 1. 浏览器支持

Internet Explorer 10、Opera、Chrome 和 Safari 支持 `max` 属性。

> **注意：**Firefox 或者 Internet Explorer 9 及之前的版本不支持 `<input>` 标签的 `max` 属性。

> **注意：**由于 Internet Explorer 10 不支持这些 `input` 类型，`max` 属性将不适用于 IE 10 中的 date 和 time。

### 2. 定义和用法

`max` 属性规定 `<input>` 元素的最大值。

> **提示：**`max` 属性与 `min` 属性配合使用，可创建合法值范围。

> **注意：**`max` 和 `min` 属性适用于以下 `input` 类型：number、range、date、datetime、datetime-local、month、time 和 week。

### 3. HTML 可用版本

HTML 5

### 4. 语法

```html
<input max="number|date">
```

### 5. 属性值

| 值     | 描述                               |
| :----- | :--------------------------------- |
| number | 数字值。规定输入字段允许的最大值。 |
| date   | 日期。规定输入字段允许的最大值。   |

### 6. 示例

```html
<!DOCTYPE html>
<html>
    <head> 
        <meta charset="utf-8"> 
        <title>W3Cschool(w3cschool.cn)</title> 
    </head>
    <body>

        <form action="/statics/demosource/demo-form.php">

         输入 1980-01-01 之前的日期:
          <input type="date" name="bday" max="1979-12-31"><br>

         输入 2000-01-01 之后的日期:
          <input type="date" name="lday" min="2000-01-02"><br>

          数量 (在1和5之间):
          <input type="number" name="quantity" min="1" max="5"><br>

          <input type="submit">
        </form>

        <p><strong>注意:</strong> Internet Explorer 9及更早IE版本，Firefox不支持input标签的  max 和 min 属性。</p>
        <p><strong>注意:</strong>在Internet Explorer 10中max 和 min属性不支持输入日期和时间，IE 10 不支持这些输入类型。</p>

    </body>
</html>
```

