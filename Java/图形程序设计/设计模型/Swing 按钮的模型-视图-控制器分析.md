对于大多数组件来说，模型类将实现一个名字以 Model 结尾的接口，例如，按钮就实现了 `ButtonModel` 接口。实现了此接口的类可以定义各种按钮的状态。实际上，按钮并不复杂，在 Swing 库中有一个名为 `DefaultButtonModel` 的类就实现了这个接口。

<center><b>ButtonModel 接口的属性</b></center>

| 属性名        | 值                                                  |
| ------------- | --------------------------------------------------- |
| actionCommand | 与按钮关联的动作命令字符串                          |
| mnemonic      | 按钮的快捷键                                        |
| armed         | 如果按钮被按下且鼠标仍在按钮上则为 true             |
| enabled       | 如果按钮是可选择的则为 true                         |
| pressed       | 如果按钮被按下且鼠标按键没有释放则为 true           |
| rollover      | 如果鼠标在按钮之上则为 true                         |
| selected      | 如果按钮已经被选择（用于复选框和单选按钮）则为 true |

每个` JButton` 对象都存储了一个按钮模型对象，可以用下列方式得到它的引用。

```java
JButton button = new JButton("Blue");
ButtonModel model = button.getModel();
```

> 注意：同样的模型（即 `DefaultButtonModel`）可用于下压按钮、单选按钮、复选框、甚至是菜单项。当然，这些按钮都有各自不同的视图和控制器。当使用 Metal 观感时，`JButton` 类用 `BasicButtonUI` 类作为其视图；用 `ButtonUIListener` 类作为其控制器。通常，每个 Swing 组件都有一个相关的后缀为 UI 的视图对象，但并不是所有的 Swing 组件都有专门的控制器对象。