### 18.5　查询DOM元素

`getElementById` ， `getElementsByClassName` 和 `getElementsByTagName` 这些方法都非常有用，但其实还有更多常用（且强大）的方法可以用来定位元素，它们不仅可以通过单个条件（ID，class，和name）定位元素，还能通过元素之间的关系来定位元素。 `document` 上的 `querySelector` 和 `querySelectorAll` 方法就允许使用CSS_选择器来定位元素。

CSS选择器允许通过元素的名字（ `<p>` 、 `<div>` 、等）、ID、class（或组合class）、或者这些内容的组合来识别元素。要通过名字来定位元素，只需要使用元素的名字（不加尖括号）即可。所以a会匹配DOM中所有的<a>标签，br则会匹配所有<br>标签。而要通过class识别元素，只需要在class名字前面加一个句点符号：比如.callout可以匹配所有使用了callout这个class的元素。要匹配多个class时，多个class之间也用句点符号来分隔：.callout.fancy会匹配所有使用了callout和fancy这两个class的元素。最后，还可以把这些选择器组合起来使用，比如， `a#callout2.cal lout.fancy` 会匹配所有ID为callout2，且具有callout和fancy class的<a>标签（一般很少会见到在选择器中既使用元素名字和ID，又使用class（多个）的情况，但不排除这种可能性）。

熟悉CSS选择器的最好方法是在浏览器中加载本章中的HTML，打开console，然后试着用 `querySelectorAll` 来选择元素。比如，可以在console中输入 ** `document.querySelector.All('.callout')` ** 。本节中所有的例子都会显示出至少一条查询结果。

到目前为止，我们已经讨论过如何定位指定元素，不论它在DOM中的什么位置。而CSS选择器也允许通过元素在DOM中所处的位置来定位它们。

如果将多个CSS选择器通过空格分隔，就能查找到一个具有特定祖先的节点。比如，#content p会选择所有在ID为content的元素中的<p>元素。同样， `#content div p` 会选择出所有在 `<div>` 中的 `<p>` 元素，而这些 `<div>` 又在ID为 `content` 的元素中。

如果将多个元素选择器用大于号（>）分隔，就可以找到那些直接的子节点。例如， `#content>p` 会选出那些ID为content的元素中作为子节点的<p>元素。（注意和“#content p”区分开）。

注意，也可以把祖先选择器和直接子节点选择器结合起来使用。比如，body .content>p会从<body>的子节点中选出class属性为content的所有直接子节点中的 <p>标签。

还有更复杂的选择器，上面提到的都是最常见的。如果想学习更多的选择器用法，参阅MDN上关于CSS选择器的文档（<a class="my_markdown" href="['http://mzl.la/1Pxcg2f']">http://mzl.la/1Pxcg2f</a>）。

