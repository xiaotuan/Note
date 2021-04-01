### 14.1.1　 `effect (effectName, options, duration, callback)` 方法

`effect (effectName, options, duration, callback)` 方法可以按以下形式使用：

```css
 $(selector, context).effect (effectName, options, duration, callback)
```

这个方法允许我们生成一些jQuery UI中的基本特效，其参数在表14-1中列出（只有第一个参数是必需的）。

<center class="my_markdown"><b class="my_markdown">表14-1　 `effect ()` 方法的参数</b></center>

| 参数 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `effectName` | 对应要使用特效名字的字符串值（ `"blind"` 、 `"bounce"` 等） |
| `options` | 一个可选的对象值，用来指定效果的某些具体行为（例如 `options.mode` 中的 `"hide"` 或 `"show"` ） |
| `duration` | 特效的持续时间，以毫秒为单位，也可以使用字符串值 `"slow"` 或 `"fast"` 分别对应600ms和200ms。默认值为400ms |
| `callback` | 当作用于元素的特效结束时调用的回调函数（会被选择器对应的每个元素调用）。这是一个可选的参数 |

