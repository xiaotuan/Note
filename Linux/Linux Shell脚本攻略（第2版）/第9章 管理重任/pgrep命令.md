[toc]

### 1. 常用方法

可以使用 `pgrep` 工具获取特定命令的进程 ID 列表：

```shell
$ pgrep COMMAND
```

例如：

```shell
$ pgrep bash
3933
```

> 提示：`pgrep` 只需要命令名的一部分作为输入参数来提取 `Bash` 命令，诸如 `pgrep ash` 或者 `pgrep bas` 都能奏效。

### 2. 使用过滤器选项

指定定界符：

```shell
$ pgrep COMMAND -d DELIMITER_STRING
```

例如：

```shell
$ pgrep bash -d ":"
3933:4808
```

指定进程的用户列表：

```shell
$ pgrep -u root,slynux COMMAND
```

返回所匹配的进程数量：

```shell
$ pgrep -c COMMAND
```

