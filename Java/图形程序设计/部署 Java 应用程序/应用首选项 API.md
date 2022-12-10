`Preferences` 类以一种平台无关的方式提供了这样一个中心存储库。在 Windows 中，`Preferences` 类使用注册表来存储信息；在 `Linux` 上，信息则存储在本地文件系统中。当然，存储库实现对使用 `Preferences` 类的程序员是透明的。

`Preferences` 存储库有一个树状结构，节点路径名类似于 `/com/mycompany/myapp`。类似于包名，只要程序员用逆置的域名作为路径的开头，就可以避免命名冲突。实际上，API 的设计者就建议配置节点路径要与程序中的包名一致。

存储库的各个节点分别有一个单独的键 / 值对表，可以用来存储数值、字符串或字节数组，但不能存储可串行化的对象。

若要访问树中的一个节点，需要从用户或系统根开始：

```java
Preferences root = Preferences.userRoot();
```

或

```java
Preferences root = Preferences.systemRoot();
```

然后访问节点。可以直接提供一个节点路径名：

```java
Preferences node = root.node("/com/mycompany/myapp");
```

如果节点的路径名等于类的包名，还有一种便捷方式来获得这个节点。只需要得到这个类的一个对象，然后调用：

```java
Preferences node = Preferences.userNodeForPackage(obj.getClass());
```

或

```java
Preferences node = Preferences.systemNodeForPackage(obj.getClass());
```

一版来说，obj 往往是 this 引用。

一旦得到了节点，可以用以下方法访问键 / 值表：

```java
String get(String key, String defval);
int getInt(String key, int defval);
long getLong(String key, long defval);
float getFloat(String key, float defval);
double getDouble(String key, double defval);
boolean getBoolean(String key, boolean defval);
byte[] getByteArray(String key, byte[] defval);
```

需要说明的是，读取信息时必须指定一个默认值，以防止没有可用的存储库数据。

相应地，可以用如下的 `put` 方法向存储库写数据：

```java
put(String key, String value);
putInt(String key, int value);
putLong(String key, long value);
putFloat(String key, float value);
putDouble(String key, double value);
putBoolean(String key, boolean value);
putByteArray(String key, byte[] value);
```

可以用以下方法枚举一个节点中存储的所有键：

```java
String[] keys();
```

可以通过调用以下方法导出一个子树的首选项：

```java
void exportSubtree(OutputStream out);
void exportNode(OutputStream out);
```

数据用 XML 格式保存。可以通过调用以下方法将数据导入到另一个存储库：

```java
void importPreferences(InputStream in);
```

**示例代码：**

```java
import java.awt.EventQueue;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.prefs.Preferences;

import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.filechooser.FileNameExtensionFilter;

public class PreferencesTest {

	public static void main(String[] args) {
		EventQueue.invokeLater(() -> {
			PreferencesFrame frame = new PreferencesFrame();
			frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			frame.setVisible(true);
		});
	}

}

class PreferencesFrame extends JFrame {
	private static final int DEFAULT_WIDTH = 300;
	private static final int DEFAULT_HEIGHT = 200;
	private Preferences root = Preferences.userRoot();
	private Preferences node = root.node("/com/horstmann/corejava");
	
	public PreferencesFrame() {
		// get position, size, title form preferences
		int left = node.getInt("left", 0);
		int top = node.getInt("top", 0);
		int width = node.getInt("width", DEFAULT_WIDTH);
		int height = node.getInt("height", DEFAULT_HEIGHT);
		setBounds(left, top, width, height);
		
		// if no title given, ask user
		String title = node.get("title", "");
		if (title.equals("")) {
			title = JOptionPane.showInputDialog("Please supply a frame title: ");
		}
		if (title == null) title = "";
		setTitle(title);
		
		// set up file chooser that shows XML files
		final JFileChooser chooser = new JFileChooser();
		chooser.setCurrentDirectory(new File("."));
		chooser.setFileFilter(new FileNameExtensionFilter("XML files", "xml"));
		
		// set up menus
		JMenuBar menuBar = new JMenuBar();
		setJMenuBar(menuBar);
		JMenu menu = new JMenu("File");
		menuBar.add(menu);
		
		JMenuItem exportItem = new JMenuItem("Export preferences");
		menu.add(exportItem);
		exportItem.addActionListener(event -> {
			if (chooser.showSaveDialog(PreferencesFrame.this) == JFileChooser.APPROVE_OPTION) {
				try {
					savePreferences();
					OutputStream out = new FileOutputStream(chooser.getSelectedFile());
					node.exportSubtree(out);
					out.close();
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
		
		JMenuItem importItem = new JMenuItem("Import preferences");
		menu.add(importItem);
		importItem.addActionListener(event -> {
			if (chooser.showOpenDialog(PreferencesFrame.this) == JFileChooser.APPROVE_OPTION) {
				try {
					InputStream in = new FileInputStream(chooser.getSelectedFile());
					Preferences.importPreferences(in);
					in.close();
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
		
		JMenuItem exitItem = new JMenuItem("Exit");
		menu.add(exitItem);
		exitItem.addActionListener(event -> {
			savePreferences();
			System.exit(0);
		});
	}
	
	public void savePreferences() {
		node.putInt("left", getX());
		node.putInt("top", getY());
		node.putInt("width", getWidth());
		node.putInt("height", getHeight());
		node.put("title", getTitle());
	}
}
```

