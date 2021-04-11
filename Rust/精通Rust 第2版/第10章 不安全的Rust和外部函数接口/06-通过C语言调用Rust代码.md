### 10.3　通过C语言调用Rust代码

如前所述，当Rust程序库使用extern代码块将其函数暴露给其他语言时，默认情况下它们会暴露C的应用程序二进制接口（Application Binary Interface，ABI）（cdecl）。因此，通过C语言调用Rust代码是无缝的。它们看起来就像普通的C函数一样。我们讨论一个通过C语言调用Rust代码的示例。为此，让我们运行cargo new rust_from_c --lib命令创建一个新的项目。在Cargo.toml文件中，我们有以下代码：

```rust
# rust_from_c/Cargo.toml
[package]
name = "rust_from_c"
version = "0.1.0"
authors = ["Rahul Sharma <creativcoders@gmail.com>"]
edition = "2018"
[lib]
name = "stringutils"
crate-type = ["cdylib"]
```

在[lib]下面，我们将软件包指定为cdylib，这表明我们系统地生成一个动态加载的程序库，它在Linux中通常被称为共享对象文件（.so）。我们为stringutils库指定了一个显式名称，这将用于创建共享对象文件。

现在，让我们继续完善lib.rs中的实现代码：

```rust
// rust_from_c/src/lib.rs
use std::ffi::CStr;
use std::os::raw::c_char;
#[repr(C)]
pub enum Order {
    Gt,
    Lt,
    Eq
}
#[no_mangle]
pub extern "C" fn compare_str(a: *const c_char, b: *const c_char) -> Order
{
    let a = unsafe { CStr::from_ptr(a).to_bytes() };
    let b = unsafe { CStr::from_ptr(b).to_bytes() };
    if a > b {
        Order::Gt
    } else if a < b {
        Order::Lt
    } else {
        Order::Eq
    }
}
```

我们有一个函数compare_str，在它前面添加extern关键字，将其暴露给C语言，然后为编译器指定“C”的应用程序二进制接口（Application Binary Interface，ABI）以生成相应的代码。我们还需要添加一个#[no_mangle]属性，因为Rust默认会在函数名称中添加随机字符，以防止类型名称和函数名称在模块和软件包之间发生冲突。这被称为名称改编。如果没有此属性，我们将无法通过compare_str调用相关的函数。我们的函数根据字典顺序来比较传递给它的两个C字符串，并返回一个枚举Order，它有3个变体：Gt（大于）、Lt（小于）及Eq（等于）。你可能已经注意到，枚举定义包含#[repr(C)]属性。因该枚举会被返回C语言端，所以我们希望它以C枚举的形式进行表示，repr属性支持我们这样做。在C语言方面，我们将获得一个uint_32类型作为此函数的返回类型，因为枚举变量在Rust中是以4个字节表示的，在C语言中也是如此。请注意，在编写本书时，Rust对具有关联数据的枚举的数据布局和C枚举是一样的。但是，未来可能存在一些变化。

现在，让我们创建一个名mian.c的文件，该文件会调用Rust暴露的函数：

```rust
// rust_from_c/main.c
#include <stdint.h>
#include <stdio.h>
int32_t compare_str(const char* value, const char* substr);
int main() {
    printf("%d\n", compare_str("amanda", "brian"));
    return 0;
}
```

我们声明了compare_str函数的原型，就像任何普通函数的原型声明一样。接下来，我们在main函数中调用compare_str，传入两个字符串值。请注意，如果我们传递在堆上分配的字符串，还需要在C端释放它们。在这种情况下，我们传递了一个C字符串文本，它将传递给进程的数据段，因此我们不需要进行任何资源释放。现在，我们将创建一个简单的Makefile文件来构建stringutils软件包，并编译和链接main.c文件：

```rust
# rust_from_c/Makefile
main:
    cargo build
    gcc main.c -L ./target/debug -lstringutils -o main
```

现在可以运行make命令构建我们的软件包，然后将LD_LIBRARY_PATH设置为生成libstringutils.so文件的位置来运行main程序。接下来，我们可以这样运行main：

```rust
$ export LD_LIBRARY_PATH=./target/debug
$ ./main
```

该程序的输出结果是1，它是Rust端的Order枚举中Lt变体的值。从这个例子可以看出，当你从C/C++或任何其他支持Rust的ABI接口的语言中调用Rust函数时，我们不能将特定于Rust的数据类型传递到FFI边界。例如，传递与数据相关联的Option和Result类型是没有意义的，因为C语言对它们一无所知，无法从中解析和提取值。在这种情况下，我们需要将原始值作为返回类型从函数传递到C端，或将我们的Rust类型转换为C语言可以理解的某种格式。

现在，考虑我们之前从Rust调用C代码的情况。在手动方式中，我们需要为已在头文件中声明的所有API编写外部声明。如果这些工作能够自动化完成就太好了，让我们看看该如何做。

