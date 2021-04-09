### 3.3　函数 `init` 

每个包可以包含任意多个 `init` 函数，这些函数都会在程序执行开始的时候被调用。所有被编译器发现的 `init` 函数都会安排在 `main` 函数之前执行。 `init` 函数用在设置包、初始化变量或者其他要在程序运行前优先完成的引导工作。

以数据库驱动为例， `database` 下的驱动在启动时执行 `init` 函数会将自身注册到 `sql` 包里，因为 `sql` 包在编译时并不知道这些驱动的存在，等启动之后 `sql` 才能调用这些驱动。让我们看看这个过程中 `init` 函数做了什么，如代码清单3-5所示。

代码清单3-5　`init`函数的用法

```go
01 package postgres
02
03 import (
04　　 "database/sql"
05 )
06
07 func init() {
08　　 sql.Register("postgres", new(PostgresDriver)) 　　●――――创建一个postgres驱动的实例。这里为了展现init的作用，没有展现其定义细节。
09 }

```

这段示例代码包含在PostgreSQL数据库的驱动里。如果程序导入了这个包，就会调用 `init` 函数，促使PostgreSQL的驱动最终注册到Go的 `sql` 包里，成为一个可用的驱动。

在使用这个新的数据库驱动写程序时，我们使用空白标识符来导入包，以便新的驱动会包含到 `sql` 包。如前所述，不能导入不使用的包，为此使用空白标识符重命名这个导入可以让 `init` 函数发现并被调度运行，让编译器不会因为包未被使用而产生错误。

现在我们可以调用 `sql.Open` 方法来使用这个驱动，如代码清单3-6所示。

代码清单3-6　导入时使用空白标识符作为包的别名

```go
01 package main
02
03 import (
04　　 "database/sql"
05
06　　 _ "github.com/goinaction/code/chapter3/dbdriver/postgres"　　●――――使用空白标识符导入包，避免编译错误。
07 )
08
09 func main() 
10　　 sql.Open("postgres", "mydb") 　　●――――调用sql包提供的Open方法。该方法能工作的关键在于postgres驱动通过自己的init函数将自身注册到了sql包。
11 }

```

