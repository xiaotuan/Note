XSL 转换（XSLT）机制可以指定将 XML 文档转换为其他格式的规则，例如，转换为纯文本、XHTML 或任何其他的 XML 格式。XSLT 通常用来将某种机器可读的 XML 格式转译为另一种机器可读的 XML 格式，或者将 XML 转译为适于人类阅读的表示格式。

假设我们想要把有雇员记录的 XML 文件转换成 HTML 文件。请看这个输入文件：

```xml
<staff>
	<employee>
    	<name>Carl Cracker</name>
        <salary>75000</salary>
        <hiredate year="1987" month="12" day="15" />
    </employee>
    <employee>
    	<name>Harry Hacker</name>
        <salary>50000</salary>
        <hiredate year="1989" month="10" day="1" />
    </employee>
    <employee>
    	<name>Tony Tester</name>
        <salary>40000</salary>
        <hiredate year="1990" month="3" day="15" />
    </employee>
</staff>
```

我们希望的输出是一张 HTML 表格：

```html
<table border="1">
    <tr>
    	<td>Carl Cracker</td><td>$75000.0</td><td>1987-12-15</td>
    </tr>
    <tr>
    	<td>Harry Hacker</td><td>$50000.0</td><td>1989-10-1</td>
    </tr>
    <tr>
    	<td>Carl Cracker</td><td>$40000.0</td><td>1990-3-15</td>
    </tr>
</table>
```

具有转换模板的样式形式如下：

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
	<xsl:output method="html" />
    template1
    template2
    ...
</xsl:stylesheet>
```

下面是一个典型的模板：

```xml
<xsl:template match="/staff/employee">
	<tr><xsl:apply-templates/></tr>
</xsl:template>
```

match 属性的值是一个 XPath 表达式。该模板声明：每当看到 XPath 集 `/staff/employee` 中的一个节点时，将做以下操作：

1）产生字符串 `<tr>`。

2）在处理其子节点时，持续应用该模板。

3）当处理完所有子节点后，产生字符串 `</tr>`。

下面是一个用来转换雇员记录文件中的 name 节点的模板：

```xml
<xsl:template match="/staff/employee/name">
	<td><xsl:apply-templates/></td>
</xsl:template>
```

如果想要把属性值复制到输出中去，就不得不再做一些稍微复杂的操作了。下面是一个例子：

```xml
<xsl:template match="/staff/employee/hiredate">
	<td><xsl:value-of select="@year"/>-<xsl:value-of select="@month"/>-<xsl:value-of select="@day"</td>
