### 10.4　Weak sets

Weak sets只能包含对象，这些对象可能会被垃圾回收。跟 `WeakMap` 类似， `WeakSet` 中的值不能被迭代，这就让weak sets变得很特殊；所以很难找到它的用例。事实上，weak sets的唯一用处是判断给定对象在不在一个set中。

例如：圣诞老人可能会有一个叫作调皮（naughty）的 `WeakSet` ，这样他就知道该给谁送煤块（不调皮的孩子才会得到正常的礼物）：

```javascript
const naughty = new WeakSet();
const children = [
   { name: "Suzy" },
   { name: "Derek" },
]; 
naughty.add(children[1]);
for(let child of children) {
   if(naughty.has(child))
      console.log('Coal for ${child.name}!');
   else
      console.log('Presents for ${child.name}!');
}
```

