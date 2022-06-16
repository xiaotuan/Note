`break` 语句用于控制程序流程，可使用它来控制哪些代码将执行，哪些代码不执行，从而让程序按你的要求执行你要执行的代码。

例如：

```python
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
	city = input(prompt)
	
	if city == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() + "!")
```

