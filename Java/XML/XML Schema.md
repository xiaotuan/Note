因为 XML Schema 比起 DTD 语法要复杂许多，所以我们只涉及基本知识。更多信息请参考 <https://www.w3.org/TR/xmlschema-0/> 上的指南。

如果要在文档中引用 Schema 文件，需要在根元素中添加属性，例如：

```xml
<?xml version="1.0"?>
<configuration xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
               xsi:noNamespaceSchemaLocation="config.xsd">
	...
</configuration>
```

Schema 为每个元素都定义了类型。类型可以是简单类型，即有格式限制的字符串，或者是复杂类型。一些简单类型已经被内建到了 XML Schema 内，包括：

```
xsd:string
xsd:int
xsd:boolean
```

可以定义自己的简单类型。例如，下面是一个枚举类型：

```xml
<xsd:simpleType name="StyleType">
	<xsd:restriction base="xsd:string">
    	<xsd:enumeration value="PLAIN" />
        <xsd:enumeration value="BOLD" />
        <xsd:enumeration value="ITALIC" />
        <xsd:enumeration value="BOLD_ITALIC" />
    </xsd:restriction>
</xsd:simpleType>
```

当定义元素时，要指定它的类型：

```xml
<xsd:element name="name" type="xsd:string" />
<xsd:element name="size" type="xsd:int" />
<xsd:element name="style" type="StyleType" />
```

类型约束了元素的内容。例如，下面的元素将被验证为具有正确格式：

```xml
<size>10</size>
<style>PLAIN</style>
```

但是，下面的元素会被解析器拒绝：

```xml
<size>default</size>
<style>SLANTED</style>
```

你可以把类型组合成复杂类型，例如：

```xml
<xsd:complexType name="FontType">
	<xsd:sequence>
    	<xsd:element ref="name" />
        <xsd:element ref="size" />
        <xsd:element ref="style" />
    </xsd:sequence>
</xsd:complexType>
```

FontType 是 name、size 和 style 元素的序列。在这个类型定义中，我们使用了 ref 属性来引用在 Schema 中位于别处的定义。也可以嵌套定义，像这样：

```xml
<xsd:complexType name="FontType">
	<xsd:sequence>
    	<xsd:element name="name" type="xsd:string" />
        <xsd:element name="size" type="xsd:int" />
        <xsd:element name="style" typ="StyleType">
        	<xsd:simpleType>
            	<xsd:restriction base="xsd:string">
                	<xsd:enumeration value="PLAIN" />
                    <xsd:enumeration value="BOLD" />
                    <xsd:enumeration value="ITALIC" />
                    <xsd:enumeration value="BOLD_ITALIC" />
                </xsd:restriction>
            </xsd:simpleType>
        </xsd:element>
    </xsd:sequence>
</xsd:complexType>
```

`xsd:sequence` 结构和 DTD 中的连接符号等价，而 `xsd:choice` 结构和 `|` 操作符等价，例如：

```xml
<xsd:complexType name="contactinfo">
	<xsd:choice>
    	<xsd:element ref="email" />
        <xsd:element ref="phone" />
    </xsd:choice>
</xsd:complexType>
```

如果要允许重复元素，可以使用 `minoccurs` 和 `maxoccurs` 属性，例如，与 DTD 类型 item* 等价的形式如下：

```xml
<xsd:element name="item" type="..." minoccurs="0" maxoccurs="unbounded"></xsd:element>
```

如果要指定属性，可以把 `xsd:attribute` 元素添加到 `complexType` 定义中去：

```xml
<xsd:element name="size">
	<xsd:complexType>
    	...
        <xsd:attribute name="unit" type="xsd:string" use="optional" default="cm" />
    </xsd:complexType>
</xsd:element>
```

可以把 Schema 的元素和类型定义封装在 `xsd:schema` 元素中：

```xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
	...
</xsd:schema>
```

解析带有 Schema 的 XML 文件和解析带有 DTD 的文件相似，但有 3 点差别：

1）必须打开对命名空间的支持，即使在 XML 文件里你可能不会用到它。

```java
factory.setNamespaceAware(true);
```

2）必须通过如下的代码来准备好处理 Schema 的工厂。

```java
final String JAXP_SCHEMA_LANGUAGE = "http://java.sun.com/xml/jaxp/properties/schemaLanguage";
final String W3C_XML_SCHEMA = "http://www.w3.org/2001/XMLSchema";
factory.setAttribute(JAXP_SCHEMA_LANGUAGE, W3C_XML_SCHEMA);
```

