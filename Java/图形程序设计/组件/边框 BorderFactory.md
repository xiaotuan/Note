如果在一个窗口中有多组单选按钮，就需要用可视化的形式指明哪些按钮属于同一组。Swing 提供了一组很有用的边框来解决这个问题。

有几种不同的边框可供选择，但是使用它们的步骤完全一样：

+ 调用 `BorderFactory` 的静态方法创建边框。下面是几种可选的风格:
  + 凹斜面
  + 凸斜面
  + 蚀刻
  + 直线
  + 蒙版
  + 空（只是在组件外围创建一些空白空间）
+ 如果愿意的话，可以给边框添加标题，具体的实现方法是将边框传递给 `BroderFactory.createTitleBorder`。
+ 如果确实想把一切凸显出来，可以调用下列方法将几种边框组合起来使用：`BorderFactory.createCompoundBorder`。
+ 调用 `JComponent` 类中的 `SetBorder` 方法将结果边框添加到组件中。

例如：

```java
Border etched = BorderFactory.createEtchedBorder();
Border titled = BorderFactory.createTitledBorder(etched, "Border types");
buttonPanel.setBorder(titled);
```

`SoftBevelBorder` 类用于构造具有柔和拐角的斜面边框，`LineBorder` 类也能够构造圆拐角。这些边框只能通过类中的某个构造器构造，而没有 `BorderFactory` 方法。

**示例代码：**

```java
import java.awt.Color;
import java.awt.EventQueue;
import java.awt.GridLayout;

import javax.swing.BorderFactory;
import javax.swing.ButtonGroup;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.border.Border;

public class BorderTest {

	public static void main(String[] args) {
		EventQueue.invokeLater(() -> {
			JFrame frame = new BorderFrame();
			frame.setTitle("Border test");
			frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			frame.setVisible(true);
		});
	}
	
}

class BorderFrame extends JFrame {
	
	private JPanel demoPanel;
	private JPanel buttonPanel;
	private ButtonGroup group;
	
	public BorderFrame() {
		demoPanel = new JPanel();
		buttonPanel = new JPanel();
		group = new ButtonGroup();
		
		addRadioButton("Lowered bevel", BorderFactory.createLoweredBevelBorder());
		addRadioButton("Raised bevel", BorderFactory.createRaisedBevelBorder());
		addRadioButton("Etched", BorderFactory.createEtchedBorder());
		addRadioButton("Line", BorderFactory.createLineBorder(Color.BLUE));
		addRadioButton("Matte", BorderFactory.createMatteBorder(10, 10, 10, 10, Color.BLUE));
		addRadioButton("Empty", BorderFactory.createEmptyBorder());
		
		Border etched = BorderFactory.createEtchedBorder();
		Border titled = BorderFactory.createTitledBorder(etched, "Border types");
		buttonPanel.setBorder(titled);
		
		setLayout(new GridLayout(2, 1));
		add(buttonPanel);
		add(demoPanel);
		pack();
	}
	
	public void addRadioButton(String buttonName, Border b) {
		JRadioButton button = new JRadioButton(buttonName);
		button.addActionListener(event -> demoPanel.setBorder(b));
		group.add(button);
		buttonPanel.add(button);
	}
}
```



