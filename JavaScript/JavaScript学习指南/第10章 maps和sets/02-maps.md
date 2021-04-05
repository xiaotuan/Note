### 10.1　maps

在ES6之前，当需要把键和值映射起来的时候，一般会首选对象，因为对象能把字符串类型的键映射到任意类型的对象。不过出于这个原因而使用对象会有很多弊端：

+ 对象原型中可能存在并不需要的映射。
+ 弄清楚对象中有多少映射并没有那么简单。
+ 因为键必须是一个字符串或者符号，这样一来就不能将对象映射到值。
+ 对象不能保证自身属性的顺序。

`Map` 对象帮助解决了这些问题，它是将键和值映射起来的（即使键是一个字符串）的绝佳选择。例如：当想把user对象映射到role的时候：

```javascript
const u1 = { name: 'Cynthia' };
const u2 = { name: 'Jackson' };
const u3 = { name: 'Olive' };
const u4 = { name: 'James' };
```

从创建一个map对象开始：

```javascript
const userRoles = new Map();
```

可以使用map中的set()方法把user赋给role：

```javascript
userRoles.set(u1, 'User');
userRoles.set(u2, 'User');
userRoles.set(u3, 'Admin');
// poor James...we don't assign him a role
```

链式调用 `set()` 方法，还可以节省打字的时间：

```javascript
userRoles
   .set(u1, 'User')
   .set(u2, 'User')
   .set(u3, 'Admin');

```

还可以给map的构造函数传一个包含了数组的数组：

```javascript
const userRoles = new Map([
   [u1, 'User'],
   [u2, 'User'],
   [u3, 'Admin'],
]);
```

现在如果想知道 `u2` 中有什么role，使用 `get()` 方法就行：

```javascript
userRoles.get(u2);      // "User"
```

如果调用的key在map中不存在，就会返回一个 `undefined` 。当然，也可以用 `has()` 方法来查看map中是否包含给定的key。

```javascript
userRoles.has(u1);    // true
userRoles.get(u1);    // "User"
userRoles.has(u4);    // false
userRoles.get(u4);    // undefined
```

如果key已经在map中了，那么调用set()后key对应的value就会被替换：

```javascript
userRoles.get(u1);            // 'User'
userRoles.set(u1, 'Admin');
userRoles.get(u1);            // 'Admin'
```

`size` 属性返回map中的元素个数：

```javascript
userRoles.size;               // 3 
```

使用 `keys()` 方法可以拿到map中所有的键， `values()` 可以拿到所有的值， `entries()` 则可以以数组的方式获取键值对，数组的第一个元素为键，第二个元素为值。所有这些方法都返回一个可以迭代的对象，从而能用 `for…of` 循环来迭代：

```javascript
for(let u of userRoles.keys())
   console.log(u.name);
for(let r of userRoles.values())
   console.log(r);
for(let ur of userRoles.entries())
   console.log('${ur[0].name}: ${ur[1]}');
// 这里可以通过解构让迭代更自然
for(let [u, r] of userRoles.entries())
   console.log('${u.name}: ${r}');
// entries()方法是Map的默认迭代器，所以上例可以简写为：
for(let [u, r] of userRoles)
   console.log('${u.name}: ${r}');
```

如果需要一个数组（而不是一个可迭代的对象），可以使用展开运算符：

```javascript
[...userRoles.values()];   // [ "User", "User", "Admin" ] 
```

使用 `delete()` 方法可以删除map中的一个条目：

```javascript
userRoles.delete(u2);
userRoles.size;            // 2
```

最后，如果想删除map中的所有条目，可以调用clear()方法：

```javascript
userRoles.clear();
userRoles.size;            // 0
```

