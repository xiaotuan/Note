模块 `json` 让你能够将简单的 `Python` 数据结构转储到文件中，并在程序再次运行时加载该文件中的数据。你还可以使用 `json` 在 `Python` 程序之间分享数据。

函数 `json.dump()` 接受两个实参：要存储的数据以及可用于存储数据的文件对象，例如：

```python
import json

numbers = [ 2, 3, 5, 7, 11, 13 ]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
	json.dump(numbers, f_obj)
```

可以使用 `json.load()` 函数将 `json.dump()` 函数存储的数据读取到内存中：

```python
import json

filename = 'numbers.json'
with open(filename) as f_obj:
	numbers = json.load(f_obj)

print(numbers)
```





