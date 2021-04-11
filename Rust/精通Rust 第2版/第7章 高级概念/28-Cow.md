### 7.5.5　Cow

Cow是一种智能指针类型，提供两种版本的字符串，它表示在写入的基础上复制（Clone on Write，Cow）。它具有以下类型签名：

```rust
pub enum Cow<'a, B> where B: 'a + ToOwned + 'a + ?Sized, {
    Borrowed(&'a B),
    Owned(<B as ToOwned>::Owned),
}
```

首先，Cow有两个变体。

+ Borrowed表示某种类型B的借用版本。这个B必须实现ToOwned特征。
+ 所有权变体，其中包含该类型的所有权版本。

此类型适用需要避免不必要的内存分配的情况。一个真实的例子是名为serde_json的JSON解析器软件包。

