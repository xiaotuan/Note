### 20.1　安装pyautogui模块

`pyautogui` 模块可以向Windows操作系统、macOS和Linux操作系统发送虚拟按键和鼠标单击事件。Windows操作系统和macOS用户可以简单地使用pip来安装PyAutoGUI。但是，Linux操作系统用户首先需要安装一些PyAutoGUI依赖的软件。

要安装 PyAutoGUI，请运行 `pip install --user pyautogui` 。不要使用 `sudo` 和 `pip` ；你可能为Python安装了添加一些模块，而操作系统也使用了它，这将导致与所有依赖原始配置的脚本产生冲突。但是，当你使用 `apt-get` 安装应用程序时，应该使用 `sudo` 命令。

附录A有安装第三方模块的完整信息。要测试PyAutoGUI是否正确安装，就在交互式环境运行 `import pyautogui` ，并检查错误信息。



**警告：**
不要把你的程序保存为pyautogui.py，否则当你运行 `import pyautogui` 时，Python会导入你的程序，而不是导入PyAutoGUI。你会得到类 `似AttributeError: module 'pyautogui' has no attribute 'click'` 这样的错误信息。



