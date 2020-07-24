EJS 模板的一个示例：

```js
<% if (names.length) { %>
    <ul>
        <% names.forEach(function (name) { %>
            <li><%= name %></li>
        <% }) %>
    </ul>
<% } %>
```

尖括号和百分号组成的符号对 ( <% , %> ) 用于表达 EJS。

输出一个变量值本身用等号，代表 “在此处打印该值” ：

```js
<%= name %>
```

要打印出来转义的值，使用一个间隔符：

```js
<%- name %>
```

如果不想使用表述 EJS 的开闭标志 ( <% , %>) ，可以通过 EJS 对象提供的 open，close 方法自定义标识符:

```js
ejs.open("<<");
ejs.close(">>");
```

然后就可以使用自定义的标识符了：

```
<h1><<= title >></h1>
```