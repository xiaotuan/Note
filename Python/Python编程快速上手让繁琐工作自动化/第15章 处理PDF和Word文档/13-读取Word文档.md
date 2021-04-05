### 15.3.1　读取Word文档

让我们尝试使用 `docx` 模块。从异步社区本书对应页面下载demo.docx，并将它保存在当前工作目录中。然后在交互式环境中输入以下代码：

```javascript
 >>> import docx
❶ >>> doc = docx.Document('demo.docx')
❷ >>> len(doc.paragraphs)
   7
❸ >>> doc.paragraphs[0].text
   'Document Title'
❹ >>> doc.paragraphs[1].text
   'A plain paragraph with some bold and some italic'
❺ >>> len(doc.paragraphs[1].runs)
   4
❻ >>> doc.paragraphs[1].runs[0].text
   'A plain paragraph with some '
❼ >>> doc.paragraphs[1].runs[1].text
   'bold'
❽ >>> doc.paragraphs[1].runs[2].text
   ' and some '
❾ >>> doc.paragraphs[1].runs[3].text
   'italic'
```

在❶行，我们在Python中打开了一个.docx文档，通过调用 `docx.Document()` 来传入文档名demo.docx。这将返回一个 `Document` 对象，它有 `paragraphs` 属性，是 `Paragraph` 对象的列表。如果我们对 `doc.paragraphs` 调用 `len()` ，将返回7。这告诉我们，该文档有7个 `Paragraph` 对象❷。每个 `Paragraph` 对象都有一个 `text` 属性，该属性包含该段中文本的字符串（没有样式信息）。这里，第一个 `text` 属性包含 `'DocumentTitle'` ❸，第二个包含 `'A plain paragraph with some bold and some italic'` ❹。

每个 `Paragraph` 对象也有一个 `runs` 属性，它是 `Run` 对象的列表。 `Run` 对象也有一个 `text` 属性，包含特定运行中的文本。我们看看第二个 `Paragraph` 对象中的 `text` 属性： `'A plain paragraph with some bold and some italic'` 。对这个 `Paragraph` 对象调用 `len()` ，结果告诉我们有4个 `Run` 对象❺。第一个对象包含 `'A plain paragraph with some '` ❻。然后，文本变为粗体样式，因此 `'bold'` 开始了一个新的 `Run` 对象❼。在这之后，文本又回到了非粗体的样式，这导致了第三个 `Run` 对象： `' and some '` ❽。最后，第四个对象包含 `'italic'` ，是斜体样式❾。

有了python-docx，Python程序就能从.docx文档中读取文本，像使用其他的字符串值一样使用它。

