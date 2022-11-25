如果想要接收的输入只是 ”是“ 或 ”非“，就可以使用复选框组件。复选框自动地带有标识标签。用户通过点击某个复选框来选择相应的选项，再点击则取消选取。当复选框获得焦点时，用户也可以通过按空格键来切换选择。

复选框需要一个紧邻它的标签来说明其用途。在构造器中指定标签文本。

```java
bold = new JCheckBox("Bold");
```

可以使用 `setSelected` 方法来选定或取消选定复选框。例如：

```java
bold.setSelected(true);
```

`isSelected` 方法将返回每个复选框的当前状态。如果没有选取则为 `false`，否则为 `true`。

当用户点击复选框时将触发一个动作事件。通常，可以为复选框设置一个动作监听器。在下面程序中，两个复选框使用了同一个动作监听器。

```java
ActionListener listener = event -> {
    int mode = 0;
    if (bold.isSelected()) mode += Font.BOLD;
    if (italic.isSelected()) mode += Font.ITALIC;
    label.setFont(new Font("Serif", mode, FONTSIZE));
};

// add the check boxes
JPanel buttonPanel = new JPanel();

bold = new JCheckBox("Bold");
bold.addActionListener(listener);
```

**示例代码：**

```java
import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.Font;
import java.awt.event.ActionListener;

import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class CheckBoxTest {
	
	public static void main(String[] args) {
		EventQueue.invokeLater(() -> {
			JFrame frame = new CheckBoxFrame();
			frame.setTitle("CheckBox Test");
			frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			frame.setVisible(true);
		});
	}

}

class CheckBoxFrame extends JFrame {
	
	private static final int FONTSIZE = 24;
	
	private JLabel label;
	private JCheckBox bold;
	private JCheckBox italic;
	
	public CheckBoxFrame() {
		// add the sample text label
		
		label = new JLabel("The quick brown fox jumps over the lazy dog.");
		label.setFont(new Font("Serif", Font.BOLD, FONTSIZE));
		add(label, BorderLayout.CENTER);
		
		// this listener sets the font attribute of 
		// the label to the check box state
		ActionListener listener = event -> {
			int mode = 0;
			if (bold.isSelected()) mode += Font.BOLD;
			if (italic.isSelected()) mode += Font.ITALIC;
			label.setFont(new Font("Serif", mode, FONTSIZE));
		};
		
		// add the check boxes
		JPanel buttonPanel = new JPanel();
		
		bold = new JCheckBox("Bold");
		bold.addActionListener(listener);
		bold.setSelected(true);
		buttonPanel.add(bold);
		
		italic = new JCheckBox("Italic");
		italic.addActionListener(listener);
		buttonPanel.add(italic);
		
		add(buttonPanel, BorderLayout.SOUTH);
		pack();
	}
}
```

