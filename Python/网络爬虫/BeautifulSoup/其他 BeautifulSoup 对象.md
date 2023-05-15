+ **BeautifulSoup 对象** 

+ **标签 Tag 对象**

  BeautifulSoup 对象通过 `find` 和 `findAll` ，或者直接调用子标签获取的一列对象或单个对象，就像：

  ```python
  bsObj.div.h1
  ```

+ **NavigableString 对象**

  用来表示标签里的文字，不是标签。

+ **Comment 对象**

+ 用来查找 HTML 文档的注释标签，`<!-- 像这样 -->`