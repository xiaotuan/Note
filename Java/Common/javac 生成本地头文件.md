在 `Java 9` 后，`Oracle` 公司移除了 `javah` 生成本地头文件的工具，使用 `javac` 工具替代 `javah` 工具。使用 `javac` 工具生成本地头文件的方法如下：

```shell
javac -h 要放置头文件的目录 java文件
```

例如，在当前目录下有一个 `SerialPort.java` 文件，现在希望生成的头文件放置在当前目录下来，可以在当前目录下执行如下命令：

```shell
$ javac -h . SerialPort.java
```

