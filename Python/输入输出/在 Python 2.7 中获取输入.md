如果你使用的是 `Python 2.7`，应使用函数 `raw_input()` 来提示用户输入。这个函数与 `Python 3` 中的 `input()` 一样，也将输入解读为字符串。`Python 2.7` 也包含函数 `input()`，但它将用户输入解读为 Python 代码，并尝试运行它们。例如：

```python
age = raw_input("How old are you? ")
age = int(age)
print(age >= 18)
```