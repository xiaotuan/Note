[toc]

`JSpinner` 是包含一个文本框以及两个在文本框旁边的小按钮的构件。当点击按钮时，文本框的值就会递增或递减。

可以通过调用 `getValue` 方法来获取当前值，这个方法将返回一个 `Object`，应该将其转换为 `Integer` 并获取其中包装的值。

```java
JSpinner defaultSpinner = new JSpinner();
...
int value = (Integer) defaultSpinner.getValue();
```

还可以提供递增的上界和下界。下面的微调器的初始值为 5，边界为 0 到 10， 每次递增 0.5：

```java
JSpinner boundedSpinner = new JSpinner(new JSpinnerNumberModel(5, 0, 10, 0.5));
```

`SpinnerNumberModel` 有两个构造器，其中一个只有 `int` 参数，而另一个有 `double` 参数。只要有参数是浮点数，就会使用第二个构造器，它会将微调器的值设置为 `Double` 对象。

微调器并未限制只能是数字型值，我们可以用微调器迭代任何值集合，只需将一个 `SpinnerListModel` 传递给 `JSpinner` 构造器即可。我们可以从数组或实现了 `List` 接口的类（例如 `ArrayList`） 中构建 `SpinnerListModel`。

```java
String[] fonts = GraphicsEnvironment.getLocalGraphicsEnvironment().getAvailableFontFamilyNames();
JSpinner listSpinner = new JSpinner(new SpinnerListModel(fonts));
```

在组合框中，较高的值在较低的值的下面，因此，我们用向下箭头来导航到较高的值。但是微调器将递增数组索引，使得向上箭头可以产生较高的值。在 `SpinnerListModel` 中没有用于颠倒遍历顺序的方法，但是临时创建一个匿名子类就可以产生想要的结果：

```java
JSpinner reverseListSpinner = new JSpinner(new SpinnerListModel(fonts) {
    public Object getNextValue() {
        return super.getPreviousValue();
    }
    
    public Object getPreviousValue() {
        return super.getNextValue();
    }
})
```

微调器的另一个大显身手之处是可以让用户递增或递减日期：

```java
JSpinner dateSpinner = new JSpinner(new SpinnerDateModel());
```

你会发现微调器文本同时显示了日期和时间，例如：

```
8/05/07 9:05 PM
```

可以使用下面代码让微调器只显示日期：

```java
JSpinner batterDateSpinner = new JSpinner(new SpinnerDateModel());
String pattern = ((SimpleDateFormat) DateFormat.getDateInstance()).toPattern();
betterDateSpinner.setEditor(new JSpinner.DateEditor(betterDateSpinner, pattern));
```

使用相同的方法，还可以创建一个时间选择器：

```java
JSpinner timeSpinner = new JSpinner(new SpinnerDateModel());
pattern = ((SimpleDateFormat) DateFormat.getTimeInstance(DateFormat.SHORT)).toPattern();
timeSpinner.setEditor(new JSpinner.DateEditor(timeSpinner, pattern));
```

在定义自己的模型时，需要扩展 `AbstractSpinnerModel` 类并定义下面的 4 个方法：

```
Object getValue()
void setValue(Object value)
Object getNextValue()
Object getPreviousValue()
```

`getValue` 方法将返回模型存储的值，而 `setValue` 方法则把这个值设置为新值，如果新值并不适合用于设置，则该方法会抛出 `IllegalArgumentException`。

> 警告：`setValue` 方法必须在设置新值之后调用 `fireStateChanged` 方法，否则，微调器文本框并不会更新。

`getNextValue` 和 `getPreviousValue` 方法将分别返回位于当前之后和之前的值，或者在到达遍历的终点时返回 `null`。

> 警告：`getNextValue` 和 `getPreviousValue` 方法不应该改变当前值。当用户点击微调器的向上箭头时，`getNextValue` 方法就会被调用。如果其返回值不是 `null`，微调器的值会通过一个对 `setValue` 的调用进行设置。

**示例代码：**

