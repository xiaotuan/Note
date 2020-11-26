执行下面命令获取 Python 解释器的完整路径：

```console
$ type -a python3
python3 is /usr/local/bin/python3
```

启动 Sublime Text，并选择菜单 Tools -> Build System -> New Build System，这将打开一个新的配置文件。删除其中的所有内容，再输入如下内容：

```json
{
    "cmd": ["/usr/local/bin/python3", "-u", "$file"],
}
```

