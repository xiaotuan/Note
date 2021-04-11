### 7.13　使用serde进行序列化和反序列化

序列化和反序列化是理解任何需要以紧凑格式传输或存储数据的应用程序时会用到的两个重要概念。序列化是将内存数据类型转换为字节序列的过程，反序列化则与此相反，这意味着它可以读取数据。很多编程语言都为将数据结构转换为字节序列提供了支持。serde的强大之处在于它能够在编译期生成任何支持的类型的序列化数据，并且深度依赖过程宏。大多数情况下序列化和反序列化对serde都是零成本操作。

在本示例中，我们将探讨通过serde程序库序列化和反序列化某个自定义类型。让我们通过运行cargo new serde_demo命令创建一个新的项目，相关的Cargo.toml文件内容如下所示：

```rust
# serde_demo/Cargo.toml
[dependencies]
serde = "1.0.84"
serde_derive = "1.0.84"
serde_json = "1.0.36"
```

main.rs中的代码如下所示：

```rust
serde_demo/src/main.rs
use serde_derive::{Serialize, Deserialize};
#[derive(Debug, Serialize, Deserialize)]
struct Foo {
    a: String,
    b: u64
}
impl Foo {
    fn new(a: &str, b: u64) -> Self {
        Self {
            a: a.to_string(),
            b
        }
    }
}
fn main() {
    let foo_json = serde_json::to_string(Foo::new("It's that simple",
101)).unwrap();
    println!("{:?}", foo_json);
    let foo_value: Foo = serde_json::from_str(foo_json).unwrap();
    println!("{:?}", foo_value);
}
```

要将任何原生数据类型转换为类JSON格式，我们只需在类型上添加一个派生注释即可。这就是我们的Foo结构体采用的转换方式。

serde支持很多实现为程序包的序列化实现器，比较流行的包括serde_json、bincode及TOML。这些序列化实现器（例如serde_json）提供了to_string等类似转换方法。

