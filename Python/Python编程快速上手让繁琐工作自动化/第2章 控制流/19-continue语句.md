### 2.7.7　continue语句

像 `break` 语句一样， `continue` 语句用于循环内部。如果程序执行遇到 `continue` 语句，就会马上跳回到循环开始处，重新对循环条件求值（这也是执行到达循环末尾时发生的事情）。

让我们用 `continue` 写一个程序，要求输入名字和口令。在一个新的文件编辑器窗口中输入以下代码，将程序保存为swordfish.py：

```javascript
  while True:
      print('Who are you?')
      name = input()
    ❶ if name != 'Joe':
        ❷ continue
      print('Hello, Joe. What is the password? (It is a fish.)')
    ❸ password = input()
      if password == 'swordfish':
        ❹ break
❺ print('Access granted.')
```

如果用户输入的名字不是 `Joe` ❶， `continue` 语句❷将导致程序执行跳回到循环开始处。再次对条件求值时，执行总是进入循环，因为条件就是 `True` 。如果执行通过了  `if`  语句，用户就被要求输入口令❸。如果输入的口令是swordfish， `break` 语句执行❹，执行跳出 `while` 循环，输出 `Access granted` ❺；否则，执行继续到 `while` 循环的末尾，又跳回到循环的开始。这个程序的流程如图2-12所示。

![27.png](../images/27.png)
<center class="my_markdown"><b class="my_markdown">图2-12　swordfish.py的流程图。打叉的路径在逻辑上永远不会执行，因为循环条件总是 `True`</b></center>



**“类真”和“类假”的值**

其他数据类型中的某些值，条件认为它们等价于 `True` 和 `False` 。在用于条件时，0、0.0和' '（空字符串）被认为是 `False` ，其他值被认为是 `True` 。例如，请看下面的程序：

```javascript
name = ''
❶ while not name:
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
❷ if numOfGuests:
    ❸ print('Be sure to have enough room for all your guests.')
print('Done')
```

可以在https://autbor.com/howmanyguests/上查看这个程序的执行情况。如果用户输入一个空字符串给 `name` ，那么 `while` 循环语句的条件就会是 `True` ❶，程序继续要求输入名字。如果 `numOfGuests` 不是0❷，那么条件就被认为是 `True` ，程序就会为用户输出一条提醒信息❸。

可以用 `not name != ' '` 代替 `not name` ，用 `numOfGuests != 0` 代替 `numOfGuests` ，使用类真和类假的值会让代码更容易阅读。



运行这个程序，提供一些输入。只有你声称是Joe，它才会要求输入口令。一旦输入了正确的口令，它就会退出：

```javascript
Who are you?
I'm fine, thanks. Who are you?
Who are you?
Joe
Hello, Joe. What is the password? (It is a fish.)
Mary
Who are you?
Joe
Hello, Joe. What is the password? (It is a fish.)
swordfish
Access granted.
```

可以在https://autbor.com/hellojoe/上查看这个程序的执行情况。

