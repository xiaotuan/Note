[toc]

### 5.4　使用Query String来解析参数

在本章前面的内容中我们使用过 `Query String` 模块。它唯一的功能就是准备和处理查询字符串（ `query String` ）。

当你拿到一个查询字符串时，你可以用 `querystring.parse()` 将它转化为一个对象，如例5-1所展示的那样。默认的查询字符串分割器（ `'&amp;amp;'` ）可以使用可选的第二个参数来修改，默认的赋值符号（ `'='` ）可以使用第三个参数来修改。第四个可选参数包含一个 `decodeURIComponent` ，默认情况下会使用 `querystring. unescape()` 。如果查询字符串不是UTF-8编码，就需要修改为UTF-8。不过，大部分情况下你的查询字符串用的就是默认的分割符号、赋值符号和UTF-8编码，所以不需要指定这么多参数。

接下来让我们看看 `querystring.parse()` 函数是如何工作的，对于下面的查询字符串：

```python
somedomain.com/?value1=valueone&value1=valueoneb&value2=valuetwo
```

`querystring.parse()` 函数将会返回下面的结果：

```python
{ 
   value1: ['valueone','valueoneb'],
   value2: 'valuetwo'
}
```

如果要生成一个查询字符串，如例5-2所示，我们需要使用 `querystring. stringify()` 函数，传入需要进行转换的对象就可以。所以，如果你有一个类似于我们上面解析出来的对象，将它传给 `querystring.stringify()` ，你就会得到一个格式化后的查询字符串，它可以直接使用。在例5-2中， `querystring. stringify ()` 返回了下面的结果：

```python
msg=Hello%20World!
```

请注意，空格被转码了。除了最后一个参数的对象外， `querystring.stringify()` 函数使用了和 `querystring.parse()` 一样的可选参数。你可以提供一个自定义的 `encodeURIC omponent` 对象，否则就会使用默认的 `stringify.escape()` 函数。

