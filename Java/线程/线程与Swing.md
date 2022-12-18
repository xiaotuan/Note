[toc]

### 1. 运行耗时的任务

将线程与 Swing 一起使用时，必须遵循两个简单的原则。

（1）如果一个动作需要花费很长时间，在一个独立的工作器线程中做这件事不要在事件分配线程中做。

（2）除了事件分配线程，不要在任何线程中接触 Swing 组件。

这两条规则看起来彼此冲突。假定要启动一个独立的线程运行一个耗时的任务。线程工作的时候，通常要更新用户界面中指示执行的进度。任务完成的时候，要再一次更新 GUI 界面。但是，不能从自己的线程接触 Swing 组件。例如，如果要更新进度条或标签文本，不能从线程中设置它的值。

要解决这一问题，在任何线程中，可以使用两种有效的方法向事件队列添加任意的动作。例如，假定想在一个线程中周期性地更新标签来表明进度。

不可以从自己的线程中调用 `label.setText`，而应该使用 `EventQueue` 类的 `invokeLater` 方法和 `invokeAndWait` 方法使所调用的方法在事件分配线程中执行。

应该将 Swing 代码放置到实现 Runnable 接口的类的 run 方法中。然后，创建该类的一个对象，将其传递给静态的 `invokeLater` 或 `invokeAndWait` 方法。例如，下面是如何更新标签内容的代码：

```java
EventQueue.invokeLater(() -> {
    label.setText(percentage + "% complete");
});
```

当事件放入事件队列时，`invokeLater` 方法立即返回，而 `run` 方法被异步执行。`invokeAndWait` 方法等待直到 `run` 方法确实被执行过为止。

**示例代码：**

```java
import java.awt.EventQueue;
import java.util.Random;

import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class SwingThreadTest {

	public static void main(String[] args) {
		EventQueue.invokeLater(() -> {
			JFrame frame = new SwingThreadFrame();
			frame.setTitle("SwingThreadTest");
			frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			frame.setVisible(true);
		});
	}

}

class SwingThreadFrame extends JFrame {
	
	public SwingThreadFrame() {
		final JComboBox<Integer> combo = new JComboBox<>();
		combo.insertItemAt(Integer.MAX_VALUE, 0);
		combo.setPrototypeDisplayValue(combo.getItemAt(0));
		combo.setSelectedItem(0);
		
		JPanel panel = new JPanel();
		
		JButton goodButton = new JButton("Good");
		goodButton.addActionListener(event -> {
			new Thread(new GoodWorkerRunnable(combo)).start();
		});
		panel.add(goodButton);
		JButton badButton = new JButton("Bad");
		badButton.addActionListener(event -> {
			new Thread(new BadWorkerRunnable(combo)).start();
		});
		panel.add(badButton);
		
		panel.add(combo);
		add(panel);
		pack();
	}
}

class BadWorkerRunnable implements Runnable {
	
	private JComboBox<Integer> combo;
	private Random generator;
	
	public BadWorkerRunnable(JComboBox<Integer> aCombo) {
		combo = aCombo;
		generator = new Random();
	}
	
	@Override
	public void run() {
		try {
			while (true) {
				int i = Math.abs(generator.nextInt());
				if (i % 2 == 0) {
					combo.insertItemAt(i, 0);
				} else if (combo.getItemCount() > 0) {
					combo.removeItemAt(i % combo.getItemCount());
				}
				Thread.sleep(1);
			}
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
}

class GoodWorkerRunnable implements Runnable {
	
	private JComboBox<Integer> combo;
	private Random generator;
	
	public GoodWorkerRunnable(JComboBox<Integer> aCombo) {
		combo = aCombo;
		generator = new Random();
	}
	
	@Override
	public void run() {
		try {
			while (true) {
				EventQueue.invokeLater(() -> {
					int i = Math.abs(generator.nextInt());
					if (i % 2 == 0) {
						combo.insertItemAt(i, 0);
					} else if (combo.getItemCount() > 0) {
						combo.removeItemAt(i % combo.getItemCount());
					}
				});
				Thread.sleep(1);
			}
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
}
```

### 2. 使用 Swing 工作线程

`SwingWorker` 类使后台任务的实现不那么繁琐。`SwingWorker` 类使得实现这一任务轻而易举。覆盖 `doInBackground` 方法来完成耗时的工作，不时地调用 `publish` 来报告工作进度。这一方法在工作器线程中执行。`publish` 方法使得 process 方法在事件分配线程中执行来处理进度数据。当工作完成时，done 方法在事件分配线程中被调用以便完成 UI 的更新。

每当要再工作线程中做一些工作时，构建一个新的工作器（每一个工作器对象只能被使用一次）。然后调用 `execute` 方法。典型的方式是在事件分配线程中调用 `execute`，但没有这样的需求。

