可以通过 `Resources`  类的如下方法通过字符串获取资源 ID：

```java
 public int getIdentifier(String name, String defType, String defPackage);
```

方法参数说明如下：

+ `name` ：资源的名称
+ `defType` ：资源的类型，例如：`string`，`style`，`theme`，`raw` 等
+ `defPackage` ：资源所在的包名。

