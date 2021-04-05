### 4.4.5　使用reverse()方法反转列表中的值

如果要快速反转列表中项目的顺序，可以调用 `reverse()` 方法。在交互式环境中输入以下内容：

```javascript
>>>  spam = ['cat', 'dog', 'moose'] 
>>>  spam.reverse()
>>> spam
['moose', 'dog', 'cat'] 
```



**Python中缩进规则的例外**

在大多数情况下，代码行的缩进告诉Python它属于哪一个代码块。但是，这个规则有几个例外。例如在源代码文件中，列表实际上可以跨越几行。这些行的缩进并不重要。Python知道，没有看到结束方括号，列表就没有结束。例如，代码可以看起来像下面这样：

```javascript
spam = ['apples',
    'oranges',
                  'bananas',
'cats']
print(spam)
```

当然，从实践的角度来说，大部分人会利用Python的行为，让他们的列表看起来美观且可读，就像神奇8球（magic8ball.py）程序中的消息列表一样。

也可以在行末使用续行字符\将一条指令写成多行。可以把\看作“这条指令在下一行继续”。对于\续行字符之后的一行，缩进并不重要。例如，下面是有效的Python代码：

```javascript
print('Four score and seven ' + \
      'years ago...')
```

如果希望将一长行的Python代码安排得更为易读，这些技巧是有用的。



和  `sort()` 方法一样， `reverse()` 方法也不返回列表。这就是为什么写成 `spam.reverse()` 而不是 `spam = spam.reverse()` 。

