### 5.9.3　void运算符

void运算符只有一个用途：计算它的操作数并返回 `undefined` 。听起来好像没什么用，实际上确实没用。它可以强制表达式返回 `undefined` ，但作者从来没有遇到过这种情况。本书提及它的唯一理由是可能偶尔会碰到它被用做HTML标签 `<a>` 的URI。

```javascript
<a href="javascript:void 0">Do nothing.</a>
```

虽然不推荐这样做，但它确实是一种常见的用法。

