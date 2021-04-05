### 4.3.2　使用break或return避免不必要的计算

如果循环仅仅是为了找到一个特定值，这样就没有必要在已经找到目标值后还继续执行到最后。

比如，计算一个数字是否为素数是一个相对耗费资源的计算。如果想从1 000个数字中查找第一个素数，比较幼稚的做法可能是：

```javascript
let firstPrime = null;
for(let n of bigArrayOfNumbers) {
    if(isPrime(n) && firstPrime === null) firstPrime = n;
}
```

如果 `bigArrayOfNumbers` 有上百万个数字，而且只有最后一个是素数（事先并不知道），这样的做法还行。但是如果第一个就是素数呢？或者第5个，第15个？本可以早点结束这个计算，却需要挨个检查近百万个数字！听起来就很累。其实，当找到目标值后，就可以立刻使用 `break` 语句来结束循环：

```javascript
let firstPrime = null;
for(let n of bigArrayOfNumbers) {
    if(isPrime(n)) {
        firstPrime = n;
        break;
    }
}
```

如果循环写在一个方法中，可以用 `return` 语句来替代 `break` 。

