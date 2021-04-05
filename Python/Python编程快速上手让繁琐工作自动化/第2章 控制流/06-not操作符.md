### 2.3.2　not操作符

与 `and` 和 `or` 不同， `not` 操作符只作用于一个布尔值（或表达式），这使它成为“一元”操作符。 `not` 操作符求值为相反的布尔值：

```javascript
   >>> not True
   False
❶  >>> not not not not True
   True
```

就像在说话和写作中使用双重否定一样，你可以嵌套 `not` 操作符❶，虽然在真正的程序中并不经常这样做。表2-4为 `not` 操作符的真值表。

<center class="my_markdown"><b class="my_markdown">表2-4　 `not` 操作符的真值表</b></center>

| 表达式 | 求值为 |
| :-----  | :-----  | :-----  | :-----  |
| `not True` | `False` |
| `not False` | `True` |