3）解析器不会丢弃元素中的空白字符。

**示例代码：**

```java
import java.awt.Component;
import java.awt.EventQueue;
import java.awt.Font;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.event.ActionListener;
import java.beans.BeanInfo;
import java.beans.Introspector;
import java.beans.PropertyDescriptor;
import java.io.File;
import java.lang.reflect.Field;

import javax.swing.DefaultComboBoxModel;
import javax.swing.JCheckBox;
import javax.swing.JComboBox;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.w3c.dom.Text;

public class GridBagTest {

	public static void main(String[] args) {
		EventQueue.invokeLater(() -> {
			JFileChooser chooser = new JFileChooser(".");
			chooser.showOpenDialog(null);
			File file = chooser.getSelectedFile();
			JFrame frame = new FontFrame(file);
			frame.setTitle("GridBagTest");
			frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			frame.setVisible(true);
		});
	}

}

class FontFrame extends JFrame {
	
	private GridBagPane gridbag;
	private JComboBox<String> face;
	private JComboBox<String> size;
	private JCheckBox bold;
	private JCheckBox italic;
	
	public FontFrame(File file) {
		gridbag = new GridBagPane(file);
		add(gridbag);
		
		face = (JComboBox<String>) gridbag.get("face");
		size = (JComboBox<String>) gridbag.get("size");
		bold = (JCheckBox) gridbag.get("bold");
		italic = (JCheckBox) gridbag.get("italic");
		
		face.setModel(new DefaultComboBoxModel<String>(new String[] {
				"Serif", "SansSerif", "Monospaced", "Dialog", "DialogInput"
		}));
		
		size.setModel(new DefaultComboBoxModel<String>(new String[] {
				"8", "10", "12", "15", "18", "24", "36", "48"
		}));
		
		ActionListener listener = event -> setSample();
		
		face.addActionListener(listener);
		size.addActionListener(listener);
		bold.addActionListener(listener);
		italic.addActionListener(listener);
		
		setSample();
		pack();
	}
	
	public void setSample() {
		String fontFace = face.getItemAt(face.getSelectedIndex());
		int fontSize = Integer.parseInt(size.getItemAt(size.getSelectedIndex()));
		JTextArea sample = (JTextArea) gridbag.get("sample");
		int fontStyle = (bold.isSelected() ? Font.BOLD : 0) + (italic.isSelected() ? Font.ITALIC : 0);
		
		sample.setFont(new Font(fontFace, fontStyle, fontSize));
		sample.repaint();
	}
}

class GridBagPane extends JPanel {
	
	private GridBagConstraints constraints;
	
	public GridBagPane(File file) {
		setLayout(new GridBagLayout());
		constraints = new GridBagConstraints();
		
		try {
			DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
			factory.setValidating(true);
			
			if (file.toString().contains("-schema")) {
				factory.setNamespaceAware(true);
				final String JAXP_SCHEMA_LANGUAGE = "http://java.sun.com/xml/jaxp/properties/schemaLanguage";
				final String W3C_XML_SCHEMA = "http://www.w3.org/2001/XMLSchema";
				factory.setAttribute(JAXP_SCHEMA_LANGUAGE, W3C_XML_SCHEMA);
			}
			
			factory.setIgnoringElementContentWhitespace(true);
			
			DocumentBuilder builder = factory.newDocumentBuilder();
			Document doc = builder.parse(file);
			parseGridbag(doc.getDocumentElement());
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public Component get(String name) {
		Component[] components = getComponents();
		for (int i = 0; i < components.length; i++) {
			if (components[i].getName().equals(name)) {
				return components[i];
			}
		}
		return null;
	}
	
	private void parseGridbag(Element e) {
		NodeList rows = e.getChildNodes();
		for (int i = 0; i < rows.getLength(); i++) {
			Element row = (Element) rows.item(i);
			NodeList cells = row.getChildNodes();
			for (int j = 0; j < cells.getLength(); j++) {
				Element cell = (Element) cells.item(j);
				parseCell(cell, i, j);
			}
		}
	}
	
	private void parseCell(Element e, int r, int c) {
		// get attributes
		String value = e.getAttribute("gridx");
		if (value.length() == 0) {	// use default
			if (c == 0) constraints.gridx = 0;
			else constraints.gridx += constraints.gridwidth;
		} else {
			constraints.gridy = Integer.parseInt(value);
		}
		
		constraints.gridwidth = Integer.parseInt(e.getAttribute("gridwidth"));
		constraints.gridheight = Integer.parseInt(e.getAttribute("gridheight"));
		constraints.weightx = Integer.parseInt(e.getAttribute("weightx"));
		constraints.weighty = Integer.parseInt(e.getAttribute("weighty"));
		constraints.ipadx = Integer.parseInt(e.getAttribute("ipadx"));
		constraints.ipady = Integer.parseInt(e.getAttribute("ipady"));
		
		// use reflection to get integer values of static fields
		Class<GridBagConstraints> cl = GridBagConstraints.class;
		
		try {
			String name = e.getAttribute("fill");
			Field f = cl.getField(name);
			constraints.fill = f.getInt(cl);
			
			name = e.getAttribute("anchor");
			f = cl.getField(name);
			constraints.anchor = f.getInt(cl);
		} catch (Exception ex) {	// the reflection methods can throw various exceptions
			ex.printStackTrace();
		}
		
		Component comp = (Component) parseBean((Element) e.getFirstChild());
		add(comp, constraints);
	}
	
	private Object parseBean(Element e) {
		try {
			NodeList children = e.getChildNodes();
			Element classElement = (Element) children.item(0);
			String className = ((Text) classElement.getFirstChild()).getData();
			
			Class<?> cl = Class.forName(className);
			
			Object obj = cl.newInstance();
			
			if (obj instanceof Component) {
				((Component) obj).setName(e.getAttribute("id"));
			}
			
			for (int i = 1; i < children.getLength(); i++) {
				Node propertyElement = children.item(i);
				Element nameElement = (Element) propertyElement.getFirstChild();
				String propertyName = ((Text) nameElement.getFirstChild()).getData();
				
				Element valueElement = (Element) propertyElement.getLastChild();
				Object value = parseValue(valueElement);
				BeanInfo beanInfo = Introspector.getBeanInfo(cl);
				PropertyDescriptor[] descriptors = beanInfo.getPropertyDescriptors();
				boolean done = false;
				for (int j = 0; !done && j < descriptors.length; j++) {
					if (descriptors[j].getName().equals(propertyName)) {
						descriptors[j].getWriteMethod().invoke(obj, value);
						done = true;
					}
				}
			}
			return obj;
		} catch (Exception ex) {	// the reflection methods can throw various exceptions
			ex.printStackTrace();
			return null;
		}
	}
	
	private Object parseValue(Element e) {
		Element child = (Element) e.getFirstChild();
		if (child.getTagName().equals("bean")) return parseBean(child);
		String text = ((Text) child.getFirstChild()).getData();
		if (child.getTagName().equals("int")) {
			return new Integer(text);
		} else if (child.getTagName().equals("boolean")) {
			return new Boolean(text);
		} else if (child.getTagName().equals("string")) {
			return text;
		} else {
			return null;
		}
	}
}
```

