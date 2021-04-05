```javascript
spam
```

## 3.7　global语句

如果需要在一个函数内修改全局变量，就使用 `global` 语句。如果在函数的顶部有 `global eggs` 这样的代码，它是在告诉Python：“在这个函数中， `eggs` 指的是全局变量，所以不要用这个名字创建一个局部变量。”例如，在文件编辑器中输入以下代码，并保存为globalStatement.py：

```javascript
def spam():
  ❶ global eggs
  ❷ eggs = 'spam'
eggs = 'global'
spam()
print(eggs)
```

运行该程序，最后的 `print()` 调用将输出：

```javascript
spam
```

可以在https://autbor.com/globalstatement/上查看这个程序的执行情况。因为 `eggs` 在 `spam()` 函数的顶部被声明为 `global` ❶，所以当 `eggs` 被赋值为 `'spam'` 时❷，赋值发生在全局作用域的 `eggs` 上，没有创建局部 `eggs` 变量。

有4条法则用来区分一个变量是处于局部作用域还是全局作用域。

+ 如果变量在全局作用域中使用（即在所有函数之外），它就是全局变量。
+ 如果在一个函数中，有针对该变量的 `global` 语句，它就是全局变量。
+ 如果该变量用于函数中的赋值语句，它就是局部变量。
+ 如果该变量没有用在赋值语句中，它就是全局变量。

为了更好地理解这些法则，这里有一个示例程序。在文件编辑器中输入以下代码，并保存为sameNameLocalGlobal.py：

```javascript
def spam():
  ❶ global eggs
    eggs = 'spam' # this is the global
def bacon():
  ❷ eggs = 'bacon' # this is a local
def ham():
  ❸ print(eggs) # this is the global
eggs = 42 # this is the global
spam()
print(eggs)
```

在 `spam()` 函数中， `eggs` 是全局变量，因为在函数的开始处，有针对 `eggs` 变量的 `global` 语句❶。在 `bacon()` 函数中， `eggs` 是局部变量，因为在该函数中有针对它的赋值语句❷。在 `ham()` 函数中❸， `eggs` 是全局变量，因为在这个函数中，既没有赋值语句，也没有针对它的 `global` 语句。如果运行sameNameLocalGlobal.py，输出结果将是：

可以在https://autbor.com/sameNameLocalGlobal/上查看这个程序的执行情况。在一个函数中，一个变量要么总是全局变量，要么总是局部变量。函数中的代码没有办法先使用名为 `eggs` 的局部变量，稍后又在同一个函数中使用名为 `eggs` 全局变量。



**注意：**
如果想在一个函数中修改全局变量中存储的值，就必须对该变量使用 `global` 语句。



在一个函数中，如果试图在局部变量赋值之前就使用它，像下面的程序这样，Python就会报错。为了看到效果，请在文件编辑器中输入以下代码，并保存为sameName4.py：

```javascript
  def spam():
      print(eggs) # ERROR!
   ❶  eggs = 'spam local'
❷ eggs = 'global'
  spam()
```

运行前面的程序，会产生错误信息：

```javascript
Traceback (most recent call last):
  File "C:/test3784.py", line 6, in <module>
    spam()
  File "C:/test3784.py", line 2, in spam
    print(eggs) # ERROR!
UnboundLocalError: local variable 'eggs' referenced before assignment
```

可以在https://autbor.com/sameNameError/上查看这个程序的执行情况。发生这个错误是因为，Python看到 `spam()` 函数中有针对 `eggs` 的赋值语句❶，认为 `eggs` 变量是局部变量。但是因为 `print(eggs)` 的执行在 `eggs` 赋值之前，所以局部变量 `eggs` 并不存在。Python不会退回以使用 `eggs` 全局变量❷。



**函数作为“黑盒”**

通常，对于一个函数，你要知道的就是它的输入值（变元）和输出值。你并非总是需要加重自己的负担，弄清楚函数的代码实际是怎样工作的。如果以这种高层的方式来思考函数，通常大家会说，这里将该函数看成一个黑盒。

这个思想是现代编程的基础。本书后面的章节将向你展示一些模块，其中的函数是由其他人编写的。尽管你在好奇的时候也可以看一看源代码，但如果仅仅为了能使用它们，你并不需要知道它们是如何工作的。而且，因为鼓励在编写函数时不使用全局变量，所以你通常也不必担心函数的代码会与程序的其他部分发生交叉影响。



