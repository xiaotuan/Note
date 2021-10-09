[toc]

### 1. Kotlin 版本

```kotlin
import javax.xml.parsers.DocumentBuilderFactory

val xml = StringBuild()

val dbf = DocumentBuilderFactory.newInstance()
val db = dbf.newDocumentBuilder()

val input = InputSource()
input.characterStream = StringReader(xml.toString())
val doc = db.parse(input)

val nodes = doc.getElementsByTagName("user")
var names = ArrayList<String>()
var i = 0
while (i < nodes.length) {
    names.add(nodes.item(i).attributes.getNamedItem("name").nodeValue)
    i++
}
```

### 2. Java 版本

```java
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;
import org.xml.sax.InputSource;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

StringBuild xml = new StringBuild();

DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
DocumentBuilder db = dbf.newDocumentBuilder();

InputSource input = new InputSource();
input.setCharacterStream(new StringReader(xml.toString()));
Document doc = db.parse(input);

NodeList nodes = doc.getElementsByTagName("user");
ArrayList<String> names = new ArrayList<>();
int i = 0;
while (i < nodes.getLength()) {
    names.add(nodes.item(i).getAttributes().getNamedItem("name").getNodeValue());
    i++;
}
```

### 3. 要解析的 xml 内容

```xml
<apress>
    <users>
        <user name="Sheran" email="sheranapress@gmail.com" />
        <user name="Kevin" email="kevin@example.com" />
        <user name="Scott" email="scottm@example.com" />
    </users>
</apress>
```

