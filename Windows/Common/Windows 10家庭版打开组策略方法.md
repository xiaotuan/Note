[toc]

### 1. 创建执行脚本文件

脚本文件内容如下：

```bat
@echo off

pushd "%~dp0"

dir /b C:\Windows\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientExtensions-Package~3*.mum >List.txt

dir /b C:\Windows\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientTools-Package~3*.mum >> List.txt

for /f %%i in ('findstr /i . List.txt 2^>nul') do dism /online /norestart /add-package:"C:\Windows\servicing\Packages\%%i"

pause
```

将其保存为 `gpedit.bat` 。

### 2. 运行脚本

右键以管理员运行 gpedit.bat。

### 3. 打开组策略

按 <kbd>Win</kbd>+<kbd>R</kbd> 快捷键打开运行对话框，在输入框中输入 `gpedit.msc`，点击确定打开组策略应用。