**fontdialog-schema.xml**

```xml
<?xml version="1.0"?>
<gridbag xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:noNamespaceSchemaLocation="gridbag.xsd">
   <row>
      <cell anchor="EAST">
      <bean>
        <class>javax.swing.JLabel</class>
        <property>
          <name>text</name>
          <value><string>Face: </string></value>
        </property>
      </bean>
    </cell>
    <cell fill="HORIZONTAL" weightx="100">
      <bean id="face">
        <class>javax.swing.JComboBox</class>
      </bean>
    </cell>
    <cell gridheight="4" fill="BOTH" weightx="100" weighty="100">
      <bean id="sample">
        <class>javax.swing.JTextArea</class>
        <property>
          <name>text</name>
          <value><string>The quick brown fox jumps over the lazy dog</string></value>
        </property>
        <property>
          <name>editable</name>
          <value><boolean>false</boolean></value>
        </property>
        <property>
          <name>lineWrap</name>
          <value><boolean>true</boolean></value>
        </property>
        <property>
          <name>border</name>
          <value>
            <bean>
              <class>javax.swing.border.EtchedBorder</class>
            </bean>
          </value>
        </property>
      </bean>
    </cell>
  </row>
  <row>
    <cell anchor="EAST">
      <bean>
        <class>javax.swing.JLabel</class>
        <property>
          <name>text</name>
          <value><string>Size: </string></value>
        </property>
      </bean>
    </cell>
    <cell fill="HORIZONTAL" weightx="100">
      <bean id="size">
        <class>javax.swing.JComboBox</class>
      </bean>
    </cell>
  </row>
  <row>
    <cell gridwidth="2" fill="NONE" weighty="100" >
      <bean id="bold">
        <class>javax.swing.JCheckBox</class>
        <property>
          <name>text</name>
          <value><string>Bold</string></value>
        </property>
      </bean>
    </cell>
  </row>
  <row>
    <cell gridwidth="2" fill="NONE" weighty="100" >
      <bean id="italic">
        <class>javax.swing.JCheckBox</class>
        <property>
          <name>text</name>
          <value><string>Italic</string></value>
        </property>
      </bean>
    </cell>
  </row>
</gridbag>
```

