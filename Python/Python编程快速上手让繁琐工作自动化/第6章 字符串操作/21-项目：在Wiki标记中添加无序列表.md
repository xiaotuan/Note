### 6.7　项目：在Wiki标记中添加无序列表

在编辑一篇维基百科的文章时，你可以创建一个无序列表，即让每个表项占据一行，并在前面放置一个星号。假设你有一个非常大的列表，希望在前面添加星号，你可以在每一行开始处输入这些星号，一行接一行；也可以用一小段Python脚本，将这个任务自动化。

bulletPointAdder.py脚本将从剪贴板中取得文本，并在每一行开始处加上星号和空格，然后将这段新的文本贴回剪贴板。例如，如果我将下面的文本复制到剪贴板（取自维基百科的文章“List of Lists of Lists”）：

```javascript
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
```

然后运行bulletPointAdder.py程序，剪贴板中就会包含下面的内容：

```javascript
* Lists of animals
* Lists of aquarium life
* Lists of biologists by author abbreviation
* Lists of cultivars
```

这段前面加了星号的文本，就可以粘贴回维基百科的文章中，成为一个无序列表。

