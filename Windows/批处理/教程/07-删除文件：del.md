### 删除文件：del

+ `del d:\test.txt` ：删除指定文件，不能是隐藏、系统、只读文件
+ `del /q/a/f d:\temp\*.*` ：删除 d:\temp 文件夹里面的所有文件，包括隐藏、只读、系统文件，不包括子目录
+ `del /q/a/f/s d:\temp\*.*` ：删除 d:\temp 文件夹及子文件夹里面的所有文件，包括隐藏、只读、系统文件，不包括子目录