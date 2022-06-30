`try-except-else` 代码块的工作原理大致如下：`Python` 尝试执行 `try` 代码块中的代码；只有可能引发异常的代码才需要放在 `try` 语句中。有时候，有一些仅在 `try` 代码块成功执行时才需要运行的代码；这些代码应放在 `else` 代码块中。`except` 代码块告诉 `Python` ，如果它尝试运行 `try` 代码块中的代码时引发了指定的异常，该怎么办。

例如：

```python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0!")
	else:
		print(answer)
```

