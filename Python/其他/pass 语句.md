`Python` 有一个 `pass` 语句，可在代码块中使用它来让 `Python` 什么都不要做：

```python
def count_words(filename):
	"""计算一个文件大致包含多少个单词"""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
        pass
		# msg = "Sorry, the file " + filename + " does not exist."
		# print(msg)
	else:
		# 计算文件大致包含多少个单词
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")
	
filename = 'summing.c'
count_words(filename)
```

`pass` 语句还充当了占位符，它提醒你在程序的某个地方什么都没有做，并且以后也许要在这里做些什么。
