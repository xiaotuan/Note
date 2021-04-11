### 7.6.4　From和Into

实现将一种类型转换为另一种类型，我们可用From和Into特征。关于这两个特征有趣的部分是，我们只需实现From特征就能自动获得Into特征的实现，例如以下impl代码块：

```rust
#[stable(feature = "rust1", since = "1.0.0")]
impl<T, U> Into<U> for T where U: From<T> {
    fn into(self) -> U {
        U::from(self)
    }
}
```

