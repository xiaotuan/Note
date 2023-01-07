[toc]

### 1. 不带命名空间的文档

要建立一颗 DOM 树，你可以从一个空的文档开始。通过调用 `DocumentBuilder` 类的 `newDocument` 方法可以得到一个空文档。

```java
Document doc = builder.newDocument();
```

使用 `Document` 类的 `createElement` 方法可以构建文档里的元素：

```java
Element rootElement = doc.createElement(rootName);
Element childElement = doc.createElement(childName);
```

使用 `createTextNode` 方法可以构建文本节点：

```java
Text textNode = doc.createTextNode(textContents);
```

使用以下方法可以给文档添加根元素，给父节点添加子节点：

````java
doc.appendChild(rootElement);
rootElement.appendChild(childElement);
childElement.appendChild(textNode);
````

在建立 DOM 树时，可能还需要设置元素属性，这只需调用 `Element` 类的 `setAttribute` 方法即可：

```java
rootElement.setAttribute(name, value);
```

### 2. 带命名空间的文档

如果要使用命名空间，那么创建文档的过程就会稍微有些差异。

首先，需要将生成器工厂设置为是命名空间感知的，然后再创建生成器：

```java
DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
factory.setNamespaceAware(true);
builder = factory.newDocumentBuilder();
```

然后使用 `createElementNS` 而不是 `createElement` 来创建所有节点：

```java
String namespace = "http://www.w3.org/2000/svg";
Element rootElement = doc.createElementNS(namespace, "svg");
```

如果节点具有带命名空间前缀的限定名，那么所有必需的带有 xmlns 前缀的属性都会被自动创建。例如，如果需要在 HTML 中包含 SVG，那么久可以像下面这样构建元素：

```java
Element svgElement = doc.createElement(namespace, "svg:svg");
```

当该元素被写入 XML 文件时，它会转变为：

```xml
<svg:svg xmlns:svg="http://www.w3.org/2000/svg"></svg:svg>
```

如果需要设置的元素属性的名字位于命名空间中，那么可以使用 `Element` 类的 `setAttributeNS` 方法：

```java
rootElement.setAttributeNS(namespace, qualifiedName, value);
```

### 3. 写出文档

为了将 DOCTYPE 节点纳入输出，我们还需要将 SYSTEM 和 PUBLIC 标识符设置为输出属性。

```java
// construct the do-nothing transformation
Transformer t = TransformerFactory.newInstance().newTransformer();
// set output properties to get a DOCTYPE node
t.setOutputProperty(OutputKeys.DOCTYPE_SYSTEM, systemIdentifier);
t.setOutputProperty(OutputKeys.DOCTYPE_PUBLIC, publickIdentifier);
// set indentation
t.setOutputProperty(OutputKeys.INDENT, "yes");
t.setOutputProperty(OutputKeys.METHOD, "xml");
t.setOutputProperty("{http://xml.apache.org/xslt}indent-amout", "2");
// apply the do-nothing transformation and send the output to a file
t.transform(new DOMSource(doc), new StreamResult(new FileOutputStream(file)));
```

另一种方式是使用 `LSSerializer` 接口。为了获取实例，可以使用下面的代码：

```java
DOMImplementation impl = doc.getImplementation();
DOMImplementationLS implLS = (DOMImplementationLS) impls.getFeature("LS", "3.0");
LSSerializer ser = implLS.createLSSerializer();
```

如果需要空格和换行，可以设置下面的标志：

```java
ser.getDomConfig().setParameter("format-pretty-print", true);
```

然后可以易如反掌地将文档转换为字符串：

```java
String str = ser.writeToString(doc);
```

如果想要将输出直接写入到文件中，则需要一个 `LSOutput`：

```java
LSOutput out = implLS.createLSOutput();
out.setEncoding("UTF-8");
out.setByteStream(Files.newOutputStream(path));
ser.write(doc, out);
```

### 4. 使用 StAX 写出 XML 文档

StAX API 使我们可以直接将 XML 树写出，这需要从某个 `OutputStream` 中构建一个 `XMLStreamWriter`，就像下面这样：

