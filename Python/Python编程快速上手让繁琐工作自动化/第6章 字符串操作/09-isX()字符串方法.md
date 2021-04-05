### 6.3.2　isX()字符串方法

除了 `islower()` 和 `isupper()` 方法，还有几个字符串方法的名字以 `is` 开始。这些方法返回一个描述了字符串特点的布尔值。下面是一些常用的 `isX()` 字符串方法。

+ `isalpha()` 方法，如果字符串只包含字母，并且非空，返回 `True` 。
+ `isalnum()` 方法，如果字符串只包含字母和数字，并且非空，返回 `True` 。
+ `isdecimal()` 方法，如果字符串只包含数字字符，并且非空，返回 `True` 。
+ `isspace()` 方法，如果字符串只包含空格、制表符和换行符，并且非空，返回 `True` 。
+ `istitle()` 方法，如果字符串仅包含以大写字母开头、后面都是小写字母的单词、数字或空格，返回 `True` 。

在交互式环境中输入以下代码：

```javascript
>>> 'hello'.isalpha()
True
>>> 'hello123'.isalpha()
False
>>> 'hello123'.isalnum()
True
>>> 'hello'.isalnum()
True
>>> '123'.isdecimal()
True
>>> ' '.isspace()
True
>>> 'This Is Title Case'.istitle()
True
>>> 'This Is Title Case 123'.istitle()
True
>>> 'This Is not Title Case'.istitle()
False
>>> 'This Is NOT Title Case Either'.istitle()
False
```

如果需要验证用户输入，那么 `isX()` 字符串方法是有用的。例如，下面的程序反复询问用户年龄和口令，直到他们提供有效的输入。打开一个新的文件编辑器窗口，输入以下程序，保存为validateInput.py：

```javascript
while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')
while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')
```

在第一个 `while` 循环中，我们要求用户输入年龄，并将输入保存在 `age` 中。如果 `age` 是有效的值（数字），我们就跳出第一个 `while` 循环，转向第二个循环，询问口令；否则，我们告诉用户需要输入数字，并再次要求他们输入年龄。在第二个 `while` 循环中，我们要求用户输入口令，将用户的输入保存在 `password` 中。如果输入的是字母或数字，就跳出循环；如果不是，我们并不满意，则告诉用户口令必须是字母或数字，并再次要求他们输入口令。

该程序的输出结果如下：

```javascript
Enter your age:
forty two
Please enter a number for your age.
Enter your age:
42
Select a new password (letters and numbers only):
secr3t!
Passwords can only have letters and numbers.
Select a new password (letters and numbers only):
secr3t
```

可以在https://autbor.com/validateinput/上查看该程序的执行情况。在变量上调用 `isdecimal()` 和 `isalnum()方法` ，我们就能够测试保存在这些变量中的值是否为数字或字母。这里，这些方法帮助我们拒绝输入 `forty two` ，接受输入42，拒绝输入 `secr3t!` ，接受输入 `secr3t` 。

