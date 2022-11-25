在很多情况下，我们需要用户只选择几个选项当中的一个。当用户选择另一项的时候，前一项就自动地取消选择。这样一组选框通常称为单选按钮组（Radio Button Group）。

在 Swing 中，实现单选按钮组非常简单。为单选按钮组构造一个 `ButtonGroup` 的对象。然后，再将 `JRadioButton` 类型的对象添加到按钮组中。按钮组负责在新按钮被按下时，取消前一个被按下的按钮的选择状态：

```java
ButtonGroup group = new ButtonGroup();

JRadioButton smallButton = new JRadioButton("Small", false);
group.add(smallButton);

JRadioButton mediumButton = new JRadioButton("Medium", true);
group.add(mediumButton);
...
```

构造器的第二个参数为 `true` 表明这个按钮初始状态是被选择，其他按钮构造器的这个参数为 `false`。注意，按钮组仅仅控制按钮的行为，如果想把这些按钮组织在一起布局，需要把它们添加到容器，如 `JPanel`。

单选按钮的事件通知机制与其他按钮一样。当用户点击一个单选按钮时，这个按钮将产生一个动作事件。在示例中，定义了一个动作监听器用来把字体大小设置为特定值：

```java
ActionListener listener = event -> label.setFont(new Font("Serif", Font.PLAIN, size));
```

>   注意：如果有一组单选按钮，并知道它们之中只选择了一个。要是能够不查询组内所有的按钮就可以很快地知道哪个按钮被选择的话就好了。由于 `ButtonGroup` 对象控制着所有的按钮，所以如果这个对象能够给出被选择的按钮的引用就方便多了。事实上，`ButtonGroup` 类中有一个 `getSelection` 方法，但是这个方法并不返回被选择的单选按钮，而是返回附加在那个按钮上的模型 `ButtonModel` 的引用。对于我们来说，`ButtonMode` 中的方法没有什么实际的应用价值。`ButtonModel` 接口从 `ItemSelectable` 接口继承了一个 `getSelectedObject` 方法，但是这个方法没有用，它返回 null。`getActionCommand` 方法看起来似乎可用，这是因为一个单选按钮的 ”动作命令“ 是它的文本标签，但是它的模型的动作命令是 null。只有在通过 `setActionCommand` 命令明确地为所有单选按钮设定动作命令后，才能够通过调用方法 `buttonGroup.getSelection().getActionCommand()` 获得当前选择的按钮的动作命令。

**示例代码：**

```java
import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.Font;
import java.awt.event.ActionListener;

import javax.swing.ButtonGroup;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JRadioButton;

public class RadioButtonTest {

	public static void main(String[] args) {
		EventQueue.invokeLater(() -> {
			JFrame frame = new RadioButtonFrame();
			frame.setTitle("RadioButton test");
			frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			frame.setVisible(true);
		});
	}
	
}

class RadioButtonFrame extends JFrame {
	
	private static final int DEFAULT_SIZE = 36;
	
	private JPanel buttonPanel;
	private ButtonGroup group;
	private JLabel label;
	
	public RadioButtonFrame() {
		// add the sample text label
		label = new JLabel("The quick brown fox jumps over the lazy dog.");
		label.setFont(new Font("Serif", Font.PLAIN, DEFAULT_SIZE));
		add(label, BorderLayout.CENTER);
		
		// add the radio buttons
		buttonPanel = new JPanel();
		group = new ButtonGroup();
		
		addRadioButton("Small", 8);
		addRadioButton("Medium", 12);
		addRadioButton("Large", 18);
		addRadioButton("Extra large", 36);
		
		add(buttonPanel, BorderLayout.SOUTH);
		pack();
	}
	
	public void addRadioButton(String name, int size) {
		boolean selected = size == DEFAULT_SIZE;
		JRadioButton button = new JRadioButton(name, selected);
		group.add(button);
		buttonPanel.add(button);
		
		// this listener sets the label font size
		ActionListener listener = event -> label.setFont(new Font("Serif", Font.PLAIN, size));
		
		button.addActionListener(listener);
	}
}
```

