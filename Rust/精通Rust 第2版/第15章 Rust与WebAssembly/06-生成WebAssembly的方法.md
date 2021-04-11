### 15.3.2　生成WebAssembly的方法

有一些编译器工具链项目可以帮助开发人员将他们的代码从任何语言编译为wasm。编译原生语言代码对Web有很大影响，这意味着可以在Web上运行大多数性能敏感型代码。例如，可以使用emscripten LLVM后端将C++代码编译为wasm。emscripten项目接收由C++编译器生成的LLVM IR实现，并将其转换为wasm格式的WebAssembly模块。还有一些项目，例如AssemblyScript，它使用一个类似emscripten的工具binaryen，将TypeScript代码转换为WebAssembly。Rust还支持默认情况下使用LLVM的原生WebAssembly后端输出WebAssembly代码。将Rust编译为wasm非常简单。首先，我们需要通过运行下列代码来添加wasm：

```rust
rustup target add wasm32-unknown-unknown
```

执行上述操作之后，我们可以通过运行以下代码将任何Rust程序编译为wasm：

```rust
cargo build --target=wasm32-unknown-unknown
```

这是根据Rust软件包创建一个wasm文件所需要的最基本的条件，但是从这里开始需要大量的手工操作。幸运的是，围绕wasm和Rust生态系统涌现出了一些令人惊叹的项目，它们能够与JavaScript和Rust进行更高级别的直观交互，反之亦然。我们将探讨一个名为wasm-bindgn的项目，并快速构建一个实际的Web应用程序。

