### 2.4.2 在MongoDB shell中使用方法load()来执行脚本

还可以在MondoDB shell提示符下使用方法load(script_ path)来执行JavaScript文件。这个方法加载并立即执行指定的JavaScript文件，例如，下面的MondoDB shell加载并执行脚本文件db_update.js：

```go
load("/data/db/get_collections.js")
```

