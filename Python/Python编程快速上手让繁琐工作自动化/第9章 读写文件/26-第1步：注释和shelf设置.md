### 第1步：注释和shelf设置

我们从一个脚本框架开始，其中包含一些注释和基本设置，让你的代码看起来像这样：

```javascript
   #! python3
   # mcb.pyw - Saves and loads pieces of text to the clipboard.
❶ # Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
   #        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
   #        py.exe mcb.pyw list - Loads all keywords to clipboard.
❷ import shelve, pyperclip, sys
❸ mcbShelf = shelve.open('mcb')
  #  TODO:  Save  clipboard  content.
  # TODO: List keywords and load content.
  mcbShelf.close()
```

将一般用法信息放在文件顶部的注释中，这是常见的做法❶。如果忘了如何运行这个脚本，就可以看看这些注释，帮助自己回忆起来。然后导入模块❷。复制和粘贴需要使用 `pyperclip` 模块，读取命令行参数需要使用 `sys` 模块。 `shelve` 模块也需要准备好。当用户希望保存一段剪贴板文本时，你需要将它保存到一个 `shelf` 文件中。然后，当用户希望将文本复制回剪贴板时，你需要打开 `shelf` 文件，将它重新加载到程序中。这个 `shelf` 文件命名时带有前缀mcb❸。

