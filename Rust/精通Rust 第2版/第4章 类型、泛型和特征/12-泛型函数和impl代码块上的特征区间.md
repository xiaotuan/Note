### 4.4.2　泛型函数和impl代码块上的特征区间

这是用到特征区间最常见的地方。我们可以在函数和泛型实现上指定特征区间，如下所示：

```rust
// trait_bounds_functions.rs
use std::fmt::Debug;
trait Eatable {
    fn eat(&self);
}
#[derive(Debug)]
struct Food<T>(T);
#[derive(Debug)]
struct Apple;
impl<T> Eatable for Food<T> where T: Debug {
    fn eat(&self) {
        println!("Eating {:?}", self);
    }
}
fn eat<T>(val: T) where T: Eatable {
    val.eat();
}
fn main() {
    let apple = Food(Apple);
    eat(apple);
}
```

我们有一个泛型Food和一种特定食物类型Apple，将Apple放入Food实例并绑定到变量apple。接下来调用泛型方法eat，并将apple传递给它。注意eat的特点，类型T必须实现Eatable特征。为了让apple是“可食用”的，我们实现了Food的Eatable特征，同时指定我们的类型必须是Debug，以便其可以在方法内部输出到控制台。这是一个简单的示例，但证明了这一思路。

