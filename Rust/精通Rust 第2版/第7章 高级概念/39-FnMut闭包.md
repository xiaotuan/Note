### 7.7.2　FnMut闭包

当编译器检测出闭包改变了执行环境中引用的某个值时，它实现了FnMut特征。为了适配之前相同的代码，请参考如下代码：

```rust
// fn_mut_closure.rs
fn main() {
    let mut a = String::from("Hey!");
    let fn_mut_closure = || {
        a.push_str("Alice");
    };
    fn_mut_closure();
    println!("Main says: {}", a);
}
```

上述闭包将字符串"Alice"添加到a中。fn_mut_closure改变了它的执行环境。