要取消正在进行的工作，使用 `Future` 接口的 `cancel` 方法。当该工作呗取消的时候，`get` 方法抛出 `CancellationException` 异常。

**示例代码：**

```java
import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.List;
import java.util.Scanner;
import java.util.concurrent.CancellationException;
import java.util.concurrent.ExecutionException;

import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.SwingWorker;

public class SwingWorkerTest {

	public static void main(String[] args) {
		EventQueue.invokeLater(() -> {
			JFrame frame = new SwingWorkerFrame();
			frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			frame.setVisible(true);
		});
	}

}

class SwingWorkerFrame extends JFrame {
	
	private static final int TEXT_ROWS = 20;
	private static final int TEXT_COLUMNS = 60;
	
	private JFileChooser chooser;
	private JTextArea textArea;
	private JLabel statusLine;
	private JMenuItem openItem;
	private JMenuItem cancelItem;
	private SwingWorker<StringBuilder, ProgressData> textReader;
	
	public SwingWorkerFrame() {
		chooser = new JFileChooser();
		chooser.setCurrentDirectory(new File("."));
		
		textArea = new JTextArea(TEXT_ROWS, TEXT_COLUMNS);
		add(new JScrollPane(textArea));
		
		statusLine = new JLabel(" ");
		add(statusLine, BorderLayout.SOUTH);
		
		JMenuBar menuBar = new JMenuBar();
		setJMenuBar(menuBar);
		
		JMenu menu = new JMenu("File");
		menuBar.add(menu);
		
		openItem = new JMenuItem("Open");
		menu.add(openItem);
		openItem.addActionListener(event -> {
			// show file chooser dialog
			int result = chooser.showOpenDialog(null);
			
			// fi file selected, set it as icon of the label
			if (result == JFileChooser.APPROVE_OPTION) {
				textArea.setText("");
				openItem.setEnabled(false);
				textReader = new TextReader(chooser.getSelectedFile());
				textReader.execute();
				cancelItem.setEnabled(true);
			}
		});
		
		cancelItem = new JMenuItem("Cancel");
		menu.add(cancelItem);
		cancelItem.setEnabled(false);
		cancelItem.addActionListener(event -> textReader.cancel(true));
		pack();
	}
	
	private class ProgressData {
		public int number;
		public String line;
	}
	
	private class TextReader extends SwingWorker<StringBuilder, ProgressData> {
		
		private File file;
		private StringBuilder text = new StringBuilder();
		
		public TextReader(File file) {
			this.file = file;
		}
		
		@Override
		public StringBuilder doInBackground() throws IOException, InterruptedException {
			int lineNumber = 0;
			try (Scanner in = new Scanner(new FileInputStream(file), "utf-8")) {
				while (in.hasNextLine()) {
					String line = in.nextLine();
					lineNumber++;
					text.append(line).append("\n");
					ProgressData data = new ProgressData();
					data.number = lineNumber;
					data.line = line;
					publish(data);
					Thread.sleep(1);	// to test cancellation; no need to do this in your programs
				}
			}
			return text;
		}
		
		@Override
		public void process(List<ProgressData> data) {
			if (isCancelled()) {
				return;
			}
			StringBuilder b = new StringBuilder();
			statusLine.setText("" + data.get(data.size() - 1).number);
			for (ProgressData d : data) {
				b.append(d.line).append("\n");
			}
			textArea.append(b.toString());
		}
		
		@Override
		public void done() {
			try {
				StringBuilder result = get();
				textArea.setText(result.toString());
				statusLine.setText("Done");
			} catch (InterruptedException e) {
				e.printStackTrace();
			} catch (CancellationException ex) {
				ex.printStackTrace();
			} catch (ExecutionException ex) {
				ex.printStackTrace();
			}
			cancelItem.setEnabled(false);
			openItem.setEnabled(true);
		}
	}
}
```

### 3. 单一线程规则

对于单一线程规则存在一些例外情况。

+   可在任一个线程里添加或移除事件监听器。当然该监听器的方法会在事件分配线程中被处罚。
+   只有很少的 Swing 方法是线程安全的。在 API 文档中用这样的句子特别标明："尽管大多数 Swing 方法不是线程安全的，但这个方法是。" 在这些线程安全的方法中最有用的是：

```
JTextComponent.setText
JTextArea.insert
JTextArea.append
JTextArea.replaceRange
JComponent.repaint
JComponent.revalidate
```

>   提示：`revalidate` 方法不怎么常见，其作用是在内容改变之后强制执行组件布局。传统的 AWT 有一个 `validate` 方法强制执行组件布局。对于 Swing 组件，应该调用 `revalidate` 方法。（但是，要强制执行 `JFrame` 的布局，仍然要调用 `validate` 方法，因为 `JFrame` 是一个 `Component` 不是一个 `JComponent`。）

