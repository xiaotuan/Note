[toc]

### 1. Windows

1. 找到 `node.exe` 文件所在目录。
2. 将该目录添加到 PATH 环境变量中。

### 2. Mac

1. 找到 Node 执行程序目录。

2. 使用 `echo $PATH` 命令查看该目录是否存在 PATH 环境变量中。

3. 如果 PATH 环境变量中没有该目录，则需要编辑 `~/.bash_profile` 文件，添加下面这段脚本（假设 Node 的安装目录为 `/usr/local/bin`）：

   ```
   PATH=${PATH}:/usr/local/bin
   ```

### 3. Linux

配置方法与 Mac 系统一样。