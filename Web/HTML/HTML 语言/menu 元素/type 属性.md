[toc]

> 注意：在 HTML5 中，重定义了 `<menu>` 元素，且新增了 `type` 属性。

### 1. 浏览器支持

目前几乎没有主流浏览器支持 `type` 属性。

### 2. 定义和用法

`type` 属性规定菜单的类型。

### 3. 语法

```html
<menu type="list|context|toolbar">
```

### 4. 属性值

| 值      | 描述                                                         |
| :------ | :----------------------------------------------------------- |
| list    | 默认。规定一个列表菜单。一个用户可执行或激活的命令列表（li 元素）。 |
| context | 规定一个上下文菜单。菜单必须在用户与命令进行交互之前被激活。 |
| toolbar | 规定一个工具栏菜单。主动式命令，允许用户立即与命令进行交互。 |

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

