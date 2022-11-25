在 Swing 中，文本区没有滚动条。如果需要滚动条，可以将文本区插入到滚动窗格中。

```java
textArea = new JTextArea(8, 40);
JScrollPane scrollPane = new JScrollPane(textArea);ß
```

这是一种任意组件添加滚动功能的通用机制，而不是文本区特有的。也就是说，要想为组件添加滚动条，只需将它们放入一个滚动窗格中即可。

>   提示：`JTextArea` 组件只显示无格式的文本，没有特殊字体或者格式设置。如果想要显示格式文本（如 HTML），就需要使用 `JEditorPane` 类。

可以通过调用 `setTabSize(int c)` 方法将制表符设置为 c 列。注意，制表符不会被转换为空格，但可以让文本对齐到下一个制表符处。

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

public class TextComponentTest {å

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

