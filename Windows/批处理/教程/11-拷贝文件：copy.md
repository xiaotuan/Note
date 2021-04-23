### 拷贝文件：copy

+ `copy c:\test.txt d:\test.bak` ：复制 c:\test.txt 文件到 d:\，并重命名为 test.bak

+ `copy con test.txt` 从屏幕上等待输入，按 <kbd>Ctrl</kbd>+<kbd>Z</kbd> 结束输入，输入内容存为 test.txt 文件

  con 代表屏幕，prn 代表打印机，null 代表空设备

  > 注意：无法保存中文输入。

+ `copy 1.txt + 2.txt 3.txt` ：合并 1.txt 和 2.txt 的内容，保存为 3.txt 文件，如果不指定 3.txt，则保存到 1.txt

+ `copy test.txt +` ：复制文件到自己，实际上是修改了文件日期



