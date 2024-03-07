`sys` 模块提供了 `argv` 变量——该变量实际上是一个列表，其首项为该程序的名称，第二个参数及后续的参数为该程序的命令行参数。例如：

```python
import sys

print(sys.argv)
```

运行结果如下：

```shell
$ python .\Test.py -v test -i info
['.\\Test.py', '-v', 'test', '-i', 'info']
```



