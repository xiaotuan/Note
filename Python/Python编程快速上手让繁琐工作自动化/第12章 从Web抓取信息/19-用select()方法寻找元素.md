### 12.5.2　用select()方法寻找元素

调用一个 `BeautifulSoup` 对象的 `select()` 方法，传入一个字符串作为CSS“选择器”，就可以取得一个Web页面元素。选择器就像正则表达式：它们指定了要寻找的模式，在这个例子中，是在HTML页面中寻找，而不是在普通的文本字符串中寻找。

完整地讨论 CSS 选择器的语法超出了本书的范围（在本书的资源中，有很好的选择器指南），这里有一份选择器的简单介绍。表12-2举例展示了大多数常用CSS选择器的模式。

<center class="my_markdown"><b class="my_markdown">表12-2　CSS选择器的例子</b></center>

| 传递给select()方法的选择器 | 将匹配…… |
| :-----  | :-----  | :-----  | :-----  |
| `soup.select('div')` | 所有名为 `<div>` 的元素 |
| `soup.select('#author')` | 带有id属性为author的元素 |
| `soup.select('.notice')` | 所有使用CSS class属性名为notice的元素 |
| `soup.select('div span')` | 所有在 `<div>` 元素之内的 `<span>` 元素 |
| `soup.select('div > span')` | 所有直接在 `<div>` 元素之内的 `<span>` 元素，中间没有其他元素 |
| `soup.select('input[name]')` | 所有名为 `<input>` ，并有一个 `name` 属性，其值无所谓的元素 |
| `soup.select('input[type="button"]')` | 所有名为 `<input>` ，并有一个 `type` 属性，其值为 `button` 的元素 |

不同的选择器模式可以组合起来形成复杂的匹配。例如， `soup.select('p #author')` 将匹配所有 `id` 属性为 `author` 的元素，只要它也在一个 `<p>` 元素之内。你也可以在浏览器中右击元素，选择Inspect Element，而不是自己编写选择器。当浏览器的开发者控制台打开后，右键单击元素的HTML，选择Copy<img class="my_markdown" src="../images/85.png" style=""/>CSS Selector，将选择器字符串复制到剪贴板上，然后粘贴到你的源代码中。

`Select()` 方法将返回一个 `Tag` 对象的列表，这是 `Beautiful Soup` 表示一个HTML元素的方式。针对 `BeautifulSoup` 对象中的HTML的每次匹配，列表中都有一个 `Tag` 对象。 `Tag` 值可以传递给 `str()` 函数，显示它们代表的HTML标签。 `Tag` 值也可以有 `attrs` 属性，它将该 `Tag` 的所有HTML属性作为一个字典。利用前面的example.html文件，在交互式环境中输入以下代码：

```javascript
>>> import bs4
>>> exampleFile = open('example.html')
>>> exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
>>> elems = exampleSoup.select('#author')
>>> type(elems) # elems is a list of Tag objects.
<class 'list'>
>>> len(elems)
1
>>> type(elems[0])
<class 'bs4.element.Tag'>
>>> str(elems[0]) # The Tag object as a string.
'<span id="author">Al Sweigart</span>'
>>> elems[0].getText()
'Al Sweigart'
>>> elems[0].attrs
{'id': 'author'}
```

这段代码将带有 `id="author"` 的元素从示例HTML中找出来。 我们使用 `select('#author')` 返回一个列表，其中包含所有带有 `id="author"` 的元素。我们将这个 `Tag` 对象的列表保存在变量 `elems` 中， `len(elems)` 告诉我们列表中只有一个 `Tag` 对象，且只有一次匹配。在该元素上调用 `getText()` 方法，以返回该元素的文本或内部的HTML。一个元素的文本是在开始和结束标签之间的内容：在这个例子中，就是 `'Al Sweigart'` 。

将该元素传递给 `str()` ，以返回一个字符串，其中包含开始和结束标签，以及该元素的文本。最后， `attrs` 给了我们一个字典，其中包含该元素的属性 `'id'` ，以及 `id` 属性的值 `'author'` 。

也可以从 `BeautifulSoup` 对象中找出 `<p>` 元素。在交互式环境中输入以下代码：

```javascript
>>> pElems = exampleSoup.select('p')
>>> str(pElems[0])
'<p>Download my <strong>Python</strong> book from <a href="https://
inv">my  website</a>.</p>'
>>> pElems[0].getText()
'Download my Python book from my website.'
>>> str(pElems[1])
'<p class="slogan">Learn Python the easy way!</p>'
>>> pElems[1].getText()
'Learn Python the easy way!'
>>> str(pElems[2])
'<p>By <span id="author">Al Sweigart</span></p>'
>>> pElems[2].getText()
'By Al Sweigart'
```

这一次， `select()` 给我们一个列表，该列表包含3次匹配，我们将该列表保存在 `pElems` 中。在 `pElems[0]` 、 `pElems[1]` 和 `pElems[2]` 上使用 `str()` ，这将每个元素显示为一个字符串。在每个元素上使用 `getText()` 以显示它的文本。

