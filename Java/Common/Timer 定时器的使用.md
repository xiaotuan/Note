[toc]

### 1. 实现 ActionListener 接口

```java
class TimePrinter implements ActionListener {

	@Override
	public void actionPerformed(ActionEvent e) {
		System.out.println("At the tone, the time is " + new Date());
		Toolkit.getDefaultToolkit().beep();
	}
	
}
```

### 2. 构造 Timer 对象

```java
ActionListener listener = new TimePrinter();
Timer t = new Timer(10000, listener);
```

### 3. 开始计时

```java
t.start();
```

### 4. 完整示例代码

```java
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Date;

import javax.swing.JOptionPane;
import javax.swing.Timer;

public class JavaTest {

	public static void main(String[] args) {
		ActionListener listener = new TimePrinter();
		
		// construct a timer that calls the listener
		// once every 10 seconds
		Timer t = new Timer(10000, listener);
		t.start();
		
		JOptionPane.showMessageDialog(null, "Quit program?");
		System.exit(0);
	}

}

class TimePrinter implements ActionListener {

	@Override
	public void actionPerformed(ActionEvent e) {
		System.out.println("At the tone, the time is " + new Date());
		Toolkit.getDefaultToolkit().beep();
	}
	
}
```

