在 `Objective-C` 程序中，`id` 是一般对象类型，`id` 数据类型可以存储任何类型的对象。

```objc
id number;
```

我们可以声明一个方法，使其具有 `id` 类型的返回值。在此需要注意，对返回值和参数类型声明来说，`id` 是默认的类型：

```objc
-(id) newOb: (int) type;
```

`id` 和 `void *` 并非完全一样，下面是 `id` 在 `objc.h` 中的定义。

```objc
typedef struct objc_object {
    class isa;
} *id;
```

由此可以看出，`id` 是指向 `struct objc_object` 的一个指针。也就是说，`id` 是一个指向任何一个继承了 `Object` 或 `NSObject` 类的对象。因为 `id` 是一个指针，所以在使用 `id` 的时候不需要加星号，例如：

```objc
id foo = renhe;
```

