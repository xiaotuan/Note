### 2.1.2　HTML文档

服务端读取URL，理解我们的请求是什么，然后回应一个HTML文档。该文档实质上就是一个文本文件，我们可以使用TextMate、Notepad、vi或Emacs打开它。和大多数文本文档不同，HTML文档具有由万维网联盟指定的格式。该规范当然已经超出了本书的范畴，不过还是让我们看一个简单的HTML页面。当访问 `http://example.com` 时，可以在浏览器中选择 **View Page Source** （查看页面源代码）以看到与其相关的HTML文件。在不同的浏览器中，具体的过程是不同的；在许多系统中，可以通过右键单击找到该选项，并且大部分浏览器在你按下Ctrl + U快捷键（或Mac系统中的Cmd + U）时可以显示源代码。

> <img class="my_markdown" src="../images/2.png" style="width:69px;  height: 87px; " width="8%"/>
> 在一些页面中，该功能可能无法使用。此时，需要通过单击Chrome菜单，然后选择 **Tools**  |  **View Source** 才可以。

下面是 `http://example.com` 目前的HTML源代码。

```python
<!doctype html>
<html>
  <head>
      <title>Example Domain</title>
      <meta charset="utf-8" />
      <meta http-equiv="Content-type"
              content="text/html; charset=utf-8" />
      <meta name="viewport" content="width=device-width,
              initial-scale=1" />
      <style type="text/css"> body { background-color: ...
              } }</style>
  <body>
      <div>
              <h1>Example Domain</h1>
              <p>This domain is established to be used for
                 illustrative examples examples in documents.
                 You may use this domain in examples without
                 prior coordination or asking for permission.</p>
              <p><a href="http://www.iana.org/domains/example">
                 More information...</a></p>
      </div>
  </body>
</html>

```

我将这个HTML文档进行了格式化，使其更具可读性，而你看到的情况可能是所有文本在同一行中。在HTML中，空格和换行在大多数情况下是无关紧要的。

尖括号中间的文本（比如 `<html>` 或 `<head>` ）被称为标签。 `<html>` 是起始标签，而 `</html>` 是结束标签。这两种标签的唯一区别是/字符。这说明，标签是成对出现的。虽然一些网页对于结束标签的使用比较粗心（比如，为独立的段落使用单一的 `<p>` 标签），但是浏览器有很好的容忍度，并且会尝试推测结束的 `</p>` 标签应该在哪里。

`<p>` 和 `</p>` 标签中的所有东西被称为 `HTML` 元素。请注意，元素中可能还包括其他元素，比如示例中的 `<div>` 元素，或是包含 `<a>` 元素的第二个 `<p>` 元素。

有些标签会更加复杂，比如 `<a href="<a class="my_markdown" href="['http://www.iana.org/domains/example']">http://www.iana.org/domains/example</a>">` 。含有URL的 `href` 部分被称为属性。

最后，许多元素还包含文本，比如 `<h1>` 元素中的 `"Example Domain"` 。

对于我们来说，好消息是这些标签并不都是重要的。唯一可见的东西是body元素中的元素，即 `<body>` 和 `</body>` 标签之间的元素。 `<head>` 部分对于指明诸如字符编码的元信息来说非常重要，不过Scrapy能够处理大部分此类问题，所以很多情况下不需要关注HTML页面的这个部分。

