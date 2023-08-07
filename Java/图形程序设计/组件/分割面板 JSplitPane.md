如果要构建一个分割面板，需要设定一个方向，其值为 `JSplitPane.HORIZONTAL_SPLIT` 和 `JSplitPane.VERTICAL_SPLIT` 中的之一，随后是两个构件。例如：

```java
JSplitPane innerPane = new JSplitPane(JSplitPane.HORIZONTAL_SPLIT, planetList, planetImage);
```

如果需要，可以为分割器添加 "一触即展" 的图标。在 `Metal` 外观模式中，它们是小箭头的形式。如果你点中它们中的一个，那么分割器将会一直沿着箭头指向的方向移动，将其中的一个面板完全展开。如果要添加这项功能，请调用：

```java
innerPane.setOneTouchExpandable(true);
```

当用户调整分割器的时候，"连续布局" 特性会一直不断地刷新这两个构件的内容。这种情形看似经典，实则运行缓慢。你可以调用下面这个方法启动该功能：

```java
innerPane.setContinuousLayout(true);
```

**示例代码：**

1. splitPane/SplitPaneFrame.java

   ```java
   package splitPane;
   
   import java.awt.BorderLayout;
   
   import javax.swing.JFrame;
   import javax.swing.JLabel;
   import javax.swing.JList;
   import javax.swing.JSplitPane;
   import javax.swing.JTextArea;
   
   public class SplitPaneFrame extends JFrame {
   
   	private static final int DEFAULT_WIDTH = 300;
   	private static final int DEFAULT_HEIGHT = 300;
   	
   	private Planet[] planets = {
   			new Planet("Mercury", 2440, 0),
   			new Planet("Venus", 6502, 0),
   			new Planet("Earth", 6278, 1),
   			new Planet("Mars", 3397, 2),
   			new Planet("Jupiter", 71492, 16),
   			new Planet("Saturn", 69268, 18),
   			new Planet("Uranus", 25559, 17),
   			new Planet("Neptune", 24766, 8),
   			new Planet("Pluto", 1137, 1)
   	};
   	
   	public SplitPaneFrame() {
   		setSize(DEFAULT_WIDTH, DEFAULT_HEIGHT);
   		
   		// set up components for planet names, images, descriptions
   		
   		final JList<Planet> planetList = new JList<>(planets);
   		final JLabel planetImage = new JLabel();
   		final JTextArea planetDescription = new JTextArea();
   		
   		planetList.addListSelectionListener(event -> {
   			Planet value = (Planet) planetList.getSelectedValue();
   			
   			// update image and description
   			
   			planetImage.setIcon(value.getImage());
   			planetDescription.setText(value.getDescription());
   		});
   		
   		// set up split panes
   		
   		JSplitPane innerPane = new JSplitPane(JSplitPane.HORIZONTAL_SPLIT, planetList, planetImage);
   		
   		innerPane.setContinuousLayout(true);
   		innerPane.setOneTouchExpandable(true);
   		
   		JSplitPane outerPane = new JSplitPane(JSplitPane.VERTICAL_SPLIT, innerPane, planetDescription);
   		
   		add(outerPane, BorderLayout.CENTER);
   	}
   }
   ```

2. splitPane/Planet.java

   ```java
   package splitPane;
   
   import javax.swing.ImageIcon;
   
   public class Planet {
   
   	private String name;
   	private double radius;
   	private int moons;
   	private ImageIcon image;
   	
   	public Planet(String n, double r, int m) {
   		name = n;
   		radius = r;
   		moons = m;
   		image = new ImageIcon(getClass().getResource(name + ".gif"));
   	}
   	
   	public String toString() {
   		return name;
   	}
   	
   	public String getDescription() {
   		return "Radius: " + radius + "\nMoons: " + moons + "\n";
   	}
   	
   	public ImageIcon getImage() {
   		return image;
   	}
   }
   ```

   

