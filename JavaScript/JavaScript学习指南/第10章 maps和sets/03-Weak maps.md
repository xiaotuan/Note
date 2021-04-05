### 10.2　Weak maps

WeakMap跟Map在本质上是相同的，除了以下几点：

+ key必须是对象。
+ `WeakMap` 中的key可以被垃圾回收。
+ `WeakMap` 不能迭代或者清空。

通常，只要还有地方在引用某个对象，JavaScript就会将它保留在内存中。例如：如果有一个对象是 `Map` 中的 `key` ，那么只要这个 `Map` 存在，这个对象就会一直在内存中。但 `WeakMap` 却不是这样。正因为如此， `WeakMap` 不能被迭代（因为在迭代中，暴露处于垃圾回收过程中的对象，是非常危险的）。

正是因为 `WeakMap` 具备这些特性，才可以用它存储对象实例中的私有key。

```javascript
const SecretHolder = (function() {
   const secrets = new WeakMap();
   return class {
      setSecret(secret) {
         secrets.set(this, secret);
      }
      getSecret() {
         return secrets.get(this);
      }
   } 
})();
```

这里把 `WeakMap` 放在IIFE中，同时还放入了一个使用它的类。在IIFE外，有一个叫作 `SecretHolder` 的类，这个类的实例可以存储 `secrets` 。这样一来，secret的赋值和取值只能分别通过 `setSecret` 方法和 `getSecret` 方法完成：

```javascript
const a = new SecretHolder();
const b = new SecretHolder();
a.setSecret('secret A');
b.setSecret('secret B');
a.getSecret();    // "secret A"
b.getSecret();    // "secret B"
```

这里也可以用普通的Map，但是这样会导致SecretHolder实例中的secret永远不会被垃圾回收！

