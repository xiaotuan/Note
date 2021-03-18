[toc]

### 2.5　LXML和家族树

`lxml` 同样也有遍历HTML页面中家族树的能力。家族树是什么？当你使用浏览器的开发者工具来查看页面中的元素时，你可以展开或缩进它们，这就是在观察HTML的家族关系。网页中的每个元素都包含父亲、兄弟和孩子。这些关系可以帮助我们更加容易地遍历页面。

例如，当我希望查找页面中同一节点深度的所有元素时，就需要查找它们的兄弟；或是我希望得到页面中某个特定元素的所有子元素时。 `lxml` 允许我们通过简单的Python代码大量使用此类关系。

作为示例，让我们来查看示例页面中 `table` 元素的所有子元素。

```python
>>> table = tree.xpath('//table')[0]
>>> table.getchildren()
[<Element tr at 0x7f525158ec78>,
 <Element tr at 0x7f52515ad638>,
 <Element tr at 0x7f52515ad5e8>,
 <Element tr at 0x7f52515ad688>,
 <Element tr at 0x7f52515ad728>,
...]
```

我们还可以查看表格的兄弟元素和父元素。

```python
>>> prev_sibling = table.getprevious()
>>> print(prev_sibling)
None
>>> next_sibling = table.getnext()
>>> print(next_sibling)
<Element div at 0x7f5252fe9138>
>>> table.getparent()
<Element form at 0x7f52515ad3b8>
```

如果你需要更加通用的方式来访问页面中的所有元素，那么结合XPath表达式遍历家族关系是一个能够让你不丢失任何内容的好方式。它可以帮助你从许多不同类型的页面中抽取内容，你可以通过识别页面中那些元素附近的内容，来识别页面中某些重要的部分。即使该元素没有可识别的CSS选择器，该方法同样也可以工作。

