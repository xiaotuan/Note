### 2.3.5　write()大小限制

如果count值大于SSIZE_MAX，调用write()的结果是未定义的。

调用write()时，如果count值为零，会立即返回，且返回值为0。

