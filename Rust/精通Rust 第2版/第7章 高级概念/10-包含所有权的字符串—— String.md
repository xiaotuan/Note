### 7.2.1　包含所有权的字符串—— String

String类型来自标准库，并且是通过堆分配的UTF-8编码的字节序列。在底层它们只是 Vec<u8>类型，不过额外包含只适用于字符串的方法。它们是包含所有权的类型，这意味着保存String值的变量是其所有者。通常可以通过多种方式创建String类型，如以下代码所示：

```rust
// strings.rs
fn main() {
    let a: String = "Hello".to_string();
    let b = String::from("Hello");
    let c = "World".to_owned();
    let d = c.clone();
}
```

在上述代码中，我们以4种不同的方式创建了4个字符串。它们创建了相同的字符串类型，并具有相同的性能特征。第1个字符串a通过调用to_string方法创建字符串，该方法来自ToString特征，字符串内容为“Hello”。诸如“Hello”之类的字符串本身也具有&str类型。当我们讨论借用字符串时，会对它们进行解释。然后我们通过调用from方法创建另一个字符串b，这是String上的一个关联方法。第3个字符串c是通过ToOwned特征的to_owned特征方法创建的，该特征是&str类型——基于字面字符串而实现。第4个字符串是通过复制已有的字符串c创建的。创建字符串的第4种方法开销昂贵，我们应该尽量避免采用这种方法，因为它涉及通过迭代来复制底层字节。

由于String是在堆上分配的，因此它可以被修改，并且能够在运行时根据需要增加长度。这意味着字符串在执行此操作时会产生相应的开销，因为它们可能会在你不断添加字节时重新分配内存。堆分配是一种开销相对昂贵的操作，但幸运的是，Vec分配内存时（容量限制加倍）使该成本会按使用量平摊而降低。

String在标准库中还包含很多便捷的方法，主要有以下几种。

+ String::new()会分配一个空的String类型。
+ String::from(s: &str)会分配一个新的String类型，并通过字符串切片来填充它。
+ String::with_capacity(capacity: usize)会分配一个预定义大小、空的String类型。当你事先知道字符串的大小时，这将是非常高效的。
+ String::from_utf8(vec: Vec<u8>)尝试从bytestring分配一个新的String类型。参数的内容必须是UTF-8，否则将会失败。它会返回Result的包装器类型。
+ 字符串实例上的len()方法将会为你提供String类型的长度，并且它兼容Unicode格式。例如，一个包含单词“yö”的字符串类型的长度是2，即使它在内存中占用的是3个字节。
+ push(ch: char)和push_str(string: &str)方法用于将字符或字符串切片添加到字符串中。

当然，这是一份不太完整的清单。

下面是一个使用上述所有方法的示例：

```rust
// string_apis.rs
fn main() {
    let mut empty_string = String::new();
    let empty_string_with_capacity = String::with_capacity(50);
    let string_from_bytestring: String = String::from_utf8(vec![82, 85, 83,
    84]).expect("Creating String from bytestring failed");
    println!("Length of the empty string is {}", empty_string.len());
    println!("Length of the empty string with capacity is {}",
    empty_string_with_capacity.len());
    println!("Length of the string from a bytestring is {}",
    string_from_bytestring.len());
    println!("Bytestring says {}", string_from_bytestring);
    empty_string.push('1');
    println!("1) Empty string now contains {}", empty_string);
    empty_string.push_str("2345");
    println!("2) Empty string now contains {}", empty_string);
    println!("Length of the previously empty string is now {}",
    empty_string.len());
}
```

介绍过String之后，让我们来看看被称为字符串切片或者&str类型的借用字符串。

