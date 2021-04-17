### 19.2.1　XML 文档结构

XML 规范是由 W3C（World Wide Web Consortium）定义的一组指南，用于以纯文本的形式描述结构化数据，一种基于尖括号间标签的标记语言。XML 没有一组固定的标签。相反，XML 是一种可用于创建其他标记语言的元语言。XML文档的组成主要有以下几部分。

#### 1．XML处理指令

```c
<?xml version="1.0" standalone="yes" encoding="UTF-8"?>
```

这是一个XML处理指令。处理指令以"<?"开始，以"?>"结束。"<?"后的第一个单词是指令名，如xml, 代表XML声明。

version、standalone、 encoding 是三个特性，特性是由等号分开的名称—数值对，等号左边是特性名称，等号右边是特性的值，用引号引起来。

+ version：说明这个文档符合1.0规范。
+ standalone：说明文档在这一个文件里还是需要从外部导入、standalone 的值设为yes，说明所有的文档都在这一文件里完成。
+ encoding：指文档字符编码 。

#### 2．XML 根元素定义

XML文档的树形结构要求必须有一个根元素。根元素的起始标记要放在所有其它元素起始标记之前，根元素的结束标记要放在其他所有元素的结束标记之后，如：

```c
<?xml version="1.0"  standalone="yes"  encoding="UTF-8"?>
<Settings>
        <Person>Zhang San</Person>
</Settings>
```

#### 3．XML元素

元素的基本结构由开始标记、数据内容、结束标记组成，所有的数据内容都必须在某个标记的开始和结束标记内，而每个标记又必须包含在另一个标记的开始与结束标记内，形成嵌套式的分布，只有最外层的标记不必被其他的标记所包含。最外层的是根元素（Root），所有的元素都包含在根元素内。如：

```c
<Person>
        <Name>Zhang San</Name>
        <Sex>Male</Sex>
</Person>
```

需要注意的是，元素标记区分大小写，<Name> 与 <name>是两个不同的标记。结束标记必须有反斜杠，如 </Name> 。

+ XML元素标记命名规则如下。
+ 名字中可以包含字母，数字及其它字母。
+ 名字不能以数字或下划线开头。
+ 名字不能用xml开头。
+ 名字中不能包含空格和冒号 。

#### 4．XML属性

XML元素可以设置属性，用来描述元素的特性，属性名和属性值必须是成对出现的，属性值必须用引号引起来，通常使用双引号，除非属性值本身包含了双引号，这时可以用单引号来代替。

```c
<Person nation=“China”>
        <Name>Zhang San</Name>
        <Sex>Male</Sex>
</Person>
```

#### 5．XML中的注释

XML中注释如下。

```c
 <!-- this is comment -->
```

需要注意以下几点。

+ 注释中不要出现“--”或“-”。
+ 注释不要放在标记中。
+ 注释不能嵌套。

#### 6．CDATA

CDATA用于需要把整段文本解释成纯字符数据而不是标记的情况。当一些文本中包含很多“<”、“>”、“&”、“"”等字符而非标记时，CDATA会非常有用。

```c
<Example>
        <![CDATA[
                <Person>
                        <Name>Zhang San</Name>
                        <Sex  Male</Sex> 
<    /P  erson>
        ]]>
</Example>
```

以“<![CDATA[” 开始，以“]]>”结束。注意，在CDATA段中不要出现结束定界符“]]>”。

#### 7．Entities(实体)

Entities是XML的存储单元，一个实体可以是字符串、文件、数据库记录等。实体的用处主要是为了避免在文档中重复输入，我们可以为一个文档定义一个实体名，然后在文档里引用实体名来代替这个文档，XML解析文档时，实体名会被替换成相应的文档。

XML为五个字符定义了实体名。

| 实体 | 字符 |
| :-----  | :-----  | :-----  | :-----  |
| < | < |
| > | > |
| &amp; | & |
| &quot; | " |
| &apos; | ' |

定义并引用实体的示例：

```c
<!DOCTYPE example [
<!ENTITY intro "Here is some comment for entity of XML">
]>
<example>
        <hello>&intro;</hello>
</example>
```

#### 8．DOCTYPE

```c
“<!DOCTYPE[]>”紧随XML声明，包括所有实体的声明，如下所示。
<!DOCTYPE example 
declare your entities here
]
<example>
        Body of document
</example>
```

下面的文档显示一个保存书店图书信息的自定义 XML 文档。

```c
01  <?xml version="1.0" encoding="utf-8" ?>
02  <bookstore>
03          <books  catalog="计算机">
04                  <book ISBN="978-7-115-21928-2">
05                  <bookname>C#网络应用技术</bookname>
06                  <price>36.00</price>
07                  <author>马骏</author>
08                  <publisher>人民邮电出版社</publisher>
09          </book>
10          <book ISBN="978-7-302-33411-8">
11                  <bookName>C#高级编程</bookName>
12                  <price>148.00</price>
13                  <author>Christian Nagel</author>
14                  <publisher>清华大学出版社</publisher>
15          </book>
16          <books>
17          </bookstore>
```

此文件中的第一行即是文件处理指令。该行是一个XML文件必须要声明的东西，而且也必须位于XML文件的第一行，它主要是告诉XML解析器如何工作。其中，version是标明此XML文件所用的标准的版本号，必须要有；encoding指明了此XML文件中所使用的字符类型，可以省略，在省略此声明的时候，后面的字符码必须是Unicode字符码（建议不要省略）。因为我们在这个例子中使用的是GB 2312字符码，所以encoding这个声明也不能省略。

文件的其余部分属于文件主体，XML文件的内容信息存放在此。我们可以看到，文件主体由开始的<bookstore>和结束的</bookstore>标记组成，这个称为XML文件的“根元素”；<books>是作为直属于根元素下的“子元素”；在<books>下又有<book>“子元素”；在<book>标记下又有<bookName>、<price>、<author>、<publisher>这些子元素。catalog是<books>元素中的一个“属性”，“计算机”则是“属性值”。

