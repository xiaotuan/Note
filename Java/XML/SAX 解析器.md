SAX 解析器在解析 XML 输入数据的各个组成部分时会报告事件，但不会以任何方式存储文档，而是由事件处理器建立相应的数据结构。

在使用 SAX 解析器时，需要一个处理器来为各种解析器事件定义事件动作。`ContentHandler` 接口定义了若干个在解析文档时解析器会调用的回调方法。下面是最重要的几个：

+ `startElement` 和 `endElement` 在每当遇到起始或终止标签时调用。
+ `characters` 在每当遇到字符数据时调用。
+ `startDocument` 和 `endDocument` 分别在文档开始和结束时各调用一次。

例如，在解析以下片段时：

```xml
<font>
	<name>Helvetica</name>
    <size units="pt">36</size>
</font>
```

下面是如何得到 SAX 解析器的代码：

```java
SAXParserFactory factory = SAXParserFactory.newInstance();
SAXParser parser = factory.newSAXParser();
```

现在可以处理文档了：

```java
parser.parse(source, handler);
```

handler 属于 `DefaultHandler` 的一个子类，`DefaultHandler` 类为以下四个接口定义了空的方法：

```
ContentHandler
DTDHandler
EntityResolver
ErrorHandler
```

示例程序定义了一个处理器，它覆盖了 ContentHandler 接口的 `startElement` 方法，以观察带有 href 属性的 a 元素。

```java
DefaultHandler handler = new DefaultHandler() {
    public void startElement(String namespaceURI, String lname, String qname, Attributes attrs) throws SAXException {
        if (lname.equalsIgnoreCase("a") && attrs != null) {
            for (int i = 0; i < attrs.getLength(); i++) {
                String aname = attrs.getLocalName(i);
                if (aname.equalsIgnoreCase("href")) {
                    System.out.println(attrs.getValue(i));
                }
            }
        }
    }
};
```

与 DOM 解析器一样，命名空间处理特性默认是关闭，可以调用工厂类的 `setNamespaceAware` 方法来激活命名空间处理特性：

```java
SAXParserFactory factory = SAXParserFactory.newInstance();
factory.setNamespaceAware(true);
SAXParser saxParser = factory.newSAXParser();
```

XHTML 文件总是以一个包含对 DTD 引用的标签开头，解析器会加载这个 DTD。如果你不需要验证文件，只需调用：

```java
factory.setFeature("http://apache.org/xml/features/nonvalidating/load-external-dtd", false);
```

**示例代码：**

```java
import java.io.InputStream;
import java.net.URL;

import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;

import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;

public class SAXTest {

	public static void main(String[] args) throws Exception {
		String url;
		if (args.length == 0) {
			url = "https://www.w3.org/TR/xmlschema-0/";
			System.out.println("Using " + url);
		} else {
			url = args[0];
		}
		
		DefaultHandler handler = new DefaultHandler() {
		    public void startElement(String namespaceURI, String lname, String qname, Attributes attrs) throws SAXException {
		        if (lname.equalsIgnoreCase("a") && attrs != null) {
		            for (int i = 0; i < attrs.getLength(); i++) {
		                String aname = attrs.getLocalName(i);
		                if (aname.equalsIgnoreCase("href")) {
		                    System.out.println(attrs.getValue(i));
		                }
		            }
		        }
		    }
		};
		
		SAXParserFactory factory = SAXParserFactory.newInstance();
		factory.setNamespaceAware(true);
//		factory.setFeature("https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd", false);
		SAXParser saxParser = factory.newSAXParser();
		InputStream in = new URL(url).openStream();
		saxParser.parse(in, handler);
	}

}
```

