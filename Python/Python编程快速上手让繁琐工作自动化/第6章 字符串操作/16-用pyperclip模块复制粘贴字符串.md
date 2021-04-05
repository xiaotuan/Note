### 6.5　用pyperclip模块复制粘贴字符串

`pyperclip` 模块有 `copy()` 和 `paste()` 函数，可以向计算机的剪贴板发送文本或从它接收文本。将程序的输出发送到剪贴板，使它很容易被粘贴到邮件、文字处理程序或其他软件中。



**在Mu之外运行Python脚本**

到目前为止，你一直在使用Mu中的交互式环境和文件编辑器来运行Python脚本。但是，在每次运行一个脚本时都要打开Mu和Python脚本，这样不方便。好在，有一些快捷方式可以让你更容易地建立和运行Python脚本。这些步骤在Windows操作系统、macOS和Linux操作系统上稍有不同，但每一种都在附录B中进行了描述。请翻到附录B，学习如何方便地运行Python脚本，并能够向它们传递命令行参数。（使用Mu时，不能向程序传递命令行参数。）



`pyperclip` 模块不是Python自带的。要安装它，请参考附录A中安装第三方模块的指南。安装 `pyperclip` 模块后，在交互式环境中输入以下代码：

```javascript
>>> import pyperclip
>>> pyperclip.copy('Hello, world!')
>>> pyperclip.paste()
'Hello, world!'
```

当然，如果你的程序之外的某个程序改变了剪贴板的内容，那么 `paste()` 函数就会返回改后的内容。例如，如果我将这句话复制到剪贴板，然后调用 `paste()` 函数，看起来就会像这样：

```javascript
>>> pyperclip.paste()
'For example, if I copied this sentence to the clipboard and then called
paste(), it would look like this:'
```

