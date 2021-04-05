### 8.1.4　关键字参数allowRegexes和blockRegexes

你也可以使用正则表达式指定输入是否被接受。关键字参数 `allowRegexes` 和 `blockRegexes` 利用正则表达式字符串列表来确定 `PyInputPlus` 模块的函数将接受或拒绝哪些内容作为有效输入。例如，在交互式环境中输入以下代码，使得 `inputNum()` 函数将接收罗马数字以及常规数字作为有效输入：

```javascript
>>> import pyinputplus as pyip
>>> response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero']) 
XLII
>>> response
'XLII'
>>> response = pyip.inputNum(allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero']) 
xlii
>>> response
'xlii'
```

当然，这个正则表达式仅影响 `inputNum()` 函数从用户那里接收的字母；该函数仍会接收具有无效顺序的罗马数字，例如 `'XVX'` 或 `'MILLI'` ，因为 `r'(I|V|X|L|C|D|M)+'` 正则表达式接收这些字符串。

你还可以用 `blockRegexes` 关键字参数指定 `PyInputPlus` 模块的函数不接收的正则表达式字符串列表。在交互式环境中输入以下内容，使得 `inputNum()` 不接收偶数作为有效输入：

```javascript
>>> import pyinputplus as pyip
>>> response = pyip.inputNum(blockRegexes=[r'[02468]$']) 
42
This response is invalid.
44
This response is invalid.
43
>>> response
43
```

如果同时指定 `allowRegexes` 和 `blockRegexes` 参数，那么允许列表将优先于阻止列表。例如，在交互式环境中输入以下内容，它允许使用 `'caterpillar'` 和 `'category'` ，但会阻止包含 `'cat'` 的任何其他内容：

```javascript
>>> import pyinputplus as pyip
>>> response = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'],
blockRegexes=[r'cat'])
cat
This response is invalid.
catastrophe
This response is invalid.
category
>>> response
'category'
```

`PyInputPlus` 模块的函数可以避免你自己编写繁琐的输入验证代码，而且 `PyInputPlus` 模块的功能比这里详细介绍的更多。

