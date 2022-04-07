[toc]

### 1. 支持的对话框类型

下表列出了 `dialog` 可以创建的对话框的主要类型：

| 类型    | 用于创建类型的选项 | 含义                                                         |
| ------- | ------------------ | ------------------------------------------------------------ |
| 复选框  | --checklist        | 允许用户显示一个选项列表，每个选项都可以被单独选择           |
| 信息框  | --infobox          | 在显示消息后，对话框将立刻返回，但并不清除屏幕               |
| 输入框  | --inputbox         | 允许用户输入文本                                             |
| 菜单框  | --menu             | 允许用户选择列表中的一项                                     |
| 消息框  | --msgbox           | 向用户显示一条消息，同事显示一个 OK 按钮，用户可以通过选择该按钮继续操作 |
| 单选框  | --radiolist        | 允许用户选择列表中的一个选项                                 |
| 文本框  | --textbox          | 允许用户在带有滚动条的文本框中显示一个文件的内容             |
| 是/否框 | --yesno            | 允许用户提问，用户可以选择 yes 或 no                         |

> 提示
>
> 还有一些其他的对话框类型（例如，进度框和密码框）可用。如果想了解更多不常用的对话框类型，可以使用如下命令参考在线手册页：
>
> ```shell
> man dialog
> ```

### 2. 对话框参数

| 对话框类型  | 参数                                               |
| ----------- | -------------------------------------------------- |
| --checklist | text height width list-height [tag text status]... |
| --infobox   | text height width                                  |
| --inputbox  | text height width [initial string]                 |
| --menu      | text height width menu-height [tag item]...        |
| --msgbox    | text height width                                  |
| --radiolist | text height width list-height [tag text status]... |
| --textbox   | filename height width                              |
| --yesno     | text height width                                  |

