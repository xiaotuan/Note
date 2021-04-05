### 6.8　小程序：Pig Latin

Pig Latin是一种傻乎乎的、可伪造的语言，它会改变英语单词。如果单词以元音开头，就在单词末尾添加 `yay` 。如果单词以辅音或辅音簇（例如 `ch` 或 `gr` ）开头，那么该辅音或辅音簇会移至单词的末尾，然后加上 `ay` 。

让我们编写一个Pig Latin程序，该程序将输出如下内容：

```javascript
Enter the English message to translate into Pig Latin:
My name is AL SWEIGART and I am 4,000 years old.
Ymay amenay isyay ALYAY EIGARTSWAY andyay Iyay amyay 4,000 yearsyay oldyay.
```

该程序的工作原理是用本章介绍的方法更改字符串。在文件编辑器中输入以下源代码，并将文件另存为pigLat.py：

```javascript
# English to Pig Latin
print('Enter  the  English  message  to  translate  into  Pig  Latin:')
message = input()
VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
pigLatin = [] # A list of the words in Pig Latin. 
for word in message.split():
    # Separate the non-letters at the start of this word: 
    prefixNonLetters = ''
    while  len(word)  >  0  and  not  word[0].isalpha(): 
        prefixNonLetters  +=  word[0]
        word  =  word[1:]
    if len(word) == 0: 
        pigLatin.append(prefixNonLetters) 
        continue
    # Separate the non-letters at the end of this word: 
    suffixNonLetters = ''
    while not word[-1].isalpha(): 
        suffixNonLetters  +=  word[-1]
        word = word[:-1]
    # Remember if the word was in uppercase or title case.
    wasUpper = word.isupper()
    wasTitle = word.istitle()
    word = word.lower() # Make the word lowercase for translation.
    # Separate the consonants at the start of this word:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]
    # Add the Pig Latin ending to the word: 
    if prefixConsonants != '':
        word += prefixConsonants + 'ay' 
    else:
        word += 'yay'
    # Set the word back to uppercase or title case: 
    if wasUpper:
       word = word.upper() 
    if wasTitle:
       word  =  word.title()
    # Add the non-letters back to the start or end of the word.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)
# Join all the words back together into a single string:
print(' '.join(pigLatin))
```

让我们逐行来看这段代码，从头开始：

```javascript
# English to Pig Latin
print('Enter  the  English  message  to  translate  into  Pig  Latin:')
message = input()
VOWELS  =  ('a', 'e', 'i', 'o', 'u', 'y')
```

首先，要求用户输入英文文本以翻译成Pig Latin。另外，创建一个常数，将每个小写的元音字母（和y）保存为字符串元组。稍后将在程序中使用它。

接下来，创建 `pigLatin` 变量，用来存储翻译好的Pig Latin单词：

```javascript
pigLatin = [] # A list of the words in Pig Latin.
for word in message.split():
    # Separate the non-letters at the start of this word:
    prefixNonLetters = <code>''</code>
    while  len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:] 
    if len(word) == 0:
        pigLatin.append(prefixNonLetters) 
        continue
```

我们需要将每个单词单独作为一个字符串，因此调用 `message.split()` 方法以获得单词列表，并将其当作单独的字符串。字符串 `'My name is AL SWEIGART and I am 4,000 years old.'` 会导致 `split()` 方法返回 `['My','name','is','AL','SWEIGART','and','I', 'am','4,000'，'years'，'old.']` 。

我们需要删除每个单词开头和结尾的所有非字母字符，使得像 `'old.'`  这样的字符串转换为 `'oldyay.'` ，而不是 `'old.yay'` 。我们将这些非字母字符保存到名为 `prefixNonLetters` 的变量中。

```javascript
    # Separate the non-letters at the end of this word: 
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters  +=  word[-1] 
        word = word[:-1]
```

在单词的第一个字符上调用 `isalpha()` 方法的循环确定是否应该从单词中删除一个字符，并将其连接到 `prefixNonLetters` 的末尾。如果整个单词是由非字母字符组成的，例如 `'4,000'` ，那么我们可以简单地将其附加在 `pigLatin` 列表中，然后继续对下一个单词进行翻译。我们还需要保存单词字符串末尾的非字母字符。这段代码类似于上一个循环。

接下来，我们将确保程序能够记住该单词是全大写还是首字母大写，以便能够在将单词翻译成Pig Latin后将其恢复：

```javascript
    # Remember if the word was in uppercase or title case.
    wasUpper = word.isupper()
    wasTitle = word.istitle()
    word = word.lower() # Make the word lowercase for translation.
```

对于 `for` 循环中的其余代码，我们将使用小写的 `word` 。

要将sweigart这样的单词转换为eigart-sway，我们需要删除单词开头的所有辅音：

```javascript
# Separate the consonants at the start of this word: 
prefixConsonants = ''
while len(word) > 0 and not word[0] in VOWELS:
    prefixConsonants += word[0]
    word  =  word[1:]
```

我们使用的循环类似于从单词开头删除非字母字符的循环，只是现在我们要提取辅音，并将其存储到名为 `prefixConsonants` 的变量中。

如果单词的开头有辅音，那么它们现在在 `prefixConsonants` 中，我们应该将该变量和字符串 `'ay'` 连接到单词的末尾。否则，我们可以假设单词以元音开头，此时只需要连接 `'yay'` ：

```javascript
    # Add the Pig Latin ending to the word:
    if prefixConsonants  !=  '':
         word += prefixConsonants + 'ay' 
    else:
         word += 'yay'
```

回想一下，我们使用 `word = word.lower()` 将 `word` 设置为小写形式。如果单词最初是全大写或首字母大写的，那么这段代码会将单词转换回原来的大小写形式：

```javascript
# Set the word back to uppercase or title case:
if wasUpper:
    word = word.upper() 
if  wasTitle:
    word = word.title()
```

在 `for` 循环的末尾，我们将该单词及其最初带有的任何非字母前缀或后缀附加到 `pigLatin` 列表中：

```javascript
    # Add the non-letters back to the start or end of the word. 
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)
# Join all the words back together into a single string:
print(' '.join(pigLatin))
```

这个循环完成后，我们通过调用 `join()` 方法将字符串列表组合为一个字符串。这个字符串传递给 `print()` ，并在屏幕上显示我们的Pig Latin。

