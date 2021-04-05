### 20.2　在macOS上设置无障碍应用程序

作为一项安全措施，macOS通常不会让程序控制鼠标或键盘。要使PyAutoGUI 在macOS上工作，你必须将运行Python脚本的程序设置为无障碍应用程序。没有这一步，你的PyAutoGUI函数调用将没有任何效果。

无论你是在Mu、IDLE还是命令行窗口上运行Python程序，都要打开该程序。然后打开System Preferences并进入Accessibility标签页。当前打开的应用程序将出现在Allow the apps below to control your computer标签下。勾选Mu、IDLE、Terminal，或任何你用来运行Python脚本的应用程序。系统会提示输入口令，确认这些更改。

