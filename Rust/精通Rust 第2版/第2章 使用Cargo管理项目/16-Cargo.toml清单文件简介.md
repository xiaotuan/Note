### 2.4.3　Cargo.toml清单文件简介

为了获取项目的各种信息，Cargo在很大程度上依赖于项目的清单文件Cargo.toml。让我们仔细查看一下该文件的结构以及它能够包含的元素。如前所述，Cargo新建了一个几乎空白的清单文件，只填充了必要的字段，以便可以构建项目。每个清单文件都分为几个部分，用于指定项目的不同属性。我们将介绍通常在中型Cargo项目清单文件中会用到的属性。以下是虚构的某个大型应用程序的Cargo.toml文件：

```rust
# cargo_manifest_example/Cargo.toml
#在清单文件中，我们可以使用#编写注释
[package]
name = "cargo-metadata-example"
version = "1.2.3"
description = "An example of Cargo metadata"
documentation = "https://docs.rs/dummy_crate"
license = "MIT"
readme = "README.md"
keywords = ["example", "cargo", "mastering"]
authors = ["Jack Daniels <jack@danie.ls>", "Iddie Ezzard <iddie@ezzy>"]
build = "build.rs"
edition = "2018"
[package.metadata.settings]
default-data-path = "/var/lib/example"
[features]
default=["mysql"]
[build-dependencies]
syntex = "^0.58"
[dependencies]
serde = "1.0"
serde_json = "1.0"
time = { git = "https://github.com/rust-lang/time", branch = "master" }
mysql = { version = "1.2", optional = true }
sqlite = { version = "2.5", optional = true }
```

让我们从[package]开始，来看看尚未解释的部分。

+ description：它包含一个关于项目的、更长的、格式自由的文本字段。
+ license：它包含软件许可证标识符。
+ readme：它允许你提供一个指向项目版本库某个文件的链接。这通常是项目简介的入口点。
+ documentation：如果这是一个程序库，那么其中包含指向程序库说明文档的链接。
+ keywords：它是一组单词列表，有助于用户通过搜索引擎或者crates.io网站发现你的项目。
+ authors：它列出了该项目的主要作者。
+ build：它定义了一段Rust代码（通常是build.rs），它在编译其余程序之前编译并运行。这通常用于生成代码或者构建项目程序所依赖的原生库。
+ edition：它主要用于指定编译项目时使用的Rust版本。在我们的示例中，使用的是2018版本。之前的是2015版本，如果不存在版本密钥，则默认使用此版本。注意：2018版本创建的项目是向后兼容的，这意味着它也可以使用2015版本的程序库作为依赖项。

接下来是[package.metadata.settings]。通常，Cargo会对它无法识别的键或属性向用户发出警告，但是包含元数据的部分是个例外。它们会被Cargo忽略，因此可以用于配置项目所需的任何键/值对。

[features]、[dependencies]及[build-dependencies]会组合到一起使用。依赖关系可以通过版本号声明，如semver指南中所述：

```rust
serde = "1.0"
```

这意味着serde是一个强制依赖，我们希望使用最新的版本，即“1.0.*”。实际的版本将会在Cargo.lock文件中确定。

使用补注符号（^）可以扩展Cargo允许查找的版本范围：

```rust
syntex = "^0.58"
```

这里，我们的意图是查找最新的主版本号“0.*.*”，并且版本号至少是“0.58.*”或以上。

Cargo还允许你直接指定依赖关系到Git版本库，前提是版本库是由Cargo创建的项目，并遵循Cargo期望的目录结构。我们可以像这样从GitHub指定依赖关系：

```rust
time = { git = "https://github.com/rust-lang/time", branch = "master" }
```

这也适用于其他在线Git版本库，例如GitLab。同样，运行cargo update命令将在Cargo.lock中确定实际的调用版本（在使用Git版本库的情况下，此操作是指变更集的修订版）。

清单列表还有两个可选的依赖项，mysql和sqlite：

```rust
mysql = { version = "1.2", optional = true }
sqlite = { version = "2.5", optional = true }
```

这意味着可以在不依赖任何一个依赖项的情况下构建程序。[features]属性部分包含默认功能列表：

```rust
default = ["mysql"]
```

这意味着用户在构建程序时如果没有手动覆盖功能集，则只会引入mysql而不包括sqlite。该特性的一个应用场景是你的程序库需要进行某种特定的优化改进。不过这在嵌入式平台上的开销会非常高，因此程序库作者只能将它作为功能进行发布，这些功能只能在能够承载它们的系统上使用。另一个应用场景是在构造命令行应用程序时，提供GUI前端作为额外的特性。

这是一个关于如何使用Cargo.toml清单文件描述Cargo项目的简要介绍。有关如何使用Cargo配置项目的内容还有很多。

