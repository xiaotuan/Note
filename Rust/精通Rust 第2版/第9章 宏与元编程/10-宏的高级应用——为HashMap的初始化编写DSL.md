### 9.8　宏的高级应用——为HashMap的初始化编写DSL

了解了重复和标记树类型的知识，让我们使用重复特性在macro_rules!宏中构建一些实用的内容。在本节中，我们将构建一个暴露宏的程序，它使用户能够像下列代码那样创建HashMap：

```rust
let my_map = map! {
    1 => 2,
    2 => 3
};
```

与手动调用HashMap::new()，后跟一个或多个insert调用相比，这样更简洁和易读。让我们通过运行cargo new macro_map --lib命令创建一个新项目，然后为macro_rules!宏初始化一个代码块：

```rust
// macro_map/lib.rs
#[macro_export]
macro_rules! map {
    // todo
}
```

由于希望用户使用我们的宏，所以需要在宏定义上添加#[macro_export]属性。默认情况下，宏在模块中是私有的，与其他元素类似。我们将会调用自定义的map!宏，因为我们正在使用自己的语法来初始化HashMap，所以将采用k=>v语法，其中k表示键，v表示HashMap中的值。以下是我们在map!中的实现：

```rust
macro_rules! map {
    ( $( $k:expr => $v:expr ),* ) => {
        {
            let mut map = ::std::collections::HashMap::new();
            $(
                map.insert($k, $v);
            )*
            map
        }
    };
}
```

让我们对上述匹配规则进行解释。首先，我们将检查内部的内容，即($k:expr => $v:expr )。让我们将规则的这一部分用Y表示。Y通过在键k和值v之间使用=>来捕获它们，并将其类型指定为expr。围绕着Y，我们有($(Y),*)，表示重复Y零次或更多次，并用逗号进行分隔。在花括号内匹配规则的右侧，我们首先创建了一个HashMap实例。然后，我们编写重复器$()*，其中包含我们的map.insert($k, $v)代码片段，它们将重复与我们的宏输入相同的次数。

让我们快速地编写一个测试：

```rust
// macro_map/lib.rs
#[cfg(test)]
mod tests {
    #[test]
    fn test_map_macro() {
        let a = map! {
            "1" => 1,
            "2" => 2
        };
        assert_eq!(a["1"], 1);
        assert_eq!(a["2"], 2);
    }
}
```

通过运行cargo test命令，我们得到以下输出结果：

```rust
running 1 test
test tests::test_map_macro ... ok
```

我们的测试顺利通过。接下来我们就可以使用新鲜出炉的map!宏以简捷的方式初始化HashMap了。

