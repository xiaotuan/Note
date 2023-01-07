`XPath` 语言使得访问树节点变得很容易。例如，假设有如下 XML 文档：

```xml
<configuration>
	...
    <database>
    	<username>dbuser</username>
        <password>secret</password>
        ...
    </database>
</configuration>
```

可以通过对 `XPath` 表达式 `/configuration/database/username` 求值来得到 database 中的 username 的值。

使用 `XPath` 执行下列操作比普通的 DOM 方式要简单得多：

1）获得文档节点。

2）枚举它的子元素。

3）定位 database 元素。

4）定位其子节点中名字为 username 的节点。

5）定位其子节点中的 text 节点。

6）获取其数据。

`XPath` 可以描述 XML 文档中的一个节点集，例如，下面的 XPath：

```
/gridbag/row
```

描述了根元素 gridbag 的子元素中所有的 row 元素。可以用 `[]` 操作符来选择特定元素：

```
/gridbag/row[1]
```

这表示的是第一行（索引号从 1 开始）。

使用 `@` 操作符可以得到属性值。`XPath` 表达式：

```
/gridbag/row[1]/cell[1]/@anchor
```

`XPath` 有很多有用的函数，例如：

```
count(/gridbag/row)
```

返回 gridbag 根元素的 row 子元素的数量。精细的 `XPath` 表达式还有很多，请参见 <http://www.w3c.org/TR/xpath> 的规范，或者在 <http://www.zvon.org/xxl/XPathTutorial/General/examples.html> 上的一个非常好的在线指南。

Java SE 5.0 增加了一个 API 来计算 XPath 表达式，首先需要从 `XPathFactory` 创建一个 XPath 对象：

```java
XPathFactory xpfactory = XPathFactory.newInstance();
path = xpfactory.newXPath();
```

然后，调用 `evaluate` 方法来计算 `XPath`  表达式：

```java
String username = path.evaluate("/configuration/database/username", doc);
```

如果 `XPath` 表达式产生了一组节点，请做如下调用：

```java
NodeList nodes = (NodeList) path.evaluate("/gridbag/row", doc, XPathConstants.NODESET);
```

如果结果只有一个节点，则以 `XPathConstants.NODE` 代替：

```java
Node node = (Node) path.evaluate("/gridbag/row[1]", doc, XPathConstants.NODE);
```

如果结果是一个数字，则使用 `XPathConstants.NUMBER`：

```java
int count = ((Number) path.evaluate("count(/gridbag/row)", doc, XPathConstants.NUMBER)).intValue();
```

不必从文档的根节点开始搜索，可以从任意一个节点或节点列表开始。例如，如果你有前一次计算得到的节点，那么就可以调用：

```java
result = path.evaluate(expression, node);
```

**示例代码：**

```java
import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.StringJoiner;

import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.border.TitledBorder;
import javax.xml.namespace.QName;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpressionException;
import javax.xml.xpath.XPathFactory;

import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

public class XPathTester {

	public static void main(String[] args) {
		EventQueue.invokeLater(() -> {
			JFrame frame = new XPathFrame();
			frame.setTitle("XPathTest");
			frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			frame.setVisible(true);
		});
	}
	
}

class XPathFrame extends JFrame {
	
	private DocumentBuilder builder;
	private Document doc;
	private XPath path;
	private JTextField expression;
	private JTextField result;
	private JTextArea docText;
	private JComboBox<String> typeCombo;
	
	public XPathFrame() {
		JMenu fileMenu = new JMenu("File");
		JMenuItem openItem = new JMenuItem("Open");
		openItem.addActionListener(event -> openFile());
		fileMenu.add(openItem);
		
		JMenuItem exitItem = new JMenuItem("Exit");
		exitItem.addActionListener(event -> System.exit(0));
		fileMenu.add(exitItem);
		
		JMenuBar menuBar = new JMenuBar();
		menuBar.add(fileMenu);
		setJMenuBar(menuBar);
		
		ActionListener listener = event -> evaluate();
		expression = new JTextField(20);
		expression.addActionListener(listener);
		JButton evaluateButton = new JButton("Evaluate");
		evaluateButton.addActionListener(listener);
		
		typeCombo = new JComboBox<String>(new String[] {
				"STRING", "NODE", "NODESET", "NUMBER", "BOOLEAN"
		});
		typeCombo.setSelectedItem("STRING");
		
		JPanel panel = new JPanel();
		panel.add(expression);
		panel.add(typeCombo);
		panel.add(evaluateButton);
		docText = new JTextArea(10, 40);
		result = new JTextField();
		result.setBorder(new TitledBorder("Result"));
		
		add(panel, BorderLayout.NORTH);
		add(new JScrollPane(docText), BorderLayout.CENTER);
		add(result, BorderLayout.SOUTH);
		
		try {
			DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
			builder = factory.newDocumentBuilder();
		} catch (ParserConfigurationException e) {
			JOptionPane.showMessageDialog(this, e);
		}
		
		XPathFactory xpfactory = XPathFactory.newInstance();
		path = xpfactory.newXPath();
		pack();
	}
	
	public void openFile() {
		JFileChooser chooser = new JFileChooser();
		chooser.setCurrentDirectory(new File("."));
		
		chooser.setFileFilter(new javax.swing.filechooser.FileNameExtensionFilter("XML files", "xml"));
		int r = chooser.showOpenDialog(this);
		if (r != JFileChooser.APPROVE_OPTION) {
			return;
		}
		File file = chooser.getSelectedFile();
		try {
			docText.setText(new String(Files.readAllBytes(file.toPath())));
			doc = builder.parse(file);
		} catch (IOException e) {
			JOptionPane.showMessageDialog(this, e);
		} catch (SAXException e) {
			JOptionPane.showMessageDialog(this, e);
		}
	}
	
	public void evaluate() {
		try {
			String typeName = (String) typeCombo.getSelectedItem();
			QName returyType = (QName) XPathConstants.class.getField(typeName).get(null);
			Object evalResult = path.evaluate(expression.getText(), doc, returyType);
			if (typeName.equals("NODESET")) {
				NodeList list = (NodeList) evalResult;
				// Can't use String.join since NodeList isn't Iterable
				StringJoiner joiner = new StringJoiner(",", "{", "}");
				for (int i = 0; i < list.getLength(); i++) {
					joiner.add("" + list.item(i));
				}
				result.setText("" + joiner);
			} else {
				result.setText("" + evalResult);
			}
		} catch (XPathExpressionException e) {
			result.setText("" + e);
		} catch (Exception e) {	// reflection exception
			e.printStackTrace();
		}
	}
}
```

