把文本域添加到窗口的常用办法是将它添加到面板或者其他容器中，这与添加按钮完全一样：

```java
JPanel panel = new JPanel();
JTextField textField = new JTextField("Default input", 20);
panel.add(textField);
```

构造器的第一个参数是文本域的默认字符串，第二个参数设置了文本域的高度。在这个示例中，宽度值为 20 “列”。但是，这里所说的列不是一个精确的测量单位。一列就是在当前使用的字体下一个字符的宽度。如果希望文本域最多能够输入 n 个字符，就应该把宽度设置为 n 列。在实际中这样做效果并不理想，应该将最大输入长度再多设 1 ~ 2 个字符。

如果需要在运行时重新设置列数，可以使用 `setColumns` 方法。

> 提示：使用 `setColumns` 方法改变了一个文本域的大小之后，需要调用包含这个文本框的容器的 `revalidate` 方法。

`revalidate` 方法是 `JComponent` 类中的方法。它并不是马上就改变组件大小，而是给这个组件加一个需要改变大小的标记。这样就避免了多个组件改变大小时带来的重复计算。但是，如果想重新计算一个 `JFrame` 中的所有组件，就必须调用 `validate` 方法 —— `JFrame` 没有扩展 `JComponent`。

文本域一般初始为空白。只要不为 `JTextField` 构造器提供字符串参数，就可以构造一个空白文本域：

```java
JTextField textField = new JTextField(20);
```

可以在任何时候调用 `setText` 方法改变文本域中的内容：

```java
textField.setText("Hello");
```

可以调用 `getText` 方法来获取用户键入的文本。这个方法返回用户输入的文本。

如果想要改变显示文本的字体，就调用 `setFont` 方法。

**示例代码：**

```java
import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.GridLayout;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.SwingConstants;

public class TextComponentTest {

	public static void main(String[] args) {
		EventQueue.invokeLater(() -> {
			JFrame frame = new TextComponentFrame();
			frame.setTitle("Text Component test");
			frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			frame.setVisible(true);
		});
	}
	
}


class TextComponentFrame extends JFrame {
	
	private static final int TEXTAREA_ROWS = 8;
	private static final int TEXTAREA_COLUMNS = 20;
	
	public TextComponentFrame() {
		JTextField textField = new JTextField();
		JPasswordField passwordField = new JPasswordField();
		
		JPanel northPanel = new JPanel();
		northPanel.setLayout(new GridLayout(2, 2));
		northPanel.add(new JLabel("User name: ", SwingConstants.RIGHT));
		northPanel.add(textField);
		northPanel.add(new JLabel("Password: ", SwingConstants.RIGHT));
		northPanel.add(passwordField);
		
		add(northPanel, BorderLayout.NORTH);
		
		JTextArea textArea = new JTextArea(TEXTAREA_ROWS, TEXTAREA_COLUMNS);
		
		JScrollPane scrollPane = new JScrollPane(textArea);
		
		add(scrollPane, BorderLayout.CENTER);
		
		// add button to append text into the text area
		JPanel southPanel = new JPanel();
		
		JButton insertButton = new JButton("Insert");
		southPanel.add(insertButton);
		insertButton.addActionListener(event -> {
			textArea.append("User name: " + textField.getText() + " Password: " + new String(passwordField.getPassword()) + "\n");
		});
		
		add (southPanel, BorderLayout.SOUTH);
		pack();
	}
	
}
```

