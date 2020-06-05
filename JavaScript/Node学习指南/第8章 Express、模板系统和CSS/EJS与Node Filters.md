Node EJS 还提供了一系列预先定义的 filter，可以进一步简化 HTML 的生成过程。比如，一个名为 first 的 filter，对给定数组可以取出第一个值。另一个 filter -- downcase，接收 first filter 的结果并改为小写：

```js
var names = ['Joe Brown', 'Mary Smith', 'Tom Thumb', 'Cinder Ella']
var str = '<p><%=: users | first | downcase %></p>'
var html = ejs.render(str, { users: names })
输出结果：
<p>joe brown</p>
```

filters 可以链式调用，上一个 filter 的结果会传递给下一个作为参数。filter 的使用由等号之后紧跟的冒号触发，之后跟着数据对象。

```js
var people = [
    { name: 'Joe Brown', age: 32 },
    { name: 'Mary Smith', age: 54 },
    { name: 'Tom Thumb', age: 21 },
    { name: 'cinder Ella', age: 16 }
]
var str = "<p><%=: people | map: 'name' | sort | join %></p>"
var html = ejs.render(str, { people: people })
输出结果：
Cinder Ella, Joe Brown, Mary Smith, Tom Thumb
```

**表8-1 Node EJS filters**

| Filter | 数据类型 | 作用 |
| :-: | :- | :- |
| first | 接收并返回数组 | 返回数组第一个元素 |
| last | 接收并返回数组 | 返回数组最后一个元素 |
| capitalize | 接收并返回字符串 | 字符串第一个字母大写 |
| downcase | 接收并返回字符串 | 字符串全部转换为小写 |
| upcase | 接收并返回字符串 | 字符串全部转换为大写 |
| sort | 接收并返回数组 | 对数组应用 Array.sort 方法 |
| sort_bt: 'prop' | 接收数组和属性名称；返回数组 | 创建自定义的排序方法，根据属性对数组排序 |
| Size | 接收数组：返回数值 | 返回 Array.length |
| Plus:n | 接收两个数字或者字符串：返回数值 | 返回 a \+ b |
| Minus:n | 接收两个数值或者字符串：返回数值 | 返回 a \- b |
| Times:n | 接收两个数值或者字符串： 返回数值 | 返回 a \* b |
| Devided_by:n | 接收两个数值或者字符串：返回数值 | 返回 a / b |
| Join:'val' | 接收数组：返回字符串 | 用给定值或默认值应用 Array.join 方法 |
| truncate:n | 接收字符串和长度数值；返回字符串 | 引用 String.substr |
| truncate_words:n | 接收字符串和单词数；返回字符串 | 应用 String.spit，String.splice |
| Replace:pattern，substitution | 接收字符串、模板和替换内容；返回字符串 | 应用 String.replace |
| Prepend:value | 接收字符串和 value 字符串；返回字符串 | 把 value 加在字符串之前 |
| Append:value | 接收字符串和 value 字符串；返回字符串 | 把 value 拼在字符串之后 |
| Map:'prop' | 接收字符串和属性：返回数组 | 用 Array.map方法根据给定对象属性创建新的字符串 |
| Reverse | 接收数组或者字符串 | 如果是数组，应用 Array.reverse; 如果是字符串，分解单词，翻转，再拼接 |
| Get | 接收对象和属性 | 返回给定对象的该属性值 |
| Json | 接收对象 | 转换为 JSON 字符串 |
