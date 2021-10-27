[toc]

### 1. 通过命令名终止进程

```shell
$ killall process_name
```

### 2. 通过名称向进程发送信号

```shell
$ killall -s SIGNAL process_name
```

### 3. 通过名称强行杀死进程

```shell
$ killall -9 process_name
```

例如：

```shell
$ killall -9 gedit
```

### 4. 通过名称以及所属用户名指定进程

```shell
$ killall -u USERNAME process_name
```

> 提示：如果需要在杀死进程前进行确认，可以使用 `killall` 的 `-i` 选项。