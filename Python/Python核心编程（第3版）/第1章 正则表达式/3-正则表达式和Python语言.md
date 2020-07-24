[toc]

##### 1.3.1 re模块：核心函数和方法

**表1-2 常见的正则表达式属性**

| 函数 / 方法 | 描述 |
| :- | :- |
| 仅仅是 re 模块函数 | |
| compile(pattern, flags = 0) | 使用任何可选的标记来编译正则表达式的模式，然后返回一个正则表达式对象 |
| re 模块函数和正则表达式对象的方法 | |
| match(pattern, string, flags=0) | 尝试使用带有可选的标记的正则表达式的模式来匹配字符串。，如果匹配成功，就返回匹配对象；如果失败，就返回 None |
| search(pattern, string, flags=0) | 使用可选标记搜索字符串中第一次出现的正则表达式模式。如果匹配成功，则返回匹配对象；如果失败，则返回 None |
| findall(pattern, string[, flags]) | 查找字符串中所有（非重复）出现的正则表达式模式，并返回一个匹配列表 |
| finditer(pattern, string[, flags]) | 与 findall() 函数相同，但返回的不是一个列表，而是一个迭代器。对于每一次匹配，迭代器都返回一个匹配对象。 |
| split(pattern, string, max=0) | 根据正则表达式的模式分隔符，split 函数将字符串分割为列表，然后返回成功匹配的列表，风格最多操作 max 次（默认分割所有匹配成功的位置） |
| re 模块函数和正则表达式对象方法 | |
| sub(pattern, repl, string, count=0) | 使用 repl 替换所有正则表达式的模式在字符串中出现的位置，除非定义 count，否则就将替换所有出现的位（另见 subn() 函数，该函数返回替换操作的数目） |
| purge() | 清除隐式编译的正则表达式模式 |
| 常用的匹配对象方法（长裤文档以获取更多信息） | |
| group(num=0) | 返回整个匹配对象，或者编号为 num 的特定子组 |
| group(defualt=None) | 返回一个包含所有匹配子组的元组（如果没有成功匹配，则返回一个空元组）|
| groupdict(default=None) | 返回一个包含所有匹配的命名子组的字典，所有的子组名称作为字典的键（如果没有成功匹配，则返回一个空字典 ） |
| 常用的模块属性（用于大多数正则表达式函数的标记） | |
| re.I、re.IGNORECASE | 不区分大小写的匹配 |
| re.L、re.LOCALE | 根据所使用的本地语言环境通过 \w、\W、\b、\B、\s、\S 实现匹配 |
| re.M、re.MULTILINE | ^ 和 $ 分别匹配目标字符串中行的起始和结尾，而不是严格匹配整个字符串本身的起始和结尾 |
| re.S、re.DOTALL | "." （点号）通常匹配除了 \n （换行符）之外的所有单个字符；该标记表示 "." （点号）能够匹配全部字符 |
| re.X、re.VERBOSE | 通过反斜线转义，否则所有空格加上 #（以及在该行中所有后续文字）都被忽略，除非在一个字符类中或者允许注释并且提高可读性 |

由于正则表达式在执行过程中将进行多次比较操作，因此强烈建议使用预编译。而且，既然正则表达式式的编译是必需，那么使用预编译来提升执行性能无疑是明智之举。 `re.compile()` 能够提供此功能。

其实模块函数会对已编译的对象进行缓存，所以不是所有使用相同正则表达式模式的 `search()` 和 `match()` 都需要编译。在不同的 `Python` 版本中，缓存中已编译过的正则表达式对象的数目可能不同，而且没有文档记录。`purge()` 函数能够用于清除这些缓存。

##### 1.3.2 使用 compile() 函数编译正则表达式

对于一些特别的正则表达式编译，可选的标记可能以参数的形式给出。请参考表1-2中的条目以及在正式的官方文档中查询关于这些标记（re.IGNORECASE、re.MULTILINE、re.DOTALL、re.VERBOSE 等）。它们可以通过按位或操作符（|）合并。

这些标记也可以作为参数适用于大多数 re 模块函数。如果想要在方法中使用这些标记，它们必须已经集成到已编译的正则表达式对象之中，或者需要使用直接嵌入到正则表达式本身的（?F）标记，其中 F 是一个或者多个 i （用于 re.I/IGNORECASE）、m（用于 re.M/MULTILINE）、s（用于 re.S/DOTALL）等。如果想要同时使用多个，就把它们放在一起而不是使用按位或操作，例如，（?im）可以用于同时表示 re.IGNORECASE 和 re.MULTILINE。

##### 1.3.3 匹配对象以及 group() 和 groups() 方法

匹配对象是成功调用 `match()` 或者 `search()` 返回的对象。匹配对象有两个主要的方法：`group()` 和 `groups()`。

