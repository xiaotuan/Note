### 8.6　使用actor模型实现并发

另一种与消息传递模型非常相似的并发模型是actor模型。actor模型目前受到Erlang的欢迎。Erlang是一种在电信行业中非常流行的函数式编程语言，以其健壮性和天然的分布式特性而闻名。

actor模型是一种概念模型，它使用名为actors的实体在类型层面实现并发。它于1973年由Carl Eddie Hewitt首次提出。它避免了对锁和同步的要求，并提供了一种向系统引入并发的更简洁方法。actor模型由3部分组成。

+ Actor：这是actor模型中的核心元素。每个actor都包含其地址，使用该地址我们可以将消息发送到某个actor和邮箱，这只是一个存储它收到的消息的队列。
+ FIFO：队列通常是先进先出（First In First Out，FIFO）。actor的地址是必需的，以便其他actor可以向其发送消息。超级actor能够创建其他子actor的子actor。
+ Messages：actor之间仅通过消息进行通信，它们由actor异步处理。actix-web框架为异步包装器中的同步操作提供了一个很好的包装器。

在Rust编译器中，我们实现了actor模型的actix程序库。该程序库使用的tokio和futures软件包将在第12章进行详细介绍。该程序库的核心对象是Arbiter类型，它只是一个简单的在底层生成事件循环的线程，并且提供Addr类型作为该事件循环的句柄。一旦创建该类型，我们就可以使用这个句柄向actor发送消息。

在actix中，actor的创建遵循简单的步骤：创建一个类型，定义一个消息，并为actor类型实现消息的处理程序。完成创建后，我们可以将它添加到已经创建的某个仲裁器（arbiter）中。

每个actor都是在仲裁器中运行的。

当我们创建一个actor后，它不会马上执行。当我们将这些actor放入仲裁器线程后，它们才会开始执行。

为了让代码示例尽量简单，并演示在actix中如何构建actor和运行它们，我们将创建一个可以添加两个数字的actor。让我们通过运行cargo new actor_demo命令创建一个新项目，并在Cargo.toml中设置如下依赖项：

```rust
# actor_demo/Cargo.toml
[dependencies]
actix = "0.7.9"
futures = "0.1.25"
tokio = "0.1.15"
```

我们的main.rs中包含如下代码：

```rust
// actor_demo/src/main.rs
use actix::prelude::*;
use tokio::timer::Delay;
use std::time::Duration;
use std::time::Instant;
use futures::future::Future;
use futures::future;
struct Add(u32, u32);
impl Message for Add {
    type Result = Result<u32, ()>;
}
struct Adder;
impl Actor for Adder {
    type Context = SyncContext<Self>;
}
impl Handler<Add> for Adder {
    type Result = Result<u32, ()>;
    fn handle(&mut self, msg: Add, _: &mut Self::Context) -> Self::Result {
        let sum = msg.0 + msg.0;
        println!("Computed: {} + {} = {}",msg.0, msg.1, sum);
        Ok(msg.0 + msg.1)
    }
}
fn main() {
    System::run(|| {
        let addr = SyncArbiter::start(3, || Adder);
        for n in 5..10 {
            addr.do_send(Add(n, n+1));
        }
        tokio::spawn(futures::lazy(|| {
            Delay::new(Instant::now() + Duration::from_secs(1)).then(|_| {
                System::current().stop();
                future::ok::<(),()>(())
            })
        }));
    });
}
```

在上述代码中，我们创建了一个名为Adder的actor。该actor可以发送和接收Add类型的信息。这是一个元组结构，它封装了两个要添加的数字。为了让Adder接收和处理Add类型的信息，我们通过Add消息类型为参数化的Adder实现了Handler特征。在Handler实现中，我们输出正在执行的计算并返回给定数字的总和。

接下来，在main函数中，我们首先通过调用其接收闭包的run方法来创建一个系统级actor。在闭包中，我们通过调用其start方法启动一个包含3个线程的SyncArbiter；然后创建了3个准备接收消息的actor。它返回的Addr类型是事件循环的句柄，以便我们可以将消息发送到Adder类型的actor实例。

然后我们向仲裁器地址addr发送了5条消息。由于System::run是一个一直在执行的父事件循环，因此我们生成一个未来计划以便在延迟1秒后停止系统actor。可以忽略这部分代码的细节，因为它只是以异步方式关闭系统actor。

接下来，让我们看看该程序的输出结果：

```rust
$ cargo run
Running `target/debug/actor_demo`
Computed: 5 + 6 = 10
Computed: 6 + 7 = 12
Computed: 7 + 8 = 14
Computed: 8 + 9 = 16
Computed: 9 + 10 = 18
```

与actix程序库类似，Rust生态系统中还有其他程序库，它们实现了适用于不同用例的各种并发模型。

