### 7.12　用sub()方法替换字符串

正则表达式不仅能找到文本模式，而且能够用新的文本替换掉这些模式。 `Regex` 对象的 `sub()` 方法需要传入两个参数。第一个参数是一个字符串，用于替换发现的匹配。第二个参数是一个字符串，即正则表达式。 `sub()` 方法返回替换完成后的字符串。

例如，在交互式环境中输入以下代码：

```javascript
>>> namesRegex = re.compile(r'Agent \w+')
>>> namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
'CENSORED gave the secret documents to CENSORED.'
```

有时候，你可能需要使用匹配的文本本身作为替换的一部分。在 `sub()` 方法的第一个参数中，可以输入 `\1` 、 `\2` 、 `\3` ，表示“在替换中输入分组 `1` 、 `2` 、 `3` 的文本”。

例如，假定想要隐去某些人的姓名，只显示他们姓名的第一个字母。要做到这一点，可以使用正则表达式 `Agent (\w)\w*` ，传入 `r'\1****'` 作为 `sub()` 方法的第一个参数。字符串中的 `\1` 将由分组 `1` 匹配的文本所替代，也就是正则表达式的 `(\w)` 分组：

```javascript
>>> agentNamesRegex = re.compile(r'Agent (\w)\w*')
>>> agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent
Eve knew Agent Bob was a double agent.')
A**** told C**** that E**** knew B**** was a double agent.'
```

