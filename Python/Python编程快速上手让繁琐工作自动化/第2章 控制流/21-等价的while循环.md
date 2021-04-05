### 2.7.9　等价的while循环

实际上可以用 `while` 循环来做和 `for` 循环同样的事，只是 `for` 循环更简洁。让我们用与 `for` 循环等价的 `while` 循环覆写fiveTimes.py：

```javascript
print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1
```

可以在https://autbor.com/fivetimeswhile/查看这个程序的执行情况。运行这个程序，输出结果应该和使用 `for` 循环的fiveTimes.py程序一样。

