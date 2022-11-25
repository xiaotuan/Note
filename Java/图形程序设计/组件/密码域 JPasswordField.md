密码域是一种特殊类型的文本域。为了避免有不良企图的人看到密码，用户输入的字符不显示出来。每个输入的字符都用回显字符表示，典型的回显字符是星号（*）。Swing 提供了 `JPasswordField` 类来实现这样的文本域。

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

## javax.swing.JPasswordField 1.2

+ `JPasswordField(String text, int columns)`

  构造一个新的密码域对象

+ `void setEchoChar(char echo)`

  为密码域设置回显字符。注意：独特的观感可以选择自己的回显字符。0 表示重新设置为默认的回显字符。

+ `char[] getPassword()`

  返回密码域中的文本。为了安全起见，在使用之后应该覆写返回的数组内容（密码并不是以 `String` 的形式返回，这是因为字符串在被垃圾回收器回收之前会一致驻留在虚拟机中）。