### 5.13.1　将if…else语句转化成条件表达式

如果 `if...else` 语句用于确定某个值，不论该值是赋值语句的一部分，还是表达式的一小部分，再或者是函数的返回值，一般建议使用条件运算符来代替。条件运算符让代码更紧凑易读。例如：

```javascript
if(isPrime(n)) {
    label = 'prime';
} else {
    label = 'non-prime';
} 
```

可以被写成：

```javascript
label = isPrime(n) ? 'prime' : 'non-prime';
```

