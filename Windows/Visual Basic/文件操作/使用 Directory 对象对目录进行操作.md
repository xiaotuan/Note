[toc]

目录操作使用的是`System.IO.Directory`，下面是这些方法的调用：

+ 要创建目录，调用 `System.IO.Directory` 的 `CreateDirectory()` 方法，并传递要创建的新目录的名称，如下所示：

  ```vb
  System.IO.Directory.CreateDirectory("c:\my new directory")
  ```

+ 要判断目录是否存在，调用 `System.IO.Directory` 的 `Exist()` 方法，并传递要查询的目录名，如下所示：

  ```vb
  MsgBox(System.IO.Directory.Exists("c:\temp"))
  ```

+ 要移动目录，调用 `System.IO.Directory` 的 `Move()` 方法。`Move()` 方法有两个参数，第一个是当前目录名，另一个是新目录名及其路径。移动目录时，目录的内容也将移动。

  ```vb
  System.IO.Directory.Move("c:\current directory name", "c:\new directory name")
  ```

+ 删除目录比删除文件更危险，因为删除目录时，目录下的所有文件和子目录也将被删除。要删除目录，调用 `System.IO.Directory` 的 `Delete()` 方法，并将要删除的目录传递给它。例如：

  ```vb
  System.IO.Directory.Delete("C:\temp")
  ```
  
  如果目录中存在文件或子目录，需要使用如下代码进行删除：
  
  ```vb
  System.IO.Directory.Delete("C:\temp", True)
  ```

> 注意：要将目录发送到回收站，而不是永久性删除它，可像下面这样使用对象 My：
>
> ```vb
> My.Computer.FileSystem.DieleteDirectory("D:\OldDir", FileIO.UIOption.AllDialogs, FileIO.RecycleOption.SendToRecycleBin, FileIO.UICancelOption.ThrowException)
> ```
>