**gridbag.dtd**

```xml
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">

   <xsd:element name="gridbag" type="GridBagType"/>

   <xsd:element name="bean" type="BeanType"/>

   <xsd:complexType name="GridBagType">
      <xsd:sequence>
         <xsd:element name="row" type="RowType" minOccurs="0" maxOccurs="unbounded"/>
      </xsd:sequence>
   </xsd:complexType>

   <xsd:complexType name="RowType">
      <xsd:sequence>
         <xsd:element name="cell" type="CellType" minOccurs="0" maxOccurs="unbounded"/>
      </xsd:sequence>
   </xsd:complexType>

   <xsd:complexType name="CellType">
      <xsd:sequence>
         <xsd:element ref="bean"/>
      </xsd:sequence>
      <xsd:attribute name="gridx" type="xsd:int" use="optional"/>
      <xsd:attribute name="gridy" type="xsd:int" use="optional"/>
      <xsd:attribute name="gridwidth" type="xsd:int" use="optional" default="1" />
      <xsd:attribute name="gridheight" type="xsd:int" use="optional" default="1" />
      <xsd:attribute name="weightx" type="xsd:int" use="optional" default="0" />
      <xsd:attribute name="weighty" type="xsd:int" use="optional" default="0" />
      <xsd:attribute name="fill" use="optional" default="NONE">
        <xsd:simpleType>
          <xsd:restriction base="xsd:string">
            <xsd:enumeration value="NONE" />
            <xsd:enumeration value="BOTH" />
            <xsd:enumeration value="HORIZONTAL" />
            <xsd:enumeration value="VERTICAL" />
          </xsd:restriction>
        </xsd:simpleType>
      </xsd:attribute>
      <xsd:attribute name="anchor" use="optional" default="CENTER">
        <xsd:simpleType>
          <xsd:restriction base="xsd:string">
            <xsd:enumeration value="CENTER" />
            <xsd:enumeration value="NORTH" />
            <xsd:enumeration value="NORTHEAST" />
            <xsd:enumeration value="EAST" />
            <xsd:enumeration value="SOUTHEAST" />
            <xsd:enumeration value="SOUTH" />
            <xsd:enumeration value="SOUTHWEST" />
            <xsd:enumeration value="WEST" />
            <xsd:enumeration value="NORTHWEST" />
          </xsd:restriction>
        </xsd:simpleType>
      </xsd:attribute>
      <xsd:attribute name="ipady" type="xsd:int" use="optional" default="0" />
      <xsd:attribute name="ipadx" type="xsd:int" use="optional" default="0" />
   </xsd:complexType>

   <xsd:complexType name="BeanType">
      <xsd:sequence>
         <xsd:element name="class" type="xsd:string"/>
         <xsd:element name="property" type="PropertyType" minOccurs="0" maxOccurs="unbounded"/>
      </xsd:sequence>
      <xsd:attribute name="id" type="xsd:ID" use="optional" />
   </xsd:complexType>

   <xsd:complexType name="PropertyType">
      <xsd:sequence>
         <xsd:element name="name" type="xsd:string"/>
         <xsd:element name="value" type="ValueType"/>
      </xsd:sequence>
   </xsd:complexType>

   <xsd:complexType name="ValueType">
      <xsd:choice>
         <xsd:element ref="bean"/>
         <xsd:element name="int" type="xsd:int"/>
         <xsd:element name="string" type="xsd:string"/>
         <xsd:element name="boolean" type="xsd:boolean"/>
      </xsd:choice>
   </xsd:complexType>
</xsd:schema>
```

