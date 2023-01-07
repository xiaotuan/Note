StAX 解析器是一种 "拉解析器（pull parser）"，与安装事件处理器不同，你只需使用下面这样的基本循环来迭代所有的事件：

```java
InputStream in = url.openStream();
XMLInputFactory factory = XMLInputFactory.newInstance();
XMLStreamReader parser = factory.createXMLStreamReader(in);
while (parser.hasNext()) {
    int event = parser.next();
    // call parser methods to obtain event details
}
```

要分析属性值，需要调用如下方法：

```java
String units = parser.getAttributeValue(null, "units");
```

默认情况下，命名空间处理是启用的，你可以通过像下面这样修改工厂来使其无效：

```java
XMLInputFactory factory = XMLInputFactory.newInstance();
factory.setProperty(XMLInputFactory.IS_NAMESPACE_AWARE, false);
```

**示例代码：**

```java
import java.io.InputStream;
import java.net.URL;

import javax.xml.stream.XMLInputFactory;
import javax.xml.stream.XMLStreamConstants;
import javax.xml.stream.XMLStreamReader;

public class StAXTest {

	public static void main(String[] args) throws Exception {
		String urlString;
		if (args.length == 0) {
			urlString = "https://www.w3.org/TR/xmlschema-0/";
			System.out.println("Using " + urlString);
		} else {
			urlString = args[0];
		}
		
		URL url = new URL(urlString);
		InputStream in = url.openStream();
		XMLInputFactory factory = XMLInputFactory.newInstance();
		XMLStreamReader parser = factory.createXMLStreamReader(in);
		while (parser.hasNext()) {
			int event = parser.next();
			if (event == XMLStreamConstants.START_ELEMENT) {
				if (parser.getLocalName().equals("a")) {
					String href = parser.getAttributeValue(null, "href");
					if (href != null) {
						System.out.println(href);
					}
				}
			}
		}
	}

}
```

