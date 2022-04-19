[toc]

### 1. if 语句

if 语句的通用形式如下所示：

```python
if conditional_test:
    do something
```

例如：

```python
age = 19
if age >= 18:
	print("You are old enough to vote!")
```

在 if 语句中，缩进的作用与 for 循环中相同。如果测试通过了，将执行 if 语句后面所有缩进的代码行，否则将忽略它们。

```python
age = 19
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
```

### 2. if-else 语句

if-else 语句块类似于简单的 if 语句，但其中的 else 语句让你能够指定条件测试未通过时要执行的操作。

```python
age = 17
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")
```

### 3. if-elif-else 语句

Python 只执行 if-elif-else 结构中的一个代码块，它依次检查每个条件测试，直到遇到通过了的条件测试。测试通过后，Python 将执行紧跟在它后面的代码，并跳过余下的测试。

```python
age = 12

if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")
```

#### 3.1 使用多个 elif 代码块

可根据需要使用任意数量的 elif 代码块。例如：

```python
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
else:
	price = 3

print("Your admission cost is $" + str(price) + ".")
```

#### 3.2 省略 else 代码块

Python 并不要求 if-elif 结构后面必须有 else 代码块。例如：

```python
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
elif age >= 65:
	price = 35

print("Your admission cost is $" + str(price) + ".")

```

