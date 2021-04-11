### 11.5.1　log ——为Rust日志记录提供外观

log软件包来自GitHub上的rust-lang nursery组织，它由社区管理。它提供了单独的宏来记录不同的日志级别，例如error!、warn!、info!、debug!及trace!，并按照优先级从高到低的顺序进行排列。这些宏是该软件包用户的主要交互点。它们在内部会调用此软件包的log!宏，以便执行所有日志记录操作，例如检查日志级别和格式化日志消息。此软件包的核心组件是其他后端软件包实现的log特征。该特征定义了记录器所需的操作，并具有其他API，例如检查是否启用了日志记录或刷新任何已缓存的日志。

log软件包还提供了一个名为STATIC_MAX_LEVEL的最大日志级别常量，可以在编译期于项目范围内配置。通过此常量，你可以使用cargo特性标记来设置应用程序的日志级别，这允许对应用程序及其所有依赖项的日志进行编译期过滤。这些层面的过滤器可以分别在Cargo.toml中设置，用于调试版和发布版程序：max_level_<LEVEL>（调试版）和release_max_level_<LEVEL>（发布版）。在二进制项目中，你可以使用编译期日志级别指定log程序库的依赖关系，如下所示：

```rust
[dependencies]
log = "0.4.6", features = ["release_max_level_error", "max_level_debug"] }
```

将此常量设置为所需的值是一种很好的做法，因为默认情况下，该级别设置是Off。它还允许日志宏优化掉禁用级别的任何日志调用。程序库应该只链接到log软件包，而不是链接到任何日志记录器实现的软件包，因为二进制软件包应该控制日志记录的内容和如何进行日志记录。仅在你的应用程序中使用此软件包不会产生任何日志输出，因为你需要用到诸如env_logger或log4rs的日志记录软件包。

为了了解log软件包的实际效用，我们将通过cargo new user_auth --lib命令创建一个程序库，并在Cargo.toml文件中将log软件包添加为依赖项：

```rust
# user_auth/Cargo.toml
[dependencies]
log = "0.4.6"
```

该程序将模拟用户登录API。我们的lib.rs文件包含一个User结构体，它有一个名为sign_in的方法：

```rust
// user_auth/lib.rs
use log::{info, error};
pub struct User {
    name: String,
    pass: String
}
impl User {
    pub fn new(name: &str, pass: &str) -> Self {
        User {name: name.to_string(), pass: pass.to_string()}
    }
    pub fn sign_in(&self, pass: &str) {
        if pass != self.pass {
            info!("Signing in user: {}", self.name);
        } else {
            error!("Login failed for user: {}", self.name);
        }
    }
}
```

在sign_in方法中，我们有一些用于表示用户登录成功还是失败的日志调用。我们将使用此软件包和创建的User示例调用sign_in方法的二进制软件包。由于引用的log软件包自身不会产生任何日志输出，我们将使用env_logger作为此示例的日志记录后端。让我们来探讨一下env_logger。

