[toc]

自定义内容提供器步骤如下：

+ 定义数据模型（通常是 `SQLite` 数据库，其扩展自 `ContentProvider` 类）。
+ 定义其统一资源标识符（ `URI` ）。
+ 在 `AndroidManifest.xml` 中声明内容提供器。
+ 实现 `ContentProvider` 的抽象方法（ `query()`、`insert()`、`update()` 、`delete()`、`getType()` 和 `onCreate()` ）。

### 1. 定义数模型

#### 1.1 定义数据库表列名类



