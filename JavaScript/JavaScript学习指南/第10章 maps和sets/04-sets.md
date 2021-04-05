### 10.3　sets

set是一个不允许重复数据的集合（跟数学中集合的概念一样）。这里继续沿用前面的例子，如果想要给user赋多个role。例如：所有user都会有一个“ `User` ”role，但是管理员既有“ `User` ”role，也有“ `Admin` ”role。不过，从逻辑上讲，一个user拥有重复的role很不合理。而set就是处理这种情况的理想数据结构，下面来看看它的实现：

首先，创建一个Set实例：

```javascript
const roles = new Set(); 
```

如果想添加一个user role，可以用 `add``()` 方法：

```javascript
roles.add("User");     // Set [ "User" ] 
```

如果想把这个user变成管理员，继续调用 `add()` 方法：

```javascript
roles.add("Admin");       // Set [ "User", "Admin" ] 
```

跟 `Map` 一样， `Set` 也有 `size` 属性：

```javascript
roles.size;               // 2 
```

这就是set的优美之处：不需要在添加元素的时候检查set中是否已经有这个元素了。如果添加早已存在于set中的值，什么都不会发生：

```javascript
roles.add("User");       // Set [ "User", "Admin" ]
roles.size;              // 2
```

删除role的时候，调用 `delete()` 方法就行，当它返回true的时候表示这个role在set中，否则返回 `false` 。

```javascript
roles.delete("Admin");         // true
roles;                         // Set [ "User" ]
roles.delete("Admin");         // false
```

