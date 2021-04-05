### 10.1.4　用send2trash模块安全地删除

因为Python内置的 `shutil.rmtree()` 函数将不可恢复地删除文件和文件夹，所以用起来可能有危险。删除文件和文件夹更好的方法是使用第三方的 `send2trash` 模块。你可以在命令行窗口中运行 `pip install send2trash` 来安装该模块（参见附录A，其中更详细地解释了如何安装第三方模块）。

利用 `send2trash` 比用Python常规的删除函数要安全得多，因为它会将文件夹和文件发送到计算机的回收站，而不是永久删除它们。如果因程序bug而用 `send2trash` 删除了某些你不想删除的东西，那么稍后可以从回收站恢复。

安装 `send2trash` 后，在交互式环境中输入以下代码：

```javascript
>>> import send2trash
>>> baconFile = open('bacon.txt', 'a') # creates the file
>>> baconFile.write('Bacon is not a vegetable.')
25
>>> baconFile.close()
>>> send2trash.send2trash('bacon.txt')
```

一般来说，总是应该使用 `send2trash.send2trash()` 函数来删除文件和文件夹。虽然它将文件发送到回收站，让你稍后能够恢复它们，但是这不像永久删除文件，它不会释放磁盘空间。如果你希望程序释放磁盘空间，就要用 `os` 和 `shutil` 来删除文件和文件夹。请注意， `send2trash()` 函数只能将文件发送到回收站，不能从中恢复文件。

