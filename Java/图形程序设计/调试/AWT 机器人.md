`Robot` 类可以向任何 AWT 程序发送按键和鼠标点击事件。这个类就是用来自动测试用户界面的。

要得到一个机器人，首先需要得到一个 `GraphicsDevice` 对象。可以通过以下调用序列得到默认屏幕设备：

```java
GraphicsEnvironment environment = GraphicsEnvironment.getLocalGraphicsEnvironment();
GraphicsDevice screen = environment.getDefaultScreenDevice();
```

然后构造一个机器人：

```java
Robot robot = new Robot(screen);
```

若要发送一个按键事件，需告知机器人模拟按下和松开按键：

````java
robot.keyPress(KeyEvent.VK_TAB);
robot.keyRelease(KeyEvent.VK_TAB);
````

对于鼠标点击事件，首先需要移动鼠标，然后按下再释放鼠标按钮：

```java
robot.mouseMove(x, y);	// x and y are absolute screen pixel coordinates.
robot.mousePress(InputEvent.BUTTON1_MASK);
robot.mouseRelease(InputEvent.BUTTON1_MASK);
```

我们的思路是首先模拟按键和鼠标输入，然后截屏来查看应用是否完成了它该完成的工作。截屏需要使用 `createScreenCapture` 方法：

```java
Rectangle rect = new Rectangle(x, y, width, height);
BufferedImage image = robot.createScreenCapture(rect);
```

最后，通常我们都希望在机器人指令之间增加一个很小的延迟，使应用能跟得上。可以使用 `delay` 方法并提供延迟时间（毫秒数）。例如：

```java
robot.delay(1000);	// delay by 1000 milliseconds
```

**示例代码：**

```java
```