</xsl:template>
```

在 Java 平台下产生 XML 的转换极其简单，只需为每个样式表设置一个转换器工厂，然后得到一个转换器对象，并告诉它把一个源转换成结果。

```java
File styleSheet = new File(filename);
StreamSource styleSource = new StreamSource(styleSheet);
Transformer t = TransformerFactory.newInstance().newTransformer(styleSource);
t.transform(source, result);
```

`transform` 方法的参数是 `Source` 和 `Result` 接口的实现类的对象。`Source` 接口有 4 个实现类：

```
DOMSource
SAXSource
StAXSource
StreamSource
```

你可以从一个文件、流、阅读器或 URL 中构建 `StreamSource` 对象，或者从 DOM 树节点中构建 `DOMSource` 对象。例如，在上一节中，我们调用了如下的标识转换：

```java
t.transform(new DOMSource(doc), result);
```

**示例代码：**

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.StringTokenizer;

import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.sax.SAXSource;
import javax.xml.transform.stream.StreamResult;
import javax.xml.transform.stream.StreamSource;

import org.xml.sax.ContentHandler;
import org.xml.sax.DTDHandler;
import org.xml.sax.EntityResolver;
import org.xml.sax.ErrorHandler;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;
import org.xml.sax.SAXNotRecognizedException;
import org.xml.sax.SAXNotSupportedException;
import org.xml.sax.XMLReader;
import org.xml.sax.helpers.AttributesImpl;

public class TransformTest {

	public static void main(String[] args) throws Exception {
		Path path;
		if (args.length > 0) {
			path = Paths.get(args[0]);
		} else {
			path = Paths.get("C:\\Users\\XiaoTuan\\Desktop", "makehtml.xsl");
		}
		try (InputStream styleIn = Files.newInputStream(path)) {
			StreamSource styleSource = new StreamSource(styleIn);
			
			Transformer t = TransformerFactory.newInstance().newTransformer(styleSource);
			t.setOutputProperty(OutputKeys.INDENT, "yes");
			t.setOutputProperty(OutputKeys.METHOD, "xml");
			t.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "2");
			
			try (InputStream docIn = Files.newInputStream(Paths.get("C:\\Users\\XiaoTuan\\Desktop", "employee.dat"))) {
				t.transform(new SAXSource(new EmployeeReader(), new InputSource(docIn)), new StreamResult(System.out));
			}
		}
	}
}

class EmployeeReader implements XMLReader {
	
	private ContentHandler handler;
	
	public void parse(InputSource source) throws IOException, SAXException {
		InputStream stream = source.getByteStream();
		BufferedReader in = new BufferedReader(new InputStreamReader(stream));
		String rootElement = "staff";
		AttributesImpl atts = new AttributesImpl();
		
		if (handler == null) {
			throw new SAXException("No content handler");
		}
		
		handler.startDocument();
		handler.startElement("", rootElement, rootElement, atts);
		String line;
		while ((line = in.readLine()) != null) {
			handler.startElement("", "employee", "employee", atts);
			StringTokenizer t = new StringTokenizer(line, "|");
			
			handler.startElement("", "name", "name", atts);
			String s = t.nextToken();
			handler.characters(s.toCharArray(), 0, s.length());
			handler.endElement("", "name", "name");
			
			handler.startElement("", "salary", "salary", atts);
			s = t.nextToken();
			handler.characters(s.toCharArray(), 0, s.length());
			handler.endElement("", "salary", "salary");
			
			atts.addAttribute("", "year", "year", "CDATA", t.nextToken());
			atts.addAttribute("", "month", "month", "CDATA", t.nextToken());
			atts.addAttribute("", "day", "day", "CDATA", t.nextToken());
			handler.startElement("", "hiredate", "hiredate", atts);
			handler.endElement("", "hiredate", "hiredate");
			atts.clear();
			
			handler.endElement("", "employee", "employee");
		}
		
		handler.endElement("", rootElement, rootElement);
		handler.endDocument();
	}
	
	public void setContentHandler(ContentHandler newValue) {
		handler = newValue;
	}
	
	public ContentHandler getContentHandler() {
		return handler;
	}
	
	// the following methods are just do-nothing implementations
	@Override
	public void parse(String systemId) throws IOException, SAXException {}
	@Override
	public void setErrorHandler(ErrorHandler handler) {}
	@Override
	public ErrorHandler getErrorHandler() { return null; }
	@Override
	public void setDTDHandler(DTDHandler handler) {}
	@Override
	public DTDHandler getDTDHandler() { return null; }
	@Override
	public void setEntityResolver(EntityResolver resolver) {}
	@Override
	public EntityResolver getEntityResolver() { return null; }
	@Override
	public void setProperty(String name, Object value) throws SAXNotRecognizedException, SAXNotSupportedException {}
	@Override
	public Object getProperty(String name) throws SAXNotRecognizedException, SAXNotSupportedException { return null; }
	@Override
	public void setFeature(String name, boolean value) throws SAXNotRecognizedException, SAXNotSupportedException {}
	@Override
	public boolean getFeature(String name) throws SAXNotRecognizedException, SAXNotSupportedException { return false; }
}
```

**makehtml.xsl**

```xsl
<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet 
   xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
   version="1.0">

   <xsl:output method="html"/>

   <xsl:template match="/staff">
      <table border="1"><xsl:apply-templates/></table>
   </xsl:template>

   <xsl:template match="/staff/employee">
      <tr><xsl:apply-templates/></tr>
   </xsl:template>

   <xsl:template match="/staff/employee/name">
      <td><xsl:apply-templates/></td>
   </xsl:template>

   <xsl:template match="/staff/employee/salary">
      <td>$<xsl:apply-templates/></td>
   </xsl:template>

   <xsl:template match="/staff/employee/hiredate">
      <td><xsl:value-of select="@year"/>-<xsl:value-of 
      select="@month"/>-<xsl:value-of select="@day"/></td>
   </xsl:template>

</xsl:stylesheet>
```

**employee.dat**

````
Carl Cracker|75000.0|1987|12|15
Harry Hacker|50000.0|1989|10|1
Tony Tester|40000.0|1990|3|15
````

