### 19.2.2　操作XML的命名空间和相关类

#### 1．C#对XML的支持

.NET框架提供了对XML的强大支持，而且.NET框架本身也普遍采用XML格式来存储各种配置信息，比如我们前面讲到的应用程序配置文件App.config文件。

在.NET类库中，名称空间System.Xml下面就包含了大量的操作XML文档的类型。这些类型构成了两种XML文档的处理模型。

（1）流式处理模型。

在流式处理模型中，我们将XML文档作为一个数据流来进行处理，将逐个处理XML文档中的数据。在这种模型下，我们可以快速读取大体积的XML文档，而且内存占用少，程序性能好。类型System.Xml.XmlReader就提供了流式处理模型，使用XmlReader就可以快速读取XML文档。

使用流式处理模型是有缺点的，首先它只能读取XML文档，不能修改XML文档；其次是检索XML文档内容不方便，不能使用XPath技术；而且编程接口比较简单，处理XML文档不够方便。当程序需要比较简单地从XML文档读取数据，则可以采用流式处理模型。

（2）DOM处理模型。

在DOM处理模型中，我们首先使用文档对象模型的思想解析整个XML文档，在内存中生成一个对象树来表述XML文档。比如使用一个XmlElement对象来映射到XML文档中的一个元素，使用XmlAttribute对象来映射到XML文档中的一个属性。这样我们编程操作内存中的对象就映射为操作XML文档。

使用DOM处理XML文档具有相当大的优点，首先是处理方便，我们可以使用各种编程技巧来处理XML文档对象树状结构，比如可以递归遍历XML文档的一部分或全部，可以向树状结构插入、修改或删除XML元素，可以设置XML元素的属性。

在DOM模式下，我们可以使用XPath技术在XML文档树状结构中进行快速检索和定位，这为处理XML文档带来比较大的方便。

在C#中，我们可以很简单地使用DOM方式处理XML文档。首先实例化一个System.Xml.XmlDocument类型，调用它的Load方法即可加载XML文档并生成XML节点对象树状结构，然后就可以遍历这个对象树，新增、修改和删除节点，而且其中的任意一个节点都可以使用SelectNodes或SelectSingleNode方法通过XPath相对路径快速查找其他的节点。

在名称空间System.Xml下面大部分类型都是用来支持DOM处理模型的。其中很多类型配合起来共同组织成XMLDOM，XMLDOM是一种很典型的文档对象模型的应用。

System.Xml名称空间下的支持DOM的类型主要有以下几种。

+ XmlNode 是DOM结构中的所有类型的基础类型，它定义了所有XML节点的通用属性和方法，是XMLDOM的基础。它具有一个ChildNodes属性，表示它所包含的子XML节点。
+ XmlAttribute 表示XML属性，它只保存在XmlElement的Attributes 列表中。
+ XmlDocument表示XML文档本身，是XMLDOM模型中的顶级对象，它用于对XML文档进行整体的控制，并且是其他程序访问XML文档对象树的唯一入口。
+ XmlLinkedNode在XmlNode的基础上实现了访问前后同级节点的方法。
+ XmlElement元素表示XML元素，是XMLDOM中使用最多的对象类型。它具有Attributes属性可以处理它所拥有的属性，可以使用ChildNodes属性获得它所有的子节点，并提供了一些添加和删除子节点的方法。
+ XmlCharacterData表示XML文档中的字符数据的基础类型。字符文本数据是分布在各个XMLElement之间的纯文本数据。XmlAttribute中的文本数据是不属于XML文本块的。
+ XmlCDATASection 表示XML文档中的CDATA节，CDATA数据是采用“<![CDATA[ ]]>”包括起来的纯文本数据。由于XML采用尖括号进行标记，因此具有和HTML类似的转义字符。在一般的XML纯文本段中若遇到尖括号等特殊字符时，需要使用转义字符，当文本段中包含大量的这类特殊字符时，手动书写和查看XML文档将比较困难，为了改善XML文档的可读性，在此可以使用CDATA节。在CDATA节中，所有的字符，包括特殊字符都不需要转义，这样查看和修改XML文档都比较方便。
+ XmlComment表示一段注释，XML注释和HTML注释一样，使用一对“<!-- -->”包含起来。
+ XmlText表示一段纯文本数据。
+ XmlWhitespace表示XML文档中一段纯粹由空白字符组成的文本块，空白字符包括空格、制表符、换行和回车符，全角空格不属于空白字符。XmlDocument在解析XML文档时会处理空白字符，当XmlDocument对象的PreserveWhitespace属性为true时，会为XML文档中的纯空白文本块生成XmlWhitespace对象；若该属性为false时，则会忽略掉纯空白文本，不会生成XmlWhitespace对象，好像原始的XML文档中不存在这样的空白文本块一样。

#### 2．操作XML文档常用类

.Net框架为我们提供了以下一些命名空间：System.Xml、System.Xml.Schema、System.Xml.Serialization、System.Xml.Xpath以及 System.Xml.Xsl来包容与XML操作相关的类。本文中我们将主要讨论System.Xml命名空间，其他的内容请读者自行查阅相关资料。

System.Xml命名空间包含各种各样的XML类，这些类可使用读取器、编写器和符合W3C DOM 要求的组件来对 XML 数据进行分析、验证和操作。下面列出了XML命名空间中主要的类。

+ XmlNode：是重要的抽象类，DOM树中的每个节点都应是它的派出。
+ XmlDocument类 ：实现 W3C 文档对象模型级别1核心以及核心DOM级别2。
+ XmlTextReader类 ：提供对XML数据的快速、非缓存和只进的读取访问。
+ XmlNodeReader类 ：为给定的DOM节点子树提供 XmlReader。
+ XmlValidatingReader类 ：提供DTD、XDR和XSD架构验证。
+ XmlTextWriter类 ：提供生成XML的快速、只进的方式。
+ mlDataDocument类 ：提供可与数据集关联的XmlDocument的实现。可通过数据集的关系表示形式或XmlDataDocument的树表示形式同时查看和操作结构化XML。
+ XPathDocument类 ：为XSLT提供了一种进行 XML 文档处理的快速和高性能的缓存。
+ XPathNavigator类 ：为用于存储的W3C XPath 1.0数据模型提供了一种光标样式模型以便于浏览。
+ XslTransform类：是与W3C XSLT 1.0规范兼容的XSLT处理器，用于转换XML文档。
+ XmlSchema 对象模型类：提供一组可进行浏览的类，这些类直接反映W3C XSD规范。它们提供以编程方式创建XSD架构的功能。
+ XmlSchemaCollection类：提供XDR和XSD架构库。这些缓存在内存中的架构为XmlValidating Reader提供快速的、分析时验证XmlReader类。

