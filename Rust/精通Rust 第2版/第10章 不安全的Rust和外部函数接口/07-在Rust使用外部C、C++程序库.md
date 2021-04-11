### 10.4　在Rust使用外部C/C++程序库

考虑到过去30年中编写的软件数目，很多系统软件都是用C/C++编写的。你可能希望链接到通过C/C++编写的现有程序库以供Rust使用，因为重写Rust中的所有内容（即使希望如此）对复杂项目来说是不现实的。但与此同时，为这些程序库手动编写FFI绑定也比较麻烦，并容易出错。幸运的是，有一些工具可以帮助我们自动完成对C/C++程序库的绑定。对本示例来说，Rust方面所需的代码比之前调用Rust的C/C++代码的示例要简单得多，因为这一次我们会使用一个名为bindgen的便捷软件包，它可以自动生成对C/C++的FFI绑定库。

如果想要集成包含大量API的复杂程序库，那么bindgen是比较适合的工具。手动编写这些绑定可能非常容易出错，但bindgen可通过自动化执行此过程来帮助我们。我们将使用该软件包为简单的C程序库levenshtein.c生成绑定，该程序主要用于查找两个字符串之间的最小编辑距离。编辑距离适用于多种应用，例如字符串模糊匹配、自然语言处理及拼写检查等。接下来，让我们通过运行cargo new edit_distance --lib命令创建新项目。

在使用bindgen之前，我们来安装一下依赖项，因为bindgen需要用到它们：

```rust
$ apt-get install llvm-3.9-dev libclang-3.9-dev clang-3.9
```

接下来，在Cargo.toml文件中，我们需要将bindgen和cc软件包添加为构建依赖项：

```rust
# edit_distance/Cargo.toml
[build-dependencies]
bindgen = "0.43.0"
cc = "1.0"
```

bindgen软件包将用于根据levenshtein.h头文件生成绑定，cc软件包将用于被我们的程序库编译为共享对象，以便我们可以在Rust中访问它。我们的程序库相关的文件位于项目根目录下的lib文件夹中。

接下来将创建我们的build.rs文件，它将在编译任何源文件之前运行。它会做两件
事——首先，它将levenshtein.c文件编译为共享对象（.so）；其次，它将生成levenshtein.h文件中定义的API的绑定：

```rust
// edit_distance/build.rs
use std::path::PathBuf;
fn main() {
    println!("cargo:rustc-rerun-if-changed=.");
    println!("cargo:rustc-link-search=.");
    println!("cargo:rustc-link-lib=levenshtein");
    cc::Build::new()
        .file("lib/levenshtein.c")
        .out_dir(".")
        .compile("levenshtein.so");
    let bindings = bindgen::Builder::default()
        .header("lib/levenshtein.h")
        .generate()
        .expect("Unable to generate bindings");
    let out_path = PathBuf::from("./src/");
    bindings.write_to_file(out_path.join("bindings.rs")).expect("Couldn't
write bindings!");
}
```

在上述代码中，我们告诉Cargo程序库的搜索路径是当前目录，链接的程序库名称是levenshtein。如果当前目录中的任何文件发生变化，我们还会告知Cargo程序库重新运行build.rs中的代码：

```rust
println!("cargo:rustc-rerun-if-changed=.");
println!("cargo:rustc-link-search=.");
println!("cargo:rustc-link-lib=levenshtein");
```

然后，通过创建一个新的Build实例为程序库创建一个编译管道，并为file方法提供适当的C源文件。我们还将输出目录设置为out_dir，将程序库名称传递给compile方法：

```rust
cc::Build::new().file("lib/levenshtein.c")
                .out_dir(".")
                .compile("levenshtein");
```

接下来，我们创建一个bindgen构建实例，传递头文件的路径，调用generate()，然后在调用write_to_file之前将其写入bindings.rs文件：

```rust
let bindings = bindgen::Builder::default().header("lib/levenshtein.h")
                                          .generate()
                                          .expect("Unable to generate
bindings");
```

现在，当我们运行cargo build命令后，将会在src/.目录下生成一个bindings.rs文件。如前所述，对暴露FFI绑定的所有程序库来说，提供安全的包装器是一种比较好的做法。所以我们将会在src/lib.rs中创建一个名为levenshtein_safe的函数，用于包装bindings.rs中的不安全函数：

```rust
// edit_distance/src/lib.rs
mod bindings;
use crate::bindings::levenshtein;
use std::ffi::CString;
pub fn levenshtein_safe(a: &str, b: &str) -> u32 {
    let a = CString::new(a).unwrap();
    let b = CString::new(b).unwrap();
    let distance = unsafe { levenshtein(a.as_ptr(), b.as_ptr()) };
    distance
}
```

我们从bindings.rs导入不安全的函数，将它们包装到levenshtein_safe函数中，并在不安全代码块中调用我们的levenshtein函数，传递与C语言兼容的字符串。这时候应该对我们的levenshtein_safe函数进行一些测试。我们将在软件包根目录下的examples/目录中创建一个basic.rs文件，其中包含以下代码：

```rust
// edit_distance/examples/basic.rs
use edit_distance::levenshtein_safe;
fn main() {
    let a = "foo";
    let b = "fooo";
    assert_eq!(1, levenshtein_safe(a, b));
}
```

我们可以通过cargo run --example basic命令来运行它，并且应该不会看到断言失败，因为levenshtein_safe调用返回的值应该是1。目前对于这类软件包，推荐的命名约定是在其末尾添加sys后缀，因为其中只包含FFI绑定。crates.io上的大多数软件包都遵循这一约定。这是一次关于如何使用bindgen自动化跨语言交互的旋风之旅。如果你想要自动化反向的FFI绑定，例如在C语言中使用Rust程序库，那么在GitHub上还有一个名为cbindgen的等效软件包，它可以为Rust软件包生成C头文件。例如Webrender使用此软件包来将其API暴露给其他语言。鉴于C语言的历史遗留问题，而它是编程语言中的通用语言，Rust为其提供了一流的支持。许多其他语言也会调用C语言，这意味着可以从以C语言为目标的其他语言调用你的Rust代码。接下来让我们探讨一下Rust与其他语言的交互。

