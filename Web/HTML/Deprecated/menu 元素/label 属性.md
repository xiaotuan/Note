[toc]

> 注意：在 HTML5 中，重定义了 `<menu>` 元素，且新增了 `label` 属性。

### 1. 浏览器支持

目前几乎没有主流浏览器支持 `label` 属性。

### 2. 定义和用法

`label` 属性规定了菜单的可见标签。

`label` 属性通常用于显示菜单内嵌套的菜单标签。

### 3. 语法

```html
<menu label="text">
```

### 4. 属性值

| 值   | 描述                 |
| :--- | :------------------- |
| text | 规定菜单的可见标签。 |

### 5. 示例

```html
<html>
    <head>
        <meta charset="utf-8"> 
        <title>W3Cschool(w3cschool.cn)</title> 
    </head>
    <body>

        <menu type="toolbar">
         <li>
          <menu label="File">
           <button type="button" onclick="file_new()">New...</button>
           <button type="button" onclick="file_open()">Open...</button>
           <button type="button" onclick="file_save()">Save</button>
          </menu>
         </li>
         <li>
          <menu label="Edit">
           <button type="button" onclick="edit_cut()">Cut</button>
           <button type="button" onclick="edit_copy()">Copy</button>
           <button type="button" onclick="edit_paste()">Paste</button>
          </menu>
         </li>
        </menu>

        <p><b>注意:</b>目前主流浏览器并不支持 menu 标签。</p>

    </body>
</html>
```

