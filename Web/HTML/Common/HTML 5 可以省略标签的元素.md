在 `HTML5` 中，有些元素可以省略标签。具体来讲有如下 3 种情况：

+ 不允许写结束标记的元素有 `area`、`base`、`br`、`col`、`command`、`embed`、`hr`、`img`、`input`、`keygen`、`link`、`meta`、`param`、`source`、`track`、`wbr`。

  不允许写结束标记的元素是指不允许使用开始标记与结束标记将元素括起来的的形式，只允许使用 “<元素/>” 的形式进行书写。例如，`<br>…</br>` 的写法是错误的。应该写成 `<br/>`”。但是，沿袭下来的 `<br>` 这种写法也是允许的。

+ 可以省略结束标签的元素有 `li`、`dt`、`dd`、`p`、`rt`、`rp`、`optgroup`、`option`、`colgroup`、`thead`、`tbody`、`tfoot`、`tr`、`td`、`th`。

+ 可以省略整个标签的元素有 `html`、`head`、`body`、`colgroup`、`tbody`。