```java
XMLOutputFactory factory = XMLOutputFactory.newInstance();
XMLStreamWriter writer = factory.createXMLStreamWriter(out);
```

要产生 XML 文件头，需要调用：

```xml
writer.writeStartDocument();
```

然后调用

```java
writer.writeStartElement(name);
```

添加属性需要调用：

```java
writer.writeAttribute(name, value);
```

现在，可以通过再次调用 `writeStartElement` 添加新的子节点，或者用下面的调用写出字符：

```java
writer.writeCharacters(text);
```

在写完所有子节点之后，调用：

```java
writer.writeEndElement();
```

要写出没有子节点的元素（例如 `<img../>`），可以使用下面的调用：

```java
writer.writeEmptyElement(name);
```

最后，在文档的结尾，调用：

```java
writer.writeEndDocument();
```

### 6. 示例代码

```java
import java.awt.Color;
import java.awt.Dimension;
import java.awt.EventQueue;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.geom.Rectangle2D;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import javax.swing.JComponent;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.stream.XMLOutputFactory;
import javax.xml.stream.XMLStreamException;
import javax.xml.stream.XMLStreamWriter;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;

import org.w3c.dom.Document;
import org.w3c.dom.Element;

public class XMLWriteTest {

	public static void main(String[] args) {
		EventQueue.invokeLater(() -> {
			JFrame frame = new XMLWriteFrame();
			frame.setTitle("XMLWriteTest");
			frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			frame.setVisible(true);
		});
	}

}

class XMLWriteFrame extends JFrame {
	
	private RectangleComponent comp;
	private JFileChooser chooser;
	
	public XMLWriteFrame() {
		chooser = new JFileChooser();
		
		// add component to frame
		
		comp = new RectangleComponent();
		add(comp);
		
		// set up menu bar
		
		JMenuBar menuBar = new JMenuBar();
		setJMenuBar(menuBar);
		
		JMenu menu = new JMenu("File");
		menuBar.add(menu);
		
		JMenuItem newItem = new JMenuItem("New");
		menu.add(newItem);
		newItem.addActionListener(event -> comp.newDrawing());
		
		JMenuItem saveItem = new JMenuItem("Save with DOM/XSLT");
		menu.add(saveItem);
		saveItem.addActionListener(event -> saveDocument());
		
		JMenuItem saveStAXItem = new JMenuItem("Save with StAX");
		menu.add(saveStAXItem);
		saveStAXItem.addActionListener(event -> saveStAX());
		
		JMenuItem exitItem = new JMenuItem("Exit");
		menu.add(exitItem);
		exitItem.addActionListener(event -> System.exit(0));
		pack();
	}
	
	public void saveDocument() {
		try {
			if (chooser.showSaveDialog(this) != JFileChooser.APPROVE_OPTION) {
				return;
			}
			File file = chooser.getSelectedFile();
			Document doc = comp.buildDocument();
			Transformer t = TransformerFactory.newInstance().newTransformer();
			t.setOutputProperty(OutputKeys.DOCTYPE_SYSTEM, "http://www.w3.org/TR/2000/CR-SVG-20000802/DTD/svg-20000802.dtd");
			t.setOutputProperty(OutputKeys.DOCTYPE_PUBLIC, "-//W3C//DTD SVG 20000802//EN");
			t.setOutputProperty(OutputKeys.INDENT, "yes");
			t.setOutputProperty(OutputKeys.METHOD, "xml");
			t.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "2");
			t.transform(new DOMSource(doc), new StreamResult(Files.newOutputStream(file.toPath())));
		} catch (TransformerException | IOException ex) {
			ex.printStackTrace();
		}
	}
	
	public void saveStAX() {
		if (chooser.showSaveDialog(this) != JFileChooser.APPROVE_OPTION) {
			return;
		}
		File file = chooser.getSelectedFile();
		XMLOutputFactory factory = XMLOutputFactory.newInstance();
		try {
			XMLStreamWriter writer = factory.createXMLStreamWriter(Files.newOutputStream(file.toPath()));
			try {
				comp.writeDocument(writer);
			} finally {
				writer.close();	// Not autocloseable
			}
		} catch (XMLStreamException | IOException ex) {
			ex.printStackTrace();
		}
	}
}

class RectangleComponent extends JComponent {
	
	private static final Dimension PREFERRED_SIZE = new Dimension(300, 200);
	
	private List<Rectangle2D> rects;
	private List<Color> colors;
	private Random generator;
	private DocumentBuilder builder;
	
	public RectangleComponent() {
		rects = new ArrayList<>();
		colors = new ArrayList<>();
		generator = new Random();
		
		DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
		factory.setNamespaceAware(true);
		try {
			builder = factory.newDocumentBuilder();
		} catch (ParserConfigurationException e) {
			e.printStackTrace();
		}
	}
	
	public void newDrawing() {
		int n = 10 + generator.nextInt(20);
		rects.clear();
		colors.clear();
		for (int i = 1; i <= n; i++) {
			int x = generator.nextInt(getWidth());
			int y = generator.nextInt(getHeight());
			int width = generator.nextInt(getWidth() - x);
			int height = generator.nextInt(getHeight() - y);
			rects.add(new Rectangle(x, y, width, height));
			int r = generator.nextInt(256);
			int g = generator.nextInt(256);
			int b = generator.nextInt(256);
			colors.add(new Color(r, g, b));
		}
		repaint();
	}
	
	public void paintComponent(Graphics g) {
		if (rects.size() == 0) {
			newDrawing();
		}
		Graphics2D g2 = (Graphics2D) g;
		
		// draw all rectangles
		for (int i = 0; i < rects.size(); i++) {
			g2.setPaint(colors.get(i));
			g2.fill(rects.get(i));
		}
	}
	
	public Document buildDocument() {
		String namespace = "http://www.w3.org/200/svg";
		Document doc = builder.newDocument();
		Element svgElement = doc.createElementNS(namespace, "svg");
		doc.appendChild(svgElement);
		svgElement.setAttribute("width", "" + getWidth());
		svgElement.setAttribute("height", "" + getHeight());
		for (int i = 0; i < rects.size(); i++) {
			Color c = colors.get(i);
			Rectangle2D r = rects.get(i);
			Element rectElement = doc.createElementNS(namespace, "rect");
			rectElement.setAttribute("x", "" + r.getX());
			rectElement.setAttribute("y", "" + r.getY());
			rectElement.setAttribute("width", "" + r.getWidth());
			rectElement.setAttribute("height", "" + r.getHeight());
			rectElement.setAttribute("fill", String.format("#%06x", c.getRGB() & 0xFFFFFF));
			svgElement.appendChild(rectElement);
		}
		return doc;
	}
	
	public void writeDocument(XMLStreamWriter writer) throws XMLStreamException {
		writer.writeStartDocument();
		writer.writeDTD("<!DOCTYPE svg PUBLIC \"-//W3C/DTD SVG 20000802//EN\" \"http://www.w3.org/TR/2000/CR-SVG-20000802/DTD/svg-20000802.dtd\">");
		writer.writeStartElement("svg");
		writer.writeDefaultNamespace("http://www.w3.org/2000/svg");
		writer.writeAttribute("width", "" + getWidth());
		writer.writeAttribute("height", "" + getHeight());
		for (int i = 0; i < rects.size(); i++) {
			Color c = colors.get(i);
			Rectangle2D r = rects.get(i);
			writer.writeEmptyElement("rect");
			writer.writeAttribute("x", "" + r.getX());
			writer.writeAttribute("y", "" + r.getY());
			writer.writeAttribute("width", "" + r.getWidth());
			writer.writeAttribute("height", "" + r.getHeight());
			writer.writeAttribute("fill", String.format("#%06x", c.getRGB() & 0xFFFFFF));
		}
		writer.writeEndDocument();
	}
	
	public Dimension getPreferredSize() {
		return PREFERRED_SIZE;
	}
}
```

