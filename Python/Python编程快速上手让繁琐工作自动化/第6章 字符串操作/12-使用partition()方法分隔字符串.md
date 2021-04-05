### 6.3.5　使用partition()方法分隔字符串

`partition()` 字符串方法可以将字符串分成分隔符字符串前后的文本。这个方法在调用它的字符串中搜索传入的分隔符字符串，然后返回3个子字符串的元组，包含“之前的文本”“分隔符”和“之后的文本”。在交互式环境中输入以下内容：

```javascript
>>> 'Hello, world!'.partition('w')
('Hello, ', 'w', 'orld!')
>>> 'Hello, world!'.partition('world')
('Hello, ', 'world', '!')
```

如果传递给 `partition()` 方法的分隔符字符串在 `partition()` 调用的字符串中多次出现，则该方法仅在第一次出现处分隔字符串：

```javascript
>>> 'Hello, world!'.partition('o')
('Hell', 'o', ', world!')
```

如果找不到分隔符字符串，则返回的元组中的第一个字符串将是整个字符串，而其他两个字符串为空：

```javascript
>>> 'Hello, world!'.partition('XYZ')
('Hello, world!', '', '')
```

可以利用多重赋值技巧将3个返回的字符串赋给3个变量：

```javascript
>>> before, sep, after = 'Hello, world!'.partition(' ')
>>> before
'Hello,'
>>> after
'world!'
```

每当你需要特定分隔符字符串之前的文本、该特定分隔符字符串以及它之后的部分时，都可以用 `partition()` 方法分隔字符串。

