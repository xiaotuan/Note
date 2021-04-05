### 3.2　返回值和return语句

如果调用 `len()` 函数，并向它传入像 `'Hello'` 这样的参数，函数调用就求值为整数5。这是传入的字符串的长度。一般来说，函数调用求值的结果，称为函数的“返回值”。

用 `def` 语句创建函数时，可以用 `return` 语句指定应该返回什么值。 `return` 语句包含以下部分。

+ `return` 关键字。
+ 函数应该返回的值或表达式。

如果在 `return` 语句中使用了表达式，返回值就是该表达式求值的结果。例如，下面的程序定义了一个函数，它根据传入的数字参数，返回一个不同的字符串。在文件编辑器中输入以下代码，并保存为magic8Ball.py：

```javascript
❶ import random
❷ def getAnswer(answerNumber):
    ❸ if answerNumber == 1:
           return 'It is certain'
      elif answerNumber == 2:
           return 'It is decidedly so'
      elif answerNumber == 3:
           return 'Yes'
      elif answerNumber == 4:
           return 'Reply hazy try again'
      elif answerNumber == 5:
           return 'Ask again later'
      elif answerNumber == 6:
           return 'Concentrate and ask again'
      elif answerNumber == 7:
           return 'My reply is no'
      elif answerNumber == 8:
           return 'Outlook not so good'
      elif answerNumber == 9:
           return 'Very doubtful'
❹ r = random.randint(1, 9)
❺ fortune = getAnswer(r)
❻ print(fortune)
```

可以在https://autbor.com/magic8ball/上查看这个程序的执行情况。在这个程序开始时，Python首先导入 `random` 模块❶。然后 `getAnswer()` 函数被定义❷。因为函数是被定义（而不是被调用）的，所以执行会跳过其中的代码。接下来， `random.randint()` 函数被调用，带两个参数，分别为1和9❹。它求值为1和9之间的一个随机整数（包括1和9），这个值被存在一个名为 `r` 的变量中。

`getAnswer()` 函数被调用，以 `r` 作为参数❺。程序执行转移到 `getAnswer()` 函数的顶部❸， `r` 的值被保存到名为 `answerNumber` 的变元中。然后，根据 `answerNumber` 中的值，函数返回许多可能字符串中的一个。程序执行返回到程序底部的代码行，即原来调用 `getAnswer()` 函数的地方❺。返回的字符串被赋给一个名为 `fortune` 的变量，然后它又被传递给 `print()` 调用❻，并被输出在屏幕上。

请注意，因为可以将返回值作为参数传递给另一个函数调用，所以你可以将下面3行代码：

```javascript
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
```

缩写成1行等价的代码：

```javascript
print(getAnswer(random.randint(1, 9)))
```

记住，表达式是值和操作符的组合。函数调用可以用在表达式中，因为它求值为它的返回值。

