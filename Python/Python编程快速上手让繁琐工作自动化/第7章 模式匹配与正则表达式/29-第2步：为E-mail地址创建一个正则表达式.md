### 第2步：为E-mail地址创建一个正则表达式

还需要一个正则表达式来匹配E-mail地址。让你的程序看起来像这样：

```javascript
#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
import pyperclip, re
phoneRegex = re.compile(r'''(
--snip--
# Create email regex.
emailRegex = re.compile(r'''(
  ❶ [a-zA-Z0-9._%+-]+ # username
  ❷ @ # @ symbol
  ❸ [a-zA-Z0-9.-]+ # domain name
     (\.[a-zA-Z]{2,4}) # dot-something
     )''', re.VERBOSE)
# TODO: Find matches in clipboard text.
# TODO: Copy results to the clipboard.
```

E-mail地址的用户名部分❶是一个或多个字符，字符可以包括小写和大写字母、数字、句点、下划线、百分号、加号或短横线。可以将这些全部放入一个字符分类： `[a-zA-Z0-9._%+-]` 。

域名和用户名用@符号分隔❷，域名❸允许的字符分类要少一些，只允许字母、数字、句点和短横线： `[a-zA-Z0-9.-]` 。最后是“dot-com”部分（技术上称为“顶级域名”），它实际上可以是“dot-anything”，有2～4个字符。

E-mail地址的格式有许多奇怪的规则。这个正则表达式不会匹配所有可能的、有效的E-mail地址，但它会匹配你遇到的大多数典型的E-mail地址。

