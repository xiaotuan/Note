有时，用户的输入超过一行，需要使用 `JTextArea` 组件来接受这样的输入。

在 `JTextArea` 组件的构造器中，可以指定文本区的行数和列数。例如：

```java
textArea = new JTextArea(8, 40);	// 8 lines of 40 columns each
```

还可以用 `setColumns` 方法改变列数，用 `setRows` 方法改变行数。这些数值只是首选大小——布局管理器可能会对文本区进行缩放。

如果文本区的文本超出了显示的范围，那么剩下的文本就会被剪裁掉。可以通过开启换行特性来避免裁剪过长的行：

```java
textArea.setLineWrap(true);	// long lines are wrapped
```

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

