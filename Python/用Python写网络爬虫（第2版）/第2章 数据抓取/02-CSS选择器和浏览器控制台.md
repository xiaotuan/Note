类似我们在使用 `cssselect` 时使用的标记，CSS 选择器可以表示选择元素时所使用的模式。下面是一些你需要知道的常用选择器示例。

```console
Select any tag: *
Select by tag <a>: a
Select by class of "link": .link
Select by tag <a> with class "link": a.link
Select by tag <a> with ID "home": a#home
Select by child <span> of tag <a>: a > span
Select by descendant <span> of tag <a>: a span
Select by tag <a> with attribute title of "Home": a[title=Home]
```

`cssselect` 库实现了大部分 CSS3 选择器的功能，其不支持的功能可以查看 <https://cssselect.readthedocs.io/en/latest/#supported-selectors> 。