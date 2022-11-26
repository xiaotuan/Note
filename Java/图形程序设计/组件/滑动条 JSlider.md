滑动条允许进行连续值的选择，例如，从 1 ~ 100 之间选择任意数值。

通常，可以使用下列方式构造滑动条：

```java
JSlider slider = new JSlider(min, max, initialValue);
```

如果省略最小值、最大值和初始值，其默认值分别为 0、100 和 50。

或者如果需要垂直滑动条，可以安装下列方式调用构造器：

```java
JSlider slider = new JSlider(SwingConstants.VERTICAL, min, max, initialValue);
```

当滑动条值发生变化时，`ChangeEvent` 就会发送给所有变化的监听器。为了得到这些改变的通知，需要调用 `addChangeListener` 方法并且安装一个实现了 `ChangeListener` 接口的对象。这个接口只有一个方法 `StateChanged`。在这个方法中可以获取滑动条的当前值：

```java
ChangeListener listener = event -> {
    JSlider slider = (JSlider) event.getSource();
    int value = slider.getValue();
};
```





**示例代码：**

```java
import java.awt.BorderLayout;
import java.awt.Component;
import java.awt.EventQueue;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.util.Dictionary;
import java.util.Hashtable;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JSlider;
import javax.swing.JTextField;
import javax.swing.event.ChangeListener;

public class SliderTest {

	public static void main(String[] args) {
		EventQueue.invokeLater(() -> {
			JFrame frame = new SliderFrame();
			frame.setTitle("Slider test");
			frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			frame.setVisible(true);
		});
	}
	
}

class SliderFrame extends JFrame {
	
	private JPanel sliderPanel;
	private JTextField textField;
	private ChangeListener listener;
	
	public SliderFrame() {
		sliderPanel = new JPanel();
		sliderPanel.setLayout(new GridBagLayout());
		
		// common listener for all sliders
		listener = event -> {
			// update text field when the slider value changes
			JSlider source = (JSlider) event.getSource();
			textField.setText("" + source.getValue());
		};
		
		// add a plain slider
		JSlider slider = new JSlider();
		addSlider(slider, "Plain");
		
		// add a slider with major and minor ticks
		slider = new JSlider();
		slider.setPaintTicks(true);
		slider.setMajorTickSpacing(20);
		slider.setMinorTickSpacing(5);
		addSlider(slider, "Ticks");
		
		// add a slider that snaps to ticks
		slider = new JSlider();
		slider.setPaintTicks(true);
		slider.setSnapToTicks(true);
		slider.setMajorTickSpacing(20);
		slider.setMinorTickSpacing(5);
		addSlider(slider, "Snap to ticks");
		
		// add a slider with no track
		slider = new JSlider();
		slider.setPaintTrack(true);
		slider.setMajorTickSpacing(20);
		slider.setMinorTickSpacing(5);
		slider.setPaintTrack(false);
		addSlider(slider, "No track");
		
		// add an inverted slider
		slider = new JSlider();
		slider.setPaintTicks(true);
		slider.setMajorTickSpacing(20);
		slider.setMinorTickSpacing(5);
		slider.setInverted(true);
		addSlider(slider, "Inverted");
		
		// add a slider with numeric labels
		slider = new JSlider();
		slider.setPaintTicks(true);
		slider.setPaintLabels(true);
		slider.setMajorTickSpacing(20);
		slider.setMinorTickSpacing(5);
		addSlider(slider, "Labels");
		
		// add a slider with alphabetic labels
		slider = new JSlider();
		slider.setPaintLabels(true);
		slider.setPaintTicks(true);
		slider.setMajorTickSpacing(20);
		slider.setMinorTickSpacing(5);
		
		Dictionary<Integer, Component> labelTable = new Hashtable<>();
		labelTable.put(0, new JLabel("A"));
		labelTable.put(20, new JLabel("B"));
		labelTable.put(40, new JLabel("C"));
		labelTable.put(60, new JLabel("D"));
		labelTable.put(80, new JLabel("E"));
		labelTable.put(100, new JLabel("F"));
		
		slider.setLabelTable(labelTable);
		addSlider(slider, "Custom labels");
		
		// add a slider with icon labels
		slider = new JSlider();
		slider.setPaintTicks(true);
		slider.setPaintLabels(true);
		slider.setSnapToTicks(true);
		slider.setMajorTickSpacing(20);
		slider.setMinorTickSpacing(20);
		
		labelTable = new Hashtable<Integer, Component>();
		
		// add card images
		labelTable.put(0,  new JLabel(new ImageIcon("nine.gif")));
		labelTable.put(20, new JLabel(new ImageIcon("ten.gif")));
		labelTable.put(40, new JLabel(new ImageIcon("jack.gif")));
		labelTable.put(60, new JLabel(new ImageIcon("queen.gif")));
		labelTable.put(80, new JLabel(new ImageIcon("king.gif")));
		labelTable.put(100, new JLabel(new ImageIcon("ace.gif")));
		
		slider.setLabelTable(labelTable);
		addSlider(slider, "Icon labels");
		
		// add the text field that displays the slider value
		textField = new JTextField();
		add(sliderPanel, BorderLayout.CENTER);
		add(textField, BorderLayout.SOUTH);
		pack();
	}
	
	public void addSlider(JSlider s, String description) {
		s.addChangeListener(listener);
		JPanel panel = new JPanel();
		panel.add(s);
		panel.add(new JLabel(description));
		panel.setAlignmentX(Component.LEFT_ALIGNMENT);
		GridBagConstraints gbc = new GridBagConstraints();
		gbc.gridy = sliderPanel.getComponentCount();
		gbc.anchor = GridBagConstraints.WEST;
		sliderPanel.add(panel, gbc);
	}
}
```

