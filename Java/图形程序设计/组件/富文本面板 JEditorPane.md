`JEditorPane` 能够以 `HTML` 和 `RTF` 的格式显示和编辑。（`RTF` 即 "富文本格式"，是许多微软应用进行文档交换的格式。

坦白地说，`JEditorPane` 的功能还不尽人意。`HTML` 绘制器只能显示简单的文件，但是对于在 `Web` 上经常出现的复杂页面，它往往难于处理。`HTML` 编辑器不仅功能有限，而且还不稳定。

`JEditorPane` 看似合理的一种应用就是以 `HTML` 的形式显示程序的帮助文档。

> 提示：如果想获得有关业界强度的帮助系统的更多信息，请到网站 <https://github.com/javaee/javahelp/tree/master> 上查看 `JavaHelp`。

> 提示：在默认情况下，`JEditorPane` 是处于编辑模式的。可以调用 `editorPane.setEditable(false)` 将其关闭。

可以使用 `setPage` 方法载入一个新文档。例如：

```java
JEditorPane editorPane = new JEditorPane();
editorPane.setPage(url);
```

`JEditorPane` 类继承了 `JTextComponent` 类。因此，也可以调用只能显示纯文本的 `setText` 方法。

> 提示：关于 `setPage` 是否是在一个单独的线程中载入一个新的文档，它的 `API` 文档写得也不是很清楚。不过，可以使用下面几条语句强制在一个单独线程中载入：
>
> ```java
> AbstractDocument doc = (AbstractDocument) editorPane.getDocument();
> doc.setAsynchronousLoadPriority(0);
> ```

为了监听超链接的点击事件，需要添加一个 `HyperlinkListener` 。`HyperlinkListener` 接口只有一个单一方法 `hyperlinkUpdate`，当用户移到或点击一个超链接的时候，该方法就会被调用。该方法接收一个类型为 `HyperlinkEvent` 的数据作为参数。

需要调用 `getEventType` 方法以确定发生了什么类型的事件。下面是三种可能的返回值：

```
HyperlinkEvent.EventType.ACTIVATED
HyperlinkEvent.EventType.ENTERED
HyperlinkEvent.EventType.EXITED
```

`HyperlinkEvent` 类的 `getURL` 方法返回超链接的 `URL`。例如，下面展示了怎样安装一个超链接监听器追踪用户激活的链接：

```java
editorPane.addHyperlinkListener(event -> {
    if (event.getEventType() == HyperlinkEvent.EventType.ACTIVATED) {
        try {
            editorPane.setPage(event.getURL());
        } catch (IOException e) {
            editorPane.setText("Exception: " + e);
        }
    }
});
```

**示例代码：editorPane/EditorPaneFrame.java**

```java
package editorPane;

import java.awt.BorderLayout;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.util.Stack;

import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JEditorPane;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextField;
import javax.swing.event.HyperlinkEvent;

public class EditorPaneFrame extends JFrame {

	private static final int DEFAULT_WIDTH = 600;
	private static final int DEFAULT_HEIGHT = 400;
	
	public EditorPaneFrame() {
		setSize(DEFAULT_WIDTH, DEFAULT_HEIGHT);
		
		final Stack<String> urlStack = new Stack<>();
		final JEditorPane editorPane = new JEditorPane();
		final JTextField url = new JTextField(30);
		
		// set up hyperlink listener
		
		editorPane.setEditable(false);
		editorPane.addHyperlinkListener(event -> {
			if (event.getEventType() == HyperlinkEvent.EventType.ACTIVATED) {
				try {
					// remember URL for back button
					urlStack.push(event.getURL().toString());
					// show URL in text field
					url.setText(event.getURL().toString());
					editorPane.setPage(event.getURL());
				} catch (IOException e) {
					editorPane.setText("Execption: " + e);
				}
			}
		});
		
		// set up checkbox for toggling edit moe
		
		final JCheckBox editable = new JCheckBox();
		editable.addActionListener(event -> editorPane.setEditable(editable.isSelected()));
		
		// set up load button for loading URL
		ActionListener listener = event -> {
			try {
				// remember URL for back button
				urlStack.push(url.getText());
				editorPane.setPage(url.getText());
			} catch (IOException e) {
				editorPane.setText("Exception: " + e);
			}
		};
		
		JButton loadButton = new JButton("Load");
		loadButton.addActionListener(listener);
		url.addActionListener(listener);
		
		// set up back button and button action
		
		JButton backButton = new JButton("Back");
		backButton.addActionListener(event -> {
			if (urlStack.size() <= 1) return;
			try {
				// get URL from back button
				urlStack.pop();
				// show URL in text field
				String urlString = urlStack.peek();
				url.setText(urlString);
				editorPane.setPage(urlString);
			} catch (IOException e) {
				editorPane.setText("Exception: " + e);
			}
		});
		
		add(new JScrollPane(editorPane), BorderLayout.CENTER);
		
		// put all control components in a panel
		
		JPanel panel = new JPanel();
		panel.add(new JLabel("URL"));
		panel.add(url);
		panel.add(loadButton);
		panel.add(backButton);
		panel.add(new JLabel("Editable"));
		panel.add(editable);
		
		add(panel, BorderLayout.SOUTH);
	}
}
```

