### 14.4.1　 `addClass ()` 、 `removeClass ()` 以及 `toggleClass ()` 的增强型方法

jQuery UI改进了jQuery提供的 `addClass ()` 、 `removeClass ()` 和 `toggleClass ()` 方法。表14-14中列出了这些方法的参数。

<center class="my_markdown"><b class="my_markdown">表14-14　 `addClass()` 、 `removeClass()` 和 `toggleClass()` 方法的相关参数</b></center>

| 参数 | 功能 |
| :-----  | :-----  | :-----  | :-----  |
| `className` | 一个或多个CSS类名（用空格隔开） |
| `duration` | 指定特效的持续时间，以毫秒为单位。设为0的话会直接应用新样式，而非逐渐过渡 |
| `easing` | 指定特效的演进方式 |
| `callback` | 当作用于元素的特效结束后所调用的回调函数（会被选择器选取的每个元素调用）。函数中的这个值表示的是特效所作用的DOM元素 |
| `addOrRemove` | 可选的布尔值，用来指定添加（如果设为 `true` ）还是删除CSS类（如果设为 `false` ）。如果没有指定且元素已有此CSS类，则会被移除 |

增强型的 `addClass ()` 方法用法如下：

```css
$(selector, context).addClass (className, duration, easing, callback);
```

增强型的 `removeClass ()` 方法用法如下：

```css
$(selector, context).removeClass (className, duration, easing, callback);
```

增强型的 `toggleClass ()` 方法用法如下：

```css
$(selector, context).toggleClass (className, addOrRemove, duration, easing, callback);
```

