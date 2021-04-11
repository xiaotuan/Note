### 7.3.3　编译期函数—— const fn

我们还可以定义在编译期计算其参数的常量函数（const函数）。这意味着const值声明来自const函数调用的值。const函数是纯函数，必须是可重现的。这意味着它们不能将可变参数带入任何类型，也不能包含动态的操作，例如堆分配。它们可以在非常量的地方像普通函数那样被调用，但是当它们在包含常量的上下文中调用时，可以在编译期进行相关计算。以下是我们定义常量函数的方法：

```rust
// const_fns.rs
const fn salt(a: u32) -> u32 {
    0xDEADBEEF ^ a
}
const CHECKSUM: u32 = salt(23);
fn main() {
    println!("{}", CHECKSUM);
}
```

在上述代码中，我们定义了一个const函数salt，它将u32值作为参数，并使用十六进制值0xDEADBEEF执行异或操作。const函数对于可以在编译期执行的操作非常有用。例如，假定你正在编写二进制文件解析器，需要读取文件的前4字节以完成解析器初始化和验证等步骤。以下代码演示了如何在运行时完整地执行此操作：

```rust
// const_fn_file.rs
const fn read_header(a: &[u8]) -> (u8, u8, u8, u8) {
    (a[0], a[1], a[2], a[3])
}
const FILE_HEADER: (u8,u8,u8,u8) =
read_header(include_bytes!("./const_fn_file.rs"));
fn main() {
    println!("{:?}", FILE_HEADER);
}
```

在上述代码中，read_header函数使用include_bytes!宏接收一个文件作为字节数组，它也会在编译期读取文件。然后我们从中提取4字节，并将其作为具有4个元素的元组返回。没有const函数，这些都将在运行时完成。

