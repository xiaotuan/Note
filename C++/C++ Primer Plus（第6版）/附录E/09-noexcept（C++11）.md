### E.4　noexcept（C++11）

关键字noexcept用于指出函数不会引发异常。它也可用作运算符，判断操作数（表达式）是否可能引发异常；如果操作数可能引发异常，则返回false，否则返回true。例如，请看下面的声明：

```css
int hilt(int);
int halt(int) noexcept;
```

表达式noexcept(hilt) 的结果为false，因为hilt() 的声明未保证不会引发异常，但noexcept(halt) 的结果为true。