1. spinner/SpinnerFrame.java

   ```java
   package spinner;
   
   import java.awt.BorderLayout;
   import java.awt.GraphicsEnvironment;
   import java.awt.GridLayout;
   import java.text.DateFormat;
   import java.text.SimpleDateFormat;
   
   import javax.swing.JButton;
   import javax.swing.JFrame;
   import javax.swing.JLabel;
   import javax.swing.JPanel;
   import javax.swing.JSpinner;
   import javax.swing.SpinnerDateModel;
   import javax.swing.SpinnerListModel;
   import javax.swing.SpinnerNumberModel;
   
   public class SpinnerFrame extends JFrame {
   
   	private JPanel mainPanel;
   	private JButton okButton;
   	
   	public SpinnerFrame() {
   		JPanel buttonPanel = new JPanel();
   		okButton = new JButton("OK");
   		buttonPanel.add(okButton);
   		add(buttonPanel, BorderLayout.SOUTH);
   		
   		mainPanel = new JPanel();
   		mainPanel.setLayout(new GridLayout(0, 3));
   		add(mainPanel, BorderLayout.CENTER);
   		
   		JSpinner defaultSpinner = new JSpinner();
   		addRow("Default", defaultSpinner);
   		
   		JSpinner boundedSpinner = new JSpinner(new SpinnerNumberModel(3, 0, 10, 0.5));
   		addRow("Bounded", boundedSpinner);
   		
   		String[] fonts = GraphicsEnvironment.getLocalGraphicsEnvironment().getAvailableFontFamilyNames();
   		
   		JSpinner listSpinner = new JSpinner(new SpinnerListModel(fonts));
   		addRow("List", listSpinner);
   		
   		JSpinner reverselistSpinner = new JSpinner(new SpinnerListModel(fonts) {
   			public Object getNextValue() { return super.getPreviousValue(); }
   			public Object getPreviousValue() { return super.getNextValue(); }
   		});
   		addRow("Reverse List", reverselistSpinner);
   		
   		JSpinner dateSpinner = new JSpinner(new SpinnerDateModel());
   		addRow("Date", dateSpinner);
   		
   		JSpinner betterDateSpinner = new JSpinner(new SpinnerDateModel());
   		String pattern = ((SimpleDateFormat) DateFormat.getDateInstance()).toPattern();
   		betterDateSpinner.setEditor(new JSpinner.DateEditor(betterDateSpinner, pattern));
   		addRow("Better Date", betterDateSpinner);
   		
   		JSpinner timeSpinner = new JSpinner(new SpinnerDateModel());
   		pattern = ((SimpleDateFormat) DateFormat.getTimeInstance(DateFormat.SHORT)).toPattern();
   		timeSpinner.setEditor(new JSpinner.DateEditor(timeSpinner, pattern));
   		addRow("Time", timeSpinner);
   		
   		JSpinner permSpinner = new JSpinner(new PermutationSpinnerModel("meat"));
   		addRow("Word permutations", permSpinner);
   		
   		pack();
   	}
   	
   	public void addRow(String labelText, final JSpinner spinner) {
   		mainPanel.add(new JLabel(labelText));
   		mainPanel.add(spinner);
   		final JLabel valueLabel = new JLabel();
   		mainPanel.add(valueLabel);
   		okButton.addActionListener(event -> {
   			Object value = spinner.getValue();
   			valueLabel.setText(value.toString());
   		});
   	}
   }
   ```

2. spinner/PermutationSpinnerModel.java

   ```java
   package spinner;
   
   import javax.swing.AbstractSpinnerModel;
   
   public class PermutationSpinnerModel extends AbstractSpinnerModel {
   
   	private String word;
   	
   	public PermutationSpinnerModel(String w) {
   		word = w;
   	}
   	
   	@Override
   	public Object getValue() {
   		return word;
   	}
   	
   	@Override
   	public void setValue(Object value) {
   		if (!(value instanceof String)) throw new IllegalArgumentException();
   		word = (String) value;
   		fireStateChanged();
   	}
   	
   	@Override
   	public Object getNextValue() {
   		int[] codePoints = toCodePointArray(word);
   		for (int i = codePoints.length - 1; i > 0; i--) {
   			if (codePoints[i - 1] < codePoints[i]) {
   				int j = codePoints.length - 1;
   				while (codePoints[i - 1] > codePoints[j]) {
   					j--;
   				}
   				swap(codePoints, i - 1, j);
   				reverse(codePoints, i, codePoints.length - 1);
   				return new String(codePoints, 0, codePoints.length);
   			}
   		}
   		reverse(codePoints, 0, codePoints.length - 1);
   		return new String(codePoints, 0, codePoints.length);
   	}
   	
   	@Override
   	public Object getPreviousValue() {
   		int[] codePoints = toCodePointArray(word);
   		for (int i = codePoints.length - 1; i > 0; i--) {
   			if (codePoints[i - 1] > codePoints[i]) {
   				int j = codePoints.length - 1;
   				while (codePoints[i - 1] < codePoints[j]) {
   					j--;
   				}
   				swap(codePoints, i - 1, i);
   				reverse(codePoints, i, codePoints.length - 1);
   				return new String(codePoints, 0, codePoints.length);
   			}
   		}
   		reverse(codePoints, 0, codePoints.length - 1);
   		return new String(codePoints, 0, codePoints.length);
   	}
   	
   	private static int[] toCodePointArray(String str) {
   		int[] codePoints = new int[str.codePointCount(0, str.length())];
   		for (int i = 0, j = 0; i < str.length(); i++, j++) {
   			int cp = str.codePointAt(i);
   			if (Character.isSupplementaryCodePoint(cp)) i++;
   			codePoints[j] = cp;
   		}
   		return codePoints;
   	}
   	
   	private static void swap(int[] a, int i, int j) {
   		int temp = a[i];
   		a[i] = a[j];
   		a[j] = temp;
   	}
   	
   	private static void reverse(int[] a, int i, int j) {
   		while(i < j) {
   			swap(a, i, j);
   			i++;
   			j--;
   		}
   	}
   }
   ```

3. spinner/SpinnerTest.java

   ```java
   package spinner;
   
   import java.awt.EventQueue;
   
   import javax.swing.JFrame;
   
   public class SpinnerTest {
   
   	public static void main(String[] args) {
   		EventQueue.invokeLater(() -> {
   			JFrame frame = new SpinnerFrame();
   			frame.setTitle("Spinner test");
   			frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
   			frame.setVisible(true);
   		});
   	}
   }
   ```

   