`group()` 要么返回整个匹配对象，要么根据要求返回特定子组。`groups()` 则仅返回一个包含唯一或者全部子组的元组。如果没有子组的要求，那么当 `group()` 仍然返回整个匹配是，`groups()` 返回一个空元组。

##### 1.3.4 使用 match() 方法匹配字符串

`match()` 函数试图从字符串的**起始部分**对模式进行匹配。如果匹配成功，就返回一个匹配对象；如果匹配失败，就返回 None，匹配对象的 group() 方法能够用于显示那个成功匹配。

```python
import re

m = re.match("foo", "foo")	# 模式匹配字符串
if m is not None:	# 如果匹配成功，就输出匹配内容
  m.group()
```

##### 1.3.5 使用 search() 在一个字符串中查找模式（搜索与匹配的对比）

`search()` 的工作方式与 `match()` 完全一致，不同之处在于 `search()` 会用它的字符串参数， 在任意位置对给定正则表达式模式搜索第一次出现的匹配情况。如果搜索到成功的匹配，就会返回一个匹配对象；否则，返回 None。

```python
import re

m = re.match('foo', 'seafood')	# 匹配失败
if m is not None: m.group()
```

`search()` 函数不但会搜索模式在字符串中第一次出现的位置，而且严格地对字符串从左到由搜索。

```python
import re

m = re.search('foo', 'seafood') # 使用 search() 代替，搜索成功
if m is not None: m.group()
```

##### 1.3.6 匹配多个字符串

```python
import re

bt = 'bat|bet|bit'	# 正则表达式模式：bat、bet、bit
m = re.match(bt, 'bat')	# 'bat' 是一个匹配
if m is not None: m.group()
m= re.match(bt, 'blt')	# 对于 'blt' 没有匹配
if m is not None: m.group()
m = re.match(bt, 'He bit me!') # 不能匹配字符串
if m is not None: m.group()
m = re.search(bt, 'He bit me!') # 通过搜索查找 'bit'
if m is not None: m.group()
```

##### 1.3.7 匹配任何单个字符

```python
import re 

anyend = ".end"
m = re.match(anyend, 'bend')	# 点号匹配 'b'
if m is not None: m.group()
m = re.match(anyend, 'end')	# 不匹配任何字符
if m is not None: m.group()
m = re.search('anyend', '\nend.')	# 除了 \n 之外的字符
if m is not None: m.group()
m = re.search('.end', 'The end.')	# 在搜索中匹配 ' '
if m is not None: m.group()
```

```python
import re 

patt314 = '3.14'	# 表示正则表达式的点号
pi_patt = '3\.14'	# 表示字面量的点号
m = re.match(pi_patt, '3.14')	# 精确匹配
if m is not None: m.group()
m = re.match(patt314, '3014')	# 点号匹配 '0'
if m is not None: m.group()
m = re.match(patt314, '3.14')	# 点号匹配 '.'
if m is not None: m.group()
```

##### 3.1.8 创建字符集（[ ]）

```python
import re 

m = re.match('[cr][23][dp][o2]', 'c3po')	# 匹配 ’c3po'
if m is not None: m.group()
m = re.match('[cr][23][dp][o2]', 'c2do')	# 匹配 'c2do'
if m is not None: m.group()
m = re.match('r2d2|c3po', 'c2do')	# 不匹配 'c2do'
if m is not None: m.group()
m = re.match('r2d2|c3po', 'r2d2')	# 匹配 'r2d2'
if m is not None: m.group()
```

##### 3.1.9 重复、特殊字符以及分组

```python
import re

patt = '\w+@(\w+\.)?\w+\.com'
re.match(patt, 'nobody@xxx.com').group()
re.match(patt, 'nobody@www.xxx.com').group()
```

```python
import re
patt = '\w+@(\w+\.)*\w+\.com'
re.match(patt, 'nobody@www.xxx.yyy.zzz.com').group()
```

```python
import re
m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
m.group()	# 完整匹配 'abc-123'
m.group(1)	# 子组 1 'abc'
m.group(2)	# 子组 2 '123'
m.groups()	# 全部子组 "('abc', '123')"
```

```python
import re
m = re.match('ab', 'ab')	# 没有子组
m.group()	# 完整匹配 'ab'
m.groups()	# 所有子组 '()'
m = re.match('(ab)', 'ab')	# 一个子组
m.group()	# 完整匹配 'ab'
m.group(1)	# 子组 1 'ab'
m.groups()	# 全部子组 "('ab',)"
m = re.match('(a)(b)', 'ab')	# 两个子组
m.group()	# 完整匹配 'ab'
m.group(1)	# 子组 1 'a'
m.group(2)	# 子组 2 'b'
m.groups()	# 所有子组 "('a', 'b')"
m = re.match('(a(b))', 'ab')	# 两个子组
m.group()	# 完整匹配 'ab'
m.group(1) 	# 子组 1 'ab'
m.group(2)	# 子组 2 'b'
m.groups()	# 所有子组 "('ab', 'b')"
```

##### 1.3.10 匹配字符串的起始和结尾以及单词边界

```python
import re
m = re.search('^The', 'The end.')	# 匹配
if m is not None: m.group()
m = re.search('^The', 'end. The')	# 不作为起始，不匹配
if m is not None: m.group()
m = re.search(r'\bthe', 'bite the dog')	# 在边界
if m is not None: m.group()
m = re.search(r'\bthe', 'bitethe dog')	# 有边界，不匹配
if m is not None: m.group()
m = re.search(r'\Bthe', 'bitethe dog')	# 没有边界，匹配
if m is not None: m.group()
```

通常情况下，在正则表达式中使用原始字符串是个好主意。

##### 1.3.11 使用 findall() 和 finditer() 查找每一次出现的位置

`findall()` 查询字符串中某个正则表达式模式全部的非重复出现情况。`findall()` 总是返回一个列表。如果 `findall()` 没有找到匹配的部分，就返回一个空列表，但如果匹配成功，列表将包含所有成功的匹配部分（从左向右按出现顺序排列）。

```python
import re
re.findall('car', 'car')	# ['car']
re.findall('car', 'carry the barcardi to the car')	# ['car', 'car', 'car']
```

```python
import re
s = 'This and that.'
re.findall(r'(th\w+) and (th\w+)', s, re.I)	# '[('This', 'that')]'
re.finditer(r'(th\w+) and (th\w+)', s, re.I).__next__().groups()	# "('This', 'that')"
# next(re.finditer(r'(th\w+) and (th\w+)', s, re.I)).groups()
re.finditer(r'(th\w+) and (th\w+)', s, re.I).__next()__.group(2)	# 'that'
# next(re.finditer(r'(th\w+) and (th\w+)', s, re.I)).groups(2)
[g.groups() for g in re.finditer(r'(th\w+) and (th\w+)', s, re.I)]	# "[('This', 'that')]"

re.findall(r'(th\w+)', s, re.I)	# "['This', 'that']"
it = re.finditer(r'(th\w+)', s, re.I)
g = it.__next__()
g.groups()	# "('This', )"
g.group(1)	# 'This'
g = it.__next__()
g.groups()	# "('that', )"
g.group(1)	# 'that'
[g.group(1) for g in re.finditer(r'(th\w+)', s, re.I)]	# "['This', 'that']"
```

##### 1.3.12 使用 sub() 和 subn() 搜索与替换

有两个函数 / 方法用于实现搜索和替换功能：`sub()` 和 `subn()`。两者几乎一样，都是将某字符串中所有匹配正则表达式的部分进行某种形式的替换。用来替换的部分通常是一个字符串，但它也可能是一个函数，该函数返回一个用来替换的字符串。 `subn()` 和 `sub()` 一样，但 `subn()` 还返回一个表示替换的总数，替换后的字符串和表示替换总数的数字一起作为一个拥有两个元素的元组返回。

```python
import re

re.sub('X', 'Mr.Smith', 'attn: X\n\nDear X, \n')  # 'attn: Mr.Smith\n\nDear Mr.Smith, \n'
re.subn('X', 'Mr.Smith', 'attn: X\n\nDear X,\n')  # "('attn: Mr.Smith\n\nDear Mr.Smith, \n', 2)"
print(re.sub('X', 'Mr.Smith', 'attn: X\n\nDear X, \n'))  # 'attn: Mr.Smith'
re.sub('[ae]', 'X', 'abcdef') # 'XbcdXf'
re.subn('[ae]', 'X', 'abcdef')  # "('XbcdXf', 2)"
```

使用匹配对象的 `group()` 方法除了能够取出匹配分组编号外，还可以使用 \N，其中 N 是替换字符串中使用的分组编号。

```python
import re

re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', '2/20/91')
re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', '2/20/1991')
```

##### 1.3.13 在限定模式上使用 split() 分隔字符串

```python
import re

re.split(':', 'str1:str2:str3') # "['str1', 'str2', 'str3']"

DATA = (
  'Mountain View, CA 94040',
  'Sunnyvale, CA',
  'Los Altos, 94023',
  'Cupertino 95014',
  'Palo Alto CA'
)
for datum in DATA:
  print(re.split(',|(?=(?:\d{5}|[A-Z]{2}))', datum))
# ['Mountain View', ' ', 'CA', '94040']
# ['Sunnyvale', ' ', 'CA']
# ['Los Altos', ' ', '94023']
# ['Cupertino', '95014']
# ['Palo Alto', 'CA']
```

##### 1.3.14 扩展符号

通过使用 (?isLmsux) 系列选项，用户可以直接在正则表达式里面指定一个或者多个标记，而不是通过 `compile()` 或者其他 re 模块函数。

