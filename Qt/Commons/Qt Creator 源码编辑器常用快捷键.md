

<center class="my_markdown"><b class="my_markdown">源程序编辑器的快捷操作</b></center>

| 功能                                               | 快捷键       | 解释                                                         |
| :------------------------------------------------- | :----------- | :----------------------------------------------------------- |
| Switch Header/Source                               | F4           | 在同名的头文件和源程序文件之间切换                           |
| Follow Symbol Under Cursor                         | F2           | 跟踪光标下的符号，若是变量，可跟踪到变量声明的地方；若是函数体或函数声明，可在两者之间切换 |
| Switch Between Function Declaration and Definition | Shift+F2     | 在函数的声明（函数原型）和定义（函数实现）之间切换           |
| Refactor\Rename Symbol Under Cursor                | Ctrl+Shift+R | 对光标处的符号更改名称，这将替换到所有用到这个符号的地方     |
| Refactor\Add Definition in .cpp                    |              | 为函数原型在cpp文件里生成函数体                              |
| Auto-indent Selection                              | Ctrl+I       | 为选择的文字自动进行缩进                                     |
| Toggle Comment Selection                           | Ctrl+/       | 为选择的文字进行注释符号的切换，即可以注释所选代码，或取消注释 |
| Context Help                                       | F1           | 为光标所在的符号显示帮助文件的内容                           |
| Save All                                           | Ctrl+Shift+S | 文件全部保存                                                 |
| Find/Replace                                       | Ctrl+F       | 调出查找/替换对话框                                          |
| Find Next                                          | F3           | 查找下一个                                                   |
| Build                                              | Ctrl+B       | 编译当前项目                                                 |
| Start Debugging                                    | F5           | 开始调试                                                     |
| Step Over                                          | F10          | 调试状态下单步略过，即执行当前行程序语句                     |
| Step Into                                          | F11          | 调试状态下跟踪进入，即如果当前行里有函数，就跟踪进入函数体   |
| Toggle Breakpoint                                  | F9           | 设置或取消当前行的断点设置                                   |