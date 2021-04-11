### 7.12.2　std::mem模块

关于类型及其在内存中的大小，标准库中的mem模块为我们提供了方便的API，用于检查初始化原始内存的类型大小和功能的对齐方式。这些函数中有相当一部分是不安全的，只有当程序员知道它们在做什么时才能使用。我们将限制对这些API的探索。

+ size_of返回通过泛型获得的类型大小。
+ size_of_val返回某个引用值的大小。

通常，这些方法是通过turbofish运算符::<>调用的。我们实际上并没有给这些方法提供某个类型作为参数；只是显式针对某种类型调用它们。如果我们对前面的某些零成本的泛型声明存在疑问，那么可以使用这些函数检查它们的内存开销情况。让我们看看Rust中某些类型的大小：

```rust
// mem_introspection.rs
use std::cell::Cell;
use std::cell::RefCell;
use std::rc::Rc;
fn main() {
    println!("type u8: {}", std::mem::size_of::<u8>());
    println!("type f64: {}", std::mem::size_of::<f64>());
    println!("value 4u8: {}", std::mem::size_of_val(&4u8));
    println!("value 4: {}", std::mem::size_of_val(&4));
    println!("value 'a': {}", std::mem::size_of_val(&'a'));
    println!("value \"Hello World\" as a static str slice: {}",
std::mem::size_of_val("Hello World"));
    println!("value \"Hello World\" as a String: {}",
std::mem::size_of_val("Hello World").to_string());
    println!("Cell(4)): {}", std::mem::size_of_val(&Cell::new(84)));
    println!("RefCell(4)): {}", std::mem::size_of_val(&RefCell::new(4)));
    println!("Rc(4): {}", std::mem::size_of_val(&Rc::new(4)));
    println!("Rc<RefCell(8)>): {}",
std::mem::size_of_val(&Rc::new(RefCell::new(4))));
}
```

需要重点关注的一点是各指针的大小。请考虑如下代码：

```rust
// pointer_layouts.rs
trait Position {}
struct Coordinates(f64, f64);
impl Position for Coordinates {}
fn main() {
    let val = Coordinates(1.0, 2.0);
    let ref_: &Coordinates = &val;
    let pos_ref: &Position = &val as &Position;
    let ptr:       *const Coordinates = &val as *const Coordinates;
    let pos_ptr: *const Position = &val as *const Position;
    println!("ref_: {}", std::mem::size_of_val(&ref_));
    println!("ptr: {}", std::mem::size_of_val(&ptr));
    println!("val: {}", std::mem::size_of_val(&val));
    println!("pos_ref: {}", std::mem::size_of_val(&pos_ref));
    println!("pos_ptr: {}", std::mem::size_of_val(&pos_ptr));
}
```

我们以一系列不同的方式创建指向结构体Coordinates的指针，并将它们转换为不同类型的指针后输出其大小。编译并运行上述代码后，得到了以下输出结果：

```rust
ref_: 8
ptr: 8
val: 16
pos_ref: 16
pos_ptr: 16
```

这清楚地表明，特征对象和指向特征的引用是胖指针，它们是普通指针大小的两倍。

