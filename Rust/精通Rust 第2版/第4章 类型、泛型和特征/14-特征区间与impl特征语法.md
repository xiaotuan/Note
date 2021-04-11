### 4.4.4　特征区间与impl特征语法

声明特征区间的另一种语法是impl特征语法，它是编译器的最新特性。通过这种语法，可以编写具有如下特征区间的泛型函数：

```rust
// impl_trait_syntax.rs
use std::fmt::Display;
fn show_me(val: impl Display) {
    println!("{}", val);
}
fn main() {
    show_me("Trait bounds are awesome");
}
```

我们直接使用了impl Display，而不是指定T：Display。这是impl特征语法。这为我们返回复杂或不方便表示的类型（例如函数的闭包）提供了便利。如果没有这种语法，则必须使用Box智能指针类型将其放在指针后面返回，这涉及堆分配。闭包的底层结构由实现了一系列特征的结构体组成。Fn(T) -> U特征就是其中之一。因此，通过impl特征语法，我们可以编写如下形式的函数：

```rust
// impl_trait_closure.rs
fn lazy_adder(a:u32, b: u32) -> impl Fn() -> u32 {
    move || a + b
}
fn main() {
    let add_later = lazy_adder(1024, 2048);
    println!("{:?}", add_later());
}
```

在上述代码中，我们创建了一个函数lazy_adder，它接收两个数字，并返回将这两个数字相加的闭包。然后我们调用lazy_adder，传入两个数字。这会在lazy_adder中创建一个闭包，但不会对其进行求值。在main函数中，我们在println!宏中调用adder_later。我们甚至可以在这两个地方使用如下语法：

```rust
// impl_trait_both.rs
use std::fmt::Display;
fn surround_with_braces(val: impl Display) -> impl Display {
    format!("{{{}}}", val)
}
fn main() {
    println!("{}", surround_with_braces("Hello"));
}
```

surround_with_braces会接收任何Display特征的参数，并返回用花括号包裹的字符串。这里我们返回的类型是impl Display。





![76.png](../images/76.png)
**注意**

额外的花括号是为了转义花括号自身，因为{}在用于字符串值的格式化时具有特殊含义。



通常建议将特征区间的impl特征语法用做函数的返回类型。在参数位置使用它意味着我们不能使用turbofish运算符。如果某些相关代码使用turbofish运算符来调用软件包中的某个方法，那么可能导致API不兼容。只有当我们没有可用的具体类型时才应该使用它，就像闭包那样。

