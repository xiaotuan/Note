1. 单源文件编译运行：

```console
$ javac EmployeeTest.java
$ java EmployeeTest
```

> 注意：使用 `java` 命令运行 `class` 文件时不需在文件名后面加 `.class` 文件后缀，否则会运行报错。

2. 多源文件编译（假设所有源文件都是以 `Employee` 字符开头）

```console
$ javac Employee*.jjava
$ java EmployeeTest
```

3. 编译带包名的源文件

    a. 工程目录结构如下：
    
    ```
    .基目录
      |_PackageTest.java
      |_PackageTest.class
      |_com/
          |_horstmann/
              |_corejava/
                  |_Employee.java
                  |_Employee.class
    ```
    
    编译命令如下：
    
    ```console
    $ javac PackageTest.java
    $ java PackageTest
    ```
    
    > 编译器会自动查找文件 `com/horstmann/corejava/Employee.java` 并进行编译。
    
    b. 工程目录结构如下：
    
    ```
    .基目录
      |_com/
          |_horstmann/
          |   |_corejava/
          |       |_Employee.java
          |       |_Employee.class
          |_mycmpany/
              |_PayrollApp.java
              |_PayrollApp.class
    ```
    
    编译命令如下：
    
    ```console
    $ javac com/mycompany/PayrollApp.java
    $ java com.mycompany.PayrollApp
    ```
    
    > 需要注意，编译器对文件（带有文件分隔符和扩展名 `.java` 的文件）进行操作。而 `Java` 解释器加载类（带有 . 分隔符）。

**设置类路径**

最好采用 `-classpath` （或 `-cp`）选项指定类路径：

```console
$ java -classpath /home/user/classdir:.:/home/user/archives/archive.jar MyProg.java`

或

$ java -classpath c:\classdir;.;c:\archives\archive.jar MyProg.java
```

也可以通过设置 `CLASSPATH` 环境变量完成这个操作。其详细情况依赖于所使用的 `shell`。命令格式如下：

```
export CLASSPATH=/home/user/classdir:.:/home/user/archives/archive.jar
```

在 `C shell` 中，命令格式如下：

```
setenv CLASSPATH /home/user/classdir:.:/home/user/archives/archive.jar
```

在 `Windows shell`，命令格式如下：

```
set CLASSPATH=c:\classdir;.;c:\archives\archive.jar
```

