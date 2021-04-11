### 2.3.5　Cargo工作区

随着时间的推移，你的项目可能会变得非常庞大，现在，你需要考虑是否将代码的通用部分拆分成单独的程序库，以便管理复杂性。Cargo的工作区（workspace）可以帮你做到这一点。工作区的概念是，它们允许你在可以共享相同的Cargo.lock文件和公共目录，或者输出目录的目录下创建本地程序库。为了证明这一点，我将创建一个包含Cargo工作区的新项目。工作区只是一个包含Cargo.toml文件的目录。它不包含任何[package]部分，但是其中有一个[workspace]项。让我们新建一个名为workspace_demo的新目录，并按照如下步骤添加一个Cargo.toml文件：

```rust
mkdir workspace_demo
cd workspace_demo && touch Cargo.toml
```

然后我们将[workspace]项添加到Cargo.toml文件中：

```rust
# worspace_demo/Cargo.toml
[workspace]
members = ["my_crate", "app"]
```

在[workspace]项下，members属性表示工作区目录中的程序库列表。在workspace_demo目录中，我们将创建两个程序库：一个是程序库my_crate，一个是调用my_crate库的二进制程序app。

为了保持简洁，my_crate中只包含一个公有的API，用于输出一条问候消息：

```rust
// workspace_demo/my_crate/lib.rs
pub fn greet() {
    println!("Hi from my_crate");
}
```

在我们的app程序中有main函数，它会调用my_crate程序库中的greet函数：

```rust
// workspace_demo/app/main.rs
fn main() {
    my_crate::greet();
}
```

不过，我们需要让Cargo识别my_crate中的依赖关系。由于my_crate是一个本地程序库，我们需要在app的Cargo.toml文件中将其指定为路径依赖，如下所示：

```rust
# workspace_demo/app/Cargo.toml
[package]
name = "app"
version = "0.1.0"
authors = ["creativcoder"]
edition = "2018"
[dependencies]
my_crate = { path = "../my_crate" }
```

现在，当我们运行cargo build命令时，二进制文件将在workspace_demo目录下的target目录中生成。此外，我们可以在workspace_demo目录中添加多个本地程序库。现在，如果我们想要通过crates.io添加第三方的依赖项，那么需要将它们添加到所有会调用它们的程序中。不过，在Cargo构建过程中，Cargo会确保在Cargo.lock文件中只有该依赖项的单一版本。这可以确保不会重新构建或者重复出现第三方依赖项。

