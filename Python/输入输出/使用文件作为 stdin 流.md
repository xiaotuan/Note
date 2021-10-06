可以使用如下代码将文件内容作为 `stdin` 的数据：

```python
dbfile = open(dbfilename)
import sys
sys.stdin = dbfile
```

