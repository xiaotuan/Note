[toc]

### 1. 使用 MessageBox.Show() 函数显示消息

`MessageBox.Show()` 函数可用于告诉用户一些事前或询问用户一个问题。除显示文本外，该函数也可用来显示图标、一个或多个用户可单击的按钮。显示的文本可以是任意的，但图标和按钮必须从已定义的图标和按钮列表中选择。

下面是调用 `MessageBox.Show()` 的几种方式：

+ 要显示指定的文本、在标题栏显示标题以及 "确定" 按钮，使用如下语法：

  ```vb
  MessageBox.Show(MessageText, Caption)
  ```

+ 要显示包含指定文本、标题、一个或多个按钮的消息框，使用如下语法

  ```vb
  MessageBox.Show(MessageText, Caption, Buttons)
  ```

+ 要显示包含指定文本、标题、按钮和图标的消息框，使用如下语法：

  ```vb
  MessageBox.Show(MessageText, Caption, Buttions, Icon)
  ```

在所有这些语句当中，`MessageText` 是消息框中要显示的文本，`Captions` 决定了显示在消息框标题栏中的文本，`Buttons` 决定了用户看到的按钮，`Icon` 决定消息框要显示什么图标。

> 注意：老式 `MsgBox()` 函数（现在虽然得到支持，但不建议使用它）默认将项目名用作消息框的标题。`MessageBox.Show()` 没有默认标题，因此你总是应该指定标题，否则消息框的标题栏将为空。

### 2. 指定按钮和图标

使用 `Buttons` 参数，可以在消息框中显示一个或多个按钮，其值为 `MessageBoxButtons` 类型的枚举，可用的值如下所示：

| 成员             | 说明                               |
| ---------------- | ---------------------------------- |
| AbortRetryIgnore | 显示 "终止"、"重试" 和 "忽略" 按钮 |
| OK               | 显示 "确定" 按钮                   |
| OKCancel         | 显示 "确定" 和 "取消" 按钮         |
| YesNoCancel      | 显示 "是"、"否" 和 "取消" 按钮     |
| YesNo            | 显示 "是" 和 "否" 按钮             |
| RetryCancel      | 显示 "重试" 和 "取消" 按钮         |

`Icon` 参数决定消息框中显示的符号。`Icon` 参数是 `MessageBoxIcon` 类型的枚举：

| 成员        | 说明                                   |
| ----------- | -------------------------------------- |
| Exclamation | 在一个黄色背景的三角形中显示一个惊叹号 |
| Information | 在一个圆圈中显示一个小写字母 i         |
| None        | 不显示任何符号                         |
| Question    | 在一个圆圈中显示一个问号               |
| Stop        | 在一个红色背景的圆圈中显示一个白色 X   |
| Warning     | 在一个黄色背景的三角形中显示一个惊叹号 |

例如：

```vb
MessageBox.Show("I'm about to do something...", "MessageBox sample", MessageBoxButtons.OKCancel, MessageBoxIcon.Infrormation)
```

如果在消息框显示时用户按回车键，消息框将认为用户单击了默认按钮。在每个消息框中将哪个按钮作为默认按钮，都需要仔细考虑。可以使用如下方法设置默认按钮：

```vb
MessageBox.Show("I'm about to do something irreversible...", "MessageBox sample", MessageBoxButtons.OKCancel, MessageBoxIcon.Information, MessageBoxDefaultButton.Button2)
```

如果发生某些情况而用户无法采取任何措施，不要显示给用户 "取消" 按钮：

```vb
MessageBox.Show("Something bad has happened!", "MessageBox sample", MessageBoxButtons.OK, MessageBoxIcon.Error)
```

### 3. 判断单击的是哪个按钮

`MessageBox.Show()` 函数将被单击的按钮为 `DialogResult` 枚举值返回。`DialogResult` 的可能取值如下：

| 成员   | 说明                                     |
| ------ | ---------------------------------------- |
| Abort  | 返回值为 "Abort"：通常由 "终止" 按钮发出 |
| Cancel | 返回 "Cancel"：通常由 "取消" 按钮发出    |
| Ignore | 返回 "Ignore"：通常由 "忽略" 按钮发出    |
| No     | 返回 "No"：通常由 "否" 按钮发出          |
| None   | 不返回任何值，程序继续运行               |
| OK     | 返回 "OK"：通常由 "确定" 按钮发出        |
| Retry  | 返回 "Retry"：通常由 "重试" 按钮发出     |
| Yes    | 返回 "Yes"：通常由 "是" 按钮发出         |

> 注意：`DialogResult` 值描述中的 "通常由......发出"。创建自定义对话框时，可以将 `DialogResult` 值分配给任何选择的按钮。

例如：
```vb
If (MessageBox.Show("Would you like to do X?", "MessageBox sample", MessageBoxButtons.YesNo, MessageBoxIcon.Question) = Windows.Forms.DialogResult.Yes) Then
    ' Code to do X would go here.
End If
```

### 4. 创建好的消息

除了要考虑在消息中显示的图标和按钮外，在编写消息文本时，还应遵循下列原则：

+ 使用正式语言。不要使用很长的词，避免使用缩写。尽量使文本能被立即理解、不要太花哨；消息框不是表现你文字功底的地方。
+ 将消息限制在两三行内。冗长的消息不仅让用户很难读懂，且看起来可能很吓人。当消息框用于询问问题时，问题要尽量简洁。
+ 不要让用户觉得他们做错了什么。用户确实可能犯错，但显示的消息不应让用户产生这种感觉。
+ 检查所有消息文本的拼写。
+ 避免使用术语。用户使用软件并不意味着他们是技术人员，用英语进行解释。
+ 保证按钮与文本匹配！例如，如果消息没有向用户提出问题，就不要显示 "是" / "否" 按钮。



