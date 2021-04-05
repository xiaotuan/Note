### 17.8.1　向Popen()传递命令行参数

用 `Popen()` 创建进程时，程序可以向进程传递命令行参数。要做到这一点，需要向 `Popen()` 传递一个列表作为唯一的参数。该列表中的第一个字符串是要启动的程序的可执行文件名，所有后续的字符串将是在该程序启动时，传递给该程序的命令行参数。实际上，这个列表将作为被启动程序的 `sys.argv` 的值。

大多数具有图形用户界面（GUI）的应用程序，不像基于命令行的程序那样尽可能地使用命令行参数。但大多数GUI应用程序将接收一个参数，表示应用程序启动时立即打开的文件。例如，如果你使用的是Windows操作系统，那么创建一个简单的文本文件C:\Users\Al\hello.txt，然后在交互式环境中输入以下代码：

```javascript
>>> subprocess.Popen(['C:\\Windows\\notepad.exe', 'C:\\Users\Al\\hello.txt'])
<subprocess.Popen object at 0x00000000032DCEB8>
```

这不仅会启动记事本应用程序，也会让它立即打开C:\Users\Al\hello.txt。

