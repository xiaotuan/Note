[toc]

### 1. 支持浏览器

所有主流浏览器都支持 `autocomplete` 属性。

> **提示：**在某些浏览器中，您可能需要手动启用自动完成功能（在浏览器菜单的"参数设置"中进行设置）。

### 2. 定义和用法

`autocomplete` 属性规定输入字段是否应该启用自动完成功能。

自动完成允许浏览器预测对字段的输入。当用户在字段开始键入时，浏览器基于之前键入过的值，应该显示出在字段中填写的选项。

> 注意
>
> `autocomplete` 属性适用于下面的 `<input>` 类型：text、search、url、tel、email、password、datepickers、range 和 color。

### 3. HTML 可用版本

HTML 5 可用

### 4. 语法

```html
<input autocomplete="on|off">
```

### 5. 属性值

| 值   | 描述                         |
| :--- | :--------------------------- |
| on   | 默认。规定启用自动完成功能。 |
| off  | 规定禁用自动完成功能。       |

### 6. 示例

```html
<!DOCTYPE html>
<html>
    <head> 
        <meta charset="utf-8"> 
        <title>W3Cschool(w3cschool.cn)</title> 
    </head>
    <body>

        <form action="/statics/demosource/demo-form.php" autocomplete="on">
          First name:<input type="text" name="fname" value="你好"><br>
          Last name: <input type="text" name="lname"><br>
          E-mail: <input type="email" name="email" autocomplete="off" placehder="nihao"><br>
          <input type="submit">
        </form>

        <p>填写并提交表单，然后重新刷新页面查看如何自动填充内容。</p>
        <p>注意 form的 autocomplete属性为  "on"（开），但是e-mail自动为“off”（关）。</p>

    </body>
</html>
```

