### 4.2.2　in和not in操作符

利用 `in` 和 `not in` 操作符，可以确定一个值是否在列表中。像其他操作符一样， `in` 和 `not in` 在表达式中用于连接两个值：一个是要在列表中查找的值，另一个是待查找的列表。这些表达式将求值为布尔值。在交互式环境中输入以下代码：

```javascript
>>> 'howdy' in ['hello', 'hi', 'howdy', 'heyas']
True
>>> spam = ['hello', 'hi', 'howdy', 'heyas']
>>> 'cat' in spam
False
>>> 'howdy' not in spam
False
>>> 'cat' not in spam
True
```

例如，下面的程序让用户输入一个宠物名字，然后检查该名字是否在宠物列表中。打开一个新的文件编辑器窗口，输入以下代码，并保存为myPets.py：

```javascript
myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')
```

输出结果可能像这样：

```javascript
Enter a pet name:
Footfoot
I do not have a pet named Footfoot
```

可以在https://autbor.com/mypets/上查看该程序的执行情况。

