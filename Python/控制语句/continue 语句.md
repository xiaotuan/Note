要返回到循环开头，并根据条件测试结果决定是否继续执行循环，可使用 `continue`。例如：

```python
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
		
	print(current_number)
```

