如果 `int` 值是有效的，则可以通过强制类型转换，将它赋给枚举变量：

```cpp
enum spectrum 
{
    red,
    orange,
    yellow,
    green,
    blue,
    violet,
    indigo,
    ultraviolet
};

spectrum band = spectrum(3);	// typecast 3 to type spectrum
```

> 警告：如果试图对一个不适当的值进行强制类型转换，结果是不确定的，这意味着这样做不会出错，但不能依赖得到的结果：
>
> ```cpp
> band = spectrum(40003);	// undefined
> ```

