XML 文档应当以一个文档头开始，例如：

```xml
<?xml version="1.0"?>
```

或者

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

严格来说，文档头是可选的，但是强烈推荐你使用文档头。

文档头之后通常是文档类型定义，例如：

```xml
<!DOCTYPE web-app PUBLIC "-//Sun Microsystems, Inc.//DTD Web Application 2.2//EN" "http://java.sun.com/j2ee/dtds/web-app_2_2.dtd">
```

文档类型定义是确保文档正确的一个重要机制，但是它不是必须的。

最后，XML 文档的正文包含根元素，根元素包含其他元素。例如：

```xml
<?xml version="1.0"?>
<!DOCTYPE configuration ...>
<configuration>
	<title>
    	<font>
        	<name>Helvetica</name>
            <size>36</size>
        </font>
    </title>
</configuration>
```

XML 元素可以包含属性，例如：

```xml
<size unit="pt">36</size>
```

> 提示：属性只应该用来修改值的解释，而不是用来指定值。

元素和文本是 XML 文档 "主要的支撑要素"，你可能还会遇到其他一些标记，说明如下：

+ 字符引用的形式是 `&#` 十进制值；或 `&#x` 十六进制值；例如：

  ```
  &#233; &#xE9;
  ```

+ 实体引用形式是 `&name;`。例如：

  ```
  &lt; &gt; &amp; &quot; &apos;
  ```

+ CDATA 部分（CDATA Section）用 `<![CDATA[` 和 `]]>` 来限定其界限。它们是字符数据的一种特殊形式。你可以使用它们来囊括那些含有 `<` 、`>`、`&` 之类字符的字符串，而不必将它们解释为标记，例如：

  ```xml
  <![CDATA[< & > are my favorite delimiters]]>
  ```

  > 注意：CDATA 部分不能包含字符串 `]]>`。

+ 处理指令是哪些专门在处理 XML 文档的应用程序中使用的指令，它们由 `<?` 和 `?>` 来限定其界限，例如：

  ```xml
  <?xml-stylesheet href="mystyle.css" type="text/css"?>
  ```

  每个 XML 都以一个处理指令开头：

  ```xml
  <?xml version="1.0"?>
  ```

+ 注释用 `<!--` 和 `-->` 限定其界限，例如：

  ```xml
  <!-- This is a comment.	-->
  ```

  > 注意：注释不应该含有字符串 `--`。

  