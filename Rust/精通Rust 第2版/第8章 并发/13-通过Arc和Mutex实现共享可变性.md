### 8.4.3　通过Arc和Mutex实现共享可变性

在单线程环境中探讨了Mutex的基础知识后，我们将重新讨论8.4.2小节中的示例。以下代码演示了在多线程环境下修改Arc类型包装后的Mutex值：

```rust
// arc_mutex.rs
use std::sync::{Arc, Mutex};
use std::thread;
fn main() {
    let vec = Arc::new(Mutex::new(vec![]));
    let mut childs = vec![];
    for i in 0..5 {
        let mut v = vec.clone();
        let t = thread::spawn(move || {
            let mut v = v.lock().unwrap();
            v.push(i);
        });
        childs.push(t);
    }
    for c in childs {
        c.join().unwrap();
    }
    println!("{:?}", vec);
}
```

在上述代码中，我们创建了一个Mutex值，然后生成一个线程。上述代码在你的计算机上的输出结果可能会略有不同。

在互斥锁上执行锁定将阻止其他线程调用锁定，直到锁定消失为止。因此，以一种细粒度的方式构造代码是很重要的。

编译并运行该代码将会得到以下输出结果：

```rust
$ rustc arc_mutex.rs
$ ./arc_mutex
Mutex { data: [0,1,2,3,4] }
```

还有一种与互斥锁类似的替代方法，即RwLock类型，它对类型的锁定更敏感，并且在读取比写入更频繁的情况下性能更好。接下来让我们对它进行探讨。

#### RwLock

互斥锁适用于大多数应用场景，但对于某些多线程环境，读取的发生频率高于写入的。在这种情况下，我们可以采用RwLock类型，它提供共享可变性，但可以在更细粒度上执行操作。RwLock表示Reader-Writer锁。通过RwLock，我们可以同时支持多个读取者，但在给定作用域内只允许一个写入者。这比互斥锁要好得多，互斥锁对线程所需的访问类型是未知的。

RwLock公开了两种方法。

+ read：提供对线程的读取访问权限；可以存在多个读取调用。
+ write：提供对线程的独占访问，以便将数据写入包装类型；从RwLock实例到线程只允许有一个写入访问权限。

以下是一个示例，演示使用RwLock替代Mutex：

```rust
// thread_rwlock.rs
use std::sync::RwLock;
use std::thread;
fn main() {
    let m = RwLock::new(5);
    let c = thread::spawn(move || {
        {
            *m.write().unwrap() += 1;
        }
        let updated = *m.read().unwrap();
        updated
    });
    let updated = c.join().unwrap();
    println!("{:?}", updated);
}
```

但是在某些操作系统（如Linux）上RwLock会遇到写入者饥饿问题。这种情况是因为读取者不断访问共享资源，从而导致写入者线程永远没有机会访问共享资源。

