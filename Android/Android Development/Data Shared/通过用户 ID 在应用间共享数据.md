[toc]

在将应用程序安装在设备上时会分配此用户 ID，在它保留在该设备上的整段时间内保持不变。将向应用程序所存储的任何数据分配该应用程序的用户 ID，而且这些数据通常无法供其他包访问。当使用 `getSharedPreferences(String, int)` 、`openFileOutput(String, int)` 或 `openOrCreateDatabase(String, int ,SQLiteDatabase.Cursor Factory)` 创建新文件时，可以使用 `MODE_PRIVATE`  标记来允许任何其他包读/写该文件。

如果目的在于允许一些依赖于同一组数据的协同运行的应用程序进行读写，那么可以显示指定一个你独有的并在所有需要中通用的用户 ID。

**共享用户 ID 声明**

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="com.androidbook.somepackage"
          sharedUserId="com.androidbook.myshareduserid"
          ...>
	...The rest of the xml nodes
</manifest>
```

### 1. 共享用户 ID 的性质

如果多个应用程序共享相同的签名（使用相同的 PKI 证书签名），它们可指定相同的共享用户 ID。拥有共享用户 ID，多个应用程序就可以共享数据，以及甚至在相同进程中运行。为了避免共享用户 ID 的重复，可以使用一种类似于命名 Java 类的约定。下面是在 `Android` 系统中找到的一些共享用户 ID 示例：

```console
"android.uid.system"
"android.uid.phone"
```

> 注意：共享 ID 必须指定为原始字符串而不是字符串资源。

> 注意：如果计划使用共享用户 ID，建议从一开始就使用它们。因为，由于用户 ID 更改，`Android` 不会再旧资源上运行 `chown`。

### 2. 共享数据的代码模式

`Android` 提供了一个名为 `createPackageContext()` 的 `API` 来帮助实现此目的。

**使用 createPackageContext() API**

```java
// Identify package you want to use
String targetPackageName = "com.androidbook.samplepackage1";

// Decide on an appropriate context flag
int flag = Context.CONTEXT_RESTRICTED;

// Get the target context through one of your activities
Activity myContext = ...;
Context targetContext = mContext.createPackageContext(targetPackageName, flag);

// Use context to resolve file paths
Resources res = targetContext.getResources();
File path = targetContext.getFilesDir();
```

无论是否拥有共享用户 ID，都可以使用此 API。如果共享用户 ID，则非常好的。如果没有共享用户 ID，目标应用程序将需要声明它的资源可供外部用户访问。

`createPackageContext()` 使用以下 3 中标志之一：

+ 如果标志是 `CONTEXT_INCLUDE_CODE`，`Android` 允许将目标应用程序代码加载到当前进程中。该代码然后像你的应用程序一样运行。只有在两个拥有相同的签名和一个共享用户 ID 时，此过程才能成功。如果共享用户 ID 不匹配，使用此标志将导致安全异常。
+ 如果标志是 `CONTEXT_RESTRICTED`，我们仍然应该能够访问资源路径，而不会遇到请求加载代码的极端情形。
+ 如果标志是 `CONTEXT_IGNORE_SECURITY`，将忽略证书并加载代码，但代码将在你的用户 ID 下运行。因此，文档建议如果将使用此标记，请非常小心。