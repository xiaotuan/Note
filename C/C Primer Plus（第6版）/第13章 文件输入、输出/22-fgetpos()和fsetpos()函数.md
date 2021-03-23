#### 13.5.4　 `fgetpos()` 和 `fsetpos()` 函数

`fseek()` 和 `ftell()` 潜在的问题是，它们都把文件大小限制在 `long` 类型能表示的范围内。也许20亿字节看起来相当大，但是随着存储设备的容量迅猛增长，文件也越来越大。鉴于此，ANSI C新增了两个处理较大文件的新定位函数： `fgetpos()` 和 `fsetpos()` 。这两个函数不使用 `long` 类型的值表示位置，它们使用一种新类型： `fpos_t` （代表file position type，文件定位类型）。 `fpos_t` 类型不是基本类型，它根据其他类型来定义。 `fpos_t` 类型的变量或数据对象可以在文件中指定一个位置，它不能是数组类型，除此之外，没有其他限制。实现可以提供一个满足特殊平台要求的类型，例如， `fpos_t` 可以实现为结构。

ANSI C定义了如何使用 `fpos_t` 类型。 `fgetpos()` 函数的原型如下：

```c
int fgetpos(FILE * restrict stream, fpos_t * restrict pos);
```

调用该函数时，它把 `fpos_t` 类型的值放在 `pos` 指向的位置上，该值描述了文件中的当前位置距文件开头的字节数。如果成功， `fgetpos()` 函数返回 `0` ；如果失败，返回非 `0` 。

`fsetpos()` 函数的原型如下：

```c
int fsetpos(FILE *stream, const fpos_t *pos);
```

调用该函数时，使用 `pos` 指向位置上的 `fpos_t` 类型值来设置文件指针指向偏移该值后指定的位置。如果成功， `fsetpos()` 函数返回 `0` ；如果失败，则返回非 `0` 。 `fpos_t` 类型的值应通过之前调用 `fgetpos()` 获得。

