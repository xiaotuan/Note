### 5.1.5　setdefault()方法

你常常需要为字典中的某个键设置一个默认值，当该键没有任何值时使用它。代码看起来像这样：

```javascript
spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'
```

`setdefault()` 方法提供了一种方式，可以在一行中完成这件事。传递给该方法的第一个参数是要检查的键，第二个参数是当该键不存在时要设置的值。如果该键确实存在，那么 `setdefault()` 方法就会返回键的值。在交互式环境中输入以下代码：

```javascript
>>> spam = {'name': 'Pooka', 'age': 5}
>>> spam.setdefault('color', 'black')
'black'
>>> spam
{'color': 'black', 'age': 5, 'name': 'Pooka'}
>>> spam.setdefault('color', 'white')
'black'
>>> spam
{'color': 'black', 'age': 5, 'name': 'Pooka'}
```

第一次调用 `setdefault()` 方法时， `spam` 变量中的字典变为 `{'color': 'black', 'age': 5, 'name': 'Pooka'}` 。该方法返回值 `'black'` ，因为现在该值被赋给键 `'color'` 。当 `spam.setdefault('color', 'white')` 接下来被调用时，该键的值没有被改变成 `'white'` ，因为 `spam` 变量已经有名为 `'color'` 的键了。

`setdefault()` 方法是一个很好的快捷方式，可以确保有一个键存在。下面有一个小程序，可以计算一个字符串中每个字符出现的次数。打开一个文件编辑器窗口，输入以下代码，保存为characterCount.py：

```javascript
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
❶ count.setdefault(character, 0)
❷ count[character] = count[character] + 1
print(count)
```

可以在 https://autbor.com/setdefault 上查看该程序的执行情况。程序循环迭代 `message` 变量中的每个字符，以计算每个字符出现的次数。调用 `setdefault()` 方法❶确保了键存在于 `count` 字典中（默认值是0），这样在执行 `count[character] = count[character] + 1` 时❷，就不会出现 `KeyError` 错误。程序运行时的输出结果如下：

```javascript
{' ': 13, ',': 1, '.': 1, 'A': 1, 'I': 1, 'a': 4, 'c': 3, 'b': 1, 'e': 5, 'd': 3, 'g': 2, 'i':
6, 'h': 3, 'k': 2, 'l': 3, 'o': 2, 'n': 4, 'p': 1, 's': 3, 'r': 5, 't': 6, 'w': 2, 'y': 1}
```

从输出结果可以看到，小写字母c出现了3次，空格字符出现了13次，大写字母A出现了1次。无论 `message` 变量中包含什么样的字符串，这个程序都能工作，即使该字符串有上百万个字符。

