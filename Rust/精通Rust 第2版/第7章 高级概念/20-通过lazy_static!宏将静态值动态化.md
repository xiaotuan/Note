### 7.3.4　通过lazy_static!宏将静态值动态化

如你所见，全局值只能在初始化时声明非动态的类型，并且在编译期，它在堆栈上的大小是已知的。例如，你不能将HashMap创建为静态值，因为它涉及堆分配。幸运的是，我们可以使用HashMap和其他动态集合类型（如Vec）构造全局静态值，这是通过被称为lazy_static的第三方软件包实现的。它暴露了lazy_static!宏，可用于初始化任何能够从程序中的任何位置全局访问的动态类型。以下是一个初始化Vec的代码片段，它能够在多线程环境中被修改：

```rust
// lazy_static_demo
use std::sync::Mutex;
lazy_static! {
    static ref ITEMS: Mutex<Vec<u64>> = {
        let mut v = vec![];
        v.push(9);
        v.push(2);
        v.push(1);
        Mutex::new(v)
    }
}
```

使用lazy_static!宏声明的元素需要实现Sync特征。这意味着如果某个静态值可变，那么必须使用诸如Mutex或RwLock这样的多线程类型，而不是RefCell。在第8章中我们将介绍这些类型，后文将会经常遇到这个宏。可以访问该软件包的版本库深入了解lazy_static的使用方法。