下面为一些使用 `re.I/IGNORECASE`示例，最后一个示例在 `re.M/MULTILINE` 实现多行混合：

```python
import re

re.findall(r'(?i)yes', 'yes? Yes.YES!!')  # ['yes', 'Yes', 'YES']
re.findall(r'(?i)th\w+', 'The quickest way is through this tunnel.')  # ['The', 'through', 'this']
re.findall(r'(?im)(^th[\w]+)', """
This line is the first,
another line,
that line, it's the best
""")  # ['This', 'that']
```

下一组演示使用 `re.S/DOTALL`。该标记表明点号（.）能够用来表示 \n 符号（反之其通常用于表示除了 \n 之外的全部字符）：

```python
import re

re.findall(r'th.+', '''
The first line
the second line
the third line
''')  # ['the second line', 'the third line']
re.findall(r'(?s)th.+', '''
The first line
the second line
the third line
''')  # ['the second line\nthe third line\n']
```

`re.X/VERBOSE` 标记允许用户通过抑制在正则表达式中使用空白符（除了在字符类中或者在反斜线转义中）来创建更易读的正则表达式。此外，散列、注释和井号也可以用于一个注释的开始，只要他们不再一个用反斜线转义的字符类中。

```python
import re

re.search(r'''(?x)
  \((\d{3})\) # 区号
  [ ] # 空白符
  (\d{3}) # 前缀
  - # 横线
  (\d{4}) # 终点数字
''', '(800) 555-1212').groups()
```

`(?:...)` 符号可以对部分正则表达式进行分组，但是并不会保存该分组用于后续的检索或者应用。

```python
import re

re.findall(r'http://(?:\w+\.)*(\w+\.com)', 'http://google.com http://www.google.com http://code.google.com')  # ['google.com', 'google.com', 'google.com']
re.search(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})', '(800) 555-1212').groupdict()  # {'areacode': '800', 'prefix':'555'}
```

可以同时一同使用 `(?P<name>)` 和 `<?P=name>` 符号。可以使用 `\g<name>` 来检索它们：

```python
import re

re.sub(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})', '(\g<areacode>) \g<prefix>-xxxx', '(800) 555-1212') # '(800) 555-xxxx'
```

可以在一个相同的正则表达式中重用模式，而不必稍后再次在（相同）正则表达式中指定相同的模式。

```python
import re

bool(re.match(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?P<number>\d{4}) (?P=areacode)-(?P=prefix)-(?P=number) 1(?P=areacode)(?P=prefix)(?P=number)', '(800) 555-1212 800-555-1212 18005551212')) # True
bool(re.match(r'''(?x)
  # match (800) 555-1212, save areacode, prefix, no.
  \((?P<areacode>\d{3})\)[ ](?P<prefix>\d{3})-(?P<number>\d{4})
  
  #space
  [ ]
  
  # match 800-555-1212
  (?P=areacode)-(?P=prefix)-(?P=number)
  
  # space
  [ ]
  
  # match 18005551212
  1(?P=areacode)(?P=prefix)(?P=number)
''', '(800) 555-1212 800-555-1212 18005551212'))  # True
```

可以使用 `(?=...)` 和 `(?!...)` 符号在目标字符串中实现一个前视匹配，而不必实际上使用这些字符串。

```python
import re
 
re. findall(r'\w+(?= van Rossum)', 
'''
  Guido van Rossum
  Tim Peters
  Alex Martelli
  Just van Rossum
  Raymond Hettinger
''')  # ['Guido', 'Just']
re.findall(r'(?m)^\s+(?!noreply|postmaster)(\w+)', '''
  sales@phptr.com
  postmaster@phptr.com
  eng@phptr.com
  noreply@phptr.com
  admin@phptr.com
''')  # ['sales', 'eng', 'admin']  
```

最后一个示例展示了使用条件正则表达式匹配。

```python
import re
 
bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xy'))  # True
bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xx'))  # False
```

##### 1.3.15 杂项

正则表达式对于探索原始字符串有着强大的动力，原因就是在于 ASCII 字符和正则表达式的特殊字符之间存在冲突。作为一个特殊符号，\b 表示 ASCII 字符的退格符，但是 \b 同时也是一个正则表达式的特殊符号，表示匹配一个单词的边界。对于正则表达式编译器而言，若它把两个 \b 视为字符串内容而不是单个退格符，就需要在字符串中再使用一个反斜线转义反斜线，就像这样： \\b。

```python
import re
 
m = re.match('\bblow', 'blow')  # backspace、no match
if m: m.group()
m = re.match('\\bblow', 'blow') # escaped\, now it works
if m: m.group() # 'blow'
m = re.match(r'\bblow', 'blow') # use raw string instead
if m: m.group() # 'blow'
```

