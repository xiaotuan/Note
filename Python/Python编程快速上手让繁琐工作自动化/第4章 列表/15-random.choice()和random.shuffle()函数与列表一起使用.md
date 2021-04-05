### 4.2.5　random.choice()和random.shuffle()函数与列表一起使用

`random` 模块有几个接收参数列表的函数。 `random.choice()` 函数将从列表中返回一个随机选择的表项。在交互式环境中输入以下内容：

```javascript
>>> import random
>>>  pets = ['Dog', 'Cat', 'Moose'] 
>>>    random.choice(pets) 
'Dog'
>>>    random.choice(pets) 
'Cat'
>>>    random.choice(pets) 
'Cat'
```

你可以认为 `random.choice(someList)` 是 `someList[random.randint(0, len(someList)– 1]` 的较短形式。

`random.shuffle()` 函数将对列表中的表项重新排序。该函数将就地修改列表，而不是返回新列表。在交互式环境中输入以下内容：

```javascript
>>> import random
>>> people = ['Alice', 'Bob', 'Carol', 'David'] 
>>> random.shuffle(people) 
>>> people
['Carol', 'David', 'Alice', 'Bob'] 
>>> random.shuffle(people) 
>>> people
['Alice', 'David', 'Bob', 'Carol'] 
